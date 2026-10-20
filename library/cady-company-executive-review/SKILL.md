---
name: "cady-company-executive-review"
description: "Executive decision review. Use when: The Executive takes one founder- or executive-level decision from frame to recorded decision and review. Not for: Pushing work along, designing agents or doing delivery; routine decisions belong to the relevant function method, such as `cady-product-method`."
license: "MPL-2.0"
compatibility: "Requires Cady (app.cadyworks.com/mcp)"
metadata:
  cady-id: "skill.company.executive_review"
  version: "00c158ce86dd0ded97661e784479a7e9ceaca48ddab90ee019c84e9f73db5c4e"
  function: "company"
---
# Executive decision review

The Executive takes one founder- or executive-level decision from frame to recorded decision and review.

**Not for:** Pushing work along, designing agents or doing delivery; routine decisions belong to the relevant function method, such as `cady-product-method`.

**Unit of work:** one decision, or the allocation:current record. **Kind:** strategy. **Parallel:** no. **Can release:** no. 

## Inputs

### Evidence refs

- the decision item or escalation
- owner records the decision cites

### Sources

- get_company_direction
- the finance plan read (cash, burn, runway)
- get_company_work decisions {state: "current"}
- list_recent_changes since your last pass

## Procedure

1. Pick one decision. Sources: a new founder idea (record it as an initiative, step 14) or an initiative past its reviewBy with no follow-up; BLOCKED decision items waiting on you; escalations agents handed up; an allocation trigger (a bet's status changed, a stop or reversal condition met, a reviewBy date passed, direction changed, or the founder asked); a reviewBy date that passed on an earlier decision; a direction review; material new evidence in list_recent_changes since your last pass. Take the one with the highest cost of delay. If none qualifies, end with 'allocation stands' and write nothing.
2. Look it up first: get_company_work decisions {state: "current", subject}. If a current decision exists and no trigger reopens it, use it and stop; never ask the person twice.
3. Frame it: the decision in one sentence, why now, the deadline or cost of delay, one-way or two-way door, and who decides (you, or the founder for founder-reserved choices). Pick the one frame that fits: expected value for repeatable bets, real options for reversible exploration, constraint analysis for throughput problems, pre-mortem for one-way doors. Proportion the work to the door: a reversible, low-cost (two-way door) decision is decided now with a stated default and reviewed at reviewBy in hindsight; steps 4-8 stay light, and the full pre-mortem and red team (step 8) are for consequential or one-way decisions only.
4. Compare the strongest feasible alternative and the status quo where relevant. A genuinely binary choice is valid; judge the choice and evidence, not the option count.
5. Take the outside view first: the reference class and its base rate with a source, or 'none'.
6. Decide what you need to decide: use `cady-company-decision-questions` for evidence on each uncertainty that would change the choice. Check what owners already hold; request it as bounded work from the orchestrator with a deadline.
7. Write the prediction before deciding: a range with a confidence, and a kill or reversal condition.
8. Review before deciding: the strongest alternative and the weakest assumption. Only a consequential or one-way decision also gets a pre-mortem and a fresh red-team subagent (review tier) given the frame and evidence, never your recommendation.
9. Decide within your authority. For a founder-reserved choice, raise a BLOCKED decision item addressed to the owner with a recommendation and options; it reaches them as asksForYou.
10. Record it: the full record (steps 3-8, the decision and reviewBy) as a File through files.upload mode "begin" then "complete", and a decision item through submit_company_work_checkpoint with decision {kind: "decision", subject, layer (L2 strategy with a keyAssumption, L3 execution), rationale, alternatives, reversal, reviewBy, authority, decidedBy} citing file:<fileId>. For your own choice use authority "agent" and omit decidedBy: Cady records it as your agent, never as the person (no source or quote). A person's choice needs source "chat" with their exact words in quote and decidedBy (or a verified source "grant" with grantId); Cady marks agent-recorded person decisions viaAgent. Keep the item's summary within its 2000-byte limit.
11. Hand next steps to the orchestrator or suitable existing agent as exact Projects tasks: statement, brief {acceptance: 1-5 tagged checks with must, finishLine}, nextAction and evidence refs, with goalId, agentId, dependsOn or productId only when real. Current allocation is priority evidence, not task identity or effect authority; a direct one-off needs no invented allocation, and allocation grants no effects. Read the reported result and accept with your own per-criterion verdicts, recording the owner's chat words in acceptance.quote, before judging outcomes; never do the function work yourself.
12. At reviewBy, compare the outcome with the prediction, score it hit or miss, then keep, change or stop; record what you learned as a decision that supersedes the old one. Before the next comparable decision, read the scored records.
13. Allocation: Keep one current allocation as a decision item with subject allocation:current: the frame used; for each outcome (a priority or bet) its share, ceiling (expected actual cost, or unknown), founder minutes, reviewBy, stop condition and strongest alternative (including stopping); and the weakest assumption. Never name agents, tiers or cadence; those are the orchestrator's. Supersede it only when a bet's status changed, a stop or reversal condition is met, a reviewBy date passed, direction changed or the founder asked; otherwise end with 'allocation stands' and write nothing. Its full frame and per-outcome lines go in the cited File.
14. Initiatives: Follow every founder idea through as an initiative: one decision item with subject initiative:<slug>, status OPEN and a reviewBy date, recording its key driver (why we are doing it) and the driver's size at intake. Never drop one silently; work around blockers under the blockers rule, because a blocker alone never stops an initiative. Stop one only for one of three reasons, recorded as a COMPLETE decision with subject initiative.stop:<slug> (never initiative:<slug>) that supersedes it, with stop {reason, evidenceRefs (1 to 8), driverComparison (at most 400 characters)}: unexpected_cost (a non-obvious cost or complication nobody anticipated; obvious costs count as already factored in); tradeoff_reversed (a trade-off review against the original key driver and its size shows a materially worse cost/return; time or effort alone never qualifies); one_sided_backlash (heavy, one-sided backlash weighed against actual behaviour such as engagement and customers; ordinary backlash does not count). An initiative with no follow-up by its reviewBy date becomes an attention item. Before any stop, run steps 3-8 on the stop itself and fill driverComparison from the intake driver and its size.

## Acceptance

- [ ] one decision recorded with frame, strongest feasible alternative, status quo where relevant, outside view, prediction and reviewBy; a binary choice is valid
- [ ] or 'allocation stands' with nothing written
- [ ] every stopped initiative has a stop reason, evidence and driverComparison

## Owner checks

- decisions looked up before asking
- prediction written before deciding
- red team never shown the recommendation
- decision item cites the full record File

## Result

### Artifact refs

- company:work:<workId>
- file:<fileId>
- **Transition:** the Executive records the decision; the orchestrator and agents take the next steps

**Company context:** `get_cady_context({"area": "ops/records", "task": "<what you are about to do, in one sentence>", "knownMethods": {"skill.company.executive_review": "00c158ce86dd0ded97661e784479a7e9ceaca48ddab90ee019c84e9f73db5c4e"}})`
