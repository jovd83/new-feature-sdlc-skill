#!/usr/bin/env python3
"""Build a static review page for this skill using skill-creator's eval viewer."""

from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path


def slugify(value: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    return slug or "eval"


def read_json(path: Path) -> dict | list:
    return json.loads(path.read_text(encoding="utf-8"))


def detect_skill_creator_root(explicit: str | None) -> Path:
    if explicit:
        root = Path(explicit).resolve()
        viewer = root / "eval-viewer" / "generate_review.py"
        if viewer.exists():
            return root
        raise FileNotFoundError(f"generate_review.py not found under {root}")

    candidates = [
        Path(r"C:\Users\jochi\.agents\skills\skill-creator"),
        Path.home() / ".agents" / "skills" / "skill-creator",
        Path.home() / ".codex" / "skills" / ".system" / "skill-creator",
    ]
    for root in candidates:
        if (root / "eval-viewer" / "generate_review.py").exists():
            return root.resolve()
    raise FileNotFoundError("Could not locate skill-creator. Pass --skill-creator-root explicitly.")


def build_workspace(root: Path, workspace: Path) -> None:
    evals_path = root / "evals" / "evals.json"
    evals_data = read_json(evals_path)
    assert isinstance(evals_data, dict)

    if workspace.exists():
        shutil.rmtree(workspace)
    workspace.mkdir(parents=True, exist_ok=True)

    for item in evals_data["evals"]:
        eval_name = slugify(f"{item['id']}-{item['prompt'][:40]}")
        run_dir = workspace / f"eval-{item['id']}-{eval_name}" / "with_skill"
        outputs_dir = run_dir / "outputs"
        outputs_dir.mkdir(parents=True, exist_ok=True)

        metadata = {
            "eval_id": item["id"],
            "eval_name": eval_name,
            "prompt": item["prompt"],
            "assertions": item.get("expectations", []),
        }
        (run_dir / "eval_metadata.json").write_text(json.dumps(metadata, indent=2) + "\n", encoding="utf-8")

        transcript = [
            "## Eval Prompt",
            "",
            item["prompt"],
            "",
            "## Eval Context",
            "",
            "This workspace was generated from eval definitions to review prompt quality, expected outcomes, and assertions using the skill-creator eval viewer.",
        ]
        (run_dir / "transcript.md").write_text("\n".join(transcript) + "\n", encoding="utf-8")

        expected_output = item.get("expected_output", "")
        expectations = item.get("expectations", [])
        files = item.get("files", [])

        (outputs_dir / "expected_output.md").write_text(expected_output + "\n", encoding="utf-8")
        (outputs_dir / "expectations.md").write_text(
            "\n".join([f"- {entry}" for entry in expectations]) + ("\n" if expectations else ""),
            encoding="utf-8",
        )
        (outputs_dir / "input_files.md").write_text(
            "\n".join([f"- {entry}" for entry in files]) + ("\n" if files else "None\n"),
            encoding="utf-8",
        )
        (outputs_dir / "review_notes.md").write_text(
            "Use this viewer pass to judge whether the eval prompt is realistic, whether the expected output is discriminating, and whether the expectations would catch shallow or incorrect feature-delivery behavior.\n",
            encoding="utf-8",
        )


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate a static eval review page using skill-creator's viewer.")
    parser.add_argument("path", nargs="?", default=".", help="Path to the skill repository root")
    parser.add_argument(
        "--skill-creator-root",
        default=None,
        help="Path to the skill-creator repository root containing eval-viewer/generate_review.py",
    )
    parser.add_argument(
        "--workspace",
        default="evals/review-workspace/current",
        help="Workspace path to build before invoking the viewer",
    )
    parser.add_argument(
        "--output",
        default="evals/review-workspace/review.html",
        help="Static HTML output path",
    )
    args = parser.parse_args()

    root = Path(args.path).resolve()
    workspace = (root / args.workspace).resolve()
    output = (root / args.output).resolve()
    skill_creator_root = detect_skill_creator_root(args.skill_creator_root)
    viewer_script = skill_creator_root / "eval-viewer" / "generate_review.py"

    build_workspace(root, workspace)

    command = [
        sys.executable,
        str(viewer_script),
        str(workspace),
        "--skill-name",
        root.name,
        "--static",
        str(output),
    ]
    subprocess.run(command, check=True)

    print(f"Generated review workspace: {workspace}")
    print(f"Generated static eval review: {output}")
    print(f"Viewer source: {viewer_script}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
