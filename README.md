# New Feature SDLC Skill

![Version](https://img.shields.io/badge/version-1.0.1-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
![Validate Skills](https://img.shields.io/badge/Validate-Skills-success)
[![Buy Me a Coffee](https://img.shields.io/badge/Buy%20Me%20a%20Coffee-ffdd00?style=flat&logo=buy-me-a-coffee&logoColor=black)](https://buymeacoffee.com/jovd83)


An Agent Skill for orchestrating approved feature delivery in an existing codebase from discovery through implementation, verification, and closeout.

This repository is designed for teams that want a strong "build the feature end to end" skill without hard-coding one stack, one test framework, or one documentation layout into every project.

## Metadata

- Author: `jovd83`
- Version: `1.0.1`

## What This Skill Does

- gates work on approval and scope clarity
- inspects repository conventions before imposing structure
- guides planning, technical design, implementation, testing, and reporting
- preserves traceability across requirements, docs, code, tests, and final delivery evidence
- provides small helper scripts for scaffolding lightweight artifacts

## What This Skill Does Not Do

- replace stack-specific implementation skills
- act as a bug-fix, refactor, audit, or migration skill
- force a universal `docs/` layout on repositories that already have one
- introduce shared-memory infrastructure into the repository

## Repository Structure

```text
new-feature-sdlc-skill/
|-- CHANGELOG.md
|-- CONTRIBUTING.md
|-- SKILL.md
|-- README.md
|-- VERSION
|-- agents/
|   `-- openai.yaml
|-- assets/
|   |-- icon-large.svg
|   `-- icon-small.svg
|-- references/
|   |-- project-discovery-and-gating.md
|   |-- planning-workflow.md
|   |-- implementation-playbook.md
|   |-- testing-verification.md
|   |-- reporting-contract.md
|   `-- report_template.md
|-- scripts/
|   |-- eval_report.py
|   |-- generate_eval_view.py
|   |-- quick_validate.py
|   |-- scaffold-feature.ps1
|   `-- validate-project-structure.ps1
`-- evals/
    |-- evals.json
    |-- README.md
    `-- trigger_queries.json
`-- tests/
    |-- ScaffoldFeature.Tests.ps1
    `-- ValidateProjectStructure.Tests.ps1
```

## Core Workflow

1. Confirm the request is an approved feature.
2. Inspect the repository and reuse its existing conventions.
3. Create or update planning and technical artifacts only where useful.
4. Implement the feature with minimal unrelated churn.
5. Verify with the strongest practical evidence.
6. Close with a structured implementation report.

## Installation

Place the skill folder in your Codex-discoverable skills directory, typically `~/.codex/skills` or `$CODEX_HOME/skills`.

## Recommended Invocation

Use prompts such as:

- `Use $new-feature-sdlc-skill to deliver this approved feature end to end.`
- `Use $new-feature-sdlc-skill to inspect the repo, plan the work, implement it, and return a release-ready report.`

## Scripts

### `scripts/quick_validate.py`

Validate the repository contract, metadata, scripts, and eval artifacts.

```powershell
python .\scripts\quick_validate.py .
```

### `scripts/eval_report.py`

Generate a lightweight markdown summary of the current eval inventory.

```powershell
python .\scripts\eval_report.py .
```

### `scripts/generate_eval_view.py`

Use the real review viewer from the `skill-creator` skill to generate a static HTML page for this repo's eval definitions.

```powershell
python .\scripts\generate_eval_view.py .
```

### `scripts/validate-project-structure.ps1`

Inspect or optionally create a default SDLC folder layout for repositories that want one.

```powershell
powershell -File .\scripts\validate-project-structure.ps1 -Root C:\repo -EmitJson
```

### `scripts/scaffold-feature.ps1`

Scaffold lightweight planning, technical, or report starter documents.

```powershell
powershell -File .\scripts\scaffold-feature.ps1 -Title "Forgot Password" -Type Epic -Id FEAT-42 -Root C:\repo
```

## Evaluation

The `evals/` directory contains prompt-based smoke evals, trigger routing checks, and guidance for behavioral review. Start with `evals/README.md`.

For human review of the current eval inventory, this repository can build a viewer-compatible workspace and then call `skill-creator`'s `eval-viewer/generate_review.py` in static mode.

## Validation

Run the repository validator after substantive edits:

```powershell
python .\scripts\quick_validate.py .
python .\scripts\generate_eval_view.py .
Invoke-Pester .\tests
```

## Optional Integrations

- stack-specific testing skills for Playwright, Cypress, JUnit, Rest Assured, and similar tools
- architecture or diagramming skills for richer technical artifacts
- shared-memory skills when durable cross-agent conventions must be stored outside the repo

These integrations are optional and intentionally kept outside the core skill boundary.

## Out of Scope

The following are conceptual extensions, not implemented in this repository:

- automatic promotion of feature notes into shared organizational memory
- autonomous release management or deployment orchestration
- repository-specific schema generation for every possible documentation system

## Suggested Repository Name

`feature-delivery-orchestrator-skill`

The current name is serviceable, but this alternative is more discoverable and clearer to GitHub users scanning a skill catalog.
