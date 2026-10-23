---
name: "cady-company-executive-review"
description: "Executive decision review. Use when: Make one big company decision (market, direction, pricing, a bet to start or stop) or review where effort goes. Not for: Pushing work along, designing agents or doing delivery; routine decisions belong to the relevant function method, such as `cady-product-method`."
license: "MPL-2.0"
compatibility: "Requires Cady (app.cadyworks.com/mcp)"
metadata:
  cady-id: "skill.company.executive_review"
  version: "c59604dec648151738c907b63a36ae7b3fae7c6ad9f11427f13c101c9983a9b8"
  library: "62ae69a6f667e4c1"
  function: "company"
---
# Executive decision review

**Company context:** `get_cady_context({"area": "ops/records", "task": "<what you are about to do, in one sentence>", "knownMethods": {"skill.company.executive_review": "c59604dec648151738c907b63a36ae7b3fae7c6ad9f11427f13c101c9983a9b8"}})`

Make one big company decision (market, direction, pricing, a bet to start or stop) or review where effort goes.

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
13. Allocation: keep one current allocation as a decision item with subject allocation:current, superseded only on a trigger (`../../references/allocation-and-initiatives.md`); otherwise end with 'allocation stands' and write nothing.
14. Initiatives: follow every founder idea as an initiative:<slug> decision item and stop one only for a recorded reason, as `../../references/allocation-and-initiatives.md` says.

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

## References
- [Allocation and initiatives](../../references/allocation-and-initiatives.md)
