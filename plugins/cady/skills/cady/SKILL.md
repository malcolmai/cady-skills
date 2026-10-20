---
name: "cady"
description: "Reads the company's context and approvals in Cady, then loads the matching method. Use when the work is a company's sales and outreach (cold or warm email, LinkedIn messages, replies, calls, pipeline), public posts, competitors and pricing, buying or renewing tools, choosing integrations, budget and runway, fundraising, filings and hiring, product and engineering work, and setting up or scheduling company agents. Not for personal tasks or coding with no company context. Requires a Cady account."
license: "MPL-2.0"
compatibility: "Requires Cady (app.cadyworks.com/mcp)"
metadata:
  cady-id: "cady.front-door"
  version: "3beca7fa80e9067229e5f39f420401ec770c71e93d4799dd0fd7ce05ce9d0963"
  library: "3beca7fa80e90672"
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
| `finance/pricing` | plans, prices, limits, Stripe |
| `finance/plan` | the finance plan: cash, burn, runway |

## Load a library skill

Use installed skills when you have them: Codex, claude.ai and other copied installs keep `library/` and `references/` inside this skill's folder, so read `library/<name>/SKILL.md` relative to this file, then any reference it links.

Otherwise (for example the Claude Code plugin) fetch from the index at this release tag (`3beca7fa80e90672`): `https://raw.githubusercontent.com/malcolmai/cady-skills/3beca7fa80e90672/INDEX.md` lists each skill with its path; fetch `library/<name>/SKILL.md` and the references it links from the same tag.

## Updates

Updates are manual and led by your orchestrator (or you): `claude plugin update cady@cady`; re-copy the folders for Codex or re-upload the zip for claude.ai.
Recency is one field: compare `metadata.library` in any installed SKILL.md with the tag in the library index URL the Cady MCP server instructions give; if they give none, use the latest release at github.com/malcolmai/cady-skills. If they differ, the orchestrator may update; updating is optional and the installed version keeps working. Plugin auto-update is not relied on.

## Library

### core
- `cady-core-context`: deciding who decides, or what to read, before company work.
- `cady-core-execution`: a skill points here, or before an effect, credential use, retry or recovery.
- `cady-core-run-sequence`: the user wants a task carried through to a recorded outcome.
- `cady-core-scheduling`: the user wants a scheduled or repeatable task.
- `cady-core-selected-delivery`: a decided cross-functional delivery needs checks and owner readback.
- `cady-core-skill-index`: choosing which task skill fits, or binding an agent's installed skills
- `cady-orchestrator-method`: acting as the host orchestrator.

### company
- `cady-company-decision-check`: Deciding a choice's layer (owner, function head or task), or rechecking it before others build on it.
- `cady-company-decision-questions`: A goal or decision you own needs evidence: frame its key questions and pick the cheapest research route.
- `cady-company-executive-review`: The Executive frames, decides and records one founder- or executive-level decision, or reviews the allocation.
- `cady-company-experiment`: Test the riskiest assumption with a pre-registered experiment and a decision rule set before any work starts.
- `cady-company-launch`: the company is defining its initial customer, offer and smallest test.
- `cady-company-manage-agents`: Set up, schedule, review or retire a company agent: whether one is warranted, its design, binding and first task.
- `cady-company-method`: the company needs shared direction, setup or cross-functional context.
- `cady-company-operations-compliance-register`: Which statutory and registry filings the company owes and when: find, verify and record them, or review what is due.
- `cady-company-operations-method`: setting up or maintaining compliance, people processes or operating requirements.
- `cady-company-operations-people-lifecycle`: Plan, track and verify the paperwork and account access a hire, role change or leaver needs.
- `cady-company-operations-requirement-register`: Research, independently check and record one compliance requirement as a Cady Projects decision.
- `cady-company-review`: a company needs an evidence-based operating review or first setup.
- `cady-company-taste-review`: Judging or choosing between artifacts, agent designs or prompt changes where quality depends on judgment.

