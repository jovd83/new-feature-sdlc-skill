# Testing and Verification

Use this reference before final verification and closeout.

## Goal

Produce credible evidence that the implemented feature works, integrates safely, and does not regress the affected system.

## Verification Strategy

Match the validation depth to the feature:

- unit or component tests for local logic
- integration or contract tests for module boundaries
- UI, API, or end-to-end checks for cross-surface behavior
- manual verification notes only when automation is not feasible or not yet available

## Coverage Guidance

Treat `80%` as the default target only when the repository lacks a stricter or more relevant standard.

Use this decision order:

1. Repository-defined threshold or policy
2. Team-requested threshold in the task
3. Skill default target of `80%`

If coverage cannot be measured:

- say why
- do not invent a number
- compensate with stronger explicit test evidence where possible

## Required Evidence To Capture

- tests added or updated
- commands run
- pass or fail status
- coverage result when available
- blocked or skipped verification with reason

## Regression Responsibility

If the feature breaks existing relevant tests, fix the breakage or explain the blocker before declaring completion.

## Documentation Verification

Confirm whether any of these changed and need updates:

- user guides or help pages
- API documentation
- setup instructions
- environment variables
- rollout, migration, or operational notes

## Quality Red Flags

- only running one happy-path test for a multi-state feature
- reporting coverage without measuring it
- ignoring integration surfaces touched by the feature
- treating flaky or failing legacy tests as someone else's problem

## Good Final Verification Statement

"Added service-level tests for token expiry and reset-link replay, ran the auth test suite, and verified frontend password-reset flow coverage through the existing UI runner. Coverage is reported for the modified auth service files; UI coverage is not configured in this repository."
