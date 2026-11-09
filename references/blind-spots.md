# Blind-Spot Report

## Preconditions
- Read every file in `journal/` (or the entries the user pastes).
- **Minimum 3 entries.** Fewer: say the sample is too small and give observations only.
- Prefer entries with logged outcomes. For entries with no outcome yet, use process data only (confidence, urgency, kill-criteria quality).

## Analysis steps

1. **Inventory**: count entries, asset types, total amounts, entries with outcomes.
2. **Calibration**: compare confidence (1-10) with outcomes. Do 9/10 confidence decisions do worse than 6/10? Report only if there are enough entries.
3. **Pre-mortem hit-rate**: which of the five predicted causes actually occurred? Was the user watching the early-warning signs?
4. **Kill-criteria adherence**: for entries where a trigger fired, did the user act per the rule? Record "followed / overrode / no trigger". Overrides are the key finding.
5. **Urgency record**: how many entries had urgency language? Did the cooling-off gate get shortened? What happened to those?
6. **Why Me? record**: any entries flagged as possible exit liquidity? Outcomes?
7. **Story-vs-numbers ratio**: do worse outcomes cluster where checkable facts were thin?
8. **Size drift**: did positions exceed the size rule?
9. **Review-date behaviour**: did the user re-justify, or hold by default?

## Bias vocabulary (use only when the entries support it)

| Pattern | Evidence to look for |
|---|---|
| Overconfidence | High confidence with weak checkable facts; poor calibration |
| FOMO | Urgency language present, gate shortened, bought after a run-up |
| Loss aversion / selling out of fear | Sold at a drawdown against a rule, or sold soon after a drop |
| Disposition effect | Sold winners early, held losers past kill criteria |
| Anchoring | "Will sell when it gets back to my buy price" |
| Confirmation bias | Pre-mortem causes were mild; contradicting facts not recorded |
| Authority / social proof | Idea source is a person or group, thesis restates their pitch |
| Sunk cost | Added money to a position that broke its thesis |

## Report format

1. **What the journal shows** (counts and facts)
2. **Top 3 recurring patterns**, each with: pattern, entry IDs as evidence, one sentence on cost or effect
3. **What you did well** (be honest, include real strengths)
4. **One rule to add** to future kill criteria or intake, based on the patterns
5. **Caveats**: sample size, outcome windows too short, luck vs skill

## Rules
- Cite entry IDs for every claim.
- Describe behaviour, not character. Say "In 3 of 4 entries you overrode the loss checkpoint", not "you are emotional".
- Don't predict the future from a small sample.
- Not financial advice, always include the disclaimer line.
