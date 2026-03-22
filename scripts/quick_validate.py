#!/usr/bin/env python3
"""Lightweight validator for the new-feature-sdlc-skill repository."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


class Reporter:
    def __init__(self) -> None:
        self.failures = 0
        self.warnings = 0

    def ok(self, message: str) -> None:
        print(f"PASS  {message}")

    def warn(self, message: str) -> None:
        self.warnings += 1
        print(f"WARN  {message}")

    def fail(self, message: str) -> None:
        self.failures += 1
        print(f"FAIL  {message}")


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def parse_frontmatter(path: Path, reporter: Reporter) -> tuple[dict[str, str], str] | None:
    text = read_text(path)
    match = re.match(r"^---\r?\n(.*?)\r?\n---\r?\n?(.*)$", text, re.DOTALL)
    if not match:
        reporter.fail(f"{path.name} is missing valid YAML frontmatter")
        return None

    raw_frontmatter, body = match.groups()
    data: dict[str, str] = {}
    for line in raw_frontmatter.splitlines():
        stripped = line.strip()
        if not stripped:
            continue
        if ":" not in stripped:
            reporter.fail(f"{path.name} has an invalid frontmatter line: {line}")
            return None
        key, value = stripped.split(":", 1)
        data[key.strip()] = value.strip().strip('"').strip("'")
    return data, body


def validate_json_file(path: Path, reporter: Reporter, root: Path) -> dict | list | None:
    if not path.exists():
        reporter.fail(f"Missing JSON file: {path.relative_to(root)}")
        return None
    try:
        data = json.loads(read_text(path))
    except json.JSONDecodeError as exc:
        reporter.fail(f"{path.relative_to(root)} is not valid JSON: {exc}")
        return None
    reporter.ok(f"Valid JSON: {path.relative_to(root)}")
    return data


def validate_skill(root: Path, reporter: Reporter) -> None:
    skill_path = root / "SKILL.md"
    if not skill_path.exists():
        reporter.fail("Missing SKILL.md")
        return

    parsed = parse_frontmatter(skill_path, reporter)
    if not parsed:
        return

    frontmatter, body = parsed
    if set(frontmatter) != {"name", "description"}:
        reporter.fail(f"SKILL.md frontmatter should only contain name and description, found: {sorted(frontmatter)}")
    else:
        reporter.ok("SKILL.md frontmatter only contains name and description")

    if frontmatter.get("name") != root.name:
        reporter.fail("Skill name does not match directory name")
    else:
        reporter.ok("Skill name matches directory name")

    description = frontmatter.get("description", "")
    if not description:
        reporter.fail("SKILL.md description is empty")
    elif "Use when" not in description:
        reporter.fail("SKILL.md description should include 'Use when'")
    else:
        reporter.ok("SKILL.md description includes a trigger phrase")

    for phrase in [
        "## Outcomes",
        "## Operating Model",
        "## Decision Rules",
        "## Guardrails",
        "## Memory Model",
        "## Resource Map",
        "Runtime memory",
        "Shared memory",
    ]:
        if phrase in body:
            reporter.ok(f"SKILL.md includes '{phrase}'")
        else:
            reporter.fail(f"SKILL.md is missing '{phrase}'")


def validate_openai_yaml(root: Path, reporter: Reporter) -> None:
    path = root / "agents" / "openai.yaml"
    if not path.exists():
        reporter.fail("Missing agents/openai.yaml")
        return

    text = read_text(path)
    required_patterns = {
        "display_name": r'display_name:\s*"[^"]+"',
        "short_description": r'short_description:\s*"[^"]+"',
        "icon_small": r'icon_small:\s*"[^"]+\.(svg|png)"',
        "icon_large": r'icon_large:\s*"[^"]+\.(svg|png)"',
        "brand_color": r'brand_color:\s*"#(?:[0-9A-Fa-f]{6})"',
        "default_prompt": r'default_prompt:\s*"[^"]*\$new-feature-sdlc-skill[^"]*"',
        "allow_implicit_invocation": r"allow_implicit_invocation:\s*true",
    }

    for label, pattern in required_patterns.items():
        if re.search(pattern, text):
            reporter.ok(f"agents/openai.yaml contains {label}")
        else:
            reporter.fail(f"agents/openai.yaml is missing or invalid: {label}")


def validate_evals(root: Path, reporter: Reporter) -> None:
    evals_path = root / "evals" / "evals.json"
    trigger_path = root / "evals" / "trigger_queries.json"

    evals_data = validate_json_file(evals_path, reporter, root)
    if isinstance(evals_data, dict):
        if evals_data.get("skill_name") == root.name:
            reporter.ok("evals/evals.json skill_name matches repository name")
        else:
            reporter.fail("evals/evals.json skill_name does not match repository name")

        cases = evals_data.get("evals")
        if isinstance(cases, list) and cases:
            reporter.ok("evals/evals.json contains eval cases")
            seen_ids: set[int] = set()
            for item in cases:
                if not isinstance(item, dict):
                    reporter.fail(f"Invalid eval item: {item}")
                    continue
                for field in ("id", "prompt", "expected_output", "expectations"):
                    if field not in item:
                        reporter.fail(f"Eval case missing '{field}': {item}")
                case_id = item.get("id")
                if isinstance(case_id, int):
                    if case_id in seen_ids:
                        reporter.fail(f"Duplicate eval id: {case_id}")
                    else:
                        seen_ids.add(case_id)
                        reporter.ok(f"Eval id is unique: {case_id}")
                else:
                    reporter.fail(f"Eval id must be an integer: {item}")
                prompt = item.get("prompt", "")
                if "$new-feature-sdlc-skill" in prompt:
                    reporter.ok(f"Eval prompt explicitly invokes the skill: {case_id}")
                else:
                    reporter.fail(f"Eval prompt must explicitly invoke $new-feature-sdlc-skill: {case_id}")
                expectations = item.get("expectations")
                if isinstance(expectations, list) and expectations:
                    reporter.ok(f"Eval has expectations: {case_id}")
                else:
                    reporter.fail(f"Eval expectations must be a non-empty list: {case_id}")
        else:
            reporter.fail("evals/evals.json must contain a non-empty evals list")

    trigger_data = validate_json_file(trigger_path, reporter, root)
    if isinstance(trigger_data, list) and trigger_data:
        reporter.ok("evals/trigger_queries.json contains trigger cases")
        positives = 0
        negatives = 0
        for item in trigger_data:
            if not isinstance(item, dict) or "query" not in item or "should_trigger" not in item:
                reporter.fail(f"Invalid trigger query entry: {item}")
                continue
            if not str(item["query"]).strip():
                reporter.fail(f"Trigger query is empty: {item}")
                continue
            if isinstance(item["should_trigger"], bool):
                positives += int(item["should_trigger"])
                negatives += int(not item["should_trigger"])
            else:
                reporter.fail(f"Trigger query should_trigger must be boolean: {item}")
        if positives >= 4 and negatives >= 4:
            reporter.ok("Trigger queries include a healthy balance of positives and negatives")
        else:
            reporter.fail("Trigger queries should include at least 4 positive and 4 negative cases")
    else:
        reporter.fail("evals/trigger_queries.json must contain a non-empty array")


def validate_scripts(root: Path, reporter: Reporter) -> None:
    for relative_path in [
        "scripts/generate_eval_view.py",
        "scripts/eval_report.py",
        "scripts/scaffold-feature.ps1",
        "scripts/validate-project-structure.ps1",
        "scripts/quick_validate.py",
    ]:
        if (root / relative_path).exists():
            reporter.ok(f"Script present: {relative_path}")
        else:
            reporter.fail(f"Missing script: {relative_path}")


def validate_tests(root: Path, reporter: Reporter) -> None:
    for relative_path in [
        "tests/ScaffoldFeature.Tests.ps1",
        "tests/ValidateProjectStructure.Tests.ps1",
    ]:
        if (root / relative_path).exists():
            reporter.ok(f"Test present: {relative_path}")
        else:
            reporter.fail(f"Missing test: {relative_path}")


def validate_assets(root: Path, reporter: Reporter) -> None:
    for relative_path in [
        "assets/icon-small.svg",
        "assets/icon-large.svg",
    ]:
        if (root / relative_path).exists():
            reporter.ok(f"Asset present: {relative_path}")
        else:
            reporter.fail(f"Missing asset: {relative_path}")


def validate_readme(root: Path, reporter: Reporter) -> None:
    path = root / "README.md"
    if not path.exists():
        reporter.warn("README.md is missing")
        return

    text = read_text(path)
    for phrase in [
        "## What This Skill Does",
        "## What This Skill Does Not Do",
        "## Evaluation",
        "## Validation",
        "evals.json",
        "trigger_queries.json",
        "quick_validate.py",
    ]:
        if phrase in text:
            reporter.ok(f"README.md includes '{phrase}'")
        else:
            reporter.warn(f"README.md is missing '{phrase}'")


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate the new-feature-sdlc-skill repository.")
    parser.add_argument("path", nargs="?", default=".", help="Path to the skill repository root")
    args = parser.parse_args()

    root = Path(args.path).resolve()
    reporter = Reporter()

    validate_skill(root, reporter)
    validate_openai_yaml(root, reporter)
    validate_evals(root, reporter)
    validate_scripts(root, reporter)
    validate_tests(root, reporter)
    validate_assets(root, reporter)
    validate_readme(root, reporter)

    print()
    print(f"Completed with {reporter.failures} failure(s) and {reporter.warnings} warning(s).")
    return 1 if reporter.failures else 0


if __name__ == "__main__":
    sys.exit(main())
