#!/usr/bin/env python3
"""Generate a lightweight markdown summary for the skill's eval inventory."""

from __future__ import annotations

import json
import sys
from pathlib import Path


def read_json(path: Path) -> dict | list:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    root = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path.cwd()
    evals_path = root / "evals" / "evals.json"
    trigger_path = root / "evals" / "trigger_queries.json"

    evals_data = read_json(evals_path)
    trigger_data = read_json(trigger_path)

    assert isinstance(evals_data, dict)
    assert isinstance(trigger_data, list)

    positives = sum(1 for item in trigger_data if item.get("should_trigger") is True)
    negatives = sum(1 for item in trigger_data if item.get("should_trigger") is False)

    lines = [
        f"# Eval Summary: {evals_data['skill_name']}",
        "",
        f"- Prompt eval cases: {len(evals_data['evals'])}",
        f"- Trigger-positive queries: {positives}",
        f"- Trigger-negative queries: {negatives}",
        "",
        "## Prompt Evals",
    ]

    for item in evals_data["evals"]:
        lines.append(f"- `{item['id']}`: {item['expected_output']}")

    lines.extend(
        [
            "",
            "## Trigger Queries",
            f"- Positives: {positives}",
            f"- Negatives: {negatives}",
        ]
    )

    print("\n".join(lines))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
