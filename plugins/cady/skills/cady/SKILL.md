---
name: "cady"
description: "Reads the company's context and approvals in Cady, then loads the matching method. Use when the work is a company's sales and outreach (cold or warm email, LinkedIn messages, replies, calls, pipeline), public posts, competitors and pricing, buying or renewing tools, choosing integrations, budget and runway, fundraising, filings and hiring, product and engineering work, and setting up or scheduling company agents. Not for personal tasks or coding with no company context. Requires a Cady account."
license: "MPL-2.0"
compatibility: "Requires Cady (app.cadyworks.com/mcp)"
metadata:
  cady-id: "cady.front-door"
  version: "62ae69a6f667e4c1e515fd147c4136b60e991a15b959b79b92773d5f5f653282"
  library: "62ae69a6f667e4c1"
  function: "core"
---
# Cady

Reads the company's context and approvals in Cady, then loads the matching method. Use when the work is a company's sales and outreach (cold or warm email, LinkedIn messages, replies, calls, pipeline), public posts, competitors and pricing, buying or renewing tools, choosing integrations, budget and runway, fundraising, filings and hiring, product and engineering work, and setting up or scheduling company agents. Not for personal tasks or coding with no company context.

## Connect

Connecting opens Cady in your browser; create an account there (email code or passkey) if you don't have one.
In Claude Code the first Cady call, or `/mcp`, starts sign-in; in Codex run `codex mcp login cady`.

## Start every run

    get_cady_context({"area": "<area>", "task": "<what you are about to do, in one sentence>"})

Add "agentId" when you run as a registered Cady agent, "workId" to resume a work item, and
"knownMethods" {cady-id: version} (up to 8) for the library skills you hold, so Cady returns company
content without re-sending their text. Product areas take the id from get_company_product in place of <productId>.
Then follow cady-core-run-sequence.

| Area | For |
|---|---|
| `gtm/strategy` | ICP, offer, segments, positioning, targets |
| `gtm/prospecting` | lists, enrichment, CRM records |
| `gtm/outreach` | cold and warm mail, follow-ups, replies |
| `gtm/content` | public posts, assets, website copy |
| `product/<productId>/scope` | roadmap, features, product bar |
| `product/<productId>/ui` | pages, layout, components, UI copy |
| `product/<productId>/context` | how context and records are written, served and cleaned up |
| `product/<productId>/engineering` | infrastructure, data model, MCP interface, code |
| `product/<productId>/release` | merge, gates, staging and production |
| `ops/agents` | create, schedule, approve and retire agents; what they may do |
| `ops/legal` | filings, registers, compliance, tax |
| `ops/records` | recording and consolidating decisions, files and work |
| `ops/inbox` | mail triage, commitments, follow-ups and what to record |
| `finance/pricing` | plans, prices, limits, Stripe |
| `finance/plan` | the finance plan: cash, burn, runway |

## Load a library skill

Before drafting or recommending, choose the matching skill below and read `library/<name>/SKILL.md` relative to this skill's base directory, then the references it needs. Try that local path on every host, including Claude Code; the host name does not tell you whether the library is installed.

Only if that local file is unavailable, fetch from the library source below: `INDEX.md` lists each skill with its path. Fetch the skill and its linked references from that same source. If neither local reading nor fetching is available, say the method is unavailable.

    Library source: https://raw.githubusercontent.com/malcolmai/cady-skills/62ae69a6f667e4c1/

That line is the upstream baseline at this release tag. A company's fork changes it to the fork's own raw URL and branch, so its edited skills are the ones that load.

## Your fork

This library is a best-practice baseline. Each company forks it into its own git repository or a local copy, and its orchestrator edits that fork with the company's own reasoning; Cady stores no skills. Nothing updates a fork automatically: once a month the orchestrator compares the fork's baseline tag (`metadata.library`) with the latest upstream release, reads that release's CHANGELOG.md, merges what helps by hand and records the decision. The README at github.com/malcolmai/cady-skills has the steps.

## Library

### core
- `cady-core-context`: deciding who decides, or what to read, before company work.
- `cady-core-execution`: a skill points here, or before an effect, credential use, retry or recovery.
- `cady-core-run-sequence`: the user wants a task carried through to a recorded outcome.
- `cady-core-scheduling`: the user wants a scheduled or repeatable task.
- `cady-core-skill-index`: choosing which task skill fits, or binding an agent's installed skills
- `cady-orchestrator-method`: Orchestrator role card: what this function owns and decides

### company
- `cady-company-decision-check`: Deciding a choice's layer (owner, function head or task), or rechecking it before others build on it.
- `cady-company-decision-questions`: A goal or decision you own needs evidence: frame its key questions and pick the cheapest research route.
- `cady-company-executive-review`: Make one big company decision (market, direction, pricing, a bet to start or stop) or review where effort goes.
- `cady-company-experiment`: Test the riskiest assumption with a pre-registered experiment and a decision rule set before any work starts.
- `cady-company-manage-agents`: Set up, schedule, review or retire a company agent: whether one is warranted, its design, binding and first task.
- `cady-company-method`: Company role card: what this function owns and decides
- `cady-company-operations-compliance-register`: What statutory and registry filings the company owes and when (annual returns, confirmation statements, state reports).
- `cady-company-operations-inbox-follow-through`: Bounded inbox maintenance or thread triage for follow-through, marketing handling or commitments needing tracking.
- `cady-company-operations-method`: Company Operations role card: what this function owns and decides
- `cady-company-operations-people-lifecycle`: Plan, track and verify the paperwork and account access for a new hire, a role change or someone leaving.
- `cady-company-operations-requirement-register`: Research, independently check and record one compliance requirement as a Cady Projects decision.
- `cady-company-review`: a company needs an evidence-based operating review or first setup.
- `cady-company-taste-review`: Write, edit or judge a public post (LinkedIn, X, blog), article, script or web copy, or critique a design or prompt.

