#!/usr/bin/env python3
"""TreeRAG baseline for the aligned arXiv 800-task retrieval eval.

This adapter follows the TreeRAG paper's retrieval protocol:

1. Tree-Chunking: an LLM assigns hierarchical levels and concise titles to
   preprocessed document chunks, then each chunk is embedded with its
   hierarchical title/path prefix.
2. Intent detection: an LLM predicts whether the query needs broad
   enumeration/summary traversal.
3. Bidirectional Traversal Retrieval: when intent is positive, expand an
   initially retrieved node to the leaf chunks under that node or under its
   immediate parent, then rerank under the same character budgets.

No corpus gold/pred hierarchy labels are used for TreeRAG tree construction,
and there is no heuristic/non-LLM fallback for the paper's black-box steps.
The default black-box model is this project's Qwen model
(``qwen3.5-flash``), accessed through the existing OpenAI-compatible
configuration.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
import pickle
import re
import sys
import time
import signal
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path
from threading import Lock
from typing import Any, Dict, Iterable, List, Optional, Sequence, Tuple

PACKAGE_ROOT = Path(__file__).resolve().parent
# TreeRAG 与 Gold/Flat 共用唯一的 agent_delivery 实现。显式固定路径，避免
# 直接运行本文件和经 wrapper 运行时因 sys.path 顺序不同而加载不同副本。
SHARED_AGENT_CODE_DIR = PACKAGE_ROOT.parent / "realdata"
if str(SHARED_AGENT_CODE_DIR) not in sys.path:
    sys.path.insert(0, str(SHARED_AGENT_CODE_DIR))

from agent_delivery.agent.tasks_loader import _load_tasks
from agent_delivery.agent.types import AgentTask
from agent_delivery.code.budget_eval import (
    EVIDENCE_HEADER_PROTOCOL,
    _build_retrieval_queries,
    _query_weight,
    compute_budget_retrieval_metrics,
    evaluate_at_budget,
)
from agent_delivery.code.embedding_backend import (
    DEFAULT_DENSE_EMBEDDING_MODEL,
    encode_chunks_normalized,
    encode_query_normalized,
    get_dense_encoder,
)
from agent_delivery.code.index_retrieval import Chunk
from agent_delivery.code.llm_config import load_llm_env
from agent_delivery.code.load_data import bundles_from_paths, build_parent_pointers, line_node_id
from agent_delivery.code.metrics import retrieval_metrics
from agent_delivery.code.compose_llm import compose_answer_llm
from agent_delivery.code.judge_llm import task_success_score
from agent_delivery.code.llm_usage import reset_usage, snapshot_usage
from agent_delivery.code.inspect_scoring import (
    build_inspect_pred_output,
    evidence_line_ids_from_runner,
    inspect_compose_format_block,
    load_inspect_registry,
    score_sample,
)

Scored = List[Tuple[Chunk, float]]

DEFAULT_TREERAG_LLM_MODEL = "qwen3.5-flash"
PAPER_DENSE_EMBEDDING_MODEL = "BAAI/bge-m3"
TREE_CHUNK_PROMPT_VERSION = "treerag-paper-tree-chunking-qwen-v1"
INTENT_PROMPT_VERSION = "treerag-paper-intent-qwen-v1"


def _adapter_path_label() -> str:
    return "src/treerag/eval_arxiv_treerag.py"


def _fairness_control_metadata(args: argparse.Namespace, *, candidate_cap_enabled: bool) -> Dict[str, Any]:
    """Describe the protocol actually executed; this is metadata-only."""
    return {
        "shared_controls": [
            "task_set",
            "evidence_character_budget",
            "budget_fill",
            "compose",
            "judge",
        ],
        "candidate_count_matching": (
            "legacy_enabled_from_existing_baseline_results"
            if candidate_cap_enabled
            else "disabled"
        ),
        "compute_budget_matched": False,
        "method_specific_retrieval_limits": {
            "treerag_initial_top_k": int(args.initial_top_k),
            "treerag_max_traversal_leaves": int(args.max_traversal_leaves),
        },
        "note": (
            "Methods share the final evidence-character budget, not retrieval calls, "
            "candidate counts, token usage, latency, or offline preprocessing cost."
        ),
    }


@dataclass
class TreeRagNode:
    node_id: str
    line_id: int
    level: int
    text: str
    title: str
    embedding_text: str
    parent_idx: Optional[int]
    child_indices: Tuple[int, ...]
    leaf_indices: Tuple[int, ...]


@dataclass
class TreeRagDocIndex:
    doc_id: str
    tree_source: str
    nodes: Tuple[TreeRagNode, ...]
    node_id_to_idx: Dict[str, int]
    embeddings: Any
    cache_key: str


def _local_hf_snapshot(model_name: str) -> Optional[str]:
    """Prefer a fully cached HuggingFace snapshot to avoid network probes."""
    if os.path.exists(model_name):
        return model_name
    cache_root = Path(os.environ.get("HF_HUB_CACHE") or Path.home() / ".cache" / "huggingface" / "hub")
    candidates = [model_name]
    if "/" not in model_name:
        candidates.append(f"sentence-transformers/{model_name}")
    for candidate in candidates:
        model_dir = cache_root / f"models--{candidate.replace('/', '--')}"
        refs_main = model_dir / "refs" / "main"
        if refs_main.exists():
            rev = refs_main.read_text(encoding="utf-8").strip()
            snap = model_dir / "snapshots" / rev
            if (snap / "modules.json").exists() and (snap / "config.json").exists():
                return str(snap)
        snap_root = model_dir / "snapshots"
        if snap_root.exists():
            for snap in sorted(snap_root.iterdir()):
                if (snap / "modules.json").exists() and (snap / "config.json").exists():
                    return str(snap)
    return None


def _extract_json_payload(text: str) -> Any:
    raw = str(text or "").strip()
    if not raw:
        raise RuntimeError("TreeRAG LLM returned an empty response.")
    if raw.startswith("```"):
        raw = re.sub(r"^```(?:json)?\s*", "", raw, flags=re.I)
        raw = re.sub(r"\s*```$", "", raw)
    try:
        return json.loads(raw)
    except Exception:
        pass

    start_positions = [p for p in (raw.find("{"), raw.find("[")) if p >= 0]
    if not start_positions:
        raise RuntimeError(f"TreeRAG LLM response does not contain JSON: {raw[:320]!r}")
    start = min(start_positions)
    opener = raw[start]
    closer = "}" if opener == "{" else "]"
    depth = 0
    in_str = False
    escape = False
    for i in range(start, len(raw)):
        ch = raw[i]
        if in_str:
            if escape:
                escape = False
            elif ch == "\\":
                escape = True
            elif ch == '"':
                in_str = False
            continue
        if ch == '"':
            in_str = True
        elif ch == opener:
            depth += 1
        elif ch == closer:
            depth -= 1
            if depth == 0:
                return json.loads(raw[start : i + 1])
    raise RuntimeError(f"TreeRAG LLM response contains incomplete JSON: {raw[:320]!r}")


def _resolve_treerag_model(args: argparse.Namespace) -> str:
    model = (
        str(getattr(args, "treerag_model", "") or "").strip()
        or os.environ.get("TREERAG_MODEL", "").strip()
        or DEFAULT_TREERAG_LLM_MODEL
    )
    if not model:
        raise RuntimeError("TreeRAG requires a non-empty LLM model name.")
    return model


def _resolve_openai_verify_ssl() -> bool:
    raw = os.environ.get("OPENAI_VERIFY_SSL", "").strip().lower()
    if raw in {"1", "true", "yes", "on"}:
        return True
    if raw in {"0", "false", "no", "off", ""}:
        return False
    return False


def _resolve_openai_trust_env() -> bool:
    raw = os.environ.get("OPENAI_TRUST_ENV", "").strip().lower()
    if raw in {"1", "true", "yes", "on"}:
        return True
    if raw in {"0", "false", "no", "off", ""}:
        return False
    return False


def _resolve_treerag_llm_timeout_seconds() -> float:
    raw = os.environ.get("TREERAG_LLM_TIMEOUT_SECONDS", "120").strip()
    try:
        timeout = float(raw)
    except ValueError as e:
        raise RuntimeError(f"Invalid TREERAG_LLM_TIMEOUT_SECONDS={raw!r}") from e
    if timeout <= 0:
        raise RuntimeError(f"TREERAG_LLM_TIMEOUT_SECONDS must be positive, got {timeout}")
    return timeout


class RequiredOpenAITreeRagLLM:
    """Required OpenAI-compatible client for TreeRAG's paper LLM steps."""

    def __init__(self, *, cache_path: Path, model: str, base_url: Optional[str]) -> None:
        import httpx

        api_key = os.environ.get("OPENAI_API_KEY", "").strip()
        if not api_key:
            raise RuntimeError("TreeRAG paper reproduction requires OPENAI_API_KEY; no non-LLM fallback is allowed.")
        if not model:
            raise RuntimeError("TreeRAG paper reproduction requires a model name; no non-LLM fallback is allowed.")
        self.model = model
        self.base_url = base_url
        self.api_key = api_key
        self.verify_ssl = _resolve_openai_verify_ssl()
        self.trust_env = _resolve_openai_trust_env()
        self.llm_timeout_seconds = _resolve_treerag_llm_timeout_seconds()
        self._httpx = httpx
        self.client = self._make_client()
        self.cache_path = cache_path
        self.cache_path.parent.mkdir(parents=True, exist_ok=True)
        self._lock = Lock()
        self._cache: Dict[str, Any] = {}
        self.api_calls = 0
        self.cache_hits = 0
        self.prompt_tokens = 0
        self.completion_tokens = 0
        self.total_tokens = 0
        self._usage_by_purpose: Dict[str, Dict[str, int]] = defaultdict(
            lambda: {
                "prompt_tokens": 0,
                "completion_tokens": 0,
                "total_tokens": 0,
                "api_calls": 0,
                "cache_hits": 0,
            }
        )
        if self.cache_path.exists():
            with open(self.cache_path, "r", encoding="utf-8") as f:
                for line in f:
                    if not line.strip():
                        continue
                    try:
                        row = json.loads(line)
                    except Exception:
                        continue
                    key = str(row.get("key") or "")
                    if key and "parsed" in row:
                        self._cache[key] = row["parsed"]

    def _make_client(self):
        from openai import OpenAI

        timeout = float(self.llm_timeout_seconds)
        http_client = self._httpx.Client(verify=self.verify_ssl, timeout=timeout, trust_env=self.trust_env)
        return OpenAI(api_key=self.api_key, base_url=self.base_url or None, timeout=timeout, max_retries=0, http_client=http_client)

    def _reset_client(self) -> None:
        try:
            close = getattr(self.client, "close", None)
            if callable(close):
                close()
        except Exception:
            pass
        self.client = self._make_client()

    def token_usage(self) -> Dict[str, int]:
        return {
            "prompt_tokens": int(self.prompt_tokens),
            "completion_tokens": int(self.completion_tokens),
            "total_tokens": int(self.total_tokens),
            "api_calls": int(self.api_calls),
            "cache_hits": int(self.cache_hits),
        }

    def token_usage_by_purpose(self) -> Dict[str, Dict[str, int]]:
        return {purpose: dict(values) for purpose, values in sorted(self._usage_by_purpose.items())}

    def preflight_check(self, max_tokens: int = 48) -> None:
        try:
            models = self.client.models.list()
            data = getattr(models, "data", None)
            if not isinstance(data, list):
                raise RuntimeError("TreeRAG LLM preflight could not read the models list response")
        except Exception as e:
            raise RuntimeError(f"TreeRAG LLM preflight failed while listing models: {e}") from e
        parsed = self.call_json(
            prompt_version=f"treerag-paper-preflight-qwen-v1-{int(time.time())}",
            purpose="preflight_smoke_check",
            messages=[
                {"role": "system", "content": "Return JSON only."},
                {"role": "user", "content": 'Return exactly {"ok": true}.'},
            ],
            max_tokens=max_tokens,
        )
        if not isinstance(parsed, dict) or parsed.get("ok") is not True:
            raise RuntimeError(f"TreeRAG LLM preflight smoke check returned unexpected JSON: {parsed!r}")

    def _key(self, *, prompt_version: str, purpose: str, messages: Sequence[Dict[str, str]], max_tokens: int) -> str:
        payload = {
            "prompt_version": prompt_version,
            "purpose": purpose,
            "model": self.model,
            "max_tokens": int(max_tokens),
            "messages": list(messages),
        }
        return hashlib.sha256(json.dumps(payload, ensure_ascii=False, sort_keys=True).encode("utf-8")).hexdigest()

    def call_json(
        self,
        *,
        prompt_version: str,
        purpose: str,
        messages: Sequence[Dict[str, str]],
        max_tokens: int,
    ) -> Any:
        key = self._key(prompt_version=prompt_version, purpose=purpose, messages=messages, max_tokens=max_tokens)
        with self._lock:
            cached = self._cache.get(key)
        if cached is not None:
            with self._lock:
                self.cache_hits += 1
                self._usage_by_purpose[purpose]["cache_hits"] += 1
            return cached

        last_err: Optional[BaseException] = None
        use_json_mode = True
        max_attempts = 8
        for attempt in range(1, max_attempts + 1):
            try:
                timeout_seconds = float(self.llm_timeout_seconds) + 10.0
                previous_handler = signal.getsignal(signal.SIGALRM)

                def _timeout_handler(signum: int, frame: Any) -> None:
                    raise TimeoutError(f"TreeRAG LLM {purpose} call timed out after {timeout_seconds}s")

                signal.signal(signal.SIGALRM, _timeout_handler)
                signal.setitimer(signal.ITIMER_REAL, float(timeout_seconds))
                kwargs = {
                    "model": self.model,
                    "messages": list(messages),
                    "temperature": 0,
                    "max_tokens": int(max_tokens),
                }
                if use_json_mode:
                    kwargs["response_format"] = {"type": "json_object"}
                try:
                    rsp = self.client.chat.completions.create(**kwargs)
                    content = (rsp.choices[0].message.content or "").strip()
                    parsed = _extract_json_payload(content)
                    usage = getattr(rsp, "usage", None)
                    prompt_tokens = int(getattr(usage, "prompt_tokens", 0) or 0) if usage is not None else 0
                    completion_tokens = int(getattr(usage, "completion_tokens", 0) or 0) if usage is not None else 0
                    total_tokens = int(getattr(usage, "total_tokens", 0) or 0) if usage is not None else prompt_tokens + completion_tokens
                finally:
                    signal.setitimer(signal.ITIMER_REAL, 0.0)
                    signal.signal(signal.SIGALRM, previous_handler)
                break
            except Exception as e:
                last_err = e
                msg = str(e).lower()
                if use_json_mode and ("response_format" in msg or "json_object" in msg or "unsupported" in msg):
                    use_json_mode = False
                if attempt < max_attempts:
                    print(
                        f"[treerag] LLM retry {attempt}/{max_attempts} purpose={purpose}: {type(e).__name__}: {e}",
                        file=sys.stderr,
                        flush=True,
                    )
                    self._reset_client()
                    time.sleep(min(3.0 * attempt, 20.0))
                    continue
                raise RuntimeError(f"TreeRAG LLM {purpose} call failed; no fallback is allowed: {e}") from e

        row = {
            "key": key,
            "prompt_version": prompt_version,
            "purpose": purpose,
            "model": self.model,
            "parsed": parsed,
            "raw": content,
            "usage": {
                "prompt_tokens": prompt_tokens,
                "completion_tokens": completion_tokens,
                "total_tokens": total_tokens,
            },
            "created_at": time.time(),
        }
        with self._lock:
            self._cache[key] = parsed
            self.api_calls += 1
            self.prompt_tokens += prompt_tokens
            self.completion_tokens += completion_tokens
            self.total_tokens += total_tokens
            purpose_usage = self._usage_by_purpose[purpose]
            purpose_usage["prompt_tokens"] += prompt_tokens
            purpose_usage["completion_tokens"] += completion_tokens
            purpose_usage["total_tokens"] += total_tokens
            purpose_usage["api_calls"] += 1
            with open(self.cache_path, "a", encoding="utf-8") as f:
                f.write(json.dumps(row, ensure_ascii=False) + "\n")
                f.flush()
                os.fsync(f.fileno())
        return parsed

    def smoke_check(self, max_tokens: int = 48) -> None:
        parsed = self.call_json(
            prompt_version="treerag-paper-smoke-qwen-v1",
            purpose="smoke_check",
            messages=[
                {"role": "system", "content": "Return JSON only."},
                {"role": "user", "content": 'Return exactly {"ok": true}.'},
            ],
            max_tokens=max_tokens,
        )
        if not isinstance(parsed, dict) or parsed.get("ok") is not True:
            raise RuntimeError(f"TreeRAG LLM smoke check returned unexpected JSON: {parsed!r}")


