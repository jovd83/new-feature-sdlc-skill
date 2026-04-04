# Changelog
2: 
3: ## 1.0.1 - 2026-04-03
4: 
5: ### Added
6: 
7: - GitHub repository badges (version, license, stats, support)
8: - Gotchas section to `SKILL.md` for better process guidance
9: 
10: ## 1.0.0 - 2026-03-21

Initial enterprise-grade upgrade release for `new-feature-sdlc-skill`.

### Added

- GitHub-facing packaging with README, contributing guidance, version metadata, icons, and agent metadata polish
- stronger orchestration contract in `SKILL.md` with explicit phase gates, guardrails, and memory boundaries
- new discovery reference for repository gating and artifact sizing
- prompt-based eval inventory in `evals/evals.json`
- trigger-routing eval inventory in `evals/trigger_queries.json`
- repository validator in `scripts/quick_validate.py`
- eval summary helper in `scripts/eval_report.py`
- PowerShell regression tests in `tests/`

### Changed

- rewrote planning, implementation, verification, and reporting references for stronger enterprise guidance
- upgraded scaffold and project-structure scripts for safer defaults and better reuse
- replaced the old report contract with a cleaner, evidence-based structure
- improved `agents/openai.yaml` with icons and brand color

### Validated

- `python .\scripts\quick_validate.py .`
- `Invoke-Pester .\tests`
- `python .\scripts\eval_report.py .`
