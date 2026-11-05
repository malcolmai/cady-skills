---
name: "cady-company-distil"
description: "Distil the concern tree. Use when: A due distil task names a node whose critical observations are waiting on the outer loop. Not for: Doing the work that produced the observation, or the company review that owns direction (`cady-company-executive-review`)."
license: "MPL-2.0"
compatibility: "Requires Cady (app.cadyworks.com/mcp)"
metadata:
  cady-id: "skill.company.distil"
  version: "942282b67df836b86fdc"
  library: "d63cf26c33473e84"
  function: "company"
---
# Distil the concern tree

**Point:** Turn what the work observed into the node's next point, bet or choice, once, under its authority.

**Company context:** `context_read({"area": "ops/records", "task": "<what you are about to do, in one sentence>", "knownMethods": {"skill.company.distil": "942282b67df836b86fdc@d63cf26c33473e84"}})`

**Bets** (where this differs from the default):
- Distil a node's due observations once, as a whole set, into its point, bet or choice under the node's authority. Instead of: Act on each observation as it arrives, or let a signal decide for the owner.

A due distil task names a node whose critical observations are waiting on the outer loop.

**Not for:** Doing the work that produced the observation, or the company review that owns direction (`cady-company-executive-review`).

**Unit of work:** one node's due observations. **Kind:** strategy. **Parallel:** no. **Can release:** no. 

## Always

- A bet carries the measure that would settle it; without one it is refused, so write the measure before accepting the bet.
- The observation is evidence, not authority: who may decide is the node's depth and the writer's role, never the strength of the signal.

## Inputs

### Evidence refs

- the distil task's node reference (node:<key>) and the observations the node carries
- the node's current point and its current bets and choices

### Work fields

- the node reference on the task
- which observations are due and what each recorded

## Procedure

1. Read before deciding. The task (work_read) names the node in its statement and cites it as node:<key>; read the chain of points to that node and the bets at the level above and at it with context_read's nodeKey selector, then read the node's due observations. A distil reads the whole due set, not one observation at a time. There is one task per node episode: work it once for the whole set and file no second task for the node.
2. Judge what the observations change. Is the node's point still true? Does a bet the node carries still hold against its measure, and does the evidence contradict it? Is a choice now the right answer? An observation is a signal, not a decision: the node's record is where the judgement lands, and an ordinary observation may rightly change nothing.
3. Settle the record once. Set or replace the node's point in its own sentence; accept a bet only with the option it replaced, why, its state and the measure that would settle it; record a choice with the option it replaced and why. A later decision supersedes the current one of its kind, and the history stays. Dismiss an observation only with the note that says why it was not acted on.
4. Apply the one authority rule. The owner may write any node decision. A function head may accept only a bet on a node at depth 2 or deeper, and only with a notice to the owner and the owner's one confirmation; a point, a choice or a shallower bet is the owner's, so raise it as an ask with the recommendation and its evidence instead of writing it. An agent proposes; it never accepts a node decision in the owner's place.
5. Close the episode. Every observation in the due set ends distilled (a decision was made from it) or dismissed (seen and deliberately not acted on, with its note); it never returns to recorded. Close the distil task with work_write or decisions_write or asks_write, carrying the decision it produced, the evidence behind it and the disposition of each observation, so the next episode starts from a clean node.
6. Say what to watch. Report which reading would confirm or refute an accepted bet, and the next observation that would reopen the point. That reading is C5's measurement of the node, so name it in the same words the bet's measure uses.

## Acceptance

- [ ] (check) the node's current point, bet or choice states what the due observations showed, and nothing else on the node changed
- [ ] (check) every observation in the due set is distilled or dismissed with its note
- [ ] (person) a function head's accepted bet was seen by the owner and confirmed once

## Owner checks

- the node's current point and bets read before writing anything
- every observation in the due set ends distilled or dismissed, with a note on a dismissal
- a function head's accepted bet carries the owner's notice and the owner's one confirmation

## Result

### Artifact refs

- company:work:<workId>
- **Transition:** close the distil task with the decision it produced and each observation's disposition
