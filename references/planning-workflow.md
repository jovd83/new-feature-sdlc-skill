# Planning Workflow

Use this reference after the entry gate confirms the request is an approved feature.

## Goal

Translate the request into implementation-ready scope with enough traceability to support design, coding, testing, and closeout.

## Planning Checklist

1. Identify the user outcome and the non-goals.
2. Reuse an existing ticket, epic, ADR, or feature folder if one already exists.
3. Capture acceptance criteria or equivalent success conditions.
4. Record a traceability identifier.
5. Note dependencies, rollout constraints, and unresolved decisions.

## Artifact Sizing

- Small feature: update an existing ticket, story, or concise markdown note.
- Medium feature: create or update a feature note with scope, acceptance criteria, and risks.
- Large feature: add planning plus supporting UX, technical, or rollout artifacts.

Avoid creating ceremonial documentation when the repository already has sufficient planning context.

## Recommended Planning Fields

- title
- traceability ID
- problem or opportunity
- user outcome
- in-scope behavior
- out-of-scope behavior
- acceptance criteria
- dependencies and assumptions
- rollout or migration notes
- links to technical or UX artifacts

## Acceptance Criteria Guidance

Prefer specific, testable statements.

- Good: "When a signed-in user requests a password reset, the system emails a one-time reset link that expires after 30 minutes."
- Weak: "Support forgot password."

Use Given/When/Then when it improves clarity, but do not force it when a repository uses another standard.

## UI and UX Planning

If the feature changes the user experience:

- map the affected user flow
- list reused design-system components
- identify state changes, validation states, loading states, and error states
- add lightweight wireframes only if they add clarity

## Escalate Instead of Guessing

Pause if any of these remain unresolved:

- actor or role-specific behavior
- irreversible actions
- data retention or privacy rules
- permissions and authorization behavior
- ambiguous success or failure states

## Suggested Use Of `scaffold-feature.ps1`

Use the scaffold script when the repo lacks a better template and a quick starter would save time. Treat the generated output as a draft to refine, not a finished artifact.
