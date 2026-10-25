# Model registry

## Models

- **As of:** 2026-10-07
- **Boundary:** Reference data, never a default: the host owns model selection and effort (scheduled_model_selection.host_mapping); prices and tiers are dated and sourced, an unmeasured view never sets a value-for-money rating, which needs measured quality, a row whose current price is unverified says so, and nothing here grants budget.

### Models

- **Model:** Claude Fable 5.1

#### Plans

- **Api:** available
- **Claude pro, max, team, enterprise:** available

#### Price

- **Basis:** USD per 1M tokens, input/output
- **Input:** 10
- **Output:** 50

#### Price source

- **Checked:** 2026-10-07
- **Url:** https://platform.claude.com/docs/en/about-claude/pricing
- **Price status:** verified
- **Provider:** Anthropic

#### Rating

- **Basis:** not measured
- **Date:** 2026-10-07
- **Value for money:** unrated

#### Sources

| Checked | Url |
|---|---|
| 2026-10-07 | https://platform.claude.com/docs/en/about-claude/pricing |
| 2026-09-26 | https://www.anthropic.com/claude-fable-and-mythos-5-1 |

- **Status:** current
- **Tier:** review
- **Use cases:** key plans and independent reviews; most demanding coding and dense documents
- **Model:** GPT-6 Astra

#### Plans

- **Api:** available
- **Chat gpt and codex:** unverified

#### Price

- **Basis:** USD per 1M tokens, input/output
- **Input:** 10
- **Output:** 50

#### Price source

- **Checked:** 2026-09-26
- **Url:** https://developers.openai.com/api/docs/models/gpt-6-astra
- **Price status:** verified
- **Provider:** OpenAI

#### Rating

- **Basis:** not measured
- **Date:** 2026-10-07
- **Value for money:** unrated

#### Sources

| Checked | Url |
|---|---|
| 2026-09-26 | https://developers.openai.com/api/docs/models/gpt-6-astra |

- **Status:** current
- **Tier:** review
- **Use cases:** key plans and independent reviews; deep analysis and research
- **Api id:** claude-opus-5-5
- **Model:** Claude Opus 5.5

#### Plans

- **Api:** available
- **Claude pro, max, team, enterprise:** available

#### Price

- **Basis:** USD per 1M tokens, input/output
- **Input:** 4
- **Note:** fast mode 8/40
- **Output:** 20

#### Price source

- **Checked:** 2026-10-07
- **Url:** https://platform.claude.com/docs/en/about-claude/pricing
- **Price status:** verified
- **Provider:** Anthropic

#### Rating

- **Basis:** not measured
- **Date:** 2026-10-07
- **Value for money:** unrated

#### Sources

| Checked | Url |
|---|---|
| 2026-10-07 | https://platform.claude.com/docs/en/about-claude/pricing |

- **Status:** current
- **Tier:** lead
- **Use cases:** leads: run helpers, design, integrate and judge
- **Api id:** gpt-6.1-sol
- **Model:** GPT-6.1 Sol

#### Plans

- **Api:** available
- **Chat gpt and codex:** operator_reported

#### Price

- **Basis:** USD per 1M tokens, input/output
- **Input:** 2
- **Output:** 10

#### Price source

- **Checked:** 2026-10-07
- **Url:** https://developers.openai.com/api/docs/models/gpt-6.1-sol
- **Price status:** verified
- **Provider:** OpenAI

#### Rating

- **Basis:** not measured
- **Date:** 2026-10-07
- **Value for money:** unrated

#### Sources

| Checked | Url |
|---|---|
| 2026-10-07 | https://developers.openai.com/api/docs/models/gpt-6.1-sol |

- **Status:** current
- **Tier:** lead
- **Use cases:** leads in Codex and ChatGPT; also the vision pick on OpenAI plans

#### Vision

- **Input:** text, image
- **Model:** Claude Sonnet 5.5

#### Plans

- **Api:** available
- **Claude pro, max, team, enterprise:** available

#### Price

- **Basis:** USD per 1M tokens, input/output
- **Input:** 2
- **Output:** 10

#### Price source

- **Checked:** 2026-10-07
- **Url:** https://platform.claude.com/docs/en/about-claude/pricing
- **Price status:** verified
- **Provider:** Anthropic

#### Rating

- **Basis:** not measured
- **Date:** 2026-10-07
- **Value for money:** unrated

#### Sources

| Checked | Url |
|---|---|
| 2026-10-07 | https://platform.claude.com/docs/en/about-claude/pricing |
| 2026-10-07 | https://platform.claude.com/docs/en/about-claude/models/overview |

- **Status:** current
- **Tier:** workhorse
- **Use cases:** writing and retrieval at volume; also the vision pick on Claude plans

#### Vision

- **Input:** text, image
- **Api id:** claude-sonnet-5
- **Model:** Claude Sonnet 5

#### Plans

- **Api:** available
- **Claude pro, max, team, enterprise:** available

#### Price

- **Basis:** USD per 1M tokens, input/output
- **Input:** 2
- **Note:** 1M context
- **Output:** 10

#### Price source

- **Checked:** 2026-10-07
- **Url:** https://platform.claude.com/docs/en/about-claude/pricing
- **Price status:** verified
- **Provider:** Anthropic