### gtm
- `cady-customer-success-lifecycle`: Run one customer account after the sale: onboarding to first value, health, risk, renewal, expansion or cancellation.
- `cady-customer-success-method`: Customer Success role card: what this function owns and decides
- `cady-gtm-calls`: Prepare for a sales or customer call (account brief, agenda, questions), then record its follow-up and next step.
- `cady-gtm-cold-email-cycle`: Write and send cold email to people not yet contacted, one template per segment; fix bounces, spam or deliverability.
- `cady-gtm-events`: Choose, prepare for or host an event that can advance the company purpose through real conversations.
- `cady-gtm-launch`: the company is starting a growth motion.
- `cady-gtm-linkedin-message`: Draft a LinkedIn connection note or direct message to one person, or its one follow-up; pacing and invitation limits.
- `cady-gtm-method`: GTM role card: what this function owns and decides
- `cady-gtm-offer-and-segments`: Choose or revise the target segment, offer or message angle from evidence, before a cold cycle and at its review.
- `cady-gtm-pipeline-pass`: Review the pipeline: a scheduled or requested pass over due customer tracks and their next steps.
- `cady-gtm-reply`: Answer an inbound reply in a live email, LinkedIn or host-connected message thread: a question, interest, objection, referral, not now or stop.
- `cady-gtm-tam-map`: Build a list of target companies or accounts to sell to (for a region, segment or ICP), sourced and reachable.
- `cady-gtm-warm-email`: Write a follow-up email (to a non-replier or an engaged contact) or the next note in an engaged relationship.
- `cady-marketing-method`: Marketing role card: what this function owns and decides
- `cady-sales-deal-motion`: Work one opportunity: discovery call, light qualification, proposal, close plan, handoff to success or loss review.
- `cady-sales-method`: Sales role card: what this function owns and decides

### finance
- `cady-accounting-method`: Accounting role card: what this function owns and decides
- `cady-accounting-period-close`: Close the books for a month, quarter or year: reconcile bank, payouts and revenue, and list fixes for the bookkeeper.
- `cady-finance-budget-review`: Draft or update a budget, spend allocation or decision forecast sized to the company's stage and obligations.
- `cady-finance-method`: Finance role card: what this function owns and decides
- `cady-finance-runway`: Work out burn, runway months and default alive or dead from actual cash, then decide when to cut and what first.
- `cady-finance-tax-cycle`: Plan or review an entity's tax obligations, filing preparation and material strategy changes.
- `cady-finance-vendor-spend-review`: Decide whether to buy, trial, renew or cancel a paid tool or vendor: cost, actual use, alternatives and commitment.
- `cady-fundraise-investor-list`: Decide who to pitch for a round: a ranked list of named investors and partners, sourced, with warm paths.
- `cady-fundraise-investor-outreach`: Write to investors: a warm intro request, a personalised first note, round follow-ups, or the monthly update send.
- `cady-fundraise-method`: Fundraise role card: what this function owns and decides
- `cady-fundraise-raise-materials`: Draft or revise an investor memo, deck narrative, data room or monthly investor update for a founder.
- `cady-fundraise-raise-plan`: Decide whether, when and how much to raise (SAFE, note or priced round), model dilution and run the round.

### product
- `cady-design-method`: Design role card: what this function owns and decides
- `cady-design-wcag-audit`: Audit a web or app interface against WCAG 2.2 AA with real tools and report ranked, reproducible findings.
- `cady-product-customer-interview`: Plan, run and synthesise customer discovery interviews about past behaviour, without leading questions.
- `cady-product-manage`: Decide what to build, for whom and why; run discovery and hypotheses; plan each release and run its go/no-go.
- `cady-product-method`: Product role card: what this function owns and decides
- `cady-product-research-competition`: Find who the competitors and alternatives are and how they price, position and win, for a product or pricing question.
- `cady-product-research-shared`: Create or update a company-library research piece in Competition or Technology.
- `cady-product-research-technology`: Assess technologies or technical approaches for a concrete product use case.

### engineering
- `cady-engineering-debugging`: Find and fix the root cause of a bug, failing check or production incident, then the regression test and postmortem.
- `cady-engineering-independent-review`: a change needs review before merge, or a lead coordinates native helpers.
- `cady-engineering-integrations`: comparing, choosing or connecting a tool, data source or account.
- `cady-engineering-method`: Engineering role card: what this function owns and decides
- `cady-engineering-system-cycle`: Clear a product's engineering backlog in recurring cycles from its goal map, system dimensions and state-routed motions.
- `cady-qa-method`: QA role card: what this function owns and decides
- `cady-qa-stories`: Edit or retire a user story, walk one blind as a fresh user, read story status, or file a finding on a step.
- `cady-qa-triage`: Rate a bug's severity, write a reproducible report, triage a flaky test, or verify a fix before closing it.