def _task_type_counts(tasks: Sequence[AgentTask]) -> Dict[str, int]:
    return dict(sorted(Counter(str(t.task_type or "unknown") for t in tasks).items()))


def _validate_tasks(tasks: Sequence[AgentTask], bundles_by_doc: Dict[str, Any]) -> None:
    missing: List[str] = []
    for i, task in enumerate(tasks, start=1):
        bundle = bundles_by_doc.get(task.doc_id or "")
        if bundle is None:
            missing.append(f"task#{i} missing doc_id={task.doc_id!r}")
            continue
        nodes = {line_node_id(bundle.doc_id, r.line_id) for r in bundle.lines}
        bad = [n for n in task.gold_nodes if n not in nodes]
        if bad:
            missing.append(f"task#{i} doc_id={task.doc_id!r} missing gold_nodes={bad}")
    if missing:
        raise RuntimeError("tasks are not aligned with corpus:\n" + "\n".join(missing[:20]))


def _load_required_inspect_registry(paths: Sequence[Path], tasks: Sequence[AgentTask]) -> Dict[str, Dict[str, Any]]:
    registry = load_inspect_registry(paths)
    if not registry:
        raise RuntimeError(f"--inspect-judge requires a non-empty Inspect registry; paths={list(paths)!r}")
    for idx, task in enumerate(tasks, start=1):
        iid = (task.inspect_id or "").strip()
        if not iid or iid not in registry:
            raise RuntimeError(
                "--inspect-judge requires every TreeRAG task inspect_id to exist in registry: "
                f"task#{idx} inspect_id={iid!r} registry_size={len(registry)}"
            )
    return registry


def _clean_text(text: str) -> str:
    lines = [re.sub(r"\s+", " ", ln.strip()) for ln in str(text or "").splitlines()]
    return "\n".join(ln for ln in lines if ln).strip()


def _short_title(text: str, *, max_chars: int = 160) -> str:
    text = _clean_text(text)
    if not text:
        return "empty"
    text = re.sub(r"^\s*\\(sub)*section\*?\{(.+)\}\s*$", r"\2", text)
    text = re.sub(r"^\s*\\(title|caption|paragraph|subparagraph)\*?\{(.+)\}\s*$", r"\2", text)
    return text[:max_chars]


def _ancestor_indices(parent_by_idx: Sequence[Optional[int]], idx: int) -> List[int]:
    out: List[int] = []
    cur = parent_by_idx[idx]
    seen = 0
    while cur is not None and seen < len(parent_by_idx) + 1:
        out.append(cur)
        cur = parent_by_idx[cur]
        seen += 1
    out.reverse()
    return out


def _build_embedding_text(
    *,
    level: int,
    path_titles: Sequence[str],
    title: str,
    text: str,
    path_char_limit: int,
) -> str:
    # TreeRAG embeds each chunk with high-level title context. Keep the
    # evidence text itself unchanged; the prefix only affects retrieval.
    path = " > ".join(t for t in path_titles if t).strip()
    if len(path) > path_char_limit:
        path = path[-path_char_limit:]
    parts = [f"Level: {level}"]
    if path:
        parts.append(f"Hierarchical path: {path}")
    if title:
        parts.append(f"Current title: {title}")
    parts.append(f"Chunk content: {_clean_text(text) or ' '}")
    return "\n".join(parts)


def _leaf_indices_for(
    idx: int,
    children_by_idx: Dict[int, Tuple[int, ...]],
    memo: Dict[int, Tuple[int, ...]],
) -> Tuple[int, ...]:
    if idx in memo:
        return memo[idx]
    children = children_by_idx.get(idx, ())
    if not children:
        memo[idx] = (idx,)
        return memo[idx]
    out: List[int] = []
    for child in children:
        out.extend(_leaf_indices_for(child, children_by_idx, memo))
    memo[idx] = tuple(dict.fromkeys(out))
    return memo[idx]


def _coerce_level(value: Any, *, max_level: int) -> int:
    try:
        level = int(value)
    except Exception:
        try:
            level = int(float(str(value).strip()))
        except Exception as e:
            raise RuntimeError(f"TreeRAG LLM produced a non-integer level: {value!r}") from e
    return max(0, min(int(max_level), level))


def _normalize_tree_items(
    parsed: Any,
    *,
    expected_line_ids: Sequence[int],
    max_level: int,
    strict: bool = True,
) -> Dict[int, Tuple[int, str]]:
    if isinstance(parsed, dict):
        items = parsed.get("items")
    else:
        items = parsed
    if not isinstance(items, list):
        raise RuntimeError(f"TreeRAG tree-chunking response must contain an items list, got: {parsed!r}")

    out: Dict[int, Tuple[int, str]] = {}
    for item in items:
        if not isinstance(item, dict):
            raise RuntimeError(f"TreeRAG tree-chunking item is not an object: {item!r}")
        if "line_id" not in item or "level" not in item:
            raise RuntimeError(f"TreeRAG tree-chunking item misses line_id/level: {item!r}")
        line_id = int(item["line_id"])
        if line_id in out:
            raise RuntimeError(f"TreeRAG tree-chunking response duplicated line_id={line_id}")
        title = _clean_text(str(item.get("title") or item.get("heading") or "untitled"))
        out[line_id] = (_coerce_level(item["level"], max_level=max_level), title[:180] or "untitled")

    expected = {int(x) for x in expected_line_ids}
    got = set(out)
    missing = sorted(expected - got)
    extra = sorted(got - expected)
    if strict and (missing or extra):
        raise RuntimeError(
            "TreeRAG tree-chunking response line_id mismatch: "
            f"missing={missing[:20]} extra={extra[:20]}"
        )
    return out


