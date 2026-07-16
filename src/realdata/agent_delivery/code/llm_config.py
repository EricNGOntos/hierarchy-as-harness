from __future__ import annotations

import os
from pathlib import Path


def _parse_env_line(line: str) -> tuple[str, str] | None:
    s = line.strip()
    if not s or s.startswith("#") or "=" not in s:
        return None
    k, v = s.split("=", 1)
    key = k.strip()
    val = v.strip()
    if not key:
        return None
    if (val.startswith('"') and val.endswith('"')) or (val.startswith("'") and val.endswith("'")):
        val = val[1:-1]
    return key, val


def _apply_env_file(path: Path) -> None:
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except Exception:
        return
    for line in lines:
        parsed = _parse_env_line(line)
        if not parsed:
            continue
        k, v = parsed
        if k and v and k not in os.environ:
            os.environ[k] = v


def load_llm_env() -> None:
    """
    从若干固定位置读取 LLM API 配置（若系统环境变量已存在则不覆盖）：
      1) ~/.config/realdata_treerag/llm_api.env（用户级共享，新 worktree 也可复用）
      2) src/realdata/agent_delivery/llm_api.env（当前实验包位置）
      3) core/agent_delivery/llm_api.env（兼容旧实验包布局）
      4) src/realdata/agent_delivery/llm_api.env（兼容从实验包根定位）
    按顺序加载；后读到的键仍遵守「不覆盖已在 os.environ 中的值」。
    """
    here = Path(__file__).resolve()
    candidates = [
        Path.home() / ".config" / "realdata_treerag" / "llm_api.env",
        here.parents[1] / "llm_api.env",
        here.parents[4] / "core" / "agent_delivery" / "llm_api.env",
        here.parents[4] / "src" / "realdata" / "agent_delivery" / "llm_api.env",
    ]
    for cfg in candidates:
        if cfg.exists():
            _apply_env_file(cfg)


def _env_bool(name: str, default: bool) -> bool:
    raw = os.environ.get(name, "").strip().lower()
    if not raw:
        return default
    return raw not in {"0", "false", "no", "off"}


def resolve_llm_credentials(model: str | None = None) -> tuple[str, str | None]:
    """Pick API key + base_url by model family (aligned with KNOWHERE-MAIN).

    - deepseek* → DS_KEY + DS_URL
    - qwen* / text-embedding* → ALI_API_KEYS (first) + ALI_URL
    - else → OPENAI_API_KEY + OPENAI_BASE_URL
    """
    load_llm_env()
    m = (model or "").strip().lower()

    def _first_key(raw: str) -> str:
        return (raw or "").split(",")[0].strip()

    if m.startswith("deepseek") or "deepseek" in m:
        key = (
            os.environ.get("DS_KEY", "").strip()
            or os.environ.get("DEEPSEEK_API_KEY", "").strip()
            or os.environ.get("OPENAI_API_KEY", "").strip()
        )
        base = (
            os.environ.get("DS_URL", "").strip()
            or os.environ.get("DEEPSEEK_BASE_URL", "").strip()
            or os.environ.get("OPENAI_BASE_URL", "").strip()
            or None
        )
        return key, base or None

    if (
        m.startswith("qwen")
        or "qwen" in m
        or m.startswith("text-embedding")
        or "embedding" in m
    ):
        key = _first_key(
            os.environ.get("ALI_API_KEYS", "").strip()
            or os.environ.get("DASHSCOPE_API_KEY", "").strip()
            or os.environ.get("OPENAI_API_KEY", "").strip()
        )
        base = (
            os.environ.get("ALI_URL", "").strip()
            or os.environ.get("DASHSCOPE_BASE_URL", "").strip()
            or os.environ.get("OPENAI_BASE_URL", "").strip()
            or None
        )
        return key, base or None

    key = os.environ.get("OPENAI_API_KEY", "").strip()
    base = os.environ.get("OPENAI_BASE_URL", "").strip() or None
    return key, base


def make_openai_client(*, api_key: str, base_url: str | None = None, timeout: float = 60.0):
    """Create an OpenAI-compatible client that respects SSL/proxy env toggles."""
    from openai import OpenAI  # type: ignore
    import httpx  # type: ignore

    verify_ssl = _env_bool("OPENAI_VERIFY_SSL", True)
    trust_env = _env_bool("OPENAI_TRUST_ENV", True)
    http_client = httpx.Client(verify=verify_ssl, timeout=timeout, trust_env=trust_env)
    return OpenAI(
        api_key=api_key,
        base_url=base_url or None,
        timeout=timeout,
        max_retries=0,
        http_client=http_client,
    )


def require_llm_env(*, context: str = "") -> None:
    """Require at least one usable LLM credential (OPENAI / ALI / DS)."""
    load_llm_env()
    key, _base = resolve_llm_credentials(os.environ.get("NAV_LLM_MODEL") or os.environ.get("COMPOSE_MODEL"))
    if not key:
        # Also accept DeepSeek-only or raw OPENAI.
        key = (
            os.environ.get("OPENAI_API_KEY", "").strip()
            or _first_ali()
            or os.environ.get("DS_KEY", "").strip()
        )
    if key:
        try:
            import openai  # noqa: F401
        except ImportError as exc:
            raise RuntimeError(
                f"{context + ': ' if context else ''}需要安装 openai 包（pip install openai）。"
            ) from exc
        return
    prefix = f"{context}: " if context else ""
    raise RuntimeError(
        f"{prefix}必须配置 LLM API（OPENAI_API_KEY，或 KNOWHERE 风格的 ALI_API_KEYS / DS_KEY）。"
        "请复制 src/realdata/agent_delivery/llm_api.env.example 为 llm_api.env 并填入密钥。"
    )


def _first_ali() -> str:
    raw = os.environ.get("ALI_API_KEYS", "").strip()
    return raw.split(",")[0].strip() if raw else ""
