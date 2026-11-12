---
name: "cady-orchestrator-finance-motion-pass"
description: "Orchestrate finance. Use when: A due finance pass, or an event: a new commitment, a period ending or the runway line moving. Not for: Doing the books, the budget or the raise itself (the finance agents do that), or tax and filing advice."
license: "MPL-2.0"
compatibility: "Requires Cady (app.cadyworks.com/mcp)"
metadata:
  cady-id: "skill.orchestrator_finance.motion_pass"
  version: "e5a5b0431ce40e27a3db"
  library: "4df067661df56e5b"
  function: "orchestrator_finance"
---
# Orchestrate finance

**Point:** Each pass, runway is current, the close is on time and funding starts ahead of the runway line.

**Company context:** `cady_read {"search": {"query": "<what you are about to do, in one sentence>"}}`

**Bets** (where this differs from the default):
- Set the funding start backwards from the runway line, with slack. Instead of: Starting a raise when cash feels short.

A due finance pass, or an event: a new commitment, a period ending or the runway line moving.

**Not for:** Doing the books, the budget or the raise itself (the finance agents do that), or tax and filing advice.

**Unit of work:** one pass over the company's money motion. **Kind:** execution. **Parallel:** no. 

## Inputs

### Evidence refs

- cash, burn and runway months
- the close status per period
- pending commitments
- the funding timeline

### Work fields

- the runway line
- the funding slack in months

## Procedure

1. Read cash, burn and runway months, the close status, pending commitments and the funding timeline.
2. Gate each pending commitment against runway; send one that moves the runway line to the Executive.
3. Check that the last period is closed before any plan or investor figure uses it.
4. Check the funding start date against the runway line, with its slack; start or flag the raise or grant when it is late.
5. Reconcile metrics so the plan, the books and investor material carry one number each.
6. Read each result one level down with `cady-company-challenge`. Decide inside the family's node by its point and bets, and record each call on the lowest node both pieces of work serve. Hand a call that crosses families to the orchestrator and one that would change a point, bet or goal to the Executive, with both options and the evidence.
7. Report runway, the close state, commitments gated and the funding timeline.

## Acceptance

- [ ] (check) runway is current to the last closed period
- [ ] (check) no commitment skipped the runway gate
- [ ] (check) the funding start is on or ahead of its date

## Owner checks

- a commitment that moves the runway line is the Executive's
- figures come from closed periods

## Result

### Artifact refs

- company:work:<workId>
- **Transition:** one pass recorded as a finished run
