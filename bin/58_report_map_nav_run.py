#!/usr/bin/env python3
"""Map-Nav 单次运行可读报告(通用).

吃 `bin/56_replay_map_nav_traces.py` 产出的检索结果 JSON,聚合出查问题最需要的东西:

  1. 结果得分:gold_recall(old/new)、evidence_chars、检索节点数、步数、耗时、PASS/FAIL。
  2. Gold 命中审计:逐个 gold 节点 in_retrieved / in_evidence_text。
  3. 因果序决策 TRACE:把子 agent(depth>0)步骤挂回它所属的父 DISPATCH 之下再展示,
     不被 step_idx 的合并顺序误导。
  4. 水合审计:逐个 COLLECT 展示 section、multi-collect 展开(collect_section_ids)、
     新增/命中、以及 **purge 后代证据条数**(整枝重水合销毁精选的信号)。
  5. 最终 evidence:拆成 [E#] 块逐块展示,并标注每个 gold 是否进了 evidence。

不重跑检索,纯离线消费结果 JSON。输入可为:
  - 一个 replay 目录(map_nav_trace/replay_*/) —— 优先读 all_cases.json,否则读目录下各 <id>.json
  - all_cases.json
  - 单个 <inspect_id>.json case 文件

用法:
  python bin/58_report_map_nav_run.py                     # 自动选最新 map_nav_trace/replay_*
  python bin/58_report_map_nav_run.py map_nav_trace/replay_20260714_154950
  python bin/58_report_map_nav_run.py path/to/case.json --stdout
  python bin/58_report_map_nav_run.py <dir> --out custom_REPORT.md
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple


ROOT = Path(__file__).resolve().parents[1]

# 目录里非 case 的辅助文件,加载时跳过。
_NON_CASE_FILES = {
    "all_cases.json",
    "action_space_snapshots.json",
    "canvas_payload.json",
}


# --------------------------------------------------------------------------- #
# 加载
# --------------------------------------------------------------------------- #
def _read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def _is_case(obj: Any) -> bool:
    return isinstance(obj, dict) and "steps" in obj and "inspect_id" in obj


def load_run(path: Path) -> Tuple[Dict[str, Any], List[Dict[str, Any]], Path]:
    """Return (meta, cases, report_dir) from a dir / all_cases.json / single case json."""
    if path.is_dir():
        all_cases = path / "all_cases.json"
        if all_cases.exists():
            payload = _read_json(all_cases)
            meta = {k: v for k, v in payload.items() if k != "cases"}
            return meta, list(payload.get("cases") or []), path
        cases: List[Dict[str, Any]] = []
        for fp in sorted(path.glob("*.json")):
            if fp.name in _NON_CASE_FILES:
                continue
            obj = _read_json(fp)
            if _is_case(obj):
                cases.append(obj)
        if not cases:
            raise SystemExit(f"[report] 目录里没找到 case JSON: {path}")
        return {}, cases, path

    obj = _read_json(path)
    if isinstance(obj, dict) and "cases" in obj:
        meta = {k: v for k, v in obj.items() if k != "cases"}
        return meta, list(obj.get("cases") or []), path.parent
    if _is_case(obj):
        return {}, [obj], path.parent
    raise SystemExit(f"[report] 无法识别的 JSON 结构: {path}")


def _latest_replay_dir() -> Optional[Path]:
    base = ROOT / "map_nav_trace"
    if not base.exists():
        return None
    dirs = sorted(
        (p for p in base.glob("replay_*") if p.is_dir()),
        key=lambda p: p.name,
        reverse=True,
    )
    return dirs[0] if dirs else None


# --------------------------------------------------------------------------- #
# 因果序重建
# --------------------------------------------------------------------------- #
def _short_sid(sid: Optional[str]) -> str:
    if not sid:
        return "-"
    return sid.split(":")[-1] if ":" in sid else sid


def build_causal_forest(steps: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """把子步骤挂回其父 DISPATCH 下。

    dispatch() 把子 agent 的 action_history 先 merge(排在父 DISPATCH step 之前),
    因此扁平序里,一个 DISPATCH 之前紧邻的一批更深 depth 的步骤即它的子步。
    对递归 DISPATCH 也成立(子 DISPATCH 会先成节点再被父挂上)。
    """
    pending: List[Dict[str, Any]] = []
    for st in steps:
        node = {"step": st, "children": []}
        if str(st.get("action")) == "nav_dispatch":
            depth = int(st.get("depth") or 0)
            children = [n for n in pending if int(n["step"].get("depth") or 0) > depth]
            rest = [n for n in pending if int(n["step"].get("depth") or 0) <= depth]
            node["children"] = children
            pending = rest + [node]
        else:
            pending.append(node)
    return pending


# --------------------------------------------------------------------------- #
# 渲染
# --------------------------------------------------------------------------- #
def _decision_line(st: Dict[str, Any]) -> str:
    aid = st.get("action_id") or "-"
    kind = st.get("kind") or (str(st.get("action") or "").replace("nav_", ""))
    sid = _short_sid(st.get("section_id"))
    depth = st.get("depth")
    extra = ""
    if kind == "collect":
        csids = st.get("collect_section_ids") or []
        added = st.get("n_added")
        purged = st.get("n_purged_descendant_evidence")
        if len(csids) > 1:
            extra += f" · multi→[{', '.join(_short_sid(x) for x in csids)}]"
        elif csids:
            extra += f" · →{_short_sid(csids[0])}"
        if added is not None:
            extra += f" · +{added}"
        if purged:
            extra += f" · PURGED後代×{purged}"
    elif kind == "dispatch":
        regs = st.get("dispatch_regions") or []
        extra += f" · regions=[{', '.join(_short_sid(x) for x in regs)}]"
        if st.get("n_child_reports") is not None:
            extra += f" · child_reports={st.get('n_child_reports')}"
    return f"`{aid}` {kind} {sid} (depth={depth}){extra}"


def _render_forest(
    forest: List[Dict[str, Any]], indent: int, out: List[str]
) -> None:
    pad = "  " * indent
    for node in forest:
        st = node["step"]
        out.append(f"{pad}- {_decision_line(st)}")
        reason = (st.get("llm_reason") or "").strip()
        if reason:
            out.append(f"{pad}  - reason: {reason}")
        if node["children"]:
            out.append(f"{pad}  - ↳ 子 agent 步骤(dispatch 期间运行):")
            _render_forest(node["children"], indent + 2, out)


def _parse_evidence_blocks(text: str) -> List[Tuple[str, str]]:
    """Split '[E1]\\n...\\n\\n[E2]\\n...' into [(tag, body), ...]."""
    if not text:
        return []
    blocks: List[Tuple[str, str]] = []
    for raw in re.split(r"\n\s*\n(?=\[E\d+\])", text.strip()):
        chunk = raw.strip()
        if not chunk:
            continue
        m = re.match(r"^\[(E\d+)\]\s*", chunk)
        tag = m.group(1) if m else "E?"
        body = chunk[m.end():] if m else chunk
        blocks.append((tag, body.strip()))
    return blocks


def _fmt_recall(v: Any) -> str:
    try:
        return f"{float(v):.2f}"
    except (TypeError, ValueError):
        return "n/a"


def render_case(case: Dict[str, Any]) -> str:
    iid = case.get("inspect_id", "?")
    task_type = case.get("task_type", "?")
    query = case.get("query", "")
    doc_id = case.get("doc_id", "")
    gold_nodes = list(case.get("gold_nodes") or [])
    old = case.get("old") or {}
    new = case.get("new") or {}
    steps = list(case.get("steps") or [])

    out: List[str] = []
    out.append(f"## {iid}  ·  {task_type}")
    out.append("")
    out.append(f"- **Query:** {query}")
    out.append(f"- **Doc:** `{doc_id}`")
    out.append(f"- **Gold nodes:** {', '.join(_short_sid(x) for x in gold_nodes) or '-'}")
    out.append("")

    new_recall = new.get("gold_node_recall")
    verdict = "PASS" if (isinstance(new_recall, (int, float)) and new_recall > 0) else "FAIL"
    out.append(f"### 结果得分 — **{verdict}** (new gold_recall={_fmt_recall(new_recall)})")
    out.append("")
    out.append("| 指标 | old(baseline) | new(map-nav) |")
    out.append("|---|---:|---:|")
    out.append(
        f"| gold_recall | {_fmt_recall(old.get('gold_node_recall'))} | "
        f"{_fmt_recall(new_recall)} |"
    )
    out.append(
        f"| evidence_chars | {old.get('evidence_chars', '-')} | "
        f"{new.get('evidence_chars', '-')} |"
    )
    out.append(
        f"| n_retrieved_nodes | {old.get('n_retrieved_nodes', '-')} | "
        f"{new.get('n_retrieved_nodes', '-')} |"
    )
    st_score = new.get("score_task")
    if st_score is not None:
        out.append(f"| score_task | {old.get('score_task', '-')} | {st_score} |")
    out.append(
        f"| trajectory_steps | - | {new.get('trajectory_length', len(steps))} |"
    )
    if case.get("elapsed_sec") is not None:
        out.append(f"| elapsed_sec | - | {case.get('elapsed_sec')} |")
    out.append("")

    hits = new.get("gold_node_hits") or []
    if hits:
        out.append("### Gold 命中审计")
        out.append("")
        out.append("| gold | 命中 | in_retrieved | in_evidence_text |")
        out.append("|---|:--:|:--:|:--:|")
        for h in hits:
            hit = h.get("in_retrieved") or h.get("in_evidence_text")
            out.append(
                f"| `{_short_sid(h.get('node'))}` | {'✅' if hit else '❌'} | "
                f"{h.get('in_retrieved')} | {h.get('in_evidence_text')} |"
            )
        out.append("")

    # 决策 TRACE(因果序)
    out.append("### 决策 TRACE(因果序)")
    out.append("")
    forest = build_causal_forest(steps)
    _render_forest(forest, 0, out)
    out.append("")

    # 水合审计
    collects = [s for s in steps if s.get("kind") == "collect"]
    if collects:
        out.append("### 水合审计(COLLECT)")
        out.append("")
        out.append(
            "| step | action_id | section | 展开(multi) | +added | hits | purged后代 | full |"
        )
        out.append("|---:|---|---|---|---:|---:|---:|:--:|")
        for s in collects:
            csids = s.get("collect_section_ids") or []
            expand = ", ".join(_short_sid(x) for x in csids) if len(csids) > 1 else "-"
            purged = s.get("n_purged_descendant_evidence")
            purged_disp = str(purged) if purged else ("-" if purged in (0, None) else str(purged))
            out.append(
                f"| {s.get('step_idx')} | `{s.get('action_id')}` | "
                f"`{_short_sid(s.get('section_id'))}` | {expand} | "
                f"{s.get('n_added', '-')} | {s.get('n_hits', '-')} | "
                f"{purged_disp} | {'✅' if s.get('collect_full') else ''} |"
            )
        out.append("")
        flags = _hydration_flags(collects, gold_nodes)
        if flags:
            out.append("**水合告警:**")
            for f in flags:
                out.append(f"- {f}")
            out.append("")

    # reports_context(子 agent 汇报)
    rc = (new.get("reports_context") or "").strip()
    if rc:
        out.append("### 子 agent reports_context")
        out.append("")
        out.append("```")
        out.append(rc[:2500])
        out.append("```")
        out.append("")

    # 最终 evidence
    out.append("### 最终 evidence(new)")
    out.append("")
    blocks = _parse_evidence_blocks(new.get("evidence_text") or "")
    if blocks:
        for tag, body in blocks:
            out.append(f"**[{tag}]** {body}")
            out.append("")
    else:
        out.append("_(空 evidence)_")
        out.append("")
    rn = new.get("retrieved_nodes") or []
    if rn:
        gold_set = {str(x) for x in gold_nodes}
        marked = [
            f"{_short_sid(x)}{'⭐' if str(x) in gold_set else ''}" for x in rn
        ]
        out.append(f"- retrieved_nodes: {', '.join(marked)}")
        out.append("")

    return "\n".join(out)


def _hydration_flags(collects: List[Dict[str, Any]], gold_nodes: List[str]) -> List[str]:
    flags: List[str] = []
    gold_set = {str(x) for x in gold_nodes}
    for s in collects:
        purged = s.get("n_purged_descendant_evidence") or 0
        if purged:
            flags.append(
                f"step {s.get('step_idx')} `{s.get('action_id')}` 收父节点 "
                f"`{_short_sid(s.get('section_id'))}` 时 **purge 掉 {purged} 条后代证据**"
                "(整枝重水合,可能销毁子 agent 的精选)。"
            )
        csids = [str(x) for x in (s.get('collect_section_ids') or [])]
        if len(csids) > 1:
            non_gold = [c for c in csids if c not in gold_set]
            if gold_set and non_gold and any(c in gold_set for c in csids):
                flags.append(
                    f"step {s.get('step_idx')} 整枝水合含 {len(non_gold)} 个非 gold 叶 "
                    f"(与 gold 争抢 evidence 预算)。"
                )
    return flags


# --------------------------------------------------------------------------- #
# main
# --------------------------------------------------------------------------- #
def build_report(meta: Dict[str, Any], cases: List[Dict[str, Any]]) -> str:
    out: List[str] = []
    out.append("# Map-Nav 运行报告")
    out.append("")
    if meta.get("generated_at"):
        out.append(f"- generated_at: `{meta['generated_at']}`")
    env = meta.get("env") or {}
    if env:
        keys = [
            "EMBEDDING_MODEL",
            "NAV_MAP_MODE",
            "enable_recursive_dispatch",
            "map_char_limit",
            "max_steps",
            "navigate_max_steps",
        ]
        parts = [f"{k}=`{env[k]}`" for k in keys if k in env]
        if parts:
            out.append("- env: " + " · ".join(parts))
    # 聚合
    n = len(cases)
    passed = sum(
        1
        for c in cases
        if isinstance((c.get("new") or {}).get("gold_node_recall"), (int, float))
        and (c.get("new") or {}).get("gold_node_recall") > 0
    )
    recalls = [
        float((c.get("new") or {}).get("gold_node_recall") or 0.0) for c in cases
    ]
    mean_recall = sum(recalls) / n if n else 0.0
    out.append(
        f"- 汇总: {n} case · PASS {passed}/{n} · mean gold_recall {mean_recall:.3f}"
    )
    out.append("")
    out.append("| inspect_id | task_type | gold_recall | evidence_chars | steps |")
    out.append("|---|---|---:|---:|---:|")
    for c in cases:
        new = c.get("new") or {}
        out.append(
            f"| {c.get('inspect_id')} | {c.get('task_type')} | "
            f"{_fmt_recall(new.get('gold_node_recall'))} | "
            f"{new.get('evidence_chars', '-')} | "
            f"{new.get('trajectory_length', len(c.get('steps') or []))} |"
        )
    out.append("")
    out.append("---")
    out.append("")
    for c in cases:
        out.append(render_case(c))
        out.append("")
        out.append("---")
        out.append("")
    return "\n".join(out)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "path",
        nargs="?",
        default=None,
        help="replay 目录 / all_cases.json / 单个 case.json(默认取最新 replay_*)",
    )
    parser.add_argument("--out", type=Path, default=None, help="输出 md 路径")
    parser.add_argument("--stdout", action="store_true", help="同时打印到 stdout")
    args = parser.parse_args()

    if args.path:
        in_path = Path(args.path)
    else:
        latest = _latest_replay_dir()
        if latest is None:
            raise SystemExit("[report] 未找到 map_nav_trace/replay_*,请显式传入路径。")
        in_path = latest
        print(f"[report] 使用最新 replay: {in_path}", file=sys.stderr)

    if not in_path.exists():
        raise SystemExit(f"[report] 路径不存在: {in_path}")

    meta, cases, report_dir = load_run(in_path)
    report = build_report(meta, cases)

    out_path = args.out or (report_dir / "REPORT.md")
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(report + "\n", encoding="utf-8")
    print(f"[report] wrote {out_path}  ({len(cases)} case)")
    if args.stdout:
        print("\n" + report)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
