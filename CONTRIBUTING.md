# Contributing

Keep this skill lean, auditable, and easy to maintain.

## Working Principles

- preserve the skill's trigger boundary
- prefer repository-convention-first guidance over generic boilerplate
- keep orchestration concerns separate from stack-specific implementation details
- add files only when they materially improve reliability, evaluation, or maintainability

## Change Checklist

When changing the skill, update the smallest relevant set of artifacts together:

1. Update [SKILL.md](./SKILL.md) when trigger behavior, workflow, or guardrails change.
2. Update `references/` when detailed procedures or contracts change.
3. Update `scripts/` and `tests/` together when helper behavior changes.
4. Update `evals/evals.json` and `evals/trigger_queries.json` when routing or execution expectations change.
5. Run validation and tests before considering the change complete.

## Validation Commands

```powershell
python .\scripts\quick_validate.py .
Invoke-Pester .\tests
python .\scripts\eval_report.py .
python .\scripts\generate_eval_view.py .
```

## Eval Maintenance

- keep prompts realistic and multi-step
- prefer near-miss negative trigger cases over obviously unrelated ones
- update expectations when the skill contract changes
- do not let evals drift into generic "good answer" language; make them discriminating

## Script Design Rules

- prefer deterministic behavior
- make destructive behavior opt-in
- provide machine-friendly output when it materially helps automation
- keep defaults safe for use in arbitrary repositories

## Pull Request Guidance

A good contribution should explain:

- what changed
- why the current skill or scripts needed that change
- which evals or tests were added or updated
- what validation was run
