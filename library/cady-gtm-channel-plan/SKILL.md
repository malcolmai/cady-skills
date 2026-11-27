---
name: "cady-gtm-channel-plan"
description: "Channel plan. Use when: Turn accepted persona, offer and chosen channels into channel plays and execution briefs. Not for: Choosing the persona, offer or channel mix; researching parties, writing copy, sending or installing schedules."
license: "MPL-2.0"
compatibility: "Requires Cady (app.cadyworks.com/mcp)"
metadata:
  cady-id: "skill.gtm.channel_plan"
  version: "b7fc67bc26be141df514"
  library: "7bf126ff6bc82cee"
  function: "gtm"
---
# Channel plan

**Point:** Turn accepted persona, offer and chosen channels into channel plays and execution briefs.

**Company context:** `cady_start {"task": "<what you are about to do, in one sentence>"}`

**Bets** (where this differs from the default):
- Strategy decides the mix once; execution reads references. Instead of: Rediscover or copy the persona and offer inside execution.
- Each limit protects a different constraint. Instead of: Apply one generic send cap without distinguishing the mailbox, authority and review limits.
- A kill rule set after results is not a test. Instead of: Choose the keep, scale or kill rule after seeing the results.
- Accept a result only after reading the artifact and the sourcing shortfall. Instead of: Accept the execution agent’s report without reading the review or List shortfall.

Turn accepted persona, offer and chosen channels into channel plays and execution briefs.

**Not for:** Choosing the persona, offer or channel mix; researching parties, writing copy, sending or installing schedules.

**Unit of work:** one work item per customer outreach plan. **Kind:** strategy. **Parallel:** no. 

## Inputs

### Evidence refs

- persona File ref
- offer and message decision refs
- strategy and chosen channel decision refs
- goal and target refs

### Work fields

- segmentKey (the persona's key)
- goalId

## Procedure

1. Read the accepted strategy decisions by ref (cady_read decision:<subject>): persona File, offer and message, chosen channels and daily targets. Plan only those channels; no agent, brief or standing-approval ask for an unchosen channel. A missing or contradictory decision goes back to strategy. When fit needs rechecking, refer it to strategy with `references/gtm-channels.md`; do not re-decide it here.
2. File prospect sourcing as execution work under `cady-gtm-tam-map`, with the persona and decision refs, requested identity and coverage; apply the persona disqualifiers there. A List shorter than the planned cohort is reported to strategy. Do not research parties here.
3. Set each chosen channel’s play in its brief: audience, offer, proof, stop and review condition. A cold first touch is once per party per cycle. A reply leaves the sequence and is answered first: a recorded reply goes to cady-gtm-reply first; a positive reply then hands off to cady-gtm-calls. Follow-ups are their own reviews after the outcome check; use `references/outreach-release.md`, Follow up for the counts and spacing. For events choose by fit, conversation density, cost and founder time; for posting choose topic, pillar and distribution from the accepted strategy.
4. Size the sending cohort as the least of eligible parties, the sending mailbox's cold emails left today (a warning from the company's cold email warning line, 50 a day by default, and a hard cap of 100 per UTC day), the standing approval's daily cap and 50 (one review's limit). There is no company volume cap and no warm-up: every mailbox has the same warning line and cap from its first day, and only cold email counts (a reply, an invitation, a notification or a follow-up to someone already engaged is paced but not counted). Spread LinkedIn sends across working hours. A standing approval's daily cap only narrows these limits. The strategy daily target is a ceiling, never a quota; planned daily sends never exceed the mailbox's room left today.
5. Choose one to three variants with large angle differences: about 40/30/30 early, then 70/20/10 only after a winner holds two cycles. Before the cycle use `cady-company-evidence` to pre-register the behavioural metric, pass and fail lines, sample, time box and keep, scale or kill decision. Read the cycle's outreach reviews (cady_read review:outreach/<approvalId>, each approvalId the work reported) at mid-cycle and end by variant and persona with denominators; use the GTM domain method's small-sample rule before treating evidence as decisive. A channel failing its line twice the same way goes to the strategy goal call: persist, pivot, parallel or stop.
6. For each channel identify the standing approval the person may set up in Cady: the List or motion it covers, the agents that hold the work, an optional end and an optional daily cap. A standing approval is a person's yes that agents cite with crm_outreach {id, status: sending, grantId}: propose it (quoted_approval, profileId crm.outreach.standing.v1, grant {list or motion, agentIds, expiresAt?, dailyCap?}) and the person accepts it on Home in Cady (see the authority section). The first cycle supplies the one to five rendered examples for the owner’s decision; nothing sends before that approval. Never treat a proposal as accepted, and never resume one yourself: the person accepts and resumes them, in Cady.
7. Create one execution agent per channel in use with `references/execution-agent-brief.md`.
8. Hand over the agent and first work item IDs with a recommended cadence and why it suits reply timing; whoever sets up the run chooses schedule or tracked one-off dispatch and binds it (`cady-company-manage-agents` step 10); the agent is set live once bound (no go-ahead asked).
9. Before accepting an execution agent's result, read its held review (cady_read review:outreach/<approvalId>) and the List shortfall; send back what fails the brief's doneWhen.

## Acceptance

- [ ] (check) accepted persona, offer and chosen channel refs are used; persona-matched sourcing is filed and any List shortfall reported
- [ ] (check) each chosen channel has a bounded sequence, caps, variants and pre-registered review rule
- [ ] (check) the standing approval to ask for, isolated agents and first tasks are ready for host setup

## Owner checks

- the owner gives standing approvals; whoever sets up the run chooses scheduling; status live takes the agent live

## Result

### Artifact refs

- sourcing work item
- channel execution agent and first work item refs
- **Transition:** report the plan and hand execution agents to host setup

## References
- Read [Execution agent brief](references/execution-agent-brief.md) when creating each channel agent and its first task.
- Apply `cady-company-evidence` when pre-registering each channel test.
- Read [GTM channel comparison](references/gtm-channels.md) when a chosen channel’s fit needs rechecking by strategy.
