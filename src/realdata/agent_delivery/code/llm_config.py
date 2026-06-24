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
      1) ~/.config/realdata_treerag/llm_api.env（推荐，用户级、不入库）
      2) src/realdata/agent_delivery/llm_api.env（仓库内本地副本，gitignore）
      3) core/agent_delivery/llm_api.env（兼容旧实验包布局）
    按顺序加载；后读到的键仍遵守「不覆盖已在 os.environ 中的值」。
    """
    here = Path(__file__).resolve()
    user_cfg = Path.home() / ".config" / "realdata_treerag" / "llm_api.env"
    candidates = [
        user_cfg,
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
    """未配置 OPENAI_API_KEY 时直接失败；compose/judge/nav/TreeRAG 均须 LLM。"""
    load_llm_env()
    key = os.environ.get("OPENAI_API_KEY", "").strip()
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
        f"{prefix}必须配置 LLM API（OPENAI_API_KEY）。"
        "请复制 llm_api.env.example 到 ~/.config/realdata_treerag/llm_api.env 并填入密钥，"
        "或通过环境变量导出 OPENAI_API_KEY（及可选 OPENAI_BASE_URL、COMPOSE_MODEL、JUDGE_MODEL、NAV_LLM_MODEL）。"
    )