def _tree_chunk_messages(
    bundle: Any,
    batch: Sequence[Any],
    *,
    args: argparse.Namespace,
    start: int,
    end: int,
    repair_line_ids: Optional[Sequence[int]] = None,
) -> List[Dict[str, str]]:
    line_char_limit = int(args.tree_line_char_limit)
    chunks = [
        {
            "line_id": int(rec.line_id),
            "text": (_clean_text(rec.content) or " ")[:line_char_limit],
        }
        for rec in batch
    ]
    return [
        {
            "role": "system",
            "content": (
                "You are the TreeRAG Tree-Chunking black-box model for scientific long-document retrieval. "
                "Given ordered preprocessed document chunks, assign each chunk a hierarchy level and a short retrieval title. "
                "Use only the provided chunk text. Return JSON only."
            ),
        },
        {
            "role": "user",
            "content": (
                "Follow the TreeRAG Tree-Chunking behavior.\n"
                "For every input chunk, return exactly one object with these fields:\n"
                "- line_id: copy the input integer exactly\n"
                "- level: integer hierarchy depth, where 0 is document/global title/front matter, "
                "1 is a top-level section, 2 is a subsection/topic, 3 is paragraph/detail, "
                f"and deeper details may use up to {int(args.tree_max_level)}\n"
                "- title: concise semantic title for retrieval; do not answer any question\n\n"
                'Return exactly this JSON shape: {"items":[{"line_id":1,"level":0,"title":"..."}]}.\n\n'
                + (
                    "Important: return entries for every line_id listed below and no others.\n"
                    if repair_line_ids is not None
                    else ""
                )
                + (
                    f"Target line_ids: {sorted(int(x) for x in repair_line_ids)}\n\n"
                    if repair_line_ids is not None
                    else ""
                )
                + f"Document id: {bundle.doc_id}\n"
                f"Batch line index range: {start}-{end - 1}\n"
                "Chunks JSON:\n"
                + json.dumps(chunks, ensure_ascii=False, indent=2)
            ),
        },
    ]


def _llm_tree_annotations(
    bundle: Any,
    *,
    args: argparse.Namespace,
    llm: RequiredOpenAITreeRagLLM,
) -> Tuple[List[int], List[str]]:
    lines = list(bundle.lines)
    if not lines:
        raise RuntimeError(f"doc_id={bundle.doc_id} has no lines for TreeRAG")

    batch_size = int(args.tree_lines_per_call)
    if batch_size <= 0:
        batch_size = len(lines)
    levels_by_line: Dict[int, int] = {}
    titles_by_line: Dict[int, str] = {}
    def _annotate_batch(batch: Sequence[Any], start: int, end: int) -> None:
        if not batch:
            return
        pending_line_ids = [int(r.line_id) for r in batch]
        attempts = 0
        while pending_line_ids:
            attempts += 1
            current_batch = [r for r in batch if int(r.line_id) in set(pending_line_ids)]
            try:
                parsed = llm.call_json(
                    prompt_version=TREE_CHUNK_PROMPT_VERSION,
                    purpose="tree_chunking",
                    messages=_tree_chunk_messages(
                        bundle,
                        current_batch,
                        args=args,
                        start=start,
                        end=end,
                        repair_line_ids=pending_line_ids if attempts > 1 else None,
                    ),
                    max_tokens=int(args.tree_max_tokens),
                )
                normalized = _normalize_tree_items(
                    parsed,
                    expected_line_ids=[int(r.line_id) for r in current_batch],
                    max_level=int(args.tree_max_level),
                    strict=False,
                )
                for line_id, (level, title) in normalized.items():
                    levels_by_line[line_id] = level
                    titles_by_line[line_id] = title
                got = set(normalized)
                pending_line_ids = [lid for lid in pending_line_ids if lid not in got]
                if pending_line_ids and len(current_batch) > 1 and attempts >= 2:
                    mid = len(current_batch) // 2
                    if mid <= 0:
                        break
                    _annotate_batch(current_batch[:mid], start, start + mid)
                    _annotate_batch(current_batch[mid:], start + mid, end)
                    return
                if attempts >= 3 and pending_line_ids:
                    raise RuntimeError(
                        f"TreeRAG tree-chunking still missing line_ids after retries for doc_id={bundle.doc_id}: {pending_line_ids[:20]}"
                    )
            except Exception:
                if len(current_batch) > 1:
                    mid = len(current_batch) // 2
                    if mid <= 0:
                        raise
                    _annotate_batch(current_batch[:mid], start, start + mid)
                    _annotate_batch(current_batch[mid:], start + mid, end)
                    return
                if attempts >= 3:
                    raise
                continue

    for start in range(0, len(lines), batch_size):
        end = min(len(lines), start + batch_size)
        _annotate_batch(lines[start:end], start, end)

    levels: List[int] = []
    titles: List[str] = []
    for rec in lines:
        lid = int(rec.line_id)
        if lid not in levels_by_line or lid not in titles_by_line:
            raise RuntimeError(f"TreeRAG LLM tree annotations missing doc_id={bundle.doc_id} line_id={lid}")
        levels.append(levels_by_line[lid])
        titles.append(titles_by_line[lid])
    return levels, titles


def _parse_tree(
    bundle: Any,
    *,
    args: argparse.Namespace,
    llm: RequiredOpenAITreeRagLLM,
    path_char_limit: int,
) -> List[TreeRagNode]:
    lines = list(bundle.lines)
    if not lines:
        raise RuntimeError(f"doc_id={bundle.doc_id} has no lines for TreeRAG")
    levels, titles = _llm_tree_annotations(bundle, args=args, llm=llm)
    if len(levels) != len(lines):
        raise RuntimeError(f"doc_id={bundle.doc_id} level count does not match line count")

    parents = build_parent_pointers(levels)
    children_tmp: Dict[int, List[int]] = defaultdict(list)
    for idx, pidx in enumerate(parents):
        if pidx is not None:
            children_tmp[pidx].append(idx)
    children_by_idx = {idx: tuple(vals) for idx, vals in children_tmp.items()}
    leaf_memo: Dict[int, Tuple[int, ...]] = {}

    nodes: List[TreeRagNode] = []
    for idx, rec in enumerate(lines):
        ancestors = _ancestor_indices(parents, idx)
        path_titles = [titles[a] for a in ancestors]
        text = _clean_text(rec.content)
        title = titles[idx]
        node_id = f"{bundle.doc_id}:TREERAG_{int(rec.line_id)}"
        nodes.append(
            TreeRagNode(
                node_id=node_id,
                line_id=int(rec.line_id),
                level=int(levels[idx]),
                text=text or " ",
                title=title,
                embedding_text=_build_embedding_text(
                    level=int(levels[idx]),
                    path_titles=path_titles,
                    title=title,
                    text=text,
                    path_char_limit=path_char_limit,
                ),
                parent_idx=parents[idx],
                child_indices=children_by_idx.get(idx, ()),
                leaf_indices=_leaf_indices_for(idx, children_by_idx, leaf_memo),
            )
        )
    return nodes


def _tree_cache_key(args: argparse.Namespace, doc_id: str, line_count: int) -> str:
    payload = {
        "doc_id": doc_id,
        "line_count": line_count,
        "embedding_model": args.embedding_model,
        "tree_model": getattr(args, "resolved_treerag_model", None) or getattr(args, "treerag_model", None) or DEFAULT_TREERAG_LLM_MODEL,
        "tree_chunk_prompt_version": TREE_CHUNK_PROMPT_VERSION,
        "tree_lines_per_call": int(args.tree_lines_per_call),
        "tree_line_char_limit": int(args.tree_line_char_limit),
        "tree_max_level": int(args.tree_max_level),
        "tree_max_tokens": int(args.tree_max_tokens),
        "path_char_limit": int(args.path_char_limit),
        "treerag_adapter": "paper_llm_tree_chunking_btr_v2",
    }
    return hashlib.sha256(json.dumps(payload, sort_keys=True).encode("utf-8")).hexdigest()[:16]


def _serialize_task(task: AgentTask) -> Dict[str, Any]:
    return {
        "query": task.query,
        "doc_id": task.doc_id,
        "gold_nodes": list(task.gold_nodes),
        "gold_answer": task.gold_answer,
        "task_type": task.task_type,
        "cross_section": task.cross_section,
        "inspect_id": task.inspect_id,
        "compose_format_hint": task.compose_format_hint,
    }


def _deserialize_task(payload: Dict[str, Any]) -> AgentTask:
    return AgentTask(
        query=str(payload.get("query", "")),
        doc_id=payload.get("doc_id"),
        gold_nodes=list(payload.get("gold_nodes") or []),
        gold_answer=str(payload.get("gold_answer", "")),
        task_type=str(payload.get("task_type", "unknown")),
        cross_section=payload.get("cross_section"),
        inspect_id=payload.get("inspect_id"),
        compose_format_hint=str(payload.get("compose_format_hint", "")),
    )


def _serialize_chunk(chunk: Chunk) -> Dict[str, Any]:
    return {
        "node_id": chunk.node_id,
        "doc_id": chunk.doc_id,
        "text": chunk.text,
        "line_ids": list(chunk.line_ids),
        "section_id": chunk.section_id,
        "text_line_id_groups": [list(g) for g in chunk.text_line_id_groups] if chunk.text_line_id_groups is not None else None,
    }


def _deserialize_chunk(payload: Dict[str, Any]) -> Chunk:
    groups = payload.get("text_line_id_groups")
    return Chunk(
        node_id=str(payload["node_id"]),
        doc_id=str(payload["doc_id"]),
        text=str(payload.get("text", "")),
        line_ids=tuple(int(x) for x in (payload.get("line_ids") or [])),
        section_id=payload.get("section_id"),
        text_line_id_groups=(
            tuple(tuple(int(y) for y in group) for group in groups)
            if groups is not None
            else None
        ),
    )


def _serialize_scored_chunks(scored: Sequence[Tuple[Chunk, float]]) -> List[Dict[str, Any]]:
    return [{"chunk": _serialize_chunk(chunk), "score": float(score)} for chunk, score in scored]


def _deserialize_scored_chunks(payload: Sequence[Dict[str, Any]]) -> List[Tuple[Chunk, float]]:
    out: List[Tuple[Chunk, float]] = []
    for item in payload:
        out.append((_deserialize_chunk(item["chunk"]), float(item["score"])))
    return out


def _task_checkpoint_signature(args: argparse.Namespace) -> str:
    payload = {
        "test_jsonl": str(Path(args.test_jsonl).resolve()),
        "tasks": str(Path(args.tasks).resolve()),
        "budgets": str(args.budgets),
        "embedding_model": args.embedding_model,
        "tree_model": getattr(args, "resolved_treerag_model", None) or getattr(args, "treerag_model", None) or DEFAULT_TREERAG_LLM_MODEL,
        "intent_mode": args.intent_mode,
        "tree_lines_per_call": int(args.tree_lines_per_call),
        "tree_line_char_limit": int(args.tree_line_char_limit),
        "tree_max_level": int(args.tree_max_level),
        "tree_max_tokens": int(args.tree_max_tokens),
        "intent_max_tokens": int(args.intent_max_tokens),
        "initial_top_k": int(args.initial_top_k),
        "root_to_leaf_decay": float(args.root_to_leaf_decay),
        "leaf_to_parent_decay": float(args.leaf_to_parent_decay),
        "max_traversal_leaves": int(args.max_traversal_leaves),
        "path_char_limit": int(args.path_char_limit),
        "max_tasks": int(args.max_tasks),
        "max_docs": int(args.max_docs),
        "adapter": "paper_llm_tree_chunking_btr_v2",
    }
    return hashlib.sha256(json.dumps(payload, sort_keys=True).encode("utf-8")).hexdigest()


