---
name: "cady-company-distil"
description: "Distil the concern tree. Use when: A due distil task names a node whose critical observations are waiting on the outer loop. Not for: Doing the work that produced the observation, or the company review that owns direction (`cady-company-executive-review`)."
license: "MPL-2.0"
compatibility: "Requires Cady (app.cadyworks.com/mcp)"
metadata:
  cady-id: "skill.company.distil"
  version: "9a7d00069afe0564cd83"
  library: "cb563a1c3ed92251"
  function: "company"
---
# Distil the concern tree

**Point:** Turn what the work observed into the node's next point, bet or choice, once, under its authority.

**Company context:** `cady_read {"search": {"query": "<what you are about to do, in one sentence>"}}`

**Bets** (where this differs from the default):
- Distil a node's due observations once, as a whole set, into its point or bet under the authority of its basis. Instead of: Act on each observation as it arrives, or let a signal decide for the owner.

A due distil task names a node whose critical observations are waiting on the outer loop.

**Not for:** Doing the work that produced the observation, or the company review that owns direction (`cady-company-executive-review`).

**Unit of work:** one node's due observations. **Kind:** strategy. **Parallel:** no. 

## Always

- A bet carries the measure that would settle it; without one it is refused, so write the measure before accepting the bet.
- The observation is evidence, not authority: who may decide is the node's depth and the writer's role, never the strength of the signal.

## Inputs

### Evidence refs

- the distil task's node reference (node:<key>) and the observations the node carries
- the node's current point and its current bets

### Work fields

- the node reference on the task
- which observations are due and what each recorded

## Procedure

1. Read before deciding. The task (work_read) names the node in its statement and cites it as node:<key>. call cady_start {node: the node's path}; it returns that node's point and bets, and what governs it above; if it shows none, say the bets were not read. Then read the node's due observations. A distil reads the whole due set, not one observation at a time. The top of every company's tree is the same four families: go-to-market (demand), product (what is offered, priced and delivered), finance (company-level money in and out) and operations (how the company runs); a family needs no agent. There is one task per node episode: work it once for the whole set and file no second task for the node.
2. Judge what the observations change. Is the node's point still true? Does a bet the node carries still hold against its measure, or does the evidence contradict it? An observation is a signal, not a decision: an ordinary one may rightly change nothing, and a narrow lesson goes to its owning home (product map, test or check, method, work result), not the tree.
3. Settle the record once, with decisions_write at the node's path (`cady-company-decision-check` step 6). Set or replace the node's point in its own sentence. Write a bet as we do X, not Y, because W, with its basis (validated, citing a reading or two independent runs; hypothesis, naming what would accept it, what would reject it and after doing what; owner decided; or resource constraint) and the measure that would settle it. A later item supersedes the current one of its kind, and the history stays. Dismiss an observation only with the note that says why it was not acted on.
4. Authority follows the basis. A member decides by role, and an Admin's quoted words make a bet owner decided. A point or a bet you write is current at once and the owner is told; one call reverts it, and cited evidence is still the better record. Replacing an owner-decided bet needs the Admin's quoted words; otherwise it waits as an ask carrying the recommendation and evidence, and so does any one-way door. Your override grants no outside-effect permission.
5. Close the episode. Every observation in the due set ends distilled (a decision was made from it) or dismissed (seen and deliberately not acted on, with its note); it never returns to recorded. Close the distil task with work_write {id, status: done, result, evidenceRefs}, the result carrying the point or bet it produced, the evidence behind it and the disposition of each observation, so the next episode starts from a clean node.
6. Say what to watch. Report which reading would confirm or refute an accepted bet, and the next observation that would reopen the point. That reading is C5's measurement of the node, so name it in the same words the bet's measure uses.

## Acceptance

- [ ] (check) the node's current point or bet states what the due observations showed, and nothing else on the node changed
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
