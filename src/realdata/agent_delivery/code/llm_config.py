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


def resolve_thinking_mode(raw: str | None = None) -> str | None:
    """Normalize thinking toggle: ``enabled`` / ``disabled`` / None (API default)."""
    text = (raw if raw is not None else os.environ.get("LLM_THINKING", "")).strip().lower()
    if not text:
        text = os.environ.get("NAV_PLANNER_THINKING", "").strip().lower()
    if not text or text in {"auto", "default"}:
        return None
    if text in {"1", "true", "yes", "on", "enable", "enabled", "think"}:
        return "enabled"
    if text in {"0", "false", "no", "off", "disable", "disabled", "nothink", "nonthink"}:
        return "disabled"
    if text in {"enabled", "disabled"}:
        return text
    return None


def chat_thinking_extra(
    *,
    mode: str | None = None,
    model: str = "",
    reasoning_effort: str | None = None,
) -> dict:
    """Build ``extra`` kwargs for ``cached_chat_completion`` / chat.completions.

    DeepSeek V4 (official): ``extra_body={"thinking": {"type": "enabled"|"disabled"}}``.
    DashScope-compatible gateways: ``extra_body={"enable_thinking": bool}``.
    Style is chosen by ``LLM_THINKING_STYLE`` (``deepseek`` | ``dashscope``) or
    inferred from model / base URL.
    """
    resolved = resolve_thinking_mode(mode)
    style = os.environ.get("LLM_THINKING_STYLE", "").strip().lower()
    model_l = (model or "").lower()
    base = (
        os.environ.get("NAV_PLANNER_BASE_URL", "").strip()
        or os.environ.get("OPENAI_BASE_URL", "").strip()
        or os.environ.get("DS_URL", "").strip()
    ).lower()
    if not style:
        if "dashscope" in base or "aliyun" in base:
            style = "dashscope"
        else:
            style = "deepseek"
    body: dict = {}
    if resolved == "enabled":
        if style == "dashscope":
            body["enable_thinking"] = True
        else:
            body["thinking"] = {"type": "enabled"}
    elif resolved == "disabled":
        if style == "dashscope":
            body["enable_thinking"] = False
        else:
            body["thinking"] = {"type": "disabled"}
    effort = (
        reasoning_effort
        if reasoning_effort is not None
        else os.environ.get("LLM_REASONING_EFFORT", "").strip()
        or os.environ.get("NAV_PLANNER_REASONING_EFFORT", "").strip()
    )
    out: dict = {}
    if body:
        out["extra_body"] = body
    # reasoning_effort is a top-level OpenAI-compatible field for DeepSeek V4.
    if effort and resolved != "disabled":
        out["reasoning_effort"] = effort
    # Keep mode in cache key even when body empty (auto).
    out["_thinking_mode"] = resolved or "auto"
    if "deepseek" in model_l:
        out["_thinking_family"] = "deepseek"
    return out


def resolve_chat_credentials(
    *,
    model: str = "",
    api_key_env: str = "",
    base_url_env: str = "",
) -> tuple[str, str | None]:
    """Resolve API key / base URL, with DeepSeek ``DS_KEY``/``DS_URL`` fallback.

    Order: explicit planner envs → model-family DS_* → OPENAI_*.
    """
    key = ""
    base = None
    if api_key_env:
        key = os.environ.get(api_key_env, "").strip()
    if base_url_env:
        base = os.environ.get(base_url_env, "").strip() or None
    model_l = (model or "").lower()
    if (not key) and model_l.startswith("deepseek"):
        key = os.environ.get("DS_KEY", "").strip() or os.environ.get(
            "DEEPSEEK_API_KEY", ""
        ).strip()
        if not base:
            base = (
                os.environ.get("DS_URL", "").strip()
                or os.environ.get("DEEPSEEK_BASE_URL", "").strip()
                or None
            )
    if not key:
        key = os.environ.get("OPENAI_API_KEY", "").strip()
    if not base:
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
    """未配置 API key 时直接失败；compose/judge/nav/TreeRAG 均须 LLM。

    Accepts ``OPENAI_API_KEY`` or DeepSeek ``DS_KEY`` / ``DEEPSEEK_API_KEY``
    (planner may route deepseek-* models to DS_* via ``resolve_chat_credentials``).
    """
    load_llm_env()
    key = (
        os.environ.get("OPENAI_API_KEY", "").strip()
        or os.environ.get("DS_KEY", "").strip()
        or os.environ.get("DEEPSEEK_API_KEY", "").strip()
        or os.environ.get("NAV_PLANNER_API_KEY", "").strip()
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
        f"{prefix}必须配置 LLM API（OPENAI_API_KEY 或 DS_KEY）。"
        "请复制 src/realdata/agent_delivery/llm_api.env.example 为 llm_api.env 并填入密钥，"
        "或通过环境变量导出 OPENAI_API_KEY（及可选 OPENAI_BASE_URL、COMPOSE_MODEL、JUDGE_MODEL、NAV_LLM_MODEL）。"
    )
