# Reporting Contract

Use this contract for substantive end-to-end feature work. Keep the headings stable so humans and downstream tooling can parse the report consistently.

## Required Markdown Structure

````markdown
### Feature: [Feature Title]
Technical ID: [Traceability ID or "None assigned"]

#### Scope Summary
- Requested outcome:
- Implemented scope:
- Explicit non-goals:

#### Planning and Traceability
- Approval source:
- Planning artifacts:
- Acceptance criteria or equivalent references:

#### Technical Design
- Architecture or technical docs updated:
- Diagrams updated:
- Key design decisions:

#### Implementation Highlights
- Main code changes:
- Key modules or files touched:
- Dependencies added or changed:

#### Verification
- Tests added or updated:
- Commands run:
- Coverage result:
- Manual verification:

#### Documentation and Operational Updates
- README or setup changes:
- User-facing docs:
- Release notes, changelog, or migration notes:

#### Risks and Follow-ups
- Open risks:
- Deferred work:
- Blockers or deviations:

#### Final Status
- Status:
- Ready for review:
- Ready for release:
````

## Rules

- Do not claim artifacts that were not created.
- Do not claim tests or coverage that were not run.
- Use `None`, `Not needed`, or `Blocked: ...` rather than leaving fields ambiguous.
- Keep the report concise but evidence-based.
