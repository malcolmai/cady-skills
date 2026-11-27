---
name: "cady-company-decision"
description: "Who decides, and how to record it. Use when: Before a choice or an effect: whether it is decided, who decides, how to test a big call and how to record it. Not for: Gathering the evidence a call needs (`cady-company-evidence`), the weekly goal calls (`cady-company-weekly-review`), or doing the task itself."
license: "MPL-2.0"
compatibility: "Requires Cady (app.cadyworks.com/mcp)"
metadata:
  cady-id: "skill.company.decision"
  version: "60acdd73218891019fef"
  library: "f5e8b22b566aee82"
  function: "company"
---
# Who decides, and how to record it

**Point:** Settle whether a choice is decided and whose it is, test a consequential one first, and record it once.

**Company context:** `cady_start {"task": "<what you are about to do, in one sentence>"}`

**Bets** (where this differs from the default):
- Decide or ask by risk (what breaks, for whom, how reversibly) and independent review, not by the decision's layer. Instead of: Ask the owner about every decision labelled company-level and decide everything below that alone.
- Spend the owner's time only on top-level judgement they have not stated and on authority only they hold. Instead of: Check with the owner whenever a choice feels important, to be safe.
- Write the chain from the goal down to the choice, with impact, the strongest alternative and why it loses, and dated premises. Instead of: Decide from judgement and report the choice, leaving the reasoning in the conversation.
- Size the process to the door: decide a reversible, cheap call now with a default and reviewBy; keep the outside view, pre-mortem and red team for one-way or consequential calls. Instead of: Run the same full analysis (options, base rates, pre-mortem, red team) on every company decision for rigour.
- Replace or rule out any bet, the owner's included, in one call; the owner is told and reverts it in one call. Instead of: Leave a decision someone else made, especially the owner's, in place and ask before changing it.

Before a choice or an effect: whether it is decided, who decides, how to test a big call and how to record it.

**Not for:** Gathering the evidence a call needs (`cady-company-evidence`), the weekly goal calls (`cady-company-weekly-review`), or doing the task itself.

**Unit of work:** one choice or effect. **Kind:** strategy. **Parallel:** yes. 

## Inputs

### Evidence refs

- the governing decisions and goal, and the decision item or escalation

## Procedure

1. Already decided? Read the governing decisions and goal (cady_read decision:<subject> and the goal). If one still holds, follow it and never ask again; if a premise changed or a newer point, bet or goal conflicts, recheck it at its own layer and cite what changed.
2. Whose is it? Strategy (where resources go, how functions work together) is a point or bet on the company tree; otherwise L1 (a goal, a hire, a spend envelope) is the company's, L2 (how a function pursues a goal) its head's, L3 (how a task is done) any agent's. The owner keeps the permission edge (their account, a fact only they hold), payments, signing and filing, and a top-level call (ICP, problem, offer, stage) they have not stated; what they stated is recorded at once, never asked back.
3. Size the work to the door. Write the chain from the goal down (one line for a small call): the pain served, this choice, why now, the strongest alternative and dated premises. Decide a two-way door now with a default and a review date. A one-way or consequential door adds the outside view (a sourced base rate, or 'none'), the evidence that would change it, a prediction written first and the review of step 4. Hold a high-risk change you cannot test or review.
4. A one-way or consequential call others build on gets an independent review first (`cady-engineering-independent-review`): a fresh-context reviewer given only the record, plus a pre-mortem and a red team, never your recommendation. Ask only what it cannot resolve; an unstated top-level call still contested after it is a todo (todos_set, written as `../cady/references/asking.md` says), not yours.
5. Record it once, in place: a point or bet with decisions_set (its fields say where), a goal call with work_set, a narrow call in the work result, and a consequential call also as a File (files_set) the result cites. A call the person states in chat is recorded at once as a bet and never asked again; a premise resting on their word says so in why. Mark sensitive only what would truly harm if seen.
6. Any point or bet, the owner's included, is yours to replace or rule out in one call; the owner is told and reverts it in one call. Update the open tasks that state the old choice. Replacing grants no permission and never undoes an owner's stop. Record an owner's correction at the scope they gave, never widened; with a node served, the finishing work_set also sends it as an observation.

## Acceptance

- [ ] (check) decisions rechecked before deciding; an agent decision others build on records its chain, losing alternative and dated premises, and a one-way door its outside view, prediction and review
- [ ] (person) no permission-edge or unstated, contested top-level call taken by an agent; a person's stated call recorded at once as a bet; a correction, with a node served, also sent as an observation

## Owner checks

- a bet an agent replaced or ruled out reaches the owner

## Result

### Artifact refs

- company:work:<workId>
- file:<fileId>
- **Transition:** the choice or effect recorded at its layer, with provenance

## References
- Read [Asking and refusals](../cady/references/asking.md) when you would ask, a call is refused, a permission is missing or you rely on an assumption.
