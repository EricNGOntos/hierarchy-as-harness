#!/usr/bin/env python3
from __future__ import annotations

import os
import sys
import time


def main() -> int:
    from agent_delivery.code.llm_config import load_llm_env, make_openai_client

    load_llm_env()
    key = os.environ.get("OPENAI_API_KEY", "").strip()
    base = os.environ.get("OPENAI_BASE_URL", "").strip() or None
    model = (
        os.environ.get("NAV_LLM_MODEL", "").strip()
        or os.environ.get("COMPOSE_MODEL", "").strip()
        or "gpt-4o-mini"
    )
    if not key:
        print("OPENAI_API_KEY is missing", file=sys.stderr)
        return 2
    print(f"base_url={base}")
    print(f"model={model}")
    print(f"verify_ssl={os.environ.get('OPENAI_VERIFY_SSL', '<default:true>')}")
    print(f"trust_env={os.environ.get('OPENAI_TRUST_ENV', '<default:true>')}")
    t0 = time.perf_counter()
    try:
        client = make_openai_client(api_key=key, base_url=base, timeout=30.0)
        rsp = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": "Reply with OK only."},
                {"role": "user", "content": "ping"},
            ],
            temperature=0,
            max_tokens=4,
        )
    except Exception as exc:
        print(f"endpoint_check=FAIL elapsed={time.perf_counter() - t0:.2f}s", file=sys.stderr)
        print(f"{type(exc).__name__}: {exc}", file=sys.stderr)
        return 1
    text = (rsp.choices[0].message.content or "").strip()
    print(f"endpoint_check=OK elapsed={time.perf_counter() - t0:.2f}s response={text!r}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
