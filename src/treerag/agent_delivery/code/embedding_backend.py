"""
稠密向量检索（sentence-transformers）：与词重叠二选一，用于拉大 paraphrase 与层级策略差异。
"""
from __future__ import annotations

import hashlib
import json
import os
import sys
from pathlib import Path
from typing import Any, List, Tuple

# 默认嵌入：较 MiniLM-L6 更强，且覆盖中英文（realdata 以中文条款为主）；可被 CLI / 环境变量覆盖。
DEFAULT_DENSE_EMBEDDING_MODEL = "paraphrase-multilingual-MiniLM-L12-v2"


def resolve_embedding_model(explicit: str | None) -> str:
    """CLI 显式传入优先，否则 BODYRICH_EMBEDDING_MODEL / EMBEDDING_MODEL，否则仓库默认。"""
    if explicit and explicit.strip():
        return explicit.strip()
    env = (
        os.environ.get("BODYRICH_EMBEDDING_MODEL", "").strip()
        or os.environ.get("EMBEDDING_MODEL", "").strip()
    )
    return env or DEFAULT_DENSE_EMBEDDING_MODEL


def _resolve_local_hf_snapshot(model_name: str) -> str:
    """Return a local HuggingFace snapshot path when offline mode is requested."""
    model = str(model_name or "").strip()
    if not model or os.path.exists(model) or "/" not in model:
        return model
    org, name = model.split("/", 1)
    hub_dir = Path(os.environ.get("HF_HOME", str(Path.home() / ".cache" / "huggingface")))
    snapshots_dir = hub_dir / "hub" / f"models--{org}--{name}" / "snapshots"
    if not snapshots_dir.exists():
        return model
    required_any = ("pytorch_model.bin", "model.safetensors")
    candidates: List[Path] = []
    for snap in snapshots_dir.iterdir():
        if not snap.is_dir():
            continue
        has_config = (snap / "config.json").exists()
        has_tokenizer = (snap / "tokenizer.json").exists() or (snap / "tokenizer_config.json").exists()
        has_model = any((snap / fname).exists() for fname in required_any)
        has_modules = (snap / "modules.json").exists()
        if has_config and has_tokenizer and has_model:
            candidates.append(snap)
        elif has_modules and has_config and has_tokenizer:
            candidates.append(snap)
    if not candidates:
        return model
    candidates.sort(key=lambda p: p.stat().st_mtime, reverse=True)
    return str(candidates[0])


def get_dense_encoder(model_name: str):
    """懒加载 SentenceTransformer。"""
    try:
        from sentence_transformers import SentenceTransformer
    except ImportError as e:
        raise ImportError(
            "稠密检索需要: pip install sentence-transformers torch\n"
            "（CPU 可跑，首次会下载模型）"
        ) from e
    local_only = os.environ.get("BODYRICH_EMBEDDING_LOCAL_FILES_ONLY", "1").strip().lower() not in {
        "0",
        "false",
        "no",
        "off",
    }
    if local_only:
        os.environ.setdefault("HF_HUB_OFFLINE", "1")
        os.environ.setdefault("TRANSFORMERS_OFFLINE", "1")
        model_name = _resolve_local_hf_snapshot(model_name)
    try:
        return SentenceTransformer(
            model_name,
            local_files_only=local_only,
            tokenizer_kwargs={"fix_mistral_regex": False},
        )
    except TypeError:
        # Older sentence-transformers versions may not expose local_files_only.
        return SentenceTransformer(model_name)


def _embedding_cache_enabled() -> bool:
    raw = os.environ.get("BODYRICH_EMBEDDING_CACHE", "1").strip().lower()
    return raw not in {"0", "false", "no", "off"}


def _embedding_cache_dir() -> Path:
    raw = os.environ.get("BODYRICH_EMBEDDING_CACHE_DIR", "").strip()
    return Path(raw) if raw else Path("cache") / "embeddings"


def _embedding_cache_key(model: Any, chunks: List[Any]) -> str:
    model_name = str(getattr(model, "model_name", None) or type(model).__name__)
    h = hashlib.sha256()
    h.update(json.dumps({"model": model_name, "n": len(chunks)}, sort_keys=True).encode("utf-8"))
    for chunk in chunks:
        payload = {
            "node_id": str(getattr(chunk, "node_id", "")),
            "doc_id": str(getattr(chunk, "doc_id", "")),
            "text": str(getattr(chunk, "text", "") or ""),
            "line_ids": list(getattr(chunk, "line_ids", ()) or ()),
        }
        h.update(json.dumps(payload, ensure_ascii=False, sort_keys=True).encode("utf-8"))
    return h.hexdigest()


