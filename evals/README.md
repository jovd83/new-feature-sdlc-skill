# Evaluation Guide

Use these artifacts to validate that the skill is both discoverable and behaviorally useful.

## Prompt-Based Smoke Evals

`evals.json` follows the prompt-based eval structure used by the skill-creation workflow:

- each eval has an `id`, `prompt`, `expected_output`, optional `files`, and `expectations`
- prompts are realistic multi-step feature-delivery requests rather than toy one-liners
- expectations are qualitative but still concrete enough for grading or human review

## Trigger Evaluation

`trigger_queries.json` contains positive and negative trigger examples. A good result should:

- trigger on approved end-to-end feature requests
- avoid triggering on bug fixes, refactors, test-only work, ops incidents, or unapproved ideas

## Behavioral Evaluation Ideas

Run forward tests with tasks such as:

1. An approved backend-only feature in a repo with no `docs/` structure.
2. An approved UI feature in a repo that already has ADRs and design docs.
3. An approved cross-service feature where coverage tooling is partially missing.
4. A request that looks feature-like but is actually a refactor.

## What To Look For

- the skill inspects the repository before prescribing structure
- the skill asks for approval only when needed
- the skill does not hallucinate coverage or validation
- the final report follows the reporting contract
- the skill scales documentation to the size of the feature

## Suggested Regression Checks

- validate `SKILL.md` frontmatter and trigger phrasing after edits
- validate `evals/evals.json` and `evals/trigger_queries.json`
- run the PowerShell scripts on a temporary directory
- run `Invoke-Pester .\tests`
- run `python .\scripts\eval_report.py .`
- run `python .\scripts\generate_eval_view.py .` to generate a static review page with the `skill-creator` viewer
- confirm report headings remain stable for downstream parsing