#### Rating

- **Basis:** not measured
- **Date:** 2026-10-07
- **Value for money:** unrated

#### Sources

| Checked | Url |
|---|---|
| 2026-10-07 | https://platform.claude.com/docs/en/about-claude/pricing |
| 2026-09-26 | https://www.anthropic.com/news/claude-sonnet-5 |

- **Status:** old
- **Tier:** workhorse
- **Use cases:** superseded by Claude Sonnet 5.5 at the same price; use it only where 5.5 is unavailable
- **Model:** Terra

#### Plans

- **Api:** available
- **Work and codex:** unavailable

#### Price

- **Basis:** USD per 1M tokens, input/output; last verified list price, current price unverified
- **Input:** 2.5
- **Note:** Unverified: GPT-5.6 list price before a reported 20% cut; current price unverified
- **Output:** 15.0
- **Price of:** GPT-5.6 Terra list price before a reported 20% cut
- **Price status:** unverified
- **Provider:** OpenAI

#### Rating

- **Basis:** price unverified
- **Date:** 2026-10-07
- **Value for money:** unrated

#### Sources

| Checked | Url |
|---|---|
| 2026-09-26 | https://openai.com/index/gpt-5-6 |
| 2026-10-13 | local: codex exec -m gpt-6-terra refused with a ChatGPT-account login ('not supported when using Codex with a ChatGPT account') |

- **Status:** current
- **Tier:** workhorse
- **Use cases:** mid-cost writing and retrieval with an API key login
- **Model:** Luna

#### Plans

- **Api:** available
- **Work and codex:** available

#### Price

- **Basis:** USD per 1M tokens, input/output; last verified list price, current price unverified
- **Input:** 1.0
- **Note:** Unverified: GPT-5.6 list price before a reported 80% cut; current price unverified
- **Output:** 6.0
- **Price of:** GPT-5.6 Luna list price before a reported 80% cut
- **Price status:** unverified
- **Provider:** OpenAI

#### Rating

- **Basis:** price unverified
- **Date:** 2026-10-07
- **Value for money:** unrated

#### Sources

| Checked | Url |
|---|---|
| 2026-09-26 | https://openai.com/index/gpt-5-6 |

- **Status:** current
- **Tier:** workhorse
- **Use cases:** cheap writing, bounded edits, triage and probes
- **Api id:** deepseek-v4.1-flash
- **Model:** DeepSeek V4.1 Flash

#### Plans

- **Api:** available

#### Price

- **Basis:** USD per 1M tokens, input/output
- **Input:** 0.15
- **Note:** off-peak; peak hours double
- **Output:** 0.6

#### Price source

- **Checked:** 2026-09-26
- **Url:** https://api-docs.deepseek.com/quick_start/pricing/
- **Price status:** verified
- **Provider:** DeepSeek

#### Rating

- **Basis:** not measured
- **Date:** 2026-10-07
- **Value for money:** unrated

#### Sources

| Checked | Url |
|---|---|
| 2026-09-26 | https://api-docs.deepseek.com/quick_start/pricing/ |

- **Status:** current
- **Tier:** workhorse
- **Use cases:** cheap coding writer: mechanical edits, bulk deletions, test fixes
- **Refresh:** The orchestrator re-checks this registry every 7 days, sooner when a new model ships. Find new releases on https://aireleasetracker.com/, read general early feedback to judge whether a new model is good, and weight our own measured experience on real tasks above both. Drop a model from the registry once a newer one covers its work; do not keep exclusion lists. Past stale_after_days the registry is served with stale: true; treat its prices and picks as possibly out of date, never as a refusal.
- **Refresh every days:** 7
- **Refresh owner:** orchestrator
- **Selection criterion:** Prefer the model with good value for money for the job and avoid low value-for-money models, judged on verified prices and measured quality; an unverified price or an unmeasured view alone never sets a rating.
- **Stale after days:** 14

### Tiers

#### Lead

#### Picks

| Model | Plan |
|---|---|
| Claude Opus 5.5 | Claude |
| GPT-6.1 Sol | OpenAI |

- **Use:** Runs helpers, designs, integrates and judges; never writes bulk code.

#### Review

#### Picks

| Model | Plan |
|---|---|
| Claude Opus 5.5 | Claude |
| GPT-6 Astra | OpenAI |

- **Use:** Key plans and independent reviews only. Give it fresh, unbiased context; it may challenge or redesign. A premium review model only when the company's owner directs it; which one, and when, is a company decision recorded in its context.

#### Vision

- **Note:** each pick's image input is sourced on its row. Re-checked at the weekly check.

#### Picks

| Model | Plan |
|---|---|
| Claude Sonnet 5.5 | Claude |
| GPT-6.1 Sol | OpenAI |

- **Use:** QA: finds visual, copy and journey issues from screenshots and captures. Strong at vision, not the most expensive.

#### Workhorse

#### Picks

| Model | Plan |
|---|---|
| Claude Sonnet 5.5 | Claude |
| Luna | OpenAI |
| Terra | API |
| DeepSeek V4.1 Flash | API |

- **Use:** Writes and retrieves: workstreams, bounded edits, triage, test fixes, bulk mechanical changes.
