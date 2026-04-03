---
name: new-feature-sdlc-skill
description: Orchestrate approved new-feature delivery in an existing codebase from discovery through implementation, testing, and closeout. Use when Codex is asked to build a net-new or materially expanded feature end to end, especially when the request expects planning artifacts, architecture updates, production code, tests, documentation, or release-ready reporting. Do not use for isolated bug fixes, narrow refactors, test-only work, ops incidents, or unapproved feature ideas.
---

# New Feature SDLC Skill

Use this skill to run a disciplined feature-delivery workflow in an established repository without turning every request into heavyweight process theater.

This skill is an orchestrator. It does not replace stack-specific implementation or testing skills. It ensures the work moves through the right gates, produces the right artifacts, and closes with evidence.

## Outcomes

- Confirm whether the work is actually an approved feature request.
- Discover repository conventions before proposing structure or code changes.
- Produce right-sized planning, design, implementation, testing, and documentation artifacts.
- Preserve traceability between requirements, design intent, code, tests, and final reporting.
- Finish with a clear implementation report that states what was done, what was verified, and what remains open.

## Do Not Use This Skill For

- Bug fixes, hotfixes, or flaky-test stabilization with no feature scope.
- Pure refactors, migrations, audits, or dependency upgrades.
- Brainstorming, roadmap exploration, or pre-approval discovery.
- Small one-file enhancements that do not need SDLC orchestration.

If the request is mixed, apply this skill only to the feature-delivery portion.

## Operating Model

Work in phases. Do not skip forward blindly, but do scale the depth to the repository and the request.

### Phase 0: Entry Gate

1. Confirm the request is a feature, not a bug fix or refactor.
2. Confirm approval status.
3. Inspect repository structure, existing docs, tests, and release conventions.
4. Decide whether the repo already has a planning and documentation system that should be reused instead of the default `docs/` layout.

If approval is unclear, pause and ask for confirmation before creating implementation artifacts.

Read [references/project-discovery-and-gating.md](./references/project-discovery-and-gating.md) at the start of every substantive run.

### Phase 1: Scope and Plan

1. Identify the user outcome, constraints, risks, and impacted surfaces.
2. Reuse existing epics, tickets, ADRs, PRDs, or feature folders when present.
3. Create missing planning artifacts only where the repository actually needs them.
4. Assign or reuse a traceability identifier such as `FEAT-123`, ticket ID, or ADR reference.

Read [references/planning-workflow.md](./references/planning-workflow.md) before creating or updating planning artifacts.

### Phase 2: Design and Technical Approach

1. Document how the feature fits the current architecture.
2. Capture interface changes, persistence changes, user-flow changes, and rollout concerns when relevant.
3. Reuse existing patterns, modules, dependency choices, naming rules, and UI language.

Read [references/implementation-playbook.md](./references/implementation-playbook.md) before making structural code changes.

### Phase 3: Implementation

1. Implement the smallest production-ready change set that satisfies the approved scope.
2. Avoid unrelated refactors unless required to make the feature testable or maintainable.
3. Keep docs, code, and tests in sync as the work evolves.

### Phase 4: Verification

1. Run the most relevant automated tests for the changed surfaces.
2. Check coverage when the repository already supports coverage reporting or when coverage can be added cheaply and safely.
3. Add broader integration, UI, API, or end-to-end checks when the feature changes cross-system behavior.
4. Record evidence, limitations, and unresolved risks explicitly.

Read [references/testing-verification.md](./references/testing-verification.md) before final verification.

### Phase 5: Closeout

1. Update user-facing and developer-facing documentation affected by the feature.
2. Summarize changed artifacts, validation evidence, and follow-up items.
3. Use the reporting contract in [references/reporting-contract.md](./references/reporting-contract.md) for substantive feature deliveries.

Use [references/report_template.md](./references/report_template.md) as the starter template when a report needs to be drafted quickly.

## Decision Rules

### Approval

- Proceed when the user explicitly says the feature is approved, signed off, greenlit, scheduled, or already accepted into delivery.
- If approval is ambiguous, ask once and do not fabricate approval.

### Repository conventions

- Prefer existing repo conventions over this skill's default folders.
- Use `scripts/validate-project-structure.ps1` only as a helper, not as a mandate to impose a foreign structure on every project.
- Use `scripts/scaffold-feature.ps1` only when the repo lacks a better native planning template or when the user wants lightweight documentation scaffolding.

### Coverage

- Treat `80%` as a default quality target, not a universal law.
- If the repository has an explicit standard, obey the repository standard.
- If coverage tooling is absent or prohibitively expensive to introduce mid-task, state that clearly and verify quality through the strongest available test evidence.

### Documentation depth

- Produce right-sized documentation.
- For small backend-only features, a concise technical note may be enough.
- For major UX or architecture changes, include stronger planning, diagrams, rollout notes, and user docs.

## Guardrails

