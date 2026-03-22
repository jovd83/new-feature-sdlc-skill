# Project Discovery and Gating

Read this first for any non-trivial feature request.

## Purpose

Decide whether this skill should run, how much SDLC structure is warranted, and which repository conventions must be reused.

## Entry Questions

Answer these before creating artifacts or editing code:

1. Is this an approved feature request?
2. Is the work materially more than a bug fix, isolated refactor, or test-only change?
3. What repository conventions already exist for planning, architecture docs, tests, and release notes?
4. What parts of the system are affected?
5. What evidence will count as "done"?

## Repository Discovery Checklist

- inspect top-level directories
- inspect existing documentation structure
- inspect package, module, or service boundaries
- inspect test layout and tooling
- inspect release-note or changelog conventions
- inspect issue or ticket references already present in the repo

## Default Folder Layout

Some repositories will want the lightweight default layout used by the helper scripts:

- `docs/functional analysis/`
- `docs/wireframes/`
- `docs/technical/`
- `docs/diagrams/`
- `docs/reports/`
- `frontend-tests/`

Use it only when the repository lacks stronger native conventions.

## Sizing Guidance

- tiny feature: likely no new diagrams and minimal planning notes
- standard feature: concise planning plus targeted technical notes and tests
- complex feature: planning, technical design, cross-surface verification, and closeout evidence

## When To Escalate

Escalate before implementation when:

- approval is missing
- the feature materially changes architecture or platform choices
- the request spans multiple bounded contexts with unclear ownership
- the repository is missing the context needed for safe implementation

## Output Of This Phase

At the end of discovery, be ready to state:

- whether the skill applies
- what scope is approved
- which artifacts need to be created or updated
- what "done" means for this repository
