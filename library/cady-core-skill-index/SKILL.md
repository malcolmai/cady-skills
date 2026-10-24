---
name: "cady-core-skill-index"
description: "Skill index: every Cady task skill with one line on when to use it. Use when: choosing which task skill fits, or binding an agent's installed skills. Not for: doing the task itself."
license: "MPL-2.0"
compatibility: "Requires Cady (app.cadyworks.com/mcp)"
metadata:
  cady-id: "cady.skill_index"
  version: "9bb8b89f620f706e02597b634fe3d2d3f3a0b21f91eaae29568a35d6ae4e001c"
  library: "c4b98ee2d7bd8432"
  function: "core"
---
# Skill index

**Company context:** `get_cady_context({"area": "ops/agents", "task": "<what you are about to do, in one sentence>", "knownMethods": {"cady.skill_index": "9bb8b89f620f706e02597b634fe3d2d3f3a0b21f91eaae29568a35d6ae4e001c"}})`

Every Cady task skill, with one line on when to use it.

## company

- `cady-company-decision-check`: Before a choice or an effect: whether it is already decided, who decides, and how to record it.
- `cady-company-decision-questions`: A goal or decision you own needs evidence: frame its key questions and pick the cheapest research route.
- `cady-company-executive-review`: Make one company-level decision (a goal to start, reshape or stop, market, pricing, a bet) or review the open goals.
- `cady-company-experiment`: Test the riskiest assumption with a pre-registered experiment and a decision rule set before any work starts.
- `cady-company-manage-agents`: Create and bind, schedule, review or retire a company agent: whether one is warranted, its design, binding and first task.
- `cady-company-taste-review`: Write, edit or judge a public post (LinkedIn, X, blog), article, script or web copy, or critique a design or prompt.
- `cady-company-voice-pack`: A member has no voice pack, drafts read like the AI, or the pack is 90 days old or the sender rewrote 5 or more drafts since its last revision.
- `cady-company-operations-compliance-register`: What statutory and registry filings the company owes and when (annual returns, confirmation statements, state reports).
- `cady-company-operations-contract-checks`: A contract that commits the company is about to be signed or was just signed: what to settle first and what it starts.
- `cady-company-operations-inbox-follow-through`: Bounded inbox maintenance or thread triage for follow-through, marketing handling or commitments needing tracking.
- `cady-company-operations-people-lifecycle`: Plan, track and verify the paperwork and access for a new hire or contractor, a role change or someone leaving.
- `cady-company-operations-requirement-register`: Research, independently check and record one compliance requirement as a Cady Projects decision.

## gtm

- `cady-customer-success-lifecycle`: Run one customer account after the sale: onboarding to first value, health, risk, renewal, expansion or cancellation.
- `cady-gtm-calls`: Prepare for a sales or customer call (account brief, agenda, questions), then record its follow-up and next step.
- `cady-gtm-cold-email-cycle`: Write and send cold email to people not yet contacted, one template per segment; fix bounces, spam or deliverability.
- `cady-gtm-events`: Choose, prepare for or host an event that can advance the company purpose through real conversations.
- `cady-gtm-linkedin-message`: Draft a LinkedIn connection note or direct message to one person, or its one follow-up; pacing and invitation limits.
- `cady-gtm-offer-and-segments`: Choose or revise the target segment, offer or message angle from evidence, before a cold cycle and at its review.
- `cady-gtm-pipeline-pass`: Review the pipeline: a scheduled or requested pass over due customer tracks and their next steps.
- `cady-gtm-reply`: Answer an inbound reply in a live email, LinkedIn or host-connected message thread: a question, interest, objection, referral, not now or stop.
- `cady-gtm-tam-map`: Build a list of target companies or accounts to sell to (for a region, segment or ICP), sourced and reachable.
- `cady-gtm-warm-email`: Write a follow-up email (to a non-replier or an engaged contact) or the next note in an engaged relationship.
- `cady-sales-deal-motion`: Work one opportunity: discovery call, light qualification, proposal, close plan, handoff to success or loss review.

## finance

- `cady-accounting-period-close`: Close the books for a month, quarter or year: reconcile bank, payouts and revenue, and list fixes for the bookkeeper.
- `cady-finance-budget-review`: Draft or update a budget or spend allocation, or review last month's spend against it.
- `cady-finance-runway`: Work out burn, runway months and default alive or dead from actual cash, then decide when to cut and what first.
- `cady-finance-tax-cycle`: Plan or review an entity's tax obligations, filing preparation and material strategy changes.
- `cady-finance-vendor-spend-review`: Decide whether to buy, trial, renew or cancel a paid tool or vendor: cost, actual use, alternatives and commitment.
- `cady-fundraise-investor-list`: Decide who to pitch for a round: a ranked list of named investors and partners, sourced, with warm paths.
- `cady-fundraise-investor-outreach`: Write to investors: a warm intro request, a personalised first note, round follow-ups, or the monthly update send.
- `cady-fundraise-raise-materials`: Draft or revise an investor memo, deck narrative, data room or monthly investor update for a founder.
- `cady-fundraise-raise-plan`: Decide whether, when and how much to raise (SAFE, note or priced round), model dilution and run the round.

## product

- `cady-design-wcag-audit`: Audit a web or app interface against WCAG 2.2 AA with real tools and report ranked, reproducible findings.
- `cady-product-customer-interview`: Plan, run and synthesise customer discovery interviews about past behaviour, without leading questions.
- `cady-product-manage`: Decide what to build, for whom and why; run discovery and hypotheses; plan each release and run its go/no-go.
- `cady-product-research-competition`: Find who the competitors and alternatives are and how they price, position and win, for a product or pricing question.
- `cady-product-research-shared`: Create or update a company-library research piece in Competition or Technology.
- `cady-product-research-technology`: Assess technologies or technical approaches for a concrete product use case.

## engineering

- `cady-engineering-debugging`: Find and fix the root cause of a bug, failing check or production incident, then the regression test and postmortem.
- `cady-engineering-system-cycle`: Clear a product's engineering backlog in recurring cycles from its goal map, system dimensions and state-routed motions.
- `cady-qa-stories`: Edit or retire a user story, walk one blind as a fresh user, read story status, or file a finding on a step.
- `cady-qa-triage`: Rate a bug's severity, write a reproducible report, triage a flaky test, or verify a fix before closing it.