def _budget_score_signature(args: argparse.Namespace, budget: int, task_checkpoint_signature: str) -> str:
    payload = {
        "task_checkpoint_signature": task_checkpoint_signature,
        "budget": int(budget),
        "compose_judge": bool(getattr(args, "compose_judge", False)),
        "inspect_judge": bool(getattr(args, "inspect_judge", False)),
        "inspect_tasks": [str(Path(p).resolve()) for p in (getattr(args, "inspect_tasks", None) or [])],
        "compose_model": os.environ.get("COMPOSE_MODEL", "").strip(),
        "judge_model": os.environ.get("JUDGE_MODEL", "").strip(),
        "judge_semantic_primary": os.environ.get("JUDGE_SEMANTIC_PRIMARY", "").strip(),
        "evidence_header_protocol": EVIDENCE_HEADER_PROTOCOL,
        "scope_scoring_protocol": "structured_item_alignment_v2",
        "adapter": "treerag_budget_score_cache_v4",
    }
    return hashlib.sha256(json.dumps(payload, ensure_ascii=False, sort_keys=True).encode("utf-8")).hexdigest()


def _load_budget_score_cache(path: Path, signature: str) -> Dict[int, Dict[str, Any]]:
    if not path.exists():
        return {}
    try:
        with open(path, "r", encoding="utf-8") as f:
            first = f.readline().strip()
            if not first:
                return {}
            meta = json.loads(first)
            if meta.get("kind") != "meta" or meta.get("signature") != signature:
                print(f"[treerag] ignoring stale budget-score cache {path}", file=sys.stderr, flush=True)
                return {}
            out: Dict[int, Dict[str, Any]] = {}
            for line in f:
                line = line.strip()
                if not line:
                    continue
                row = json.loads(line)
                if row.get("kind") != "task":
                    continue
                out[int(row["task_idx"])] = dict(row["treerag"])
            return out
    except Exception as e:
        print(f"[treerag] failed to read budget-score cache {path}: {e}", file=sys.stderr, flush=True)
        return {}


