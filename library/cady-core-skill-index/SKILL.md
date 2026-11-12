---
name: "cady-core-skill-index"
description: "Skill index: every Cady task skill with one line on when to use it. Use when: choosing which task skill fits, or binding an agent's installed skills. Not for: doing the task itself."
license: "MPL-2.0"
compatibility: "Requires Cady (app.cadyworks.com/mcp)"
metadata:
  cady-id: "cady.skill_index"
  version: "390c7396e6ad9d9d5d05"
  library: "82f67ca6a975c29f"
  function: "core"
---
# Skill index

**Company context:** `cady_read {"search": {"query": "<what you are about to do, in one sentence>"}}`

Every Cady task skill, with one line on when to use it.

## company

- `cady-company-challenge`: Reading a result one level down before accepting it, as the orchestrator or a family orchestrator.
- `cady-company-change-agent-behaviour`: Change what agents do: edit a skill, role card, run sequence, tool text or an agent's goal.
- `cady-company-decision-check`: Before a choice or an effect: whether it is already decided, who decides, and how to record it.
- `cady-company-decision-questions`: A goal or decision you own needs evidence: frame its key questions and pick the cheapest research route.
- `cady-company-distil`: A due distil task names a node whose critical observations are waiting on the outer loop.
- `cady-company-executive-review`: Run the weekly review of open goals and initiatives, or make one company-level decision between reviews.
- `cady-company-experiment`: Test the riskiest assumption with a pre-registered experiment and a decision rule set before any work starts.
- `cady-company-manage-agents`: Create and bind, schedule, review or retire a company agent: whether one is warranted, its design and first task.
- `cady-company-taste-review`: Write or edit a post, article, web copy, prompt or skill, or review a design (judge with the taste check).
- `cady-company-voice-pack`: Owner sets up or refreshes how their messages sound, or drafts read generic. Builds the pack from their sent messages.
- `cady-orchestrator-goal-pass`: A due orchestrator pass, or an event: a run finished, an ask was answered, a claim lapsed or a handover returned.

## gtm

- `cady-customer-success-lifecycle`: Run one customer account after the sale: onboarding to first value, health, risk, renewal, expansion or cancellation.
- `cady-gtm-calls`: Prepare for a sales or customer call (account brief, agenda, questions), then record its follow-up and next step.
- `cady-gtm-channel-plan`: Turn accepted persona, offer and chosen channels into channel plays and execution briefs.
- `cady-gtm-cold-email-cycle`: Write and send cold email to people not yet contacted, using one template per segment.
- `cady-gtm-events`: Prepare for or host the event named in the brief to advance the company through real conversations.
- `cady-gtm-linkedin-message`: Draft a first social DM, LinkedIn connection note or one no-reply follow-up.
- `cady-gtm-offer-and-segments`: Choose or revise the target persona, offer or message angle from evidence, before a cold cycle and at its review.
- `cady-gtm-persona-profile`: Write or revise one persona's profile (customer, investor, partner or supplier) before positioning, sourcing or copy.
- `cady-gtm-pipeline-pass`: Pass over due tracks of one motion (customer for GTM, investor for fundraising, partner) and their next steps.
- `cady-gtm-reply`: Answer an inbound reply in a live thread: a question, interest, objection, referral, not now or stop.
- `cady-gtm-tam-map`: Find who wants, where they gather: people, communities, prospects, leads, target customers, companies or accounts.
- `cady-gtm-warm-email`: Write email follow-ups, engaged notes, or partner, organiser and supplier business messages, including first approaches.
- `cady-marketing-post`: Create or edit one post for the audience, topic and placement chosen in the brief.
- `cady-orchestrator-gtm-motion-pass`: A due GTM pass, or an event: a reply, a segment crossing its reply line or a stage stalling.
- `cady-sales-deal-motion`: Work one opportunity: discovery call, light qualification, proposal, close plan, handoff to success or loss review.

## product

- `cady-design-wcag-audit`: Audit a web or app interface against WCAG 2.2 AA with real tools and report ranked, reproducible findings.
- `cady-engineering-debugging`: Find and fix the root cause of a bug, failing check or production incident, then the regression test and postmortem.
- `cady-engineering-system-cycle`: Clear a product's engineering backlog in recurring cycles from its goal map, system dimensions and state-routed motions.
- `cady-orchestrator-product-motion-pass`: A due product pass, or an event: a release due, work in progress over its limit or results arriving.
- `cady-product-customer-interview`: Plan, run and synthesise customer discovery interviews about past behaviour, without leading questions.
- `cady-product-manage`: Decide what to build and why; run discovery; plan each release and its go/no-go; run a goal to done.
- `cady-product-research`: Write or update a research file (research/<title>.md) on competitors and alternatives, or on a technology.
- `cady-qa-stories`: Edit or retire a user story, walk one blind as a fresh user, read story status, or file a finding on a step.
- `cady-qa-triage`: Rate a bug's severity, write a reproducible report, triage a flaky test, or verify a fix before closing it.

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
- `cady-orchestrator-finance-motion-pass`: A due finance pass, or an event: a new commitment, a period ending or the runway line moving.

## operations

- `cady-company-operations-compliance-register`: What statutory and registry filings the company owes and when (annual returns, confirmation statements, state reports).
- `cady-company-operations-contract-checks`: A contract that commits the company is about to be signed or was just signed: what to settle first and what it starts.
- `cady-company-operations-inbox-follow-through`: Bounded inbox maintenance or thread triage for follow-through, marketing handling or commitments needing tracking.
- `cady-company-operations-people-lifecycle`: Plan, track and verify the paperwork and access for a new hire or contractor, a role change or someone leaving.
- `cady-company-operations-requirement-register`: Research, independently check and record one compliance requirement as a Cady Projects decision.
- `cady-orchestrator-operations-motion-pass`: A due operations pass, or an event: an obligation's lead time opening or a commitment found in the inbox.
