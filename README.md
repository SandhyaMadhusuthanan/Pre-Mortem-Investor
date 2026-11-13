# Pre-Mortem Investor
![Pre-Mortem Investor demo](Assets/pre-mortem-demo.gif)

An agent skill that makes you **plan for failure before you invest or make a big money move**.

Tell the agent what you're about to buy: a stock, fund, property deposit, fixed deposit or loan. It assumes the move failed, stress-tests your position, writes exit rules you commit to in advance, and saves a decision-journal entry. Later it reviews your past entries and shows your recurring blind spots.

It is an **emotional-discipline tool, not a stock-picking tool**. It never tells you what to buy or sell.

> **Not financial advice.** This project provides analysis and structure for your own decision-making. It is not a recommendation to buy, sell or hold anything. Consider a licensed advisor for your situation.

## What this is (and isn't)
This is an educational thinking tool. It helps you question your own
decisions. It does not give personalised investment advice and is not
a SEBI-registered adviser. The author is not a lawyer. Before promoting
this widely or charging for it, check SEBI's current rules on
investment advice.

## Why

Most people lose money by panic-selling, or by never defining what "wrong" looks like. A pre-mortem plus pre-committed kill criteria moves the hard thinking to before the money is in, when you're calm.

## What it does

**Core four steps**

1. **Assume it failed.** It's three years later and the position is down 40%. It lists the five most likely causes, specific to *that* asset, with early-warning signs.
2. **Stress-test your position.** Concentration, liquidity, leverage, and whether you could really hold through a crash.
3. **Write kill criteria.** Exit rules you commit to before buying, such as "I sell if X happens, or if I'd no longer buy at today's price."
4. **Save a decision-journal entry.** Review past entries later to see where your reasoning and the outcomes diverged.

**Seven extras**

| Feature | What it does |
|---|---|
| Reversibility Score | Rates the move from two-way door (1) to one-way door (5) and maps exit costs at month 1, 12 and 36 |
| "Why Me?" Test | Asks who's selling to you and why, and flags if you may be the exit liquidity |
| Story vs Numbers Split | Separates narrative claims from checkable facts, and only scores the checkable ones |
| Cooling-Off Gate | Detects urgency language and imposes a wait scaled to size and irreversibility; withholds the verdict until it ends |
| Thesis Expiry Date | Review date plus tripwires; at the date you must re-justify the holding |
| Blind-Spot Report | Reads your journal and shows recurring biases, citing the entries |
| Future-Self Letter | A short note from you in 3 years, built from your own goals and limits |

## Repo layout

```
pre-mortem-investor/
├── SKILL.md                       # The skill: workflow and rules
├── README.md
├── LICENSE
├── .gitignore
├── references/
│   ├── pre-mortem-method.md       # Failure-cause prompts by asset class
│   ├── stress-test.md
│   ├── reversibility-and-exit-costs.md
│   ├── kill-criteria.md
│   ├── cooling-off.md
│   └── blind-spots.md
├── templates/
│   ├── journal-entry.md
│   └── future-self-letter.md
├── examples/
│   └── example-session.md
└── journal/                       # Your saved entries go here
```

## Install

**Claude Code / Cowork (filesystem skills):** copy or clone this folder into your skills directory, e.g.

```bash
git clone https://github.com/SandhyaMadhusuthanan/pre-mortem-investor.git ~/.claude/skills/pre-mortem-investor
```

**Claude.ai:** zip the folder so `SKILL.md` is inside a `pre-mortem-investor/` folder, then upload it under Settings, Skills (availability depends on your plan).

**Other agents:** paste `SKILL.md` into the system prompt or project instructions, and give the agent access to the `references/` and `templates/` files.

## Use

Just describe the move:

- "I'm about to put ₹2 lakh into a small-cap fund. Run a pre-mortem."
- "A broker says this flat's booking price is only valid till Friday. Help me think it through."
- "Review my journal and show my blind spots."
- "Log how my XYZ entry turned out."

## Saving the journal

With file access, the skill writes `journal/YYYY-MM-DD-slug.md`. In plain chat it prints the entry for you to save yourself. Journal entries contain personal financial details, so **keep the repo private** or uncomment the ignore lines in `.gitignore`.

## Limits

- It can't enforce the cooling-off period. It's a commitment device you agree to.
- It doesn't know live prices or your full finances. It only uses what you tell it, plus anything it can look up.
- Tax and fee rules vary and change. Anything unverified is labelled "verify current rules".
- Blind-spot patterns need at least 3 entries and are only as good as the data you log.

## Contributing

PRs welcome: more asset-class prompts, jurisdiction-specific exit-cost notes (with sources), and example sessions. Keep the no-advice rule intact.

## License

MIT. See `LICENSE`.
