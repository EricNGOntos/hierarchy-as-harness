"""
Dense embedding backend.

Default path is remote OpenAI-compatible /v1/embeddings (no local GPU / ST model).
Corpus pool vectors are cached under cache/embeddings*; queries can be cached too.
"""
from __future__ import annotations

import hashlib
import json
import os
import re
import sys
import time
from pathlib import Path
from typing import Any, List, Optional, Sequence, Tuple

# Remote-first default: available on the configured OpenAI-compatible gateway and
# produces 1024-d vectors. Local ST models are opt-in via BODYRICH_EMBEDDING_BACKEND=local.
DEFAULT_DENSE_EMBEDDING_MODEL = "text-embedding-v3"
DEFAULT_REMOTE_EMBEDDING_MODEL = "text-embedding-v3"


def resolve_embedding_model(explicit: str | None) -> str:
    """CLI 显式传入优先，否则 BODYRICH_EMBEDDING_MODEL / EMBEDDING_MODEL，否则仓库默认。"""
    if explicit and explicit.strip():
        return explicit.strip()
    env = (
        os.environ.get("BODYRICH_EMBEDDING_MODEL", "").strip()
        or os.environ.get("EMBEDDING_MODEL", "").strip()
    )
    return env or DEFAULT_DENSE_EMBEDDING_MODEL


def embedding_backend_kind() -> str:
    """remote|openai|local. Default remote (no local GPU requirement)."""
    raw = (
        os.environ.get("BODYRICH_EMBEDDING_BACKEND", "").strip()
        or os.environ.get("EMBEDDING_BACKEND", "").strip()
        or "remote"
    ).lower()
    if raw in {"local", "st", "sentence-transformers", "hf"}:
        return "local"
    if raw in {"remote", "openai", "api", "openai_compat"}:
        return "remote"
    return "remote"


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


class RemoteOpenAIEncoder:
    """Drop-in encoder with SentenceTransformer-like encode() for remote embeddings."""

    def __init__(
        self,
        model_name: str,
        *,
        dimensions: Optional[int] = None,
        batch_size: int = 10,
    ) -> None:
        from .llm_config import load_llm_env, make_openai_client, require_llm_env, resolve_llm_credentials

        load_llm_env()
        require_llm_env(context="Remote embeddings")
        self.model_name = str(model_name or DEFAULT_REMOTE_EMBEDDING_MODEL).strip()
        self.dimensions = dimensions
        self.batch_size = max(1, int(batch_size))
        self._dim: Optional[int] = int(dimensions) if dimensions else None
        api_key, base_url = resolve_llm_credentials(self.model_name)
        self._client = make_openai_client(api_key=api_key, base_url=base_url)

    def get_sentence_embedding_dimension(self) -> int:
        if self._dim is not None:
            return int(self._dim)
        # Probe once.
        vec = self.encode(["dimension probe"], convert_to_numpy=True)[0]
        self._dim = int(len(vec))
        return int(self._dim)

    def encode(
        self,
        texts: Sequence[str],
        *,
        convert_to_numpy: bool = True,
        batch_size: Optional[int] = None,
        show_progress_bar: bool = False,
        normalize_embeddings: bool = False,
        **_kwargs: Any,
    ):
        import numpy as np

        items = [(" " if not (t or "").strip() else str(t)) for t in texts]
        if not items:
            empty = np.zeros((0, self._dim or 0), dtype=np.float32)
            return empty if convert_to_numpy else []

        bs = max(1, int(batch_size or self.batch_size))
        # Gateway (DashScope-compat) rejects batches > 10.
        bs = min(bs, int(os.environ.get("BODYRICH_EMBEDDING_MAX_BATCH", "10") or "10"))
        out_rows: List[List[float]] = []
        n_batches = (len(items) + bs - 1) // bs
        for bi, start in enumerate(range(0, len(items), bs)):
            batch = items[start : start + bs]
            if show_progress_bar and n_batches > 1 and (bi == 0 or (bi + 1) % 5 == 0 or bi + 1 == n_batches):
                print(
                    f"[dense-remote] embed batch {bi + 1}/{n_batches} (n={len(batch)})",
                    file=sys.stderr,
                    flush=True,
                )
            vectors = self._embed_batch(batch)
            out_rows.extend(vectors)

        arr = np.asarray(out_rows, dtype=np.float32)
        if self._dim is None and arr.ndim == 2 and arr.shape[1] > 0:
            self._dim = int(arr.shape[1])
        if normalize_embeddings and arr.size:
            arr = l2_normalize_rows(arr, label=f"remote:{self.model_name}")
        return arr if convert_to_numpy else arr.tolist()

    def _embed_batch(self, batch: List[str]) -> List[List[float]]:
        last_err: Optional[Exception] = None
        max_retries = max(1, int(os.environ.get("BODYRICH_EMBEDDING_MAX_RETRIES", "4") or "4"))
        for attempt in range(max_retries):
            try:
                kwargs: dict[str, Any] = {"model": self.model_name, "input": batch}
                if self.dimensions is not None:
                    kwargs["dimensions"] = int(self.dimensions)
                resp = self._client.embeddings.create(**kwargs)
                # OpenAI may return data out of order; sort by index.
                rows = sorted(list(resp.data), key=lambda x: int(getattr(x, "index", 0)))
                if len(rows) != len(batch):
                    raise RuntimeError(
                        f"embedding response size mismatch: got {len(rows)} expected {len(batch)}"
                    )
                return [list(r.embedding) for r in rows]
            except Exception as exc:
                last_err = exc
                wait = min(8.0, 0.5 * (2 ** attempt))
                print(
                    f"[dense-remote] batch failed attempt={attempt+1}/{max_retries}: {exc}; sleep {wait:.1f}s",
                    file=sys.stderr,
                    flush=True,
                )
                time.sleep(wait)
        raise RuntimeError(
            f"remote embedding failed model={self.model_name!r}: {last_err}"
        )


