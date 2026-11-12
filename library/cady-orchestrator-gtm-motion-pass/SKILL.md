---
name: "cady-orchestrator-gtm-motion-pass"
description: "Orchestrate GTM. Use when: A due GTM pass, or an event: a reply, a segment crossing its reply line or a stage stalling. Not for: Writing or sending outreach, or setting the persona and offer (the GTM agents do both)."
license: "MPL-2.0"
compatibility: "Requires Cady (app.cadyworks.com/mcp)"
metadata:
  cady-id: "skill.orchestrator_gtm.motion_pass"
  version: "f79ede5b7d16c1840191"
  library: "d110e6194c26a326"
  function: "orchestrator_gtm"
---
# Orchestrate GTM

**Point:** Each pass, the next unit of GTM effort goes to the stage where conversion breaks, behind an evidence gate.

**Company context:** `cady_read {"search": {"query": "<what you are about to do, in one sentence>"}}`

**Bets** (where this differs from the default):
- Gate volume on evidence: a segment under its reply line goes back to positioning before another send. Instead of: Raising volume on a weak segment.

A due GTM pass, or an event: a reply, a segment crossing its reply line or a stage stalling.

**Not for:** Writing or sending outreach, or setting the persona and offer (the GTM agents do both).

**Unit of work:** one pass over the company's GTM motion. **Kind:** execution. **Parallel:** no. 

## Inputs

### Evidence refs

- the funnel per segment by stage
- each running segment's accepted persona and offer
- live threads and due follow-ups

### Work fields

- the segments in scope
- each segment's reply line

## Procedure

1. Read the funnel per segment by stage: sourced, contacted, replied, in conversation, deal, customer, kept.
2. Check the evidence gate: each running segment has an accepted persona and offer. Pause a segment below its reply line and send it back to positioning, not to more volume.
3. Clear live replies and due follow-ups before any new send.
4. Name the weakest stage and route the pass's effort there, and hand the due tracks to their holders for a pipeline pass.
5. Keep one track per contact: one owner, one next step, one channel at a time; merge or end duplicates.
6. Read each result one level down with `cady-company-challenge`. Decide inside the family's node by its point and bets, and record each call on the lowest node both pieces of work serve. Hand a call that crosses families to the orchestrator and one that would change a point, bet or goal to the Executive, with both options and the evidence.
7. Report stage counts per segment, the weakest stage, where effort went and the calls made.

## Acceptance

- [ ] (check) no segment runs past its evidence gate
- [ ] (check) no live reply waits past its turnaround
- [ ] (check) the weakest stage is named with the effort it got

## Owner checks

- a segment runs only on an accepted persona and offer
- no contact has two owners or two open next steps

## Result

### Artifact refs

- company:work:<workId>
- **Transition:** one pass recorded as a finished run
