"""Offline probe scoring against a reference fact list (fusion plan P1).

Grades each fact as correct / half / wrong (1 / 0.5 / 0) by comparing the
composed answer to the fact — not by keyword substring hits on answer_keys.
Case score = mean of its fact grades (max 1.0 per case).
"""

from __future__ import annotations

import json
from typing import Any, Dict, List, Mapping, Sequence

# Plan §1: 对=1 / 半对=0.5 / 错=0
GRADE_CORRECT = 1.0
GRADE_HALF = 0.5
GRADE_WRONG = 0.0
_VALID_GRADES = {GRADE_CORRECT, GRADE_HALF, GRADE_WRONG}
_GRADE_ALIASES = {
    "correct": GRADE_CORRECT,
    "full": GRADE_CORRECT,
    "对": GRADE_CORRECT,
    "half": GRADE_HALF,
    "partial": GRADE_HALF,
    "半对": GRADE_HALF,
    "wrong": GRADE_WRONG,
    "incorrect": GRADE_WRONG,
    "错": GRADE_WRONG,
    "0": GRADE_WRONG,
    "0.5": GRADE_HALF,
    "1": GRADE_CORRECT,
    "1.0": GRADE_CORRECT,
}

_SCORE_PURPOSE = "nav_probe_reference_score_v1"


def resolve_reference_facts(case: Mapping[str, Any]) -> List[Dict[str, str]]:
    """Prefer ``reference_facts``; else one fact from ``reference_answer`` prose."""
    raw = case.get("reference_facts")
    out: List[Dict[str, str]] = []
    if isinstance(raw, list):
        for i, row in enumerate(raw):
            if isinstance(row, str):
                fact = row.strip()
                fid = f"f{i + 1}"
            elif isinstance(row, dict):
                fact = str(row.get("fact") or row.get("text") or "").strip()
                fid = str(row.get("id") or f"f{i + 1}").strip() or f"f{i + 1}"
            else:
                continue
            if fact:
                out.append({"id": fid, "fact": fact})
    if out:
        return out
    prose = str(case.get("reference_answer") or "").strip()
    if prose:
        return [{"id": "f1", "fact": prose}]
    return []


def coerce_grade(raw: Any) -> float:
    if isinstance(raw, (int, float)):
        val = float(raw)
        if val in _VALID_GRADES:
            return val
        if val >= 1.0:
            return GRADE_CORRECT
        if val <= 0.0:
            return GRADE_WRONG
        return GRADE_HALF
    token = str(raw or "").strip().lower()
    if token in _GRADE_ALIASES:
        return float(_GRADE_ALIASES[token])
    return GRADE_WRONG


def aggregate_fact_grades(grades: Sequence[float]) -> float:
    """Mean of per-fact grades; empty list → 0.0 (nothing to credit)."""
    vals = [float(g) for g in grades]
    if not vals:
        return 0.0
    return round(sum(vals) / float(len(vals)), 4)


def parse_grade_payload(
    obj: Mapping[str, Any],
    facts: Sequence[Mapping[str, str]],
) -> Dict[str, float]:
    """Map fact id → grade from LLM JSON; missing facts default to wrong."""
    by_id = {str(f["id"]): GRADE_WRONG for f in facts}
    rows = obj.get("grades") or obj.get("facts") or obj.get("items")
    if isinstance(rows, list):
        for row in rows:
            if not isinstance(row, dict):
                continue
            fid = str(row.get("id") or "").strip()
            if fid in by_id:
                by_id[fid] = coerce_grade(row.get("grade") or row.get("score"))
    elif isinstance(rows, dict):
        for fid, grade in rows.items():
            key = str(fid).strip()
            if key in by_id:
                by_id[key] = coerce_grade(grade)
    return by_id


def score_answer_against_facts(
    *,
    answer: str,
    facts: Sequence[Mapping[str, str]],
    query: str = "",
) -> Dict[str, Any]:
    """LLM-grade each fact. Returns grades, case_score, and raw text."""
    fact_list = [{"id": str(f["id"]), "fact": str(f["fact"])} for f in facts if f.get("fact")]
    if not fact_list:
        return {
            "grades": {},
            "case_score": 0.0,
            "n_facts": 0,
            "method": "reference_facts",
            "error": "empty_facts",
        }
    text = (answer or "").strip()
    if not text:
        grades = {f["id"]: GRADE_WRONG for f in fact_list}
        return {
            "grades": grades,
            "case_score": aggregate_fact_grades(list(grades.values())),
            "n_facts": len(fact_list),
            "method": "reference_facts",
            "error": "empty_answer",
        }

    from nav_llm import nav_chat, resolve_nav_model

    model = resolve_nav_model(
        model_env="NAV_PROBE_SCORE_MODEL",
        fallback_envs=("NAV_PLANNER_MODEL", "NAV_LLM_MODEL", "COMPOSE_MODEL"),
    )
    system = (
        "You score a retrieval answer against a checklist of reference facts.\n"
        "For each fact, grade how well the ANSWER supports it:\n"
        "  - 1 = fully supported (correct)\n"
        "  - 0.5 = partially supported (half)\n"
        "  - 0 = unsupported or contradicted (wrong)\n"
        "Judge semantic support, not keyword overlap. Use only the answer text.\n"
        "Return ONLY JSON: "
        '{"grades":[{"id":"f1","grade":1},{"id":"f2","grade":0.5}]}\n'
    )
    facts_block = "\n".join(f"- {f['id']}: {f['fact']}" for f in fact_list)
    user = (
        (f"Query: {query}\n\n" if query else "")
        + f"=== Reference facts ===\n{facts_block}\n=== End facts ===\n\n"
        + f"=== Answer ===\n{text[:8000]}\n=== End answer ===\n"
    )
    try:
        cached = nav_chat(
            purpose=_SCORE_PURPOSE,
            model=model,
            messages=[
                {"role": "system", "content": system},
                {"role": "user", "content": user},
            ],
            temperature=0.0,
            max_tokens=512,
            response_format={"type": "json_object"},
            context="Nav Probe Reference Score",
            api_key_env="NAV_PLANNER_API_KEY",
            base_url_env="NAV_PLANNER_BASE_URL",
            usage_tag="nav_probe_score",
        )
        raw = str(cached.get("content") or "").strip()
        obj = json.loads(raw) if raw.startswith("{") else {}
        grades = parse_grade_payload(obj if isinstance(obj, dict) else {}, fact_list)
        return {
            "grades": grades,
            "case_score": aggregate_fact_grades(list(grades.values())),
            "n_facts": len(fact_list),
            "method": "reference_facts",
            "raw": raw[:1000],
            "model": model,
        }
    except Exception as exc:  # noqa: BLE001
        grades = {f["id"]: GRADE_WRONG for f in fact_list}
        return {
            "grades": grades,
            "case_score": 0.0,
            "n_facts": len(fact_list),
            "method": "reference_facts",
            "error": f"{type(exc).__name__}: {exc}",
        }


def score_case_answer(case: Mapping[str, Any], answer: str) -> Dict[str, Any]:
    facts = resolve_reference_facts(case)
    result = score_answer_against_facts(
        answer=answer,
        facts=facts,
        query=str(case.get("query") or ""),
    )
    result["reference_facts"] = facts
    return result