def _append_budget_score_cache(path: Path, signature: str, task_idx: int, treerag_score: Dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not path.exists():
        meta = {"kind": "meta", "signature": signature, "created_at": time.time()}
        with open(path, "w", encoding="utf-8") as f:
            f.write(json.dumps(meta, ensure_ascii=False) + "\n")
    row = {"kind": "task", "task_idx": int(task_idx), "treerag": treerag_score}
    with open(path, "a", encoding="utf-8") as f:
        f.write(json.dumps(row, ensure_ascii=False) + "\n")
        f.flush()
        os.fsync(f.fileno())


def _load_or_build_doc_index(
    bundle: Any,
    *,
    args: argparse.Namespace,
    cache_dir: Path,
    dense_model: Any,
    llm: RequiredOpenAITreeRagLLM,
) -> Tuple[TreeRagDocIndex, bool]:
    key = _tree_cache_key(args, bundle.doc_id, len(bundle.lines))
    path = cache_dir / "trees" / f"{bundle.doc_id}.{key}.pkl"
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists() and not args.rebuild_cache:
        with open(path, "rb") as f:
            return pickle.load(f), True

    nodes = _parse_tree(bundle, args=args, llm=llm, path_char_limit=args.path_char_limit)
    embedding_chunks = [
        Chunk(
            node_id=n.node_id,
            doc_id=bundle.doc_id,
            text=n.embedding_text,
            line_ids=(n.line_id,),
            section_id=f"treerag_level_{n.level}",
        )
        for n in nodes
    ]
    embeddings = encode_chunks_normalized(dense_model, embedding_chunks, batch_size=args.embedding_batch_size)
    doc_index = TreeRagDocIndex(
        doc_id=bundle.doc_id,
        tree_source="llm_tree_chunking",
        nodes=tuple(nodes),
        node_id_to_idx={n.node_id: i for i, n in enumerate(nodes)},
        embeddings=embeddings,
        cache_key=key,
    )
    with open(path, "wb") as f:
        pickle.dump(doc_index, f)
    return doc_index, False


def _chunk_for_node(doc_index: TreeRagDocIndex, idx: int) -> Chunk:
    node = doc_index.nodes[idx]
    return Chunk(
        node_id=node.node_id,
        doc_id=doc_index.doc_id,
        text=node.text,
        line_ids=(node.line_id,),
        section_id=f"treerag_level_{node.level}",
    )


def _dense_scores(doc_index: TreeRagDocIndex, query: str, dense_model: Any) -> Any:
    import numpy as np

    qv = encode_query_normalized(dense_model, query)
    return np.asarray(doc_index.embeddings @ qv, dtype=np.float64)


def _intent_messages(query: str) -> List[Dict[str, str]]:
    return [
        {
            "role": "system",
            "content": (
                "You are the TreeRAG query-intent black-box model. "
                "Return JSON only."
            ),
        },
        {
            "role": "user",
            "content": (
                "Classify whether TreeRAG should use Bidirectional Traversal Retrieval for this query.\n"
                "Return intent=1 only for summarization, overview, comparison, enumeration, concept-listing, "
                "or broad collection questions that need multiple related chunks across a document tree.\n"
                "Return intent=0 for precise fact lookup or single-evidence questions.\n\n"
                'Return exactly this JSON shape: {"intent":1} or {"intent":0}.\n\n'
                f"Query: {query}"
            ),
        },
    ]


def _should_use_btr(
    query: str,
    *,
    mode: str,
    llm: RequiredOpenAITreeRagLLM,
    max_tokens: int,
) -> bool:
    mode = (mode or "llm").strip().lower()
    if mode == "always":
        return True
    if mode == "never":
        return False
    if mode != "llm":
        raise RuntimeError(f"unsupported TreeRAG intent mode: {mode!r}")
    parsed = llm.call_json(
        prompt_version=INTENT_PROMPT_VERSION,
        purpose="intent_detection",
        messages=_intent_messages(query),
        max_tokens=int(max_tokens),
    )
    if not isinstance(parsed, dict) or "intent" not in parsed:
        raise RuntimeError(f"TreeRAG intent response must be a JSON object with intent: {parsed!r}")
    intent = parsed.get("intent")
    if intent in (1, True, "1", "true", "True"):
        return True
    if intent in (0, False, "0", "false", "False"):
        return False
    raise RuntimeError(f"TreeRAG intent value must be 0 or 1: {parsed!r}")


def _limited_leaves(leaves: Tuple[int, ...], max_leaves: int) -> Tuple[int, ...]:
    if max_leaves <= 0 or len(leaves) <= max_leaves:
        return leaves
    return leaves[:max_leaves]


def _gather_treerag_candidates(
    doc_index: TreeRagDocIndex,
    query: str,
    *,
    dense_model: Any,
    args: argparse.Namespace,
    use_btr: bool,
) -> Scored:
    best: Dict[str, Tuple[Chunk, float]] = {}

    for qi, q in enumerate(_build_retrieval_queries(query)):
        weight = _query_weight(qi)
        sims = _dense_scores(doc_index, q, dense_model)
        if sims.size == 0:
            continue
        import numpy as np

        ranked = np.argsort(-sims)
        initial = [int(i) for i in ranked[: max(1, int(args.initial_top_k))]]
        per_query_scores: Dict[int, float] = {}

        if use_btr:
            for rank, idx in enumerate(initial):
                node = doc_index.nodes[idx]
                hit_score = float(sims[idx]) * weight
                if node.child_indices:
                    root_idx = idx
                    base_decay = float(args.root_to_leaf_decay)
                elif node.parent_idx is not None:
                    root_idx = int(node.parent_idx)
                    base_decay = float(args.leaf_to_parent_decay)
                else:
                    root_idx = idx
                    base_decay = 1.0
                leaves = _limited_leaves(doc_index.nodes[root_idx].leaf_indices, int(args.max_traversal_leaves))
                for offset, leaf_idx in enumerate(leaves):
                    leaf_dense = float(sims[leaf_idx]) * weight
                    traversal = hit_score * base_decay
                    # Keep sibling leaves close to the hit, while preserving
                    # query relevance and deterministic ordering.
                    score = max(leaf_dense, traversal - (offset * 1e-7) - (rank * 1e-8))
                    prev = per_query_scores.get(leaf_idx)
                    if prev is None or score > prev:
                        per_query_scores[leaf_idx] = score
        else:
            for rank, idx in enumerate(initial):
                per_query_scores[idx] = max(
                    per_query_scores.get(idx, float("-inf")),
                    (float(sims[idx]) * weight) - (rank * 1e-8),
                )

        for idx, score in per_query_scores.items():
            chunk = _chunk_for_node(doc_index, idx)
            prev = best.get(chunk.node_id)
            if prev is None or float(score) > float(prev[1]):
                best[chunk.node_id] = (chunk, float(score))

    out = list(best.values())
    out.sort(key=lambda x: -x[1])
    return out


def _chunks_to_retrieved_nodes(chunks: Sequence[Chunk]) -> List[str]:
    seen: set[str] = set()
    out: List[str] = []
    for c in chunks:
        for lid in c.line_ids:
            node = f"{c.doc_id}:L{lid}"
            if node not in seen:
                seen.add(node)
                out.append(node)
    return out


def _snapshot_retry_wait_delta(before: Dict[str, Dict[str, Any]], after: Dict[str, Dict[str, Any]]) -> float:
    total = 0.0
    for purpose, after_block in after.items():
        before_block = before.get(purpose, {})
        total += max(
            0.0,
            float(after_block.get("retry_wait_seconds", 0.0) or 0.0)
            - float(before_block.get("retry_wait_seconds", 0.0) or 0.0),
        )
    return total


def _effective_task_type_for_compose(
    task: AgentTask, inspect_by_id: Optional[Dict[str, Dict[str, Any]]]
) -> str:
    """Mirror Gold/Flat: prefer inspect metadata task_type when the task hits the registry."""
    base = (task.task_type or "unknown").strip() or "unknown"
    iid = str(getattr(task, "inspect_id", None) or "").strip()
    if not (inspect_by_id and iid and iid in inspect_by_id):
        return base
    inst = inspect_by_id[iid]
    md = inst.get("metadata") if isinstance(inst.get("metadata"), dict) else {}
    it = str(md.get("task_type", "") or "").strip()
    return it if it else base


def _query_tokens_for_compose(query: str) -> List[str]:
    raw = (query or "").lower()
    toks = re.findall(r"[a-z0-9_]+|[\u4e00-\u9fff]", raw)
    return [t for t in toks if t.strip()]


def _prepare_compose_evidence_text(
    query: str,
    evidence_text: str,
    *,
    budget_chars: int,
    task_type: str,
) -> str:
    text = (evidence_text or "").strip()
    if not text:
        return ""
    if os.environ.get("BODYRICH_COMPOSE_CLEAN_EVIDENCE", "1").strip().lower() in {"0", "false", "no"}:
        return text[: max(1, int(budget_chars))]

    tt = (task_type or "").strip().lower()
    keep_path = tt == "multi_hop"
    blocks: List[Tuple[str, str]] = []
    for raw_block in re.split(r"\n\s*\n(?=\[)", text):
        block = raw_block.strip()
        if not block:
            continue
        lines = block.splitlines()
        if not lines:
            continue
        header = lines[0].strip()
        body_lines = list(lines[1:]) if keep_path else [ln for ln in lines[1:] if not ln.strip().startswith("PATH:")]
        body = "\n".join(body_lines).strip()
        if not body:
            continue
        blocks.append((header, body))
    if not blocks:
        cleaned = re.sub(r"(?m)^PATH:.*\n?", "", text).strip()
        return (cleaned or text)[: max(1, int(budget_chars))]

    rerank = tt in {"scope_collection", "regulatory_coverage"}
    if rerank:
        q_toks = _query_tokens_for_compose(query)

        def _score_block(item: Tuple[str, str]) -> Tuple[int, int]:
            body = item[1].lower()
            overlap = sum(1 for t in q_toks if t in body)
            return (overlap, len(body))

        blocks.sort(key=_score_block, reverse=True)

    deduped: List[Tuple[str, str]] = []
    seen_body: set[str] = set()
    for h, b in blocks:
        b_norm = re.sub(r"\s+", " ", b).strip()
        if not b_norm or b_norm in seen_body:
            continue
        seen_body.add(b_norm)
        deduped.append((h, b))

    out_parts: List[str] = []
    used = 0
    for h, b in deduped:
        piece = f"{h}\n{b}"
        add_len = len(piece) + (2 if out_parts else 0)
        if used + add_len <= int(budget_chars):
            out_parts.append(piece)
            used += add_len
            continue
        remain = int(budget_chars) - used - (2 if out_parts else 0)
        if remain > 40:
            out_parts.append(piece[:remain])
        break
    if out_parts:
        return "\n\n".join(out_parts)
    return text[: max(1, int(budget_chars))]


def _score_at_budget(
    task: AgentTask,
    scored: Scored,
    budget: int,
    *,
    compose_judge: bool = False,
    inspect_by_id: Optional[Dict[str, Dict[str, Any]]] = None,
    use_inspect_judge: bool = False,
) -> Dict[str, Any]:
    fill = evaluate_at_budget(scored, budget_chars=budget)
    retrieved_nodes = _chunks_to_retrieved_nodes(fill.kept_chunks)
    budget_metrics = compute_budget_retrieval_metrics(fill.kept_chunks, task.gold_nodes)
    line_metrics = retrieval_metrics(retrieved_nodes, task.gold_nodes, k_list=(1, 3, 5))
    out: Dict[str, Any] = {
        "evidence_chars_actual": fill.evidence_chars_actual,
        "n_chunks_kept": fill.n_chunks_kept,
        "truncated_last": fill.truncated_last,
        "kept_chunk_ids": [c.node_id for c in fill.kept_chunks],
        "retrieved_nodes": retrieved_nodes,
        "evidence_text": fill.evidence_text,
        "evidence_preview": fill.evidence_text[:800],
        "budget": budget_metrics,
        "line_retrieval": line_metrics,
    }
    if not compose_judge:
        return out

    inspect_task: Optional[Dict[str, Any]] = None
    format_constraints = task.compose_format_hint
    iid = (task.inspect_id or "").strip()
    if inspect_by_id and iid and iid in inspect_by_id:
        inspect_task = inspect_by_id[iid]
        if not format_constraints:
            format_constraints = inspect_compose_format_block(inspect_task)

    eff_tt = _effective_task_type_for_compose(task, inspect_by_id)
    compose_evidence = _prepare_compose_evidence_text(
        task.query,
        fill.evidence_text or "",
        budget_chars=int(budget),
        task_type=eff_tt,
    )
    compose_usage_before = snapshot_usage()
    compose_t0 = time.time()
    composed = compose_answer_llm(
        task.query,
        task_type=eff_tt,
        evidence_text=compose_evidence,
        max_answer_chars=min(1024, max(256, int(budget))),
        budget_chars=int(budget),
        format_constraints=format_constraints,
    )
    compose_retry_wait_seconds = _snapshot_retry_wait_delta(compose_usage_before, snapshot_usage())
    compose_seconds = max(0.0, time.time() - compose_t0 - compose_retry_wait_seconds)
    judge_usage_before = snapshot_usage()
    judge_t0 = time.time()
    score_evidence = float(budget_metrics["coverage_budget_lenient"])
    inspect_meta: Dict[str, Any] = {"inspect_judge_used": False, "inspect_id": iid or None}
    if use_inspect_judge:
        if inspect_task is None:
            raise RuntimeError(f"--inspect-judge enabled but inspect_id={iid!r} is missing from registry")
        eids = evidence_line_ids_from_runner(
            retrieved_nodes=retrieved_nodes,
            kept_chunks=fill.kept_chunks,
            doc_id=task.doc_id,
        )
        pred_out = build_inspect_pred_output(composed, evidence_line_ids=eids, inspect_task=inspect_task)
        c_sc, e_sc, insp_extra = score_sample(inspect_task, pred_out)
        score_task = float(c_sc)
        score_evidence = float(e_sc)
        inspect_meta = {
            "inspect_judge_used": True,
            "inspect_id": iid,
            "inspect_evidence_score": float(e_sc),
            "inspect_content_score": float(c_sc),
            **{f"inspect_{k}": v for k, v in insp_extra.items()},
        }
    else:
        score_task = task_success_score(
            task.task_type,
            composed,
            task.gold_answer,
            gold_nodes=task.gold_nodes,
            evidence_text=fill.evidence_text,
        )
    judge_retry_wait_seconds = _snapshot_retry_wait_delta(judge_usage_before, snapshot_usage())
    judge_seconds = max(0.0, time.time() - judge_t0 - judge_retry_wait_seconds)
    out.update(
        {
            "composed_answer": composed,
            "score_task": float(score_task),
            "score_evidence": float(score_evidence),
            "compose_seconds": compose_seconds,
            "judge_eval_seconds": judge_seconds,
            "retry_wait_seconds": compose_retry_wait_seconds + judge_retry_wait_seconds,
            **inspect_meta,
        }
    )
    return out


def _mean(xs: Iterable[Optional[float]]) -> Optional[float]:
    vals = [float(x) for x in xs if x is not None and not math.isnan(float(x))]
    return float(sum(vals) / len(vals)) if vals else None


def _summarize_arm(rows: Sequence[Dict[str, Any]], arm: str) -> Dict[str, Any]:
    out = {
        "chunk_hit@1_mean": _mean(r[arm]["budget"]["chunk_hit@1"] for r in rows),
        "mrr_chunks_mean": _mean(r[arm]["budget"]["mrr_chunks"] for r in rows),
        "coverage_budget_lenient_mean": _mean(r[arm]["budget"]["coverage_budget_lenient"] for r in rows),
        "precision@1_line_mean": _mean(r[arm]["line_retrieval"]["precision@1"] for r in rows),
        "precision@5_line_mean": _mean(r[arm]["line_retrieval"]["precision@5"] for r in rows),
        "coverage_line_mean": _mean(r[arm]["line_retrieval"]["coverage"] for r in rows),
        "evidence_chars_actual_mean": _mean(r[arm]["evidence_chars_actual"] for r in rows),
        "n_chunks_kept_mean": _mean(r[arm]["n_chunks_kept"] for r in rows),
    }
    if any("score_task" in r.get(arm, {}) for r in rows):
        out["score_task_mean"] = _mean(r[arm].get("score_task") for r in rows)
        out["score_evidence_mean"] = _mean(r[arm].get("score_evidence") for r in rows)
    return out


def _per_type(rows: Sequence[Dict[str, Any]], arm: str) -> Dict[str, Dict[str, Any]]:
    by_type: Dict[str, List[Dict[str, Any]]] = defaultdict(list)
    for row in rows:
        by_type[str(row.get("task_type") or "unknown")].append(row)
    return {tt: {"n": len(rs), **_summarize_arm(rs, arm)} for tt, rs in sorted(by_type.items())}


def _fmt(v: Any) -> str:
    return f"{float(v):.3f}" if isinstance(v, (int, float)) else "-"


def _fmt_delta(v: Any) -> str:
    return f"{float(v):+.3f}" if isinstance(v, (int, float)) else "-"


def _existing_result_paths() -> List[Path]:
    # Canonical fair-protocol Gold/Flat result (used for the summary markdown comparison;
    # also the cap source only if TREERAG_FAIR_CAP=1, which is OFF by default).
    return [
        PACKAGE_ROOT.parent.parent / "results" / "fair_clean_gold_flat_fair_clean_goldnav_e2_v1_b500.json",
    ]


def _raptor_result_paths() -> List[Path]:
    return [
        PACKAGE_ROOT / "results" / "arxiv_raptor_official_800equal_b300.json",
        PACKAGE_ROOT / "results" / "arxiv_raptor_official_800equal_b500.json",
        PACKAGE_ROOT / "results" / "arxiv_raptor_official_800equal_b1000.json",
    ]


def _llamaindex_result_paths() -> List[Path]:
    return [
        PACKAGE_ROOT / "results" / "arxiv_llamaindex_hierarchical_800equal_b300.json",
        PACKAGE_ROOT / "results" / "arxiv_llamaindex_hierarchical_800equal_b500.json",
        PACKAGE_ROOT / "results" / "arxiv_llamaindex_hierarchical_800equal_b1000.json",
    ]


def _task_match_key_from_task(task: Any) -> Tuple[str, str, str]:
    return (
        str(getattr(task, "inspect_id", "") or "").strip(),
        str(getattr(task, "doc_id", "") or "").strip(),
        str(getattr(task, "query", "") or "").strip(),
    )


def _task_match_key_from_row(row: Dict[str, Any]) -> Tuple[str, str, str]:
    return (
        str(row.get("inspect_id", "") or "").strip(),
        str(row.get("doc_id", "") or "").strip(),
        str(row.get("query", "") or "").strip(),
    )


def _cap_from_row(row: Dict[str, Any]) -> Optional[int]:
    vals: List[int] = []
    cc = row.get("candidate_counts") or {}
    vals.extend(int(cc[a]) for a in ("gold_hier", "pred_hier", "flat") if a in cc)
    for arm in ("hierarchical_gold", "hierarchical_pred", "flat"):
        arm_obj = row.get(arm)
        if isinstance(arm_obj, dict) and arm_obj.get("n_scored_candidates") is not None:
            vals.append(int(arm_obj.get("n_scored_candidates") or 0))
    positive_vals = [v for v in vals if v > 0]
    if not positive_vals:
        return None
    return min(positive_vals)


def _existing_cap_by_task(tasks: Sequence[Any]) -> Dict[int, int]:
    requested_keys = {_task_match_key_from_task(task) for task in tasks}
    key_caps_all: Dict[Tuple[str, str, str], int] = {}
    fallback_idx_caps: Dict[int, int] = {}

    for p in _existing_result_paths():
        if not p.exists():
            continue
        data = json.load(open(p, "r", encoding="utf-8"))
        rows = data.get("rows") or []
        idx_caps: Dict[int, int] = {}
        key_caps: Dict[Tuple[str, str, str], int] = {}
        for row in rows:
            if not isinstance(row, dict):
                continue
            cap = _cap_from_row(row)
            if cap is None:
                continue
            try:
                idx_caps[int(row.get("task_idx"))] = int(cap)
            except Exception:
                pass
            key = _task_match_key_from_row(row)
            if any(key):
                key_caps[key] = int(cap)
                prev = key_caps_all.get(key)
                key_caps_all[key] = int(cap) if prev is None else min(int(cap), int(prev))
        if not fallback_idx_caps and idx_caps:
            fallback_idx_caps = idx_caps

    aligned: Dict[int, int] = {}
    for i, task in enumerate(tasks, start=1):
        cap = key_caps_all.get(_task_match_key_from_task(task))
        if isinstance(cap, int) and cap > 0:
            aligned[i] = int(cap)
    if aligned:
        return aligned
    if fallback_idx_caps and len(fallback_idx_caps) == len(tasks):
        return fallback_idx_caps
    return {}


def _budget_from_payload(payload: Dict[str, Any], path: Path) -> Optional[int]:
    cfg = ((payload.get("summary") or {}).get("config") or {})
    raw = cfg.get("budget_chars")
    if raw is not None:
        return int(raw)
    m = re.search(r"_b(\d+)\.json$", path.name, re.IGNORECASE)
    if m:
        return int(m.group(1))
    return None


def _load_payloads(paths: Sequence[Path]) -> Dict[int, Dict[str, Any]]:
    out: Dict[int, Dict[str, Any]] = {}
    for p in paths:
        if not p.exists():
            continue
        d = json.load(open(p, "r", encoding="utf-8"))
        budget = _budget_from_payload(d, p)
        if budget is None:
            continue
        out[budget] = d
    return out


def _write_markdown(
    results: Sequence[Dict[str, Any]],
    path: Path,
    existing: Dict[int, Dict[str, Any]],
    raptor: Dict[int, Dict[str, Any]],
    llamaindex: Dict[int, Dict[str, Any]],
) -> None:
    lines: List[str] = ["# TreeRAG Baseline on arXiv 800", ""]
    lines.append(
        "Protocol: TreeRAG paper-style LLM Tree-Chunking path-prefix embeddings + LLM intent detection + Bidirectional Traversal Retrieval; retrieval-only metrics aligned to Gold/Pred/Flat, RAPTOR, and LlamaIndex arXiv 800 evaluations."
    )
    lines.append("")
    for payload in results:
        s = payload["summary"]
        budget = int(s["config"]["budget_chars"])
        base = (existing.get(budget) or {}).get("summary") or {}
        rap_sum = (raptor.get(budget) or {}).get("summary") or {}
        lih_sum = (llamaindex.get(budget) or {}).get("summary") or {}
        gold = base.get("gold_hier") or {}
        pred = base.get("pred_hier") or {}
        flat = base.get("flat") or {}
        rap = rap_sum.get("raptor_official") or {}
        lih = lih_sum.get("llamaindex_hierarchical") or {}
        tr = s["treerag"]
        lines.append(f"## budget={budget} (n={s['n_tasks']})")
        lines.append("")
        cfg = s.get("config") or {}
        usage = cfg.get("token_usage") or {}
        lines.append("Run accounting:")
        lines.append(f"- Runtime seconds: {_fmt(cfg.get('runtime_seconds'))}")
        lines.append(f"- Index/build seconds: {_fmt(cfg.get('index_seconds'))}")
        lines.append(f"- Retrieval/eval seconds: {_fmt(cfg.get('retrieval_eval_seconds'))}")
        lines.append(f"- Tree source: {cfg.get('tree_source')}")
        lines.append(f"- Tree/intent model: {cfg.get('tree_model')}")
        lines.append(f"- Intent mode: {cfg.get('intent_mode')}")
        lines.append(f"- LLM/API tokens: prompt={int(usage.get('prompt_tokens', 0) or 0)}, completion={int(usage.get('completion_tokens', 0) or 0)}, total={int(usage.get('total_tokens', 0) or 0)}")
        lines.append(f"- Doc-index cache hits: {int(cfg.get('doc_index_cache_hits', 0) or 0)} / {int(cfg.get('n_docs_indexed_for_tasks', 0) or 0)} docs")
        lines.append(f"- LLM cache hits: {int(cfg.get('llm_cache_hits', 0) or 0)}")
        lines.append("")
        lines.append("Effective scored candidates:")
        if base.get("effective_scored"):
            for arm, label in [("gold_hier", "Gold-hier"), ("pred_hier", "Pred-hier"), ("flat", "Flat-react")]:
                es = base["effective_scored"].get(arm) or {}
                lines.append(f"- {label}: n={int(es.get('n_chunks', 0))}, mean/task={_fmt(es.get('n_chunks_mean_per_task'))}")
        if rap_sum.get("effective_scored"):
            esr = rap_sum["effective_scored"].get("raptor_official") or {}
            lines.append(f"- RAPTOR-official: n={int(esr.get('n_chunks', 0))}, mean/task={_fmt(esr.get('n_chunks_mean_per_task'))}")
        if lih_sum.get("effective_scored"):
            esl = lih_sum["effective_scored"].get("llamaindex_hierarchical") or {}
            lines.append(f"- LlamaIndex-Hierarchical: n={int(esl.get('n_chunks', 0))}, mean/task={_fmt(esl.get('n_chunks_mean_per_task'))}")
        est = s["effective_scored"]["treerag"]
        lines.append(f"- TreeRAG: n={int(est.get('n_chunks', 0))}, mean/task={_fmt(est.get('n_chunks_mean_per_task'))}")
        lines.append("")
        lines.append("| Metric | Gold-hier | Pred-hier | Flat-react | RAPTOR-official | LlamaIndex-Hier | TreeRAG | d(Gold-TR) | d(Pred-TR) | d(Flat-TR) | d(RAPTOR-TR) | d(LIH-TR) |")
        lines.append("| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |")
        for key, label in [
            ("coverage_budget_lenient_mean", "Coverage@budget_lenient"),
            ("mrr_chunks_mean", "MRR@chunks"),
            ("chunk_hit@1_mean", "ChunkHit@1"),
            ("precision@1_line_mean", "Precision@1 line"),
            ("precision@5_line_mean", "Precision@5 line"),
            ("coverage_line_mean", "Coverage line"),
            ("evidence_chars_actual_mean", "Evidence chars"),
        ]:
            tv = tr.get(key)
            vals = [gold.get(key), pred.get(key), flat.get(key), rap.get(key), lih.get(key)]
            deltas = [
                (v - tv) if isinstance(v, (int, float)) and isinstance(tv, (int, float)) else None
                for v in vals
            ]
            lines.append(
                f"| {label} | {_fmt(vals[0])} | {_fmt(vals[1])} | {_fmt(vals[2])} | {_fmt(vals[3])} | {_fmt(vals[4])} | {_fmt(tv)} | "
                f"{_fmt_delta(deltas[0])} | {_fmt_delta(deltas[1])} | {_fmt_delta(deltas[2])} | {_fmt_delta(deltas[3])} | {_fmt_delta(deltas[4])} |"
            )
        lines.append("")
        lines.append("### Per-type · Coverage@budget_lenient")
        lines.append("")
        lines.append("| task_type | n | TreeRAG |")
        lines.append("| --- | ---: | ---: |")
        for tt, row in sorted((s.get("per_type_treerag") or {}).items()):
            lines.append(f"| {tt} | {int(row.get('n', 0))} | {_fmt(row.get('coverage_budget_lenient_mean'))} |")
        lines.append("")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def run_eval(args: argparse.Namespace) -> List[Dict[str, Any]]:
    run_t0 = time.time()
    if args.embedding_model != PAPER_DENSE_EMBEDDING_MODEL:
        print(
            f"[warn] embedding_model={args.embedding_model!r}; TreeRAG paper experiments use {PAPER_DENSE_EMBEDDING_MODEL!r}",
            file=sys.stderr,
        )

    cache_dir = Path(args.cache_dir)
    load_llm_env()
    if getattr(args, "compose_judge", False):
        os.environ["JUDGE_SEMANTIC_PRIMARY"] = "1"
        os.environ["COMPOSE_USE_LLM"] = "1"
        os.environ["COMPOSE_STRICT"] = "1"
    args.resolved_treerag_model = _resolve_treerag_model(args)
    base_url = os.environ.get("OPENAI_BASE_URL", "").strip() or None
    llm = RequiredOpenAITreeRagLLM(
        cache_path=cache_dir / "llm_cache.jsonl",
        model=args.resolved_treerag_model,
        base_url=base_url,
    )
    preflight_seconds = 0.0
    if not args.skip_llm_preflight:
        preflight_t0 = time.time()
        llm.preflight_check(max_tokens=int(args.intent_max_tokens))
        preflight_seconds = time.time() - preflight_t0
    print(f"[treerag] using TreeRAG black-box model: {args.resolved_treerag_model}", file=sys.stderr, flush=True)

    embedding_t0 = time.time()
    embedding_load_path = _local_hf_snapshot(args.embedding_model) or args.embedding_model
    if embedding_load_path != args.embedding_model:
        print(f"[treerag] using local embedding snapshot: {embedding_load_path}", file=sys.stderr, flush=True)
    dense_model = get_dense_encoder(embedding_load_path)
    embedding_load_seconds = time.time() - embedding_t0

    data_t0 = time.time()
    tasks = _load_tasks(args.tasks)
    if args.max_tasks > 0:
        tasks = tasks[: args.max_tasks]
    inspect_paths = list(getattr(args, "inspect_tasks", None) or [])
    inspect_by_id = (
        _load_required_inspect_registry(inspect_paths, tasks)
        if bool(getattr(args, "inspect_judge", False))
        else None
    )
    bundles = bundles_from_paths(args.test_jsonl, tree_source="flat", max_docs=args.max_docs)
    bundles_by_doc = {b.doc_id: b for b in bundles}
    _validate_tasks(tasks, bundles_by_doc)

    needed_doc_ids = sorted({str(t.doc_id) for t in tasks})
    missing = [d for d in needed_doc_ids if d not in bundles_by_doc]
    if missing:
        raise RuntimeError(f"missing TreeRAG documents for tasks: {missing[:10]}")
    data_load_seconds = time.time() - data_t0

    t0 = time.time()
    doc_indices: Dict[str, TreeRagDocIndex] = {}
    cache_hits = 0
    for i, doc_id in enumerate(needed_doc_ids, start=1):
        doc_indices[doc_id], hit = _load_or_build_doc_index(
            bundles_by_doc[doc_id],
            args=args,
            cache_dir=cache_dir,
            dense_model=dense_model,
            llm=llm,
        )
        cache_hits += int(hit)
        if i % 10 == 0 or i == len(needed_doc_ids):
            print(f"[treerag] indexed {i}/{len(needed_doc_ids)} docs", file=sys.stderr, flush=True)
    index_seconds = time.time() - t0

    # Fair protocol: no per-method candidate-count cap. All methods share only the
    # b500 char budget + identical compose + identical judge. The legacy asymmetric
    # cap can be re-enabled for reproducibility via TREERAG_FAIR_CAP=1.
    if os.environ.get("TREERAG_FAIR_CAP", "0").strip().lower() in {"1", "true", "yes"}:
        cap_by_task = _existing_cap_by_task(tasks)
    else:
        cap_by_task = {}
    checkpoint_path = cache_dir / "treerag_task_scores.jsonl"
    checkpoint_signature = _task_checkpoint_signature(args)
    checkpoint_meta = {"kind": "meta", "signature": checkpoint_signature, "created_at": time.time()}
    resumed_by_task: Dict[int, Dict[str, Any]] = {}
    if checkpoint_path.exists() and not args.rebuild_cache:
        try:
            with open(checkpoint_path, "r", encoding="utf-8") as f:
                first = f.readline().strip()
                if first:
                    meta = json.loads(first)
                    if meta.get("kind") == "meta" and meta.get("signature") == checkpoint_signature:
                        for line in f:
                            line = line.strip()
                            if not line:
                                continue
                            payload = json.loads(line)
                            if payload.get("kind") != "task":
                                continue
                            task_idx = int(payload["task_idx"])
                            resumed_by_task[task_idx] = {
                                "task_idx": task_idx,
                                "task": _deserialize_task(payload["task"]),
                                "treerag": _deserialize_scored_chunks(payload["treerag"]),
                                "treerag_raw_count": int(payload.get("treerag_raw_count", 0)),
                                "fair_candidate_cap": int(payload.get("fair_candidate_cap", 0)),
                                "btr_used": bool(payload.get("btr_used", False)),
                            }
                    else:
                        print(f"[treerag] ignoring stale checkpoint {checkpoint_path}", file=sys.stderr, flush=True)
        except Exception as e:
            print(f"[treerag] failed to read checkpoint {checkpoint_path}: {e}", file=sys.stderr, flush=True)
    if resumed_by_task:
        invalidated = 0
        for task_idx, current_task in enumerate(tasks, start=1):
            cached = resumed_by_task.get(task_idx)
            if cached is None:
                continue
            cached_task = cached.get("task")
            retrieval_identity_matches = bool(
                cached_task is not None
                and str(cached_task.query) == str(current_task.query)
                and str(cached_task.doc_id) == str(current_task.doc_id)
                and str(cached_task.task_type) == str(current_task.task_type)
            )
            if retrieval_identity_matches:
                # Gold answer/nodes may be repaired without changing retrieval.
                cached["task"] = current_task
            else:
                resumed_by_task.pop(task_idx, None)
                invalidated += 1
        print(f"[treerag] resumed {len(resumed_by_task)}/{len(tasks)} tasks from checkpoint", file=sys.stderr, flush=True)
        if invalidated:
            print(f"[treerag] invalidated {invalidated} checkpoint rows after task identity check", file=sys.stderr, flush=True)
    t1 = time.time()
    scored_by_task_map: Dict[int, Dict[str, Any]] = dict(resumed_by_task)
    for ti, task in enumerate(tasks, start=1):
        if ti in scored_by_task_map:
            if ti % 10 == 0 or ti == len(tasks):
                print(f"[treerag] scored {ti}/{len(tasks)} tasks", file=sys.stderr, flush=True)
            continue
        doc_index = doc_indices[str(task.doc_id)]
        use_btr = _should_use_btr(
            task.query,
            mode=args.intent_mode,
            llm=llm,
            max_tokens=int(args.intent_max_tokens),
        )
        scored_raw = _gather_treerag_candidates(
            doc_index,
            task.query,
            dense_model=dense_model,
            args=args,
            use_btr=use_btr,
        )
        cap = int(cap_by_task.get(ti, 0))
        scored = scored_raw[: min(len(scored_raw), cap)] if cap > 0 else scored_raw
        for chunk, _score in scored:
            if not chunk.line_ids:
                raise RuntimeError(f"task#{ti} retrieved empty-provenance chunk {chunk.node_id}")
        record = {
            "task_idx": ti,
            "task": task,
            "treerag": scored,
            "treerag_raw_count": len(scored_raw),
            "fair_candidate_cap": cap,
            "btr_used": use_btr,
        }
        scored_by_task_map[ti] = record
        try:
            if not checkpoint_path.exists():
                with open(checkpoint_path, "w", encoding="utf-8") as f:
                    f.write(json.dumps(checkpoint_meta, ensure_ascii=False) + "\n")
            with open(checkpoint_path, "a", encoding="utf-8") as f:
                record_json = {
                    "kind": "task",
                    "task_idx": ti,
                    "task": _serialize_task(task),
                    "treerag": _serialize_scored_chunks(scored),
                    "treerag_raw_count": len(scored_raw),
                    "fair_candidate_cap": cap,
                    "btr_used": use_btr,
                }
                f.write(json.dumps(record_json, ensure_ascii=False) + "\n")
                f.flush()
                os.fsync(f.fileno())
        except Exception as e:
            print(f"[treerag] checkpoint save failed for task {ti}: {e}", file=sys.stderr, flush=True)
        if ti % 10 == 0 or ti == len(tasks):
            print(f"[treerag] scored {ti}/{len(tasks)} tasks", file=sys.stderr, flush=True)
    retrieval_eval_seconds = time.time() - t1
    scored_by_task = [scored_by_task_map[i] for i in sorted(scored_by_task_map)]

    results: List[Dict[str, Any]] = []
    budgets = [int(x) for x in str(args.budgets).split(",") if x.strip()]
    for budget in budgets:
        reset_usage()
        budget_t0 = time.time()
        budget_compose_seconds = 0.0
        budget_judge_seconds = 0.0
        budget_retry_wait_seconds = 0.0
        budget_cache_path = cache_dir / f"treerag_budget_scores_b{budget}.jsonl"
        budget_score_signature = _budget_score_signature(args, budget, checkpoint_signature)
        cached_budget_scores = (
            _load_budget_score_cache(budget_cache_path, budget_score_signature)
            if not args.rebuild_cache
            else {}
        )
        if cached_budget_scores:
            print(
                f"[treerag] budget={budget} reused {len(cached_budget_scores)}/{len(scored_by_task)} cached compose/judge scores",
                file=sys.stderr,
                flush=True,
            )
        rows: List[Dict[str, Any]] = []
        for item in scored_by_task:
            task = item["task"]
            scored = item["treerag"]
            task_idx = int(item["task_idx"])
            cached_score = cached_budget_scores.get(task_idx)
            if cached_score is not None:
                treerag_score = cached_score
                treerag_score["score_cache_hit"] = True
            else:
                treerag_score = _score_at_budget(
                    task,
                    scored,
                    budget,
                    compose_judge=bool(getattr(args, "compose_judge", False)),
                    inspect_by_id=inspect_by_id,
                    use_inspect_judge=bool(getattr(args, "inspect_judge", False)),
                )
                treerag_score["score_cache_hit"] = False
                _append_budget_score_cache(
                    budget_cache_path,
                    budget_score_signature,
                    task_idx,
                    treerag_score,
                )
                budget_compose_seconds += float(treerag_score.get("compose_seconds", 0.0) or 0.0)
                budget_judge_seconds += float(treerag_score.get("judge_eval_seconds", 0.0) or 0.0)
                budget_retry_wait_seconds += float(treerag_score.get("retry_wait_seconds", 0.0) or 0.0)
            rows.append(
                {
                    "task_idx": task_idx,
                    "query": task.query,
                    "doc_id": task.doc_id,
                    "task_type": task.task_type,
                    "gold_nodes": task.gold_nodes,
                    "candidate_counts": {
                        "treerag": len(scored),
                        "treerag_raw": int(item.get("treerag_raw_count", len(scored))),
                        "fair_candidate_cap": int(item.get("fair_candidate_cap", 0)),
                    },
                    "candidate_type": {
                        "treerag": "treerag_tree_chunking_bidirectional_traversal",
                    },
                    "treerag_btr_used": bool(item.get("btr_used", False)),
                    "treerag": treerag_score,
                }
            )
        budget_eval_seconds = time.time() - budget_t0
        budget_retrieval_fill_seconds = max(
            0.0,
            budget_eval_seconds - budget_compose_seconds - budget_judge_seconds - budget_retry_wait_seconds,
        )
        summary_arm = _summarize_arm(rows, "treerag")
        compose_judge_usage = snapshot_usage()
        token_usage = llm.token_usage()
        token_usage_by_purpose = llm.token_usage_by_purpose()
        cold_start_seconds = preflight_seconds + embedding_load_seconds + data_load_seconds + index_seconds
        retrieval_framework_seconds = retrieval_eval_seconds + budget_retrieval_fill_seconds
        online_response_seconds = retrieval_framework_seconds + budget_compose_seconds
        warm_end_to_end_eval_seconds = online_response_seconds + budget_judge_seconds
        runtime_seconds = cold_start_seconds + warm_end_to_end_eval_seconds
        token_usage_by_purpose = {**token_usage_by_purpose, **compose_judge_usage}
        total_prompt_tokens = int(token_usage.get("prompt_tokens", 0) or 0)
        total_completion_tokens = int(token_usage.get("completion_tokens", 0) or 0)
        total_tokens = int(token_usage.get("total_tokens", 0) or 0)
        total_api_calls = int(token_usage.get("api_calls", 0) or 0)
        total_cache_hits = int(token_usage.get("cache_hits", 0) or 0)
        for block in compose_judge_usage.values():
            total_prompt_tokens += int(block.get("prompt_tokens", 0) or 0)
            total_completion_tokens += int(block.get("completion_tokens", 0) or 0)
            total_tokens += int(block.get("total_tokens", 0) or 0)
            total_api_calls += int(block.get("api_calls", 0) or 0)
            total_cache_hits += int(block.get("cache_hits", 0) or 0)
        total_retry_wait_seconds = float(token_usage.get("retry_wait_seconds", 0.0) or 0.0)
        for block in compose_judge_usage.values():
            total_retry_wait_seconds += float(block.get("retry_wait_seconds", 0.0) or 0.0)
        cost_block = {
            "total_seconds": warm_end_to_end_eval_seconds,
            "api_seconds": warm_end_to_end_eval_seconds,
            "cold_start_seconds": cold_start_seconds,
            "preflight_seconds": preflight_seconds,
            "embedding_load_seconds": embedding_load_seconds,
            "data_load_seconds": data_load_seconds,
            "index_build_seconds": index_seconds,
            "retrieval_candidate_seconds": retrieval_eval_seconds,
            "budget_fill_seconds": budget_retrieval_fill_seconds,
            "retrieval_framework_seconds": retrieval_framework_seconds,
            "compose_seconds": budget_compose_seconds,
            "online_response_seconds": online_response_seconds,
            "retry_wait_seconds": total_retry_wait_seconds,
            "judge_eval_seconds": budget_judge_seconds,
            "warm_end_to_end_eval_seconds": warm_end_to_end_eval_seconds,
            "end_to_end_eval_seconds": runtime_seconds,
            "runtime_seconds": runtime_seconds,
            "offline_preprocess_seconds": cold_start_seconds,
            "offline_index_build_seconds": index_seconds,
            "online_retrieval_seconds": retrieval_framework_seconds,
            "online_compose_seconds": budget_compose_seconds,
            "online_eval_seconds": warm_end_to_end_eval_seconds,
            "total_with_preprocessing_seconds": runtime_seconds,
            "timing_semantics": {
                "online_response_seconds": "retrieval_framework_seconds + compose_seconds; excludes judge_eval_seconds and offline cold/index build.",
                "warm_end_to_end_eval_seconds": "online_response_seconds + judge_eval_seconds; excludes offline cold/index build.",
                "end_to_end_eval_seconds": "cold_start_seconds + warm_end_to_end_eval_seconds; includes offline preprocessing/index build.",
                "offline_preprocess_seconds": "preflight_seconds + embedding_load_seconds + data_load_seconds + index_build_seconds.",
            },
            "token_usage_by_purpose": token_usage_by_purpose,
            "token_usage_total": {
                "prompt_tokens": total_prompt_tokens,
                "completion_tokens": total_completion_tokens,
                "total_tokens": total_tokens,
                "api_calls": total_api_calls,
                "cache_hits": total_cache_hits,
                "retry_wait_seconds": total_retry_wait_seconds,
            },
        }
        payload = {
            "summary": {
                "experiment": "arxiv_treerag_retrieval_aligned",
                "n_tasks": len(rows),
                "task_type_counts": _task_type_counts(tasks),
                "config": {
                    "test_jsonl": str(Path(args.test_jsonl).resolve()),
                    "tasks": str(Path(args.tasks).resolve()),
                    "budget_chars": budget,
                    "embedding_model": args.embedding_model,
                    "embedding_model_load_path": embedding_load_path,
                    "paper": "TreeRAG: Unleashing the Power of Hierarchical Storage for Enhanced Knowledge Retrieval in Long Documents",
                    "paper_url": "https://aclanthology.org/2025.findings-acl.20/",
                    "tree_source": "llm_tree_chunking",
                    "tree_model": args.resolved_treerag_model,
                    "intent_model": args.resolved_treerag_model,
                    "tree_chunking": "LLM Tree-Chunking levels/titles over preprocessed line chunks + path-title prefix embeddings",
                    "retrieval": "dense initial retrieval + bidirectional traversal retrieval for LLM-positive intent queries",
                    "intent_mode": args.intent_mode,
                    "tree_chunk_prompt_version": TREE_CHUNK_PROMPT_VERSION,
                    "intent_prompt_version": INTENT_PROMPT_VERSION,
                    "tree_lines_per_call": int(args.tree_lines_per_call),
                    "tree_line_char_limit": int(args.tree_line_char_limit),
                    "tree_max_level": int(args.tree_max_level),
                    "tree_max_tokens": int(args.tree_max_tokens),
                    "intent_max_tokens": int(args.intent_max_tokens),
                    "initial_top_k": int(args.initial_top_k),
                    "root_to_leaf_decay": float(args.root_to_leaf_decay),
                    "leaf_to_parent_decay": float(args.leaf_to_parent_decay),
                    "max_traversal_leaves": int(args.max_traversal_leaves),
                    "path_char_limit": int(args.path_char_limit),
                    "evidence_header_protocol": EVIDENCE_HEADER_PROTOCOL,
                    "fairness_control": _fairness_control_metadata(
                        args, candidate_cap_enabled=bool(cap_by_task)
                    ),
                    "llm_tree_chunking_required_by_paper": True,
                    "llm_intent_required_by_paper": True,
                    "llm_calls_in_this_adapter": True,
                    "llm_compose": bool(getattr(args, "compose_judge", False)),
                    "llm_judge": bool(getattr(args, "compose_judge", False)),
                    "inspect_judge": bool(getattr(args, "inspect_judge", False)),
                    "inspect_tasks": [str(p) for p in inspect_paths],
                    "token_usage": cost_block["token_usage_total"],
                    "token_usage_by_purpose": token_usage_by_purpose,
                    "cache_dir": str(cache_dir.resolve()),
                    "llm_cache_path": str((cache_dir / "llm_cache.jsonl").resolve()),
                    "budget_score_cache_path": str(budget_cache_path.resolve()),
                    "budget_score_cache_hits": sum(1 for row in rows if (row.get("treerag") or {}).get("score_cache_hit")),
                    "task_checkpoint_hits": len(resumed_by_task),
                    "doc_index_cache_hits": int(cache_hits),
                    "llm_cache_hits": int(token_usage.get("cache_hits", 0)),
                    "n_corpus_docs_loaded": len(bundles),
                    "n_docs_indexed_for_tasks": len(needed_doc_ids),
                    "preflight_seconds": preflight_seconds,
                    "embedding_load_seconds": embedding_load_seconds,
                    "data_load_seconds": data_load_seconds,
                    "index_seconds": index_seconds,
                    "retrieval_eval_seconds": retrieval_eval_seconds,
                    "runtime_seconds": runtime_seconds,
                    "cost_measurement": {
                        "timing": "observed_cache_assisted_run",
                        "tokens": "billed_incremental_tokens_cache_hits_are_zero",
                    },
                    "timing_semantics": {
                        "online_response_seconds": "Use this for online latency: retrieval_framework_seconds + compose_seconds.",
                        "judge_eval_seconds": "Report separately as evaluation-only time.",
                        "cold_start_seconds/index_build_seconds": "Report separately as offline TreeRAG build cost.",
                        "end_to_end_eval_seconds": "Includes offline cold/index build; do not compare it to per-query online response.",
                    },
                    "btr_tasks": sum(1 for item in scored_by_task if item.get("btr_used")),
                },
                "cost": {
                    "treerag": cost_block,
                },
                "treerag": summary_arm,
                "per_type_treerag": _per_type(rows, "treerag"),
                "effective_scored": {
                    "treerag": {
                        "n_chunks": sum(len(item["treerag"]) for item in scored_by_task),
                        "n_chunks_mean_per_task": sum(len(item["treerag"]) for item in scored_by_task) / float(max(1, len(scored_by_task))),
                    }
                },
            },
            "rows": rows,
        }
        out_path = Path(str(args.out_template).format(budget=budget))
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"[treerag] saved {out_path}", file=sys.stderr, flush=True)
        results.append(payload)

    existing = _load_payloads(_existing_result_paths())
    raptor = _load_payloads(_raptor_result_paths())
    llamaindex = _load_payloads(_llamaindex_result_paths())
    _write_markdown(results, Path(args.summary_md), existing, raptor, llamaindex)
    print(f"[treerag] saved {args.summary_md}", file=sys.stderr, flush=True)
    _write_manifest(args, cache_dir, llm, len(bundles), len(needed_doc_ids), len(tasks), cache_hits, time.time() - run_t0)
    return results


