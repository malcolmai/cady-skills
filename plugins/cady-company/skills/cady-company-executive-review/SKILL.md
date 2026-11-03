---
name: "cady-company-executive-review"
description: "Executive decision review. Use when: Make one company-level decision (a goal to start, reshape or stop, market, pricing, a bet) or review the open goals. Not for: Pushing work along, designing agents or doing delivery; routine decisions belong to the relevant function method, such as `cady-product-method`."
license: "MPL-2.0"
compatibility: "Requires Cady (app.cadyworks.com/mcp)"
metadata:
  cady-id: "skill.company.executive_review"
  version: "63a4b1dfa28d34540095"
  library: "b14f38171b325388"
  function: "company"
---
# Executive decision review

**Point:** Make one company decision well, sized to its door, and predict its outcome so the Executive's calls get calibrated.

**Company context:** `context_read({"area": "ops/records", "task": "<what you are about to do, in one sentence>", "knownMethods": {"skill.company.executive_review": "63a4b1dfa28d34540095@b14f38171b325388"}})`

**Bets** (where this differs from the default):
- Size the process to the door: decide a reversible, cheap call now with a default and reviewBy; keep pre-mortem and red team for one-way or consequential calls. Instead of: Run the same full analysis (options, base rates, pre-mortem, red team) on every company decision for rigour.
- For a consequential call, take the outside view first: a sourced base rate for the reference class, or write 'none'. Instead of: Forecast from the company's own plan and specifics (the inside view).
- Write the prediction before deciding and score it hit or miss at reviewBy; read the scored records before the next comparable decision. Instead of: Record the decision and its rationale, and judge it later by whether things turned out well.
- Give the red-team subagent the frame and evidence, never your recommendation. Instead of: Ask a reviewer to check the decision you have reached.
- End every decision in exact tasks for the owning function, with doneWhen lines, and do none of the work yourself. Instead of: Hand the decision down as a recommendation and let the team work out next steps, or start the first step yourself.

Make one company-level decision (a goal to start, reshape or stop, market, pricing, a bet) or review the open goals.

**Not for:** Pushing work along, designing agents or doing delivery; routine decisions belong to the relevant function method, such as `cady-product-method`.

**Unit of work:** one decision, or one weekly review of the open goals. **Kind:** strategy. **Parallel:** no. **Can release:** no. 

## Inputs

### Evidence refs

- the decision item or escalation
- owner records the decision cites

### Sources

- records_read company:direction
- the finance plan read (cash, burn, runway)
- work_read decisions {state: "current"}
- list_recent_changes since your last pass
- each function head's current situation call

## Procedure

1. Start each pass from the operating review of the open goals (the company review assessment: for each goal its intended condition, dated evidence, owner and on track, slipping or unknown), then pick one decision. Sources: a goal call reason, a goal slipping or meeting its stop condition; a new founder idea (a proposed goal, step 14); BLOCKED decision items waiting on you; escalations agents handed up; a direction change; material new evidence in list_recent_changes since your last pass. Take the one with the highest cost of delay. If none qualifies, end with 'goals stand' and write nothing.
2. Look it up first: work_read decisions {state: "current", subject} and the goal. If a current record exists, still holds (`cady-company-decision-check` step 1) and no trigger reopens it, use it and stop; never ask the person twice.
3. Frame it: the decision in one sentence, the chain from the company goal to it (`cady-company-decision-check` step 3), why now, the deadline or cost of delay, one-way or two-way door, and who decides (`cady-company-decision-check` steps 3 and 4). Pick the one frame that fits: expected value for repeatable bets, real options for reversible exploration, constraint analysis for throughput problems, pre-mortem for one-way doors. Proportion the work to the door: a reversible, low-cost (two-way door) decision is decided now with a stated default and reviewed at reviewBy in hindsight; steps 4-8 stay light, and the full pre-mortem and red team (step 8) are for consequential or one-way decisions only.
4. Compare the strongest feasible alternative and the status quo where relevant. A genuinely binary choice is valid; judge the choice and evidence, not the option count.
5. For a consequential or one-way decision, take the outside view first: the reference class and its base rate with a source, or 'none'.
6. Decide what you need to decide: use `cady-company-decision-questions` for evidence on each uncertainty that would change the choice. Check what owners already hold; request it as bounded work from the orchestrator with a deadline.
7. Write the prediction before deciding: for a one-way door a range with a confidence and a kill or reversal condition; for a two-way door the stated default and its reviewBy are enough.
8. Review before deciding: the strongest alternative and the weakest assumption, re-read against current state when it is over a week old. Only a consequential or one-way decision also gets a pre-mortem and a fresh red-team subagent (review tier) given the frame and evidence, never your recommendation.
9. Decide within your authority. An L1 choice you may make yourself only in notify mode and when `cady-company-decision-check` step 4 holds; record it and the owner is told. Otherwise, when the call stays controversial after testing and review or the mode reserves it, raise a BLOCKED decision item addressed to the owner with a recommendation and options; it reaches them as asksForYou.
10. Record it: the full record (steps 3-8, the decision and reviewBy) as a File through files_update or files_create mode "begin" then "complete", and a decision item through work_create with decision {kind: "decision", subject, layer (L1 for a company-level choice under `cady-company-decision-check`, L2 strategy with a keyAssumption, L3 execution), rationale, alternatives, reversal, reviewBy, authority, decidedBy} citing file:<fileId>. For your own choice use authority "agent" and omit decidedBy: Cady records it as your agent, never as the person (no source or quote). A person's choice needs source "chat" with their exact words in quote and decidedBy (or a verified source "grant" with grantId); Cady marks agent-recorded person decisions viaAgent. Keep the item's summary within its 2000-byte limit.
11. File next steps as exact Projects tasks, each naming its owning function by its methodId, that function's role card or task skill (the orchestrator dispatches): headline, brief {doneWhen: 1-5 plain lines}, nextAction and evidence refs, with goalId, dependsOn or productId only when real. A goal is priority evidence, not task identity or effect authority; a direct one-off needs no invented goal, and a goal grants no effects. Read the reported result before judging outcomes, and correct a wrong one with corrects; never do the function work yourself.
12. At reviewBy, compare the outcome with the prediction, score it hit or miss, then keep, change or stop; record what you learned as a decision that supersedes the old one. Before the next comparable decision, read the scored records.
13. Goals: keep the company's priorities as open goal work items (`../../references/company-goals.md`), each with its reason, target, stop condition, expected cost and strongest alternative. Start, reshape or stop one only on a trigger from step 1; otherwise end with 'goals stand' and write nothing. On a direction change, make each open goal's call; supersede or withdraw decisions that assumed the old offer, citing the new direction; close CRM tracks for audiences the new direction drops (crm_tracks_set no_longer_relevant).
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
