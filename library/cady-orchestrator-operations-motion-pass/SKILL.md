---
name: "cady-orchestrator-operations-motion-pass"
description: "Orchestrate operations. Use when: A due operations pass, or an event: an obligation's lead time opening or a commitment found in the inbox. Not for: Preparing a filing, a contract check or a joiner's paperwork itself (the operations agents do that), or legal advice."
license: "MPL-2.0"
compatibility: "Requires Cady (app.cadyworks.com/mcp)"
metadata:
  cady-id: "skill.orchestrator_operations.motion_pass"
  version: "e2cd4f2a343887ef5045"
  library: "04d8d277d668b7e6"
  function: "orchestrator_operations"
---
# Orchestrate operations

**Point:** Each pass, every obligation inside its lead time is started and every inbox commitment is tracked.

**Company context:** `cady_read {"search": "<what you are about to do, in one sentence>"}`

**Bets** (where this differs from the default):
- Start an obligation when its lead time opens, not at its deadline. Instead of: Working obligations by due date.

A due operations pass, or an event: an obligation's lead time opening or a commitment found in the inbox.

**Not for:** Preparing a filing, a contract check or a joiner's paperwork itself (the operations agents do that), or legal advice.

**Unit of work:** one pass over the company's obligations. **Kind:** execution. **Parallel:** no. 

## Inputs

### Evidence refs

- the obligations calendar with each lead time
- commitments found in the inbox

### Work fields

- the obligations in scope
- each obligation's lead time and the cost of a miss

## Procedure

1. Read the obligations calendar with each lead time, and the commitments found in the inbox.
2. Start each obligation whose lead time has opened.
3. Rank the rest by the cost of a miss and spend prevention effort from the top.
4. Track each commitment to done or an explicit decline.
5. Read each result one level down with `cady-company-challenge`. Decide inside the family's node by its point and bets, and record each call on the lowest node both pieces of work serve. Hand a call that crosses families to the orchestrator and one that would change a point, bet or goal to the Executive, with both options and the evidence.
6. Report obligations started, those at risk, and commitments open, done or declined.

## Acceptance

- [ ] (check) no obligation inside its lead time is unstarted
- [ ] (check) no inbox commitment is untracked

## Owner checks

- obligations start by lead time, not deadline
- a declined commitment says so to whoever it was made to

## Result

### Artifact refs

- company:work:<workId>
- **Transition:** one pass recorded as a finished run