def _write_manifest(
    args: argparse.Namespace,
    cache_dir: Path,
    llm: RequiredOpenAITreeRagLLM,
    n_corpus_docs: int,
    n_indexed_docs: int,
    n_tasks: int,
    cache_hits: int,
    runtime_seconds: float,
) -> None:
    manifest = {
        "baseline": "treerag",
        "adapter": _adapter_path_label(),
        "paper": "TreeRAG: Unleashing the Power of Hierarchical Storage for Enhanced Knowledge Retrieval in Long Documents",
        "paper_url": "https://aclanthology.org/2025.findings-acl.20/",
        "embedding_model": args.embedding_model,
        "embedding_model_load_path": _local_hf_snapshot(args.embedding_model) or args.embedding_model,
        "tree_source": "llm_tree_chunking",
        "tree_model": getattr(args, "resolved_treerag_model", DEFAULT_TREERAG_LLM_MODEL),
        "intent_model": getattr(args, "resolved_treerag_model", DEFAULT_TREERAG_LLM_MODEL),
        "default_black_box_model": DEFAULT_TREERAG_LLM_MODEL,
        "paper_black_box_steps": {
            "tree_chunking": True,
            "intent_classification": True,
        },
        "llm_calls_in_this_adapter": True,
        "token_usage": llm.token_usage(),
        "token_usage_by_purpose": llm.token_usage_by_purpose(),
        "llm_cache_path": str((cache_dir / "llm_cache.jsonl").resolve()),
        "n_corpus_docs_loaded": n_corpus_docs,
        "n_docs_indexed_for_tasks": n_indexed_docs,
        "n_tasks": n_tasks,
        "doc_index_cache_hits": int(cache_hits),
        "llm_cache_hits": int(llm.cache_hits),
        "runtime_seconds": runtime_seconds,
        "params": {
            "intent_mode": args.intent_mode,
            "tree_chunk_prompt_version": TREE_CHUNK_PROMPT_VERSION,
            "intent_prompt_version": INTENT_PROMPT_VERSION,
            "tree_lines_per_call": int(args.tree_lines_per_call),
            "tree_line_char_limit": int(args.tree_line_char_limit),
            "tree_max_level": int(args.tree_max_level),
            "tree_max_tokens": int(args.tree_max_tokens),
            "intent_max_tokens": int(args.intent_max_tokens),
            "initial_top_k": int(args.initial_top_k),
            "root_to_leaf_decay": float(args.root_to_leaf_decay),
            "leaf_to_parent_decay": float(args.leaf_to_parent_decay),
            "max_traversal_leaves": int(args.max_traversal_leaves),
            "path_char_limit": int(args.path_char_limit),
            "embedding_batch_size": int(args.embedding_batch_size),
        },
    }
    cache_dir.mkdir(parents=True, exist_ok=True)
    (cache_dir / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--test-jsonl", type=Path, default=PACKAGE_ROOT / "data" / "full_eval_predictions_prevline_fallback.jsonl")
    p.add_argument("--tasks", type=Path, default=PACKAGE_ROOT / "data" / "tasks_arxiv_bodyrich_800_equal_prevline_quality_repaired.jsonl")
    p.add_argument("--budgets", default="300,500,1000")
    p.add_argument("--out-template", default=str(PACKAGE_ROOT / "results" / "arxiv_treerag_800equal_b{budget}.json"))
    p.add_argument("--summary-md", type=Path, default=PACKAGE_ROOT / "results" / "summary_treerag_800equal.md")
    p.add_argument("--cache-dir", type=Path, default=PACKAGE_ROOT / "cache" / "treerag")
    p.add_argument("--embedding-model", default=PAPER_DENSE_EMBEDDING_MODEL)
    p.add_argument("--max-docs", type=int, default=0)
    p.add_argument("--max-tasks", type=int, default=0)
    p.add_argument(
        "--treerag-model",
        default=None,
        help=f"OpenAI-compatible model for TreeRAG Tree-Chunking and intent detection. Default: TREERAG_MODEL or {DEFAULT_TREERAG_LLM_MODEL}.",
    )
    p.add_argument(
        "--intent-mode",
        choices=("llm", "always", "never"),
        default="llm",
        help="Use llm for the paper intent classifier; always/never are diagnostic switches.",
    )
    p.add_argument("--tree-lines-per-call", type=int, default=60)
    p.add_argument("--tree-line-char-limit", type=int, default=700)
    p.add_argument("--tree-max-level", type=int, default=4)
    p.add_argument("--tree-max-tokens", type=int, default=12000)
    p.add_argument("--intent-max-tokens", type=int, default=64)
    p.add_argument("--initial-top-k", type=int, default=80)
    p.add_argument("--root-to-leaf-decay", type=float, default=0.97)
    p.add_argument("--leaf-to-parent-decay", type=float, default=0.94)
    p.add_argument(
        "--max-traversal-leaves",
        type=int,
        default=0,
        help="0 keeps all leaf descendants under the traversal root, matching TreeRAG's BTR idea.",
    )
    p.add_argument("--path-char-limit", type=int, default=700)
    p.add_argument("--embedding-batch-size", type=int, default=64)
    p.add_argument(
        "--compose-judge",
        action="store_true",
        help="Run the same LLM compose + semantic judge path as Gold/Pred/Flat for end-to-end cost.",
    )
    p.add_argument(
        "--inspect-judge",
        action="store_true",
        help="Use the same Inspect scoring path as Gold/Pred/Flat; requires --inspect-tasks.",
    )
    p.add_argument(
        "--inspect-tasks",
        dest="inspect_tasks",
        action="append",
        type=Path,
        default=None,
        metavar="PATH",
        help="Inspect-format JSONL registry. Can be passed multiple times.",
    )
    p.add_argument("--rebuild-cache", action="store_true")
    p.add_argument("--skip-llm-preflight", action="store_true")
    p.add_argument("--skip-llm-smoke-check", action="store_true")
    args = p.parse_args()
    run_eval(args)


if __name__ == "__main__":
    main()
