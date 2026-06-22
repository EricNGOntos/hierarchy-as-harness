#!/usr/bin/env python3
"""Align fair-clean scope tasks to the current corpus and logical item boundaries."""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
TASKS = ROOT / "data/tasks/tasks_realdata_bodyrich_fair_clean.jsonl"
INSPECT = ROOT / "data/tasks/tasks_realdata_bodyrich_fair_clean.inspect.jsonl"

# One group per logical answer item; groups include continuation lines.
LINE_GROUPS: dict[str, list[list[int]]] = {
    "q400_scope_0001": [[83], [84]],
    "q400_scope_0002": [[94], [95], [96], [97], [98], [99]],
    "q400_scope_0003": [[105], [106], [107], [108], [109], [110]],
    "q400_scope_0004": [[120], [121], [122], [123], [124], [125]],
    "q400_scope_0005": [[63], [64], [66]],
    "q400_scope_0006": [[69], [72], [74]],
    "q400_scope_0007": [[78, 79], [81], [83], [85], [87]],
    "q400_scope_0008": [[121], [122], [123], [124], [125], [126], [127], [128], [129], [130], [131], [132]],
    "q400_scope_0009": [[26], [27], [28]],
    "q400_scope_0010": [[34], [35], [36]],
    "q400_scope_0011": [[147], [148]],
    "q400_scope_0012": [[171], [172]],
    "q400_scope_0013": [[199], [200]],
    "q400_scope_0014": [[214], [215], [216], [217], [218]],
    "q400_scope_0015": [[57], [57], [57], [57], [57], [57]],
    "q400_scope_0016": [[129], [130, 131], [132], [133], [134, 135], [136]],
    "q400_scope_0017": [[5], [6], [7, 8]],
}

SCOPE_0017_QUERY = (
    "在《线上学习平台学习管理方案（修订）.docx》，围绕问题“列出线上学习平台中心、"
    "各专家组、平台中心办公室三个管理机构及其职责”，列出直接对应的全部条目；不要回答相邻章节内容。"
)

SCOPE_0008_ITEMS = [
    "《砌体结构工程施工质量验收规范》GB50203",
    "《建筑装饰装修工程质量验收标准》GB50210",
    "《建筑节能工程施工质量验收标准》GB50411",
    "《烧结多孔砖和多孔砌块》GB13544",
    "《建筑幕墙》GB/T21086",
    "《烧结装饰砖》GB/T32982",
    "《建筑幕墙用陶板》JG/T 324",
    "《玻璃幕墙工程技术规范》JGJ102",
    "《金属与石材幕墙工程技术规范》JGJ133",
    "《外墙外保温工程技术标准》JGJ144",
    "《建筑幕墙工程技术标准》DBJ61/T 161",
    "《陶板幕墙工程技术规程》Q/TOBSG-03",
]


def _read_jsonl(path: Path) -> list[dict[str, Any]]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def _write_jsonl(path: Path, rows: list[dict[str, Any]]) -> None:
    path.write_text("".join(json.dumps(row, ensure_ascii=False) + "\n" for row in rows), encoding="utf-8")


def _logical_items(final_answer: str) -> list[str]:
    return [part.strip(" 。；") for part in str(final_answer or "").split("；") if part.strip(" 。；")]


def main() -> None:
    tasks = _read_jsonl(TASKS)
    inspect_rows = _read_jsonl(INSPECT)
    inspect_by_id = {str(row["id"]): row for row in inspect_rows}

    for task in tasks:
        iid = str(task.get("inspect_id") or "")
        if iid not in LINE_GROUPS:
            continue
        inspect = inspect_by_id[iid]
        target = dict(inspect["target"])
        if iid == "q400_scope_0008":
            target["final_answer"] = "；".join(SCOPE_0008_ITEMS) + "。"
        if iid == "q400_scope_0017":
            task["query"] = SCOPE_0017_QUERY
            inspect["input"] = SCOPE_0017_QUERY
            corpus_items = [
                "（一）十一在线平台中心：负责课程体系设计、课程开发计划审批、课程考核标准设定、平台建设费用审批等相关事宜。",
                "（二）各专家组：负责各领域内员工培训需求征集，教材、课件及习题开发，课件修改、适时更新、审核，业务答疑，题库组建等工作，集团对口业务部门负责人为各专业课程开发责任人，统筹推进本业务系统课程开发工作。",
                "（三）十一在线平台中心办公室：负责线上学习平台搭建，维护平台基本信息，监督各专家组及相关部门及时更新学习内容，组织各专家组和二级单位平台管理员进行平台管理培训，并对各专家组课程开发情况、学员学习情况进行跟踪和定期调研，反馈十一在线平台中心。",
            ]
            target["final_answer"] = "；".join(corpus_items) + "。"

        items = _logical_items(str(target.get("final_answer") or ""))
        if iid == "q400_scope_0007" and len(items) == 6:
            # The third numbered construction step contains an internal semicolon.
            items = items[:2] + [items[2] + "；" + items[3]] + items[4:]
        groups = LINE_GROUPS[iid]
        if len(items) != len(groups):
            raise RuntimeError(f"{iid}: items={len(items)} groups={len(groups)}")
        all_ids = list(dict.fromkeys(lid for group in groups for lid in group))
        target["table"] = [
            {"序号": idx, "项": item, "对应证据行": group[0], "备注": ""}
            for idx, (item, group) in enumerate(zip(items, groups), start=1)
        ]
        target["summary"] = {"total_items": len(items), "completeness": "complete"}
        target["evidence_line_ids"] = all_ids
        inspect["target"] = target
        inspect["metadata"]["gold_line_ids"] = all_ids

        doc_id = str(task["doc_id"])
        task["gold_nodes"] = [f"{doc_id}:L{lid}" for lid in all_ids]
        task["gold_answer"] = json.dumps(target, ensure_ascii=False)

    _write_jsonl(TASKS, tasks)
    _write_jsonl(INSPECT, inspect_rows)
    print(f"repaired {len(LINE_GROUPS)} scope tasks")


if __name__ == "__main__":
    main()
