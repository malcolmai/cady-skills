---
name: "cady-gtm-channel-plan"
description: "Channel plan. Use when: Turn accepted persona, offer and chosen channels into channel plays and execution briefs. Not for: Choosing the persona, offer or channel mix; researching parties, writing copy, sending or installing schedules."
license: "MPL-2.0"
compatibility: "Requires Cady (app.cadyworks.com/mcp)"
metadata:
  cady-id: "skill.gtm.channel_plan"
  version: "96cce6d974cf45e1735a"
  library: "3a6b57b5728fb7c0"
  function: "gtm"
---
# Channel plan

**Point:** Turn accepted persona, offer and chosen channels into channel plays and execution briefs.

**Company context:** `context_read({"area": "gtm/strategy", "task": "<what you are about to do, in one sentence>", "knownMethods": {"skill.gtm.channel_plan": "96cce6d974cf45e1735a@3a6b57b5728fb7c0"}})`

**Bets** (where this differs from the default):
- Strategy decides the mix once; execution reads references. Instead of: Rediscover or copy the persona and offer inside execution.
- Each cap protects a different constraint. Instead of: Apply one generic send cap without distinguishing reputation, mailbox, authority and review limits.
- A kill rule set after results is not a test. Instead of: Choose the keep, scale or kill rule after seeing the results.
- Accept a result only after reading the artifact and the sourcing shortfall. Instead of: Accept the execution agent’s report without reading the review or List shortfall.

Turn accepted persona, offer and chosen channels into channel plays and execution briefs.

**Not for:** Choosing the persona, offer or channel mix; researching parties, writing copy, sending or installing schedules.

**Unit of work:** one work item per customer outreach plan. **Kind:** strategy. **Parallel:** no. **Can release:** no. 

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

1. Read the accepted strategy decisions by ref (records_read decision:<subject>): persona File, offer and message, chosen channels and daily targets. Plan only those channels; no agent, brief or grant ask for an unchosen channel. A missing or contradictory decision goes back to strategy. When fit needs rechecking, refer it to strategy with `../../references/gtm-channels.md`; do not re-decide it here.
2. File prospect sourcing as execution work under `cady-gtm-tam-map`, with the persona and decision refs, requested identity and coverage; apply the persona disqualifiers there. A List shorter than the planned cohort is reported to strategy. Do not research parties here.
3. Set each chosen channel’s play in its brief: audience, offer, proof, stop and review condition. A cold first touch is once per party per cycle. A reply leaves the sequence and is answered first: a recorded reply goes to cady-gtm-reply first; a positive reply then hands off to cady-gtm-calls. Follow-ups are their own reviews after the outcome check; use `../../references/outreach-release.md`, Follow up for the counts and spacing. For events choose by fit, conversation density, cost and founder time; for posting choose topic, pillar and distribution from the accepted strategy.
4. Size the sending cohort as the least of eligible parties, weekly company cap remaining, sender warm-up capacity, grant cap and 50 (one review's limit). Email: company 100 per rolling day and 500 per rolling week; a new mailbox warms with normal human mail for two to four weeks, then about 10 cold sends a day, rising about 10 a week to 30–50 per mailbox. LinkedIn: 20 per rolling day and 100 per rolling week, spread across working hours. Grant caps only narrow company ceilings. The strategy daily target is a ceiling, never a quota; planned daily sends never exceed the mailbox capToday.
5. Choose one to three variants with large angle differences: about 40/30/30 early, then 70/20/10 only after a winner holds two cycles. Before the cycle use `cady-company-experiment` to pre-register the behavioural metric, pass and fail lines, sample, time box and keep, scale or kill decision. Read crm.get_outreach_review({cycleKey}) at mid-cycle and end by variant and persona with denominators; use the GTM domain method's Direction rule before treating evidence as decisive. A channel failing its line twice the same way goes to the strategy goal call: persist, pivot, parallel or stop.
6. For each channel identify grant terms to ask for: channel, sender, cohort listIds, caps, followUps {max, delayDays} and expiry. A grant is a separate recurring permission; see the authority section's grant line. The first prepare-only cycle supplies the one to five rendered examples for the owner’s grant decision. Never activate a grant on the owner’s behalf.
7. Create one execution agent per channel in use with `../../references/execution-agent-brief.md`.
8. Hand the agent and first work item IDs to the orchestrator, with a recommended cadence and why it suits reply timing; the orchestrator chooses schedule or tracked one-off dispatch, binds and takes the agent live. cady-core-execution owns executor and capability checks.
9. Before accepting an execution agent's result, read its held review (records_read review:outreach/<approvalId>) and the List shortfall; send back what fails the brief's doneWhen.

## Acceptance

- [ ] (check) accepted persona, offer and chosen channel refs are used; persona-matched sourcing is filed and any List shortfall reported
- [ ] (check) each chosen channel has a bounded sequence, caps, variants and pre-registered review rule
- [ ] (check) grant terms, isolated agents and prepare-only first tasks are ready for the orchestrator

## Owner checks

- the owner decides grants; the orchestrator chooses scheduling and go-live

## Result

### Artifact refs

- sourcing work item
- channel execution agent and first work item refs
- **Transition:** the claim holder reports the plan and hands execution agents to the orchestrator

## References
- Read [Execution agent brief](../../references/execution-agent-brief.md) when creating each channel agent and its first task.
- Apply `cady-company-experiment` (`../cady-company-experiment/SKILL.md`) when pre-registering each channel test.
- Read [GTM channel comparison](../../references/gtm-channels.md) when a chosen channel’s fit needs rechecking by strategy.