def get_dense_encoder(model_name: str):
    """Return a dense encoder. Default: remote OpenAI-compatible embeddings."""
    kind = embedding_backend_kind()
    model = resolve_embedding_model(model_name)
    if kind == "remote":
        dims_raw = os.environ.get("BODYRICH_EMBEDDING_DIMENSIONS", "").strip()
        dimensions = int(dims_raw) if dims_raw.isdigit() else None
        batch = int(os.environ.get("BODYRICH_EMBEDDING_BATCH_SIZE", "10") or "10")
        print(
            f"[dense] backend=remote model={model} dimensions={dimensions or 'default'}",
            file=sys.stderr,
            flush=True,
        )
        return RemoteOpenAIEncoder(model, dimensions=dimensions, batch_size=batch)

    # Local sentence-transformers path (optional; needs local weights / CPU-or-GPU).
    try:
        from sentence_transformers import SentenceTransformer
    except ImportError as e:
        raise ImportError(
            "local dense backend requires: pip install sentence-transformers torch\n"
            "Or set BODYRICH_EMBEDDING_BACKEND=remote (default) to use API embeddings."
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
        model = _resolve_local_hf_snapshot(model)
    print(f"[dense] backend=local model={model}", file=sys.stderr, flush=True)
    try:
        return SentenceTransformer(
            model,
            local_files_only=local_only,
            tokenizer_kwargs={"fix_mistral_regex": False},
        )
    except TypeError:
        return SentenceTransformer(model)


def _embedding_cache_enabled() -> bool:
    raw = os.environ.get("BODYRICH_EMBEDDING_CACHE", "1").strip().lower()
    return raw not in {"0", "false", "no", "off"}


_L2_EPS = 1e-12


def _embedding_row_ok(vec: Any, *, eps: float = _L2_EPS) -> bool:
    """True when a vector is finite and has usable L2 norm (not all-zero/NaN)."""
    import numpy as np

    arr = np.asarray(vec, dtype=np.float32).reshape(-1)
    if arr.size == 0:
        return False
    if not bool(np.isfinite(arr).all()):
        return False
    return float(np.linalg.norm(arr)) >= float(eps)


def l2_normalize_rows(
    emb: Any,
    *,
    eps: float = _L2_EPS,
    label: str = "",
) -> Any:
    """L2-normalize embedding rows for cosine-via-dot-product.

    - Non-finite entries are zeroed (and logged).
    - Near-zero rows stay zero vectors (do NOT divide by eps → huge garbage).
    - Valid rows become unit vectors so ``mat @ qv`` equals cosine similarity.
    """
    import numpy as np

    arr = np.asarray(emb, dtype=np.float32)
    if arr.size == 0:
        return arr
    out = np.array(arr, dtype=np.float32, copy=True)
    bad = ~np.isfinite(out)
    if bad.any():
        if out.ndim == 1:
            n_bad = 1
        else:
            n_bad = int(np.any(bad, axis=tuple(range(1, out.ndim))).sum())
        tag = f" {label}" if label else ""
        print(
            f"[dense] sanitize non-finite rows={n_bad}{tag}",
            file=sys.stderr,
            flush=True,
        )
        out[bad] = 0.0

    if out.ndim == 1:
        nrm = float(np.linalg.norm(out))
        if nrm < float(eps):
            return np.zeros_like(out)
        return out / nrm

    norms = np.linalg.norm(out, axis=1, keepdims=True)
    zero = norms.ravel() < float(eps)
    safe = np.maximum(norms, float(eps))
    out = out / safe
    if zero.any():
        out[zero] = 0.0
        tag = f" {label}" if label else ""
        print(
            f"[dense] zero-norm rows kept as zero n={int(zero.sum())}{tag}",
            file=sys.stderr,
            flush=True,
        )
    return out


def _texts_embedding_cache_key(model: Any, texts: Sequence[str], *, namespace: str = "texts") -> str:
    model_name = _model_cache_name(model)
    h = hashlib.sha256()
    h.update(json.dumps({"model": model_name, "ns": namespace, "n": len(texts)}, sort_keys=True).encode("utf-8"))
    for text in texts:
        h.update(b"\0")
        h.update(((text or "").strip() or " ").encode("utf-8"))
    return h.hexdigest()


def encode_texts_normalized(
    model,
    texts: Sequence[str],
    *,
    batch_size: int = 10,
    namespace: str = "texts",
):
    """Encode raw texts to L2-normalized vectors with disk + optional process reuse."""
    import numpy as np

    cleaned = [(t or "").strip() or " " for t in texts]
    if not cleaned:
        return np.zeros((0, 0), dtype=np.float32)

    cache_path = None
    if _embedding_cache_enabled():
        cache_dir = _embedding_cache_dir() / "texts"
        cache_dir.mkdir(parents=True, exist_ok=True)
        cache_path = cache_dir / f"{_texts_embedding_cache_key(model, cleaned, namespace=namespace)}.npy"
        if cache_path.exists():
            try:
                emb = np.load(cache_path, allow_pickle=False)
                if int(emb.shape[0]) == len(cleaned):
                    emb = l2_normalize_rows(emb, label=f"text-cache:{namespace}")
                    print(f"[dense] loaded text embedding cache: {cache_path}", file=sys.stderr, flush=True)
                    return emb
            except Exception as exc:
                print(f"[dense] ignoring bad text embedding cache {cache_path}: {exc}", file=sys.stderr, flush=True)

    n = len(cleaned)
    mn = _model_cache_name(model)
    show_bar = n > 64
    if show_bar:
        print(f"[dense] 编码 {n} 个 texts（{mn} ns={namespace}）…", file=sys.stderr, flush=True)
    emb = model.encode(
        cleaned,
        convert_to_numpy=True,
        batch_size=max(1, min(int(batch_size), 10)),
        show_progress_bar=show_bar,
    )
    normalized = l2_normalize_rows(emb, label=f"texts:{namespace}")

    if cache_path is not None:
        tmp_path = cache_path.with_suffix(cache_path.suffix + ".tmp")
        try:
            with tmp_path.open("wb") as f:
                np.save(f, normalized, allow_pickle=False)
                f.flush()
                os.fsync(f.fileno())
            tmp_path.replace(cache_path)
            print(f"[dense] saved text embedding cache: {cache_path}", file=sys.stderr, flush=True)
        except Exception as exc:
            try:
                tmp_path.unlink(missing_ok=True)
            except Exception:
                pass
            print(f"[dense] failed to save text embedding cache {cache_path}: {exc}", file=sys.stderr, flush=True)
    return normalized


def encode_labeled_texts_normalized(
    model,
    *,
    doc_id: str,
    channel: str,
    unit_ids: Sequence[str],
    texts: Sequence[str],
    batch_size: int = 10,
    namespace: str = "default",
):
    """Persist path/content unit vectors per doc; only re-encode changed texts.

    Cache layout: cache/.../map_units/{model}/{namespace}/{doc_id}/{channel}.npz
    with arrays unit_ids, text_sha1, embeddings.
    """
    import numpy as np

    if len(unit_ids) != len(texts):
        raise ValueError("unit_ids and texts length mismatch")
    cleaned = [(t or "").strip() or " " for t in texts]
    ids = [str(u) for u in unit_ids]
    if not ids:
        return np.zeros((0, 0), dtype=np.float32)

    text_sha = [hashlib.sha1(t.encode("utf-8")).hexdigest() for t in cleaned]
    model_name = _model_cache_name(model)
    safe_model = re.sub(r"[^a-zA-Z0-9._-]+", "_", model_name)[:120]
    safe_ns = re.sub(r"[^a-zA-Z0-9._-]+", "_", str(namespace or "default"))[:80]
    safe_doc = re.sub(r"[^a-zA-Z0-9._-]+", "_", str(doc_id))[:180]
    safe_channel = re.sub(r"[^a-zA-Z0-9._-]+", "_", str(channel or "channel"))[:40]
    cache_dir = _embedding_cache_dir() / "map_units" / safe_model / safe_ns / safe_doc
    cache_path = cache_dir / f"{safe_channel}.npz"

    cached_by_id: dict[str, tuple[str, Any]] = {}
    if _embedding_cache_enabled() and cache_path.exists():
        try:
            data = np.load(cache_path, allow_pickle=True)
            old_ids = [str(x) for x in data["unit_ids"].tolist()]
            old_sha = [str(x) for x in data["text_sha1"].tolist()]
            old_emb = data["embeddings"]
            if len(old_ids) == len(old_sha) == int(old_emb.shape[0]):
                n_skip = 0
                for i, uid in enumerate(old_ids):
                    vec = old_emb[i]
                    # D2: bad/zero rows must miss and be re-encoded.
                    if not _embedding_row_ok(vec):
                        n_skip += 1
                        continue
                    cached_by_id[uid] = (old_sha[i], vec)
                print(
                    f"[dense] loaded map unit cache: {cache_path} "
                    f"({len(cached_by_id)} units"
                    + (f", skipped_bad={n_skip}" if n_skip else "")
                    + ")",
                    file=sys.stderr,
                    flush=True,
                )
        except Exception as exc:
            print(f"[dense] ignoring bad map unit cache {cache_path}: {exc}", file=sys.stderr, flush=True)

    miss_indices: List[int] = []
    for i, uid in enumerate(ids):
        hit = cached_by_id.get(uid)
        if hit is None or hit[0] != text_sha[i]:
            miss_indices.append(i)

    dim = 0
    if cached_by_id:
        sample = next(iter(cached_by_id.values()))[1]
        dim = int(np.asarray(sample).shape[0])

    if miss_indices:
        chunk = max(
            1,
            int(os.environ.get("NAV_MAP_UNIT_ENCODE_CHUNK", "40") or "40"),
        )
        print(
            f"[dense] map unit encode doc={doc_id} channel={channel} "
            f"miss={len(miss_indices)}/{len(ids)} chunk={chunk}",
            file=sys.stderr,
            flush=True,
        )

        sha_by_id = {ids[i]: text_sha[i] for i in range(len(ids))}

        def checkpoint() -> None:
            if not _embedding_cache_enabled():
                return
            ready_ids = [
                uid
                for uid in ids
                if uid in cached_by_id and cached_by_id[uid][0] == sha_by_id[uid]
            ]
            if not ready_ids:
                return
            local_dim = dim
            if local_dim <= 0:
                local_dim = int(np.asarray(cached_by_id[ready_ids[0]][1]).shape[0])
            if local_dim <= 0:
                return
            emb = np.zeros((len(ready_ids), local_dim), dtype=np.float32)
            shas = []
            for j, uid in enumerate(ready_ids):
                sh, vec = cached_by_id[uid]
                emb[j] = np.asarray(vec, dtype=np.float32)
                shas.append(sh)
            cache_dir.mkdir(parents=True, exist_ok=True)
            tmp_path = cache_dir / f".{safe_channel}.writing.npz"
            try:
                np.savez_compressed(
                    tmp_path,
                    unit_ids=np.asarray(ready_ids, dtype=object),
                    text_sha1=np.asarray(shas, dtype=object),
                    embeddings=emb,
                )
                tmp_path.replace(cache_path)
                print(
                    f"[dense] checkpoint map unit cache: {cache_path} "
                    f"({len(ready_ids)}/{len(ids)})",
                    file=sys.stderr,
                    flush=True,
                )
            except Exception as exc:
                try:
                    tmp_path.unlink(missing_ok=True)
                except Exception:
                    pass
                print(
                    f"[dense] checkpoint save failed {cache_path}: {exc}",
                    file=sys.stderr,
                    flush=True,
                )

        for start in range(0, len(miss_indices), chunk):
            part = miss_indices[start : start + chunk]
            miss_texts = [cleaned[i] for i in part]
            print(
                f"[dense] encode slice {start // chunk + 1}/"
                f"{(len(miss_indices) + chunk - 1) // chunk} "
                f"n={len(part)} doc={doc_id} channel={channel}",
                file=sys.stderr,
                flush=True,
            )
            miss_emb = encode_texts_normalized(
                model,
                miss_texts,
                batch_size=batch_size,
                namespace=f"map_unit:{channel}:slice{start}",
            )
            if dim == 0 and int(miss_emb.shape[0]) > 0:
                dim = int(miss_emb.shape[1])
            for j, i in enumerate(part):
                cached_by_id[ids[i]] = (text_sha[i], miss_emb[j])
            checkpoint()
            # Soft pacing against gateway rate limits / long-call kills.
            time.sleep(float(os.environ.get("NAV_MAP_UNIT_ENCODE_SLEEP", "0.2") or "0.2"))

    if dim <= 0:
        return np.zeros((len(ids), 0), dtype=np.float32)

    out = np.zeros((len(ids), dim), dtype=np.float32)
    for i, uid in enumerate(ids):
        _sha, vec = cached_by_id[uid]
        out[i] = np.asarray(vec, dtype=np.float32)
    # Final pass: keep cosine-via-dot contract even if a caller stuffed raw vectors.
    out = l2_normalize_rows(out, label=f"map_unit:{doc_id}:{channel}")

    if _embedding_cache_enabled():
        cache_dir.mkdir(parents=True, exist_ok=True)
        # numpy savez appends .npz unless the path already ends with it.
        tmp_path = cache_dir / f".{safe_channel}.writing.npz"
        try:
            np.savez_compressed(
                tmp_path,
                unit_ids=np.asarray(ids, dtype=object),
                text_sha1=np.asarray(text_sha, dtype=object),
                embeddings=out,
            )
            tmp_path.replace(cache_path)
            if miss_indices:
                print(f"[dense] saved map unit cache: {cache_path}", file=sys.stderr, flush=True)
        except Exception as exc:
            try:
                tmp_path.unlink(missing_ok=True)
            except Exception:
                pass
            print(f"[dense] failed to save map unit cache {cache_path}: {exc}", file=sys.stderr, flush=True)
    return out


def _embedding_cache_dir() -> Path:
    raw = os.environ.get("BODYRICH_EMBEDDING_CACHE_DIR", "").strip()
    if raw:
        return Path(raw)
    # Keep remote caches separate from legacy local-bge 1024-d files.
    if embedding_backend_kind() == "remote":
        return Path("cache") / "embeddings_remote"
    return Path("cache") / "embeddings"


def _model_cache_name(model: Any) -> str:
    return str(getattr(model, "model_name", None) or type(model).__name__)


def _embedding_cache_key(model: Any, chunks: List[Any]) -> str:
    model_name = _model_cache_name(model)
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


def _query_cache_enabled() -> bool:
    raw = os.environ.get("BODYRICH_QUERY_EMBEDDING_CACHE", "1").strip().lower()
    return raw not in {"0", "false", "no", "off"}


def _query_cache_path(model: Any, query: str) -> Path:
    h = hashlib.sha256()
    h.update(_model_cache_name(model).encode("utf-8"))
    h.update(b"\0")
    h.update((query or "").encode("utf-8"))
    return _embedding_cache_dir() / "queries" / f"{h.hexdigest()}.npy"


def encode_chunks_normalized(model, chunks: List[Any], *, batch_size: int = 10):
    cached = _load_embedding_cache(model, chunks)
    if cached is not None:
        return l2_normalize_rows(cached, label="chunk-cache")

    texts = [(getattr(c, "text", None) or " ").strip() or " " for c in chunks]
    n = len(texts)
    mn = _model_cache_name(model)
    show_bar = n > 64
    if show_bar:
        print(f"[dense] 编码 {n} 个 chunk（{mn}）…", file=sys.stderr, flush=True)
    emb = model.encode(
        texts,
        convert_to_numpy=True,
        batch_size=batch_size,
        show_progress_bar=show_bar,
    )
    normalized = l2_normalize_rows(emb, label="chunks")
    _save_embedding_cache(model, chunks, normalized)
    return normalized


def encode_query_normalized(model, query: str):
    import numpy as np

    q = (query or "").strip() or " "
    if _query_cache_enabled():
        path = _query_cache_path(model, q)
        if path.exists():
            try:
                cached = np.load(path, allow_pickle=False)
                if cached.ndim == 1 and cached.size > 0:
                    return l2_normalize_rows(cached, label="query-cache")
            except Exception:
                pass

    e = model.encode([q], convert_to_numpy=True)[0]
    out = l2_normalize_rows(e, label="query")
    if _query_cache_enabled():
        try:
            path = _query_cache_path(model, q)
            path.parent.mkdir(parents=True, exist_ok=True)
            tmp = path.with_suffix(path.suffix + ".tmp")
            with tmp.open("wb") as f:
                np.save(f, out, allow_pickle=False)
                f.flush()
                os.fsync(f.fileno())
            tmp.replace(path)
        except Exception as exc:
            print(f"[dense] query cache save failed: {exc}", file=sys.stderr, flush=True)
    return out


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
    if int(getattr(emb_matrix, "shape", [0, 0])[1]) != int(qv.shape[0]):
        raise ValueError(
            "query embedding dim mismatch vs corpus cache: "
            f"query_dim={qv.shape[0]} corpus_dim={emb_matrix.shape[1]}. "
            "Do not mix remote/local models or reuse unrelated .npy caches. "
            f"model={_model_cache_name(model)!r} cache_dir={_embedding_cache_dir()}"
        )
    mat = l2_normalize_rows(emb_matrix, label="pool")
    qv = l2_normalize_rows(qv, label="pool-query")
    sims = np.nan_to_num(
        np.asarray(np.dot(mat, qv), dtype=np.float64),
        nan=0.0,
        posinf=0.0,
        neginf=0.0,
    )
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
