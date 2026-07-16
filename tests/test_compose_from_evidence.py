"""Unit tests for bin/59_compose_judge_from_evidence.py (no LLM calls)."""

from __future__ import annotations

import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "bin" / "59_compose_judge_from_evidence.py"


def _load_mod():
    spec = importlib.util.spec_from_file_location("compose_from_evidence_59", SCRIPT)
    assert spec and spec.loader
    mod = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = mod
    spec.loader.exec_module(mod)
    return mod


class ComposeFromEvidenceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.mod = _load_mod()

    def test_normalize_and_dedupe_replay_cases(self) -> None:
        mod = self.mod
        raw = {
            "inspect_id": "t1",
            "query": "q",
            "task_type": "niche_fact",
            "doc_id": "d1",
            "gold_nodes": ["d1:L1"],
            "new": {
                "evidence_text": "[E1]\nhello",
                "evidence_chars": 10,
                "retrieved_nodes": ["d1:L1"],
                "trajectory_length": 3,
                "gold_node_recall": 1.0,
            },
            "steps": [],
        }
        n1 = mod._normalize_case(raw, from_replay=True)
        self.assertIsNotNone(n1)
        assert n1 is not None
        self.assertEqual(n1["inspect_id"], "t1")
        self.assertEqual(n1["evidence_text"], "[E1]\nhello")

        bad = dict(raw)
        bad["new"] = {}
        self.assertIsNone(mod._normalize_case(bad, from_replay=True))

        deduped = mod._dedupe_cases([n1, dict(n1), dict(n1)])
        self.assertEqual(len(deduped), 1)

    def test_load_evidence_jsonl_and_fingerprint(self) -> None:
        mod = self.mod
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            jp = root / "evidence_for_compose.jsonl"
            rows = [
                {
                    "inspect_id": "a",
                    "query": "qa",
                    "evidence_text": "ea",
                    "retrieved_nodes": ["d:L1"],
                },
                {
                    "inspect_id": "b",
                    "query": "qb",
                    "evidence_text": "eb",
                    "retrieved_nodes": ["d:L2"],
                },
                {"inspect_id": "a", "query": "dup", "evidence_text": "should_drop"},
            ]
            jp.write_text(
                "\n".join(json.dumps(r, ensure_ascii=False) for r in rows) + "\n",
                encoding="utf-8",
            )
            cases = mod._load_evidence_cases(replay_dir=None, evidence_jsonl=jp)
            self.assertEqual([c["inspect_id"] for c in cases], ["a", "b"])
            fp1 = mod._evidence_fingerprint(cases)
            cases2 = [dict(cases[0]), dict(cases[1])]
            cases2[0]["evidence_text"] = "changed"
            fp2 = mod._evidence_fingerprint(cases2)
            self.assertNotEqual(fp1, fp2)

    def test_checkpoint_resume_skips_corrupt_and_incomplete(self) -> None:
        mod = self.mod
        with tempfile.TemporaryDirectory() as td:
            ckpt = Path(td) / "checkpoint.jsonl"
            sig = "sig_test"
            good_arm = {
                "composed_answer": '{"task_type":"niche_fact","answer":"x"}',
                "metrics": {"score_task": 1.0},
                "evidence_text": "e",
                "evidence_chars_actual": 1,
            }
            good_row = mod._build_row(
                task_idx=1,
                task=mod.AgentTask(
                    query="q",
                    doc_id="d",
                    gold_nodes=[],
                    inspect_id="ok1",
                    task_type="niche_fact",
                ),
                iid="ok1",
                arm_block=good_arm,
            )
            mod._append_checkpoint(
                ckpt,
                sig,
                inspect_id="ok1",
                task_idx=1,
                row=good_row,
                cost_delta={},
            )
            # Append incomplete + corrupt lines manually.
            with ckpt.open("a", encoding="utf-8") as f:
                f.write(
                    json.dumps(
                        {
                            "kind": "task",
                            "inspect_id": "bad1",
                            "row": {"inspect_id": "bad1", "hierarchical_gold_map": {}},
                        },
                        ensure_ascii=False,
                    )
                    + "\n"
                )
                f.write("{not-json\n")

            loaded = mod._load_checkpoint(ckpt, sig)
            self.assertIn("ok1", loaded)
            self.assertNotIn("bad1", loaded)

            stale = mod._load_checkpoint(ckpt, "other_sig")
            self.assertEqual(stale, {})

    def test_validate_cases_warnings(self) -> None:
        mod = self.mod
        warns = mod._validate_cases(
            [
                {
                    "inspect_id": "x",
                    "query": "",
                    "evidence_text": "",
                    "retrieved_nodes": [],
                }
            ]
        )
        self.assertTrue(any("empty evidence_text" in w for w in warns))
        self.assertTrue(any("empty retrieved_nodes" in w for w in warns))
        self.assertTrue(any("empty query" in w for w in warns))

    def test_dry_run_against_real_replay_smoke(self) -> None:
        """Offline wiring check on the real 400 replay (max 2 ids)."""
        replay = ROOT / "map_nav_trace" / "replay_20260716_173430"
        if not replay.is_dir():
            self.skipTest("replay_20260716_173430 not present")
        import subprocess

        proc = subprocess.run(
            [
                sys.executable,
                str(SCRIPT),
                "--replay-dir",
                str(replay),
                "--max-tasks",
                "2",
                "--dry-run",
                "--out",
                str(ROOT / "results" / "_dry_run_compose_from_replay.json"),
                "--checkpoint-jsonl",
                str(ROOT / "cache" / "compose_from_replay_dry" / "checkpoint.jsonl"),
            ],
            cwd=str(ROOT),
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(proc.returncode, 0, msg=proc.stderr + proc.stdout)
        self.assertIn('"dry_run": true', proc.stdout)
        self.assertIn('"n_cases": 2', proc.stdout)


if __name__ == "__main__":
    unittest.main()
