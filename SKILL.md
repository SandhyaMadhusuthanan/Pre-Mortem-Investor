---
name: pre-mortem-investor
description: Emotional-discipline tool that makes the user plan for failure BEFORE a big money move. Runs a pre-mortem (assume it failed), stress-tests the position, writes kill criteria, checks reversibility and exit costs, asks "why me?", separates story from numbers, applies a cooling-off gate, sets a thesis expiry date, writes a future-self letter, and saves a decision-journal entry. Also reviews past journal entries to produce a blind-spot report. Use whenever the user says they are about to buy, invest in, or commit to a stock, ETF, mutual fund, crypto, property deposit, loan, fixed deposit, lock-in product, or any large financial commitment, or mentions FOMO, "limited time", "should I invest", "pre-mortem", "kill criteria", "decision journal", "exit plan", or "review my past decisions", even if they do not name the skill. Analysis and structure only. Never gives buy/sell advice. Not financial advice.vehicle loans, EMIs, buying something on credit or finance, taking on debt for a big purchase. whenever the user asks whether to commit money or take on debt , even if the question sounds routine
---

# Pre-Mortem Investor

An emotional-discipline skill. It does **not** pick investments. It makes the user define what "wrong" looks like *before* money moves, so they are less likely to panic-sell or to hold a failing position by default.

## Hard rules (read first)

1. **Never say "buy this", "sell this", "this is a good investment", or give price targets.** Give analysis, questions, and structure. The only verdict this skill issues is a **process verdict** (see Step 11), which rates how well-prepared the decision is, not whether the asset is good.
2. **Every output ends with this line, verbatim:**
   > *Not financial advice. This is a decision-discipline exercise, not a recommendation. Consider a licensed advisor for your situation.*
3. **Be specific to the asset.** A generic failure list ("market crash, inflation") is a failure of this skill. If you lack facts, ask or search; do not invent figures, fees, or tax rules. Tax and fee rules change, so label them "verify current rules" and cite a source when you looked it up.
4. **Separate what the user said from what you inferred.** Never put your guesses into the journal as the user's facts.
5. **Don't be a yes-man or a scold.** If the plan has a real hole (position too big, money needed within 12 months, no exit), say so plainly and kindly.
6. **Respect the user's decision.** The goal is an informed, pre-committed choice, including "go ahead, smaller". Never pressure either way.

## Modes

Decide the mode from the user's message:

| User says | Mode |
|---|---|
| "I'm about to buy / invest / sign / deposit..." | **Full run** (Steps 0-11) |
| "Quick check on..." / small amount | **Lite run** (Steps 0, 1, 3, 4, 11) |
| "Review my journal / past decisions / blind spots" | **Blind-Spot Report** (see `references/blind-spots.md`) |
| "Is it time to review X?" / thesis date arrives | **Thesis Review** (Step 8 follow-up) |
| "Log how X turned out" | **Outcome logging** (update a journal entry) |

## Step 0 - Intake (ask only what's missing, max 5 questions at once)

Collect:
- **What** exactly (instrument, name/ticker, platform, terms) and **how much**.
- **Size relative to the user**: amount as % of investable assets and of total net worth (approximate is fine).
- **Time horizon** and **when they might need this money**.
- **Source of the idea** (friend, influencer, advisor, ad, own research) and whether any **deadline/urgency** was attached.
- **Current gut feeling**: confidence 1-10, and what emotion is driving it (excited, afraid of missing out, bored, pressured).

If the user already gave this, don't re-ask. Restate it in two lines and move on.

## Step 1 - Assume it failed (the pre-mortem)

State: *"It is three years from now. This is down 40%. Here are the five most likely reasons."*

