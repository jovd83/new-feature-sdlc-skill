# Implementation Playbook

Use this reference after scope is clear and before making structural changes.

## Goal

Implement the approved feature in a way that fits the repository's existing architecture, naming, dependency, and documentation conventions.

## Discovery Before Design

Inspect first:

- module boundaries
- naming conventions
- dependency patterns
- configuration layout
- error-handling style
- test locations and fixtures
- existing docs, ADRs, diagrams, and release-note patterns

Do not force generic architecture onto a codebase that already has a strong local pattern.

## Technical Design Expectations

Document the parts of the solution that future maintainers will need:

- new or changed interfaces
- data model changes
- API or event contract changes
- state transitions
- background jobs or async flows
- migrations, feature flags, or rollout constraints

If a diagram helps, keep it focused and current. A small accurate diagram is better than a sprawling outdated one.

## Coding Rules

- implement the smallest coherent change set
- preserve local conventions before applying general best practices
- prefer explicitness over cleverness
- keep comments sparse and useful
- avoid hidden side effects and unexplained magic constants
- update docs and code together when behavior changes

## Dependency Discipline

Before adding a new dependency:

1. Confirm the repository does not already have an acceptable tool.
2. Check whether the dependency is justified by the feature scope.
3. Record the reason in technical documentation or the final report.

Avoid stack churn for convenience alone.

## Change Management

- update `README.md` if setup, configuration, or user-visible behavior changes
- update changelog or release notes if the repo already uses them
- keep migrations, data backfills, or one-time scripts clearly separated from runtime logic

## Common Failure Modes

- implementing before understanding the local architecture
- introducing inconsistent naming or folder structures
- changing behavior without updating docs or tests
- making unrelated cleanup changes that complicate review

When in doubt, bias toward smaller, reviewable increments.