def _load_embedding_cache(model: Any, chunks: List[Any]):
    if not _embedding_cache_enabled() or not chunks:
        return None
    import numpy as np

    path = _embedding_cache_dir() / f"{_embedding_cache_key(model, chunks)}.npy"
    if not path.exists():
        return None
    try:
        emb = np.load(path, allow_pickle=False)
        if int(emb.shape[0]) == len(chunks):
            print(f"[dense] loaded embedding cache: {path}", file=sys.stderr, flush=True)
            return emb
    except Exception as exc:
        print(f"[dense] ignoring bad embedding cache {path}: {exc}", file=sys.stderr, flush=True)
    return None


def _save_embedding_cache(model: Any, chunks: List[Any], emb: Any) -> None:
    if not _embedding_cache_enabled() or not chunks:
        return
    import numpy as np

    cache_dir = _embedding_cache_dir()
    cache_dir.mkdir(parents=True, exist_ok=True)
    path = cache_dir / f"{_embedding_cache_key(model, chunks)}.npy"
    tmp_path = path.with_suffix(path.suffix + ".tmp")
    try:
        with tmp_path.open("wb") as f:
            np.save(f, emb, allow_pickle=False)
            f.flush()
            os.fsync(f.fileno())
        tmp_path.replace(path)
        print(f"[dense] saved embedding cache: {path}", file=sys.stderr, flush=True)
    except Exception as exc:
        try:
            tmp_path.unlink(missing_ok=True)
        except Exception:
            pass
        print(f"[dense] failed to save embedding cache {path}: {exc}", file=sys.stderr, flush=True)


def encode_chunks_normalized(model, chunks: List[Any], *, batch_size: int = 64):
    import numpy as np

    cached = _load_embedding_cache(model, chunks)
    if cached is not None:
        return cached

    texts = [(getattr(c, "text", None) or " ").strip() or " " for c in chunks]
    n = len(texts)
    mn = getattr(model, "model_name", None) or type(model).__name__
    show_bar = n > 300
    if show_bar:
        print(f"[dense] 编码 {n} 个 chunk（{mn}）…", file=sys.stderr, flush=True)
    emb = model.encode(
        texts,
        convert_to_numpy=True,
        batch_size=batch_size,
        show_progress_bar=show_bar,
    )
    norms = np.linalg.norm(emb, axis=1, keepdims=True) + 1e-12
    normalized = emb / norms
    _save_embedding_cache(model, chunks, normalized)
    return normalized


def encode_query_normalized(model, query: str):
    import numpy as np

    q = (query or "").strip() or " "
    e = model.encode([q], convert_to_numpy=True)[0]
    nrm = np.linalg.norm(e) + 1e-12
    return e / nrm


def dense_scores_for_pool(
    query: str,
    pool: List[Any],
    doc_id_filter: str | None,
    *,
    model,
    emb_matrix,
) -> List[Tuple[Any, float]]:
    """余弦相似度 = 归一化向量点积。emb_matrix 与 pool 行对齐。"""
    import numpy as np

    qv = encode_query_normalized(model, query)
    sims = np.asarray(emb_matrix @ qv, dtype=np.float64)
    out: List[Tuple[Any, float]] = []
    for i, c in enumerate(pool):
        if doc_id_filter and getattr(c, "doc_id", None) != doc_id_filter:
            continue
        out.append((c, float(sims[i])))
    out.sort(key=lambda x: -x[1])
    return out


def mmr_select_indices(
    relevance: Any,
    emb_candidates: Any,
    *,
    k_out: int,
    lambda_mult: float,
) -> List[int]:
    """
    标准 MMR：在 relevance（与 query 的余弦相似）与已选集合的最大相似之间权衡。
    relevance: (n,) float64；emb_candidates: (n, d) 已 L2 归一化。
    返回被选中的行下标（长度 ≤ k_out）。
    """
    import numpy as np

    rel = np.asarray(relevance, dtype=np.float64).reshape(-1)
    emb = np.asarray(emb_candidates, dtype=np.float64)
    n = int(rel.shape[0])
    if n == 0 or k_out <= 0:
        return []
    k_out = min(k_out, n)
    if k_out >= n:
        return list(range(n))

    lam = float(lambda_mult)
    lam = max(0.0, min(1.0, lam))
    selected: List[int] = []
    candidates = set(range(n))
    while len(selected) < k_out and candidates:
        best_i = -1
        best_score = -1e18
        for i in candidates:
            r = float(rel[i])
            if not selected:
                mmr = r
            else:
                sims = emb[i] @ emb[selected].T
                div = float(np.max(sims))
                mmr = lam * r - (1.0 - lam) * div
            if mmr > best_score:
                best_score = mmr
                best_i = i
        selected.append(best_i)
        candidates.remove(best_i)
    return selected
