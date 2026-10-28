---
name: "cady-company-executive-review"
description: "Executive decision review. Use when: Make one company-level decision (a goal to start, reshape or stop, market, pricing, a bet) or review the open goals. Not for: Pushing work along, designing agents or doing delivery; routine decisions belong to the relevant function method, such as `cady-product-method`."
license: "MPL-2.0"
compatibility: "Requires Cady (app.cadyworks.com/mcp)"
metadata:
  cady-id: "skill.company.executive_review"
  version: "24786c98418ce7f0aaab"
  library: "f2ab4ebd3a461f29"
  function: "company"
---
# Executive decision review

**Company context:** `get_cady_context({"area": "ops/records", "task": "<what you are about to do, in one sentence>", "knownMethods": {"skill.company.executive_review": "24786c98418ce7f0aaab@f2ab4ebd3a461f29"}})`

Make one company-level decision (a goal to start, reshape or stop, market, pricing, a bet) or review the open goals.

**Not for:** Pushing work along, designing agents or doing delivery; routine decisions belong to the relevant function method, such as `cady-product-method`.

**Unit of work:** one decision, or one weekly review of the open goals. **Kind:** strategy. **Parallel:** no. **Can release:** no. 

## Inputs

### Evidence refs

- the decision item or escalation
- owner records the decision cites

### Sources

- read_cady company:direction
- the finance plan read (cash, burn, runway)
- get_company_work decisions {state: "current"}
- list_recent_changes since your last pass
- each function head's current situation call

## Procedure

1. Start each pass from the operating review of the open goals (the company review assessment: for each goal its intended condition, dated evidence, owner and on track, slipping or unknown), then pick one decision. Sources: a goal call reason, a goal slipping or meeting its stop condition; a new founder idea (a proposed goal, step 14); BLOCKED decision items waiting on you; escalations agents handed up; a direction change; material new evidence in list_recent_changes since your last pass. Take the one with the highest cost of delay. If none qualifies, end with 'goals stand' and write nothing.
2. Look it up first: get_company_work decisions {state: "current", subject} and the goal. If a current record exists, still holds (`cady-company-decision-check` step 1) and no trigger reopens it, use it and stop; never ask the person twice.
3. Frame it: the decision in one sentence, why now, the deadline or cost of delay, one-way or two-way door, and who decides (`cady-company-decision-check` steps 3 and 4). Pick the one frame that fits: expected value for repeatable bets, real options for reversible exploration, constraint analysis for throughput problems, pre-mortem for one-way doors. Proportion the work to the door: a reversible, low-cost (two-way door) decision is decided now with a stated default and reviewed at reviewBy in hindsight; steps 4-8 stay light, and the full pre-mortem and red team (step 8) are for consequential or one-way decisions only.
4. Compare the strongest feasible alternative and the status quo where relevant. A genuinely binary choice is valid; judge the choice and evidence, not the option count.
5. For a consequential or one-way decision, take the outside view first: the reference class and its base rate with a source, or 'none'.
6. Decide what you need to decide: use `cady-company-decision-questions` for evidence on each uncertainty that would change the choice. Check what owners already hold; request it as bounded work from the orchestrator with a deadline.
7. Write the prediction before deciding: for a one-way door a range with a confidence and a kill or reversal condition; for a two-way door the stated default and its reviewBy are enough.
8. Review before deciding: the strongest alternative and the weakest assumption. Only a consequential or one-way decision also gets a pre-mortem and a fresh red-team subagent (review tier) given the frame and evidence, never your recommendation.
9. Decide within your authority. An L1 choice you may make yourself only in notify mode and above the bar in `cady-company-decision-check` step 4; record it and the owner is told. Otherwise raise a BLOCKED decision item addressed to the owner with a recommendation and options; it reaches them as asksForYou.
10. Record it: the full record (steps 3-8, the decision and reviewBy) as a File through files.upload mode "begin" then "complete", and a decision item through submit_company_work_checkpoint with decision {kind: "decision", subject, layer (L1 for a company-level choice under `cady-company-decision-check`, L2 strategy with a keyAssumption, L3 execution), rationale, alternatives, reversal, reviewBy, authority, decidedBy} citing file:<fileId>. For your own choice use authority "agent" and omit decidedBy: Cady records it as your agent, never as the person (no source or quote). A person's choice needs source "chat" with their exact words in quote and decidedBy (or a verified source "grant" with grantId); Cady marks agent-recorded person decisions viaAgent. Keep the item's summary within its 2000-byte limit.
11. Hand next steps to the orchestrator or suitable existing agent as exact Projects tasks: headline, brief {doneWhen: 1-5 plain lines}, nextAction and evidence refs, with goalId, agentId, dependsOn or productId only when real. A goal is priority evidence, not task identity or effect authority; a direct one-off needs no invented goal, and a goal grants no effects. Read the reported result before judging outcomes, and correct a wrong one with corrects; never do the function work yourself.
12. At reviewBy, compare the outcome with the prediction, score it hit or miss, then keep, change or stop; record what you learned as a decision that supersedes the old one. Before the next comparable decision, read the scored records.
13. Goals: keep the company's priorities as open goal work items (`../../references/company-goals.md`), each with its reason, target, stop condition, expected cost and strongest alternative. Start, reshape or stop one only on a trigger from step 1; otherwise end with 'goals stand' and write nothing.
14. Founder ideas: record each as a proposed goal with its reason and the reason's size at intake, and never drop one silently; stop a goal only with a recorded reason, as `../../references/company-goals.md` says.

## Acceptance

- [ ] one decision recorded with frame, strongest feasible alternative, status quo where relevant and reviewBy, plus outside view and prediction for a one-way door; a binary choice is valid
- [ ] or 'goals stand' with nothing written
- [ ] every stopped goal has a stop reason, evidence and driverComparison

## Owner checks

- decisions looked up before asking
- prediction or stated default written before deciding
- red team never shown the recommendation
- decision item cites the full record File

## Result

### Artifact refs

- company:work:<workId>
- file:<fileId>
- **Transition:** the Executive records the decision; the orchestrator and agents take the next steps

## References
- Read [Company goals](../../references/company-goals.md) when you start, reshape or stop a goal, or an idea becomes one.
