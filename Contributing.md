# Contributing

Thanks for helping improve Pre-Mortem Investor.

## Suggest a change
1. Open an Issue first and describe what you would like to change and why.
2. Wait for a reply before sending a pull request, so we agree on the direction.

## Add an example
- Put new example sessions in `examples/` and new journal entries in `examples/sample-journal/`.
- Journal entries must follow the same format as the existing ones (the fields at the top of each file), because `scripts/journal_stats.py` reads them.
- Use fictional names and amounts only. Never include real personal or financial details.

## Report a trigger problem
If the skill starts when it should not, or does not start when it should, add the exact prompt to `evals/trigger-prompts.md` and mention it in your Issue.

## India-specific rules
Any rule, rate or limit added to `references/india-notes.md` must include:
- a link to an official source (RBI, SEBI, Income Tax Department, India Post or NSI, a RERA authority, or a bank or fund document),
- the date you last checked it, and
- the words "Verify current rules."

Please do not copy rules from memory or blogs.