- Do not implement unapproved feature ideas.
- Do not invent requirements to fill business-logic gaps; ask when the ambiguity changes behavior.
- Do not silently introduce new frameworks, state managers, test runners, or infrastructure patterns.
- Do not overwrite existing design systems, ADRs, or architecture conventions with generic replacements.
- Do not report validation you did not actually run.
- Do not claim coverage numbers you did not measure.
- Do not convert runtime notes into persistent project memory unless the repo clearly wants that artifact.

## Memory Model

Use memory deliberately and keep boundaries clean.

- Runtime memory: task-local findings, temporary assumptions, active diffs, and short-lived validation notes for the current run.
- Project or skill memory: persistent local artifacts such as feature docs, ADRs, test plans, release notes, and implementation reports stored in the repository when they provide ongoing value.
- Shared memory: cross-repository or cross-agent conventions belong outside this skill. If stable organizational knowledge needs promotion, integrate with a dedicated shared-memory skill instead of embedding it here.

Promotion rules:

- Do not persist transient exploration notes by default.
- Do not promote project-local decisions into shared memory automatically.
- Persist only information that is stable, auditable, and useful for future maintainers.

## Tooling

- Use `scripts/validate-project-structure.ps1` to inspect or optionally provision default SDLC directories in repositories that want this layout.
- Use `scripts/scaffold-feature.ps1` to scaffold planning, technical, or report starter documents when lightweight templates help.
- Use stack-specific skills for implementation and test frameworks when the repository needs deeper guidance.

## Recommended Execution Pattern

1. Inspect the repository and feature context.
2. State the current understanding, major risks, and execution plan.
3. Create or update planning artifacts only where useful.
4. Implement the feature.
5. Verify with the strongest practical evidence.
6. Close with the reporting contract.

## Inputs To Capture

Capture these when available:

- approval signal or ticket reference
- feature name and user outcome
- impacted components or bounded contexts
- relevant docs, diagrams, or issue links
- delivery constraints such as deadline, rollout guardrails, or compatibility needs
- required evidence such as tests, screenshots, migration notes, or release notes

## Output Expectations

For substantive requests, the final output should include:

- feature summary and scope
- traceability references
- artifacts created or updated
- code and design highlights
- verification evidence and coverage status
- open risks, deviations, or follow-up items

Use the reporting contract exactly when the user asks for full SDLC handling, handoff-ready output, or enterprise-style reporting.

## Failure and Escalation Cases

Pause and realign when any of these occur:

- approval is missing or contradictory
- the required behavior is materially ambiguous
- the feature requires a broad refactor outside approved scope
- the repository lacks enough context to implement safely
- validation is blocked by environment, data, credentials, or missing infrastructure

When escalating, explain the blocker, the consequence of guessing, and the smallest decision needed from the user.

## Gotchas

- **Implicit Conventions**: Many repositories have naming or structural patterns that are not explicitly documented. Always look at adjacent files before creating net-new components.
- **Dependency Chains**: A "simple" feature may trigger a cascade of changes in downstream consumers that aren't immediately obvious from local file inspection.
- **Mock Over-Reliance**: When adding tests, it is easy to over-mock dependencies. This can result in passing tests that provide a false sense of security while ignoring integrated behavior.
- **Documentation Lag**: Planning artifacts (Phase 1) can quickly become stale if implementation (Phase 3) requires a pivot. Ensure that any major technical deviations are reflected back in the "design intent" or "implementation report" to avoid misleading future maintainers.
- **Context Limits**: Large features in complex codebases can hit token limits if discovery is too broad. Prefer targeted, iterative discovery over a single massive repository scan.

## Example Triggers

- "Implement the approved notification preferences feature end to end, including docs and tests."
- "Build the greenlit SSO feature and update the architecture docs and release notes."
- "Take this approved feature from planning through production-ready code and verification."

## Resource Map

- [references/project-discovery-and-gating.md](./references/project-discovery-and-gating.md): entry gate, repo discovery, and artifact-sizing rules
- [references/planning-workflow.md](./references/planning-workflow.md): planning artifacts, acceptance criteria, and traceability
- [references/implementation-playbook.md](./references/implementation-playbook.md): design, architecture, coding, and dependency discipline
- [references/testing-verification.md](./references/testing-verification.md): verification strategy, coverage, and evidence capture
- [references/reporting-contract.md](./references/reporting-contract.md): required final report contract
- [references/report_template.md](./references/report_template.md): report starter template
- [scripts/validate-project-structure.ps1](./scripts/validate-project-structure.ps1): inspect or provision default SDLC folders
- [scripts/scaffold-feature.ps1](./scripts/scaffold-feature.ps1): scaffold a planning, technical, or report starter document
- [scripts/quick_validate.py](./scripts/quick_validate.py): validate the repository contract and eval artifacts
- [evals/evals.json](./evals/evals.json): prompt-based smoke evals for feature-delivery behavior
- [evals/trigger_queries.json](./evals/trigger_queries.json): trigger and non-trigger routing checks