### gtm
- `cady-customer-success-lifecycle`: Run one customer account after the sale: onboarding to first value, health, risk, renewal, expansion or cancellation.
- `cady-customer-success-method`: a customer needs onboarding, recovery, adoption or renewal support.
- `cady-gtm-calls`: Prepare for a sales or customer call (account brief, agenda, questions), then record its follow-up and next step.
- `cady-gtm-cold-email-cycle`: Prepare a cold email cycle for parties CRM verifies as cold.
- `cady-gtm-content-production`: the user needs a post (LinkedIn, X or blog), article, script, caption or website copy.
- `cady-gtm-events`: Choose, prepare for or host an event that can advance the company purpose through real conversations.
- `cady-gtm-launch`: the company is starting a growth motion.
- `cady-gtm-linkedin-message`: Draft a LinkedIn connection note or direct message to one person, or its single follow-up.
- `cady-gtm-method`: choosing a go-to-market motion or progressing qualified commercial work.
- `cady-gtm-offer-and-segments`: Choose or revise the target segment, offer or message angle from evidence, before a cold cycle and at its review.
- `cady-gtm-pipeline-pass`: Review the pipeline: a scheduled or requested pass over due customer tracks and their next steps.
- `cady-gtm-reply`: Answer an inbound reply in a live email or LinkedIn thread: a question, interest, objection, referral, not now or stop.
- `cady-gtm-tam-map`: First-pass List of N sourced, reachable accounts for the current ICP or segment hypothesis; not the whole universe.
- `cady-gtm-warm-email`: Continue an engaged relationship, or follow up a released cold touch that got no reply.
- `cady-marketing-method`: planning content, channels, audience response or campaign learning.
- `cady-sales-deal-motion`: Work one opportunity: discovery call, light qualification, proposal, close plan, handoff to success or loss review.
- `cady-sales-method`: assessing a deal, next commitment, proposal, close or loss reason.

### finance
- `cady-accounting-method`: reconciling a period or handing exceptions to the bookkeeper.
- `cady-accounting-period-close`: Run a month, quarter or year-end close checklist in the company's own ledger and hand exceptions to its bookkeeper.
- `cady-finance-budget-review`: Draft or update a budget, spend allocation or decision forecast sized to the company's stage and obligations.
- `cady-finance-method`: reviewing runway, burn, budgets, renewals or tax preparation.
- `cady-finance-runway`: Work out burn, runway months and default alive or dead from actual cash, then decide when to cut and what first.
- `cady-finance-tax-cycle`: Plan or review an entity's tax obligations, filing preparation and material strategy changes.
- `cady-finance-vendor-spend-review`: Decide whether to buy, trial, renew or cancel a paid tool or vendor: cost, actual use, alternatives and commitment.
- `cady-fundraise-investor-list`: A financing decision calls for a sourced investor pool before contact.
- `cady-fundraise-method`: deciding whether to raise, preparing investor materials or organizing financing evidence.
- `cady-fundraise-raise-materials`: Draft or revise an investor memo, deck narrative, data room or monthly investor update for a founder.
- `cady-fundraise-raise-plan`: Decide whether, when and how much to raise, on a SAFE, note or priced round, and run the process to close.

### product
- `cady-design-method`: a product surface, marketing page, visual, deck or motion needs audience-fit design and inspection.
- `cady-design-wcag-audit`: Audit a web or app interface against WCAG 2.2 AA with real tools and report ranked, reproducible findings.
- `cady-product-customer-interview`: Plan, run and synthesise customer discovery interviews about past behaviour, without leading questions.
- `cady-product-manage`: Decide what to build, for whom and why; run discovery and hypotheses; plan each release and run its go/no-go.
- `cady-product-method`: deciding what to build, for whom, why and when to release.
- `cady-product-research-competition`: Find who the competitors and alternatives are and how they price, position and win, for a product or pricing question.
- `cady-product-research-shared`: Create or update a company-library research piece in Competition or Technology.
- `cady-product-research-technology`: Assess technologies or technical approaches for a concrete product use case.

### engineering
- `cady-engineering-debugging`: Find and fix the root cause of a bug, failing check or production incident, from reproduction to regression test.
- `cady-engineering-independent-review`: a change needs review before merge, or a lead coordinates native helpers.
- `cady-engineering-integrations`: comparing, choosing or connecting a tool, data source or account.
- `cady-engineering-method`: building, reviewing, releasing or changing a bounded technical system.
- `cady-engineering-system-cycle`: Clear a product's engineering backlog in recurring cycles from its goal map, system dimensions and state-routed motions.
- `cady-qa-method`: testing a change, investigating a failure or checking a release candidate.
- `cady-qa-triage`: Rate a bug's severity, write a reproducible report, triage a flaky test, or verify a fix before closing it.