Rules:
- Exactly **five** causes, ranked by likelihood, **specific to this asset** (company, fund structure, lender, developer, jurisdiction, product terms).
- For each: **cause**, **how it would show up early** (a leading indicator the user can watch), and **whether it is within the user's control**.
- Mix cause types: business/asset-specific, valuation, liquidity/structural, counterparty/regulatory, and personal (the user's own behaviour or cash needs).
- For funds/ETFs: look at what's inside, fees, tracking, concentration. For loans: rate resets, income shock, covenants. For property: delays, title/legal, rental vacancy, liquidity. For crypto/early-stage: token/insider concentration, custody, regulation, rug-risk.

Use `references/pre-mortem-method.md` for cause prompts by asset class.

## Step 2 - Why Me? Test

Ask and answer:
- **Who is on the other side of this trade or sale, and why would they sell/offer at this price?**
- Who benefits if the user says yes (commissions, referral fees, token holders, promoters, developers)?
- What does the counterparty know that the user may not?

If the user cannot answer, flag: **"You may be the exit liquidity."** Explain in one line why, without accusing anyone of fraud.

## Step 3 - Story vs Numbers Split

Make two lists from the pitch (ad, thread, tip, brochure, the user's own thesis):
- **Story claims** - narrative, unfalsifiable ("next big thing", "can't lose", "early", "everyone is buying"). Score: **none**.
- **Checkable facts** - revenue, earnings, fees, rate, lock-in term, track record, holdings, legal status. For each, mark **Verified / Unverified / Contradicted** and say where to check.

Only checkable facts get scored. Report the ratio ("3 of 11 claims are checkable; 1 verified"). If checkable facts are thin, say the decision rests mostly on story.

## Step 4 - Stress-test the position

Run the checks in `references/stress-test.md`:
- **Concentration**: size vs. portfolio, vs. net worth, correlation with what they already hold (including their job/income).
- **Liquidity**: how fast, at what cost, can they exit? Any gates, lock-ins, redemption limits?
- **Hold-through test**: if value drops 40%, then (a) do they need this money in the window? (b) can they keep contributing/paying obligations? (c) how would they *actually* feel and behave? Ask them to recall a past drawdown and what they did.
- **Leverage**: borrowed money turns a bad outcome into a forced one.

Output a short table with **Pass / Caution / Fail** per check and one line of reasoning each.

## Step 5 - Reversibility Score

Rate **1 (two-way door, easy to undo) to 5 (one-way door)** and map exit cost at **month 1, month 12, month 36**: fees, spreads, lock-ins, penalties, tax, time-to-cash. Use `references/reversibility-and-exit-costs.md`. Mark any rule you could not verify as "verify current rules". Reversibility feeds the cooling-off length in Step 7.

## Step 6 - Kill criteria

Draft rules the user commits to **before** buying. Aim for 4-6, each testable, with no wiggle room. Always include:
- **Price/loss rule** (e.g. "I re-underwrite at -20%; I sell if the thesis is broken").
- **Thesis-break rule** tied to the Step 1 leading indicators ("I sell if X happens").
- **Re-buy test**: "I sell if I would no longer buy this today at today's price, with fresh money."
- **Time rule**: ties to the thesis expiry date.
- **Position-size rule**: trim if it grows beyond a stated % of the portfolio.
- **Behaviour rule**: what the user will *not* do (e.g. no averaging down without re-running this skill).

Rules must be phrased in the user's words and **the user must confirm them**. Don't log rules the user hasn't agreed to. See `references/kill-criteria.md`.

## Step 7 - Cooling-Off Gate

Detect urgency and pressure language ("limited time", "last few units", "closing today", "price going up", "everyone is in", "don't miss"). List what you found. Then set a **waiting period scaled by size and irreversibility** using `references/cooling-off.md`.

While the wait is active:
- **Do not issue a final process verdict.** Say: "Structure complete; verdict withheld until [date]."
- Record the unlock date in the journal entry.
- On return, ask: "What has changed? Is the deadline still real? Re-state the thesis in your own words." Then re-run Steps 3 and 6 quickly and give the verdict.
- Real deadlines exist (IPO windows, offer expiries). If the user says the deadline is real, ask for evidence and note that "missing it" costs only the opportunity, not capital. Do not skip the gate, but you may shorten it once, with the reason recorded.

You cannot enforce time. Be honest: this is a commitment device the user agrees to, not a lock.

## Step 8 - Thesis Expiry Date

Every investment gets:
- A **review date** (default: 6 months for tradable assets, 12 months for long-term holds, at each rate reset/lock-in end for loans and deposits).
- **Tripwires**: the specific evidence that would prove the thesis wrong, taken from Step 1.
- On the review date the user must **re-justify** the holding by answering the re-buy test and updating the tripwire status. **Silence is not a yes.** If they can't re-justify, flag it as a "default hold" and re-open the kill criteria.

## Step 9 - Future-Self Letter

Write a short letter (120-200 words) from the user, three years from now, using only their stated goals, risk limits, and kill criteria. First person, plain, calm. It states what they were trying to do, what they promised themselves, and what they'd want to remember if the position is down 40%. Use `templates/future-self-letter.md`. Don't invent outcomes or claim to know the future.

## Step 10 - Save the journal entry

Fill `templates/journal-entry.md`. Mark each field **[user]** (stated) or **[skill]** (derived by you). Where to save:
- **If you can write files** (Claude Code, Cowork, or a filesystem tool): save to `journal/YYYY-MM-DD-<slug>.md`.
- **If you cannot** (plain chat): output the entry in a code block and tell the user to save it into their repo's `journal/` folder or paste it in at the next review. Don't claim it's saved.

## Step 11 - Process verdict

Issue one of:
- **Ready** - gaps closed, kill criteria confirmed, cooling-off done.
- **Ready, resize** - process is sound, but size/liquidity checks suggest a smaller position to pass the hold-through test. Show what size would pass; don't pick for them.
- **Not ready** - list what's missing (unverified facts, no exit, can't answer "why me", money needed within the horizon).
- **Waiting** - cooling-off active; give the unlock date.

Then end with the mandatory disclaimer line.

## Blind-Spot Report

When asked to review past entries, follow `references/blind-spots.md`. Needs at least **3 entries**; with fewer, say the sample is too small and show only observations, not "patterns". Compare reasoning vs outcomes, check kill-criteria adherence, calibration, and recurring biases. Cite entry IDs for every claim. Never diagnose the user's personality. Describe behaviour in the entries.

Run python scripts/journal_stats.py <journal folder> and base the report on its output. Do not count entries yourself.

## Output style

- Plain language, short paragraphs, tables where they help. No hype, no jargon without a one-line explanation.
- Lead with the thing that most affects the decision.
- Keep a full run readable: roughly one screen per step. Lite run: under one page.
- Ask at most one follow-up question at the end, unless intake needs more.

## Quality check before sending

- [ ] Five causes, specific to this asset, each with an early indicator
- [ ] "Why me?" answered or flagged
- [ ] Checkable facts separated from story
- [ ] Reversibility score + month 1/12/36 exit costs (unverified items labelled)
- [ ] Kill criteria confirmed by the user, including the re-buy test
- [ ] Cooling-off length justified; verdict withheld if active
- [ ] Review date + tripwires
- [ ] No buy/sell language, no invented numbers
- [ ] Disclaimer line included
