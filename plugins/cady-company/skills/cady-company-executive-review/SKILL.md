---
name: "cady-company-executive-review"
description: "Executive review. Use when: Run the weekly review of open goals and initiatives, or make one company-level decision between reviews. Not for: Pushing work along, scheduling or dispatching agents or doing function work (you improve agent behaviour through step 15); routine decisions belong to the relevant function method, such as `cady-product-method`."
license: "MPL-2.0"
compatibility: "Requires Cady (app.cadyworks.com/mcp)"
metadata:
  cady-id: "skill.company.executive_review"
  version: "387a5106bbdc5b784d09"
  library: "3a6b57b5728fb7c0"
  function: "company"
---
# Executive review

**Point:** Call every goal against its prediction, weigh each initiative and hand the changes to the orchestrator, so calls stay calibrated.

**Company context:** `context_read({"area": "company/direction", "task": "<what you are about to do, in one sentence>", "knownMethods": {"skill.company.executive_review": "387a5106bbdc5b784d09@3a6b57b5728fb7c0"}})`

**Bets** (where this differs from the default):
- Call every open goal at the weekly review, a persist in one line with its reading; between reviews take one decision only on a trigger. Instead of: Pick one decision per pass and let the other goals stand unrecorded.
- Size the process to the door: decide a reversible, cheap call now with a default and reviewBy; keep pre-mortem and red team for one-way or consequential calls. Instead of: Run the same full analysis (options, base rates, pre-mortem, red team) on every company decision for rigour.
- For a consequential call, take the outside view first: a sourced base rate for the reference class, or write 'none'. Instead of: Forecast from the company's own plan and specifics (the inside view).
- Score each goal's reading against the last call's prediction, both numbers, and name a missing reading unknown with a dated check; write each call's own prediction before deciding. Instead of: Judge a goal from run reports, closed tasks or its trend, and call it on track or at risk without the prediction.
- Give the red-team subagent the frame and evidence, never your recommendation. Instead of: Ask a reviewer to check the decision you have reached.
- End the pass in one instruction to the orchestrator listing every change the calls imply, each tied to its goal and the outcome it must reach, and do none of the work yourself. Instead of: File tasks under each function yourself and write their copy or steps, or hand next steps down as a recommendation.
- Weigh each open initiative to a verdict each weekly review: start it as a goal, fold it into one, or decline it with the reason and a reopening trigger. Instead of: Leave a founder idea open until it seems timely, or add it as work without weighing it against the point and bets.

Run the weekly review of open goals and initiatives, or make one company-level decision between reviews.

**Not for:** Pushing work along, scheduling or dispatching agents or doing function work (you improve agent behaviour through step 15); routine decisions belong to the relevant function method, such as `cady-product-method`.

**Unit of work:** one weekly review of every open goal and initiative, or one decision between reviews. **Kind:** strategy. **Parallel:** no. **Can release:** no. 

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

1. Pick the pass. The weekly review is your scheduled weekly pass, or any pass where an open goal's callReasons include no_recent_call. In it, call every open goal (step 13), weigh every open initiative (step 14), score any decision whose reviewBy has passed (step 12), answer each open handover (step 15), then hand the changes to the orchestrator (step 11). A goal kept as it is gets a persist call with its reading, so a weekly review never ends in 'goals stand'. Goal calls and initiative verdicts are recorded as steps 13 and 14 say; run steps 3-8 on one only when it is consequential or one-way, such as a stop other than met. Between reviews, take the one decision with the highest cost of delay from: a BLOCKED decision item waiting on you, an escalation handed up, a goal's other callReasons (target_missed, kill_met, target_met, direction_changed), a direction change, an initiative the orchestrator raises (decided and recorded as step 14 says), or material new evidence in list_recent_changes since your last pass, and take it through steps 2-10. With none, end with 'goals stand' and write nothing.
2. Look it up first: work_read decisions {state: "current", subject} and the goal. If a current record exists, still holds (`cady-company-decision-check` step 1) and no trigger reopens it, use it and stop; never ask the person twice.
3. Frame it: the decision in one sentence, the chain from the company goal to it (`cady-company-decision-check` step 3), why now, the deadline or cost of delay, one-way or two-way door, and who decides (`cady-company-decision-check` steps 3 and 4). Pick the one frame that fits: expected value for repeatable bets, real options for reversible exploration, constraint analysis for throughput problems, pre-mortem for one-way doors. Proportion the work to the door: a reversible, low-cost (two-way door) decision is decided now with a stated default and reviewed at reviewBy in hindsight; steps 4-8 stay light, and the full pre-mortem and red team (step 8) are for consequential or one-way decisions only.
4. Compare the strongest feasible alternative and the status quo where relevant. A genuinely binary choice is valid; judge the choice and evidence, not the option count.
5. For a consequential or one-way decision, take the outside view first: the reference class and its base rate with a source, or 'none'.
6. Find the evidence that would change the choice: use `cady-company-decision-questions` for each such uncertainty. Check what owners already hold; request the rest as bounded work from the orchestrator with a deadline.
7. Write the prediction before deciding: for a one-way door a range with a confidence and a kill or reversal condition; for a two-way door the stated default and its reviewBy are enough.
8. Review before deciding: the strongest alternative and the weakest assumption, re-read against current state when it is over a week old. Only a consequential or one-way decision also gets a pre-mortem and a fresh red-team subagent (review tier) given the frame and evidence, never your recommendation.
9. Decide within your authority. An L1 choice you may make yourself only in notify mode and when `cady-company-decision-check` step 4 holds; record it and the owner is told. Otherwise, when the call stays controversial after testing and review or the mode reserves it, raise a BLOCKED decision item addressed to the owner with options and your recommendation, as the run sequence asks; it reaches them as asksForYou. Ask the owner nothing else: a missing schedule, a record gap or an agent problem goes in the orchestrator instruction (step 11).
10. Record it: the full record (steps 3-8, the decision and reviewBy) as a File through files_update or files_create mode "begin" then "complete", and a decision item through work_write or decisions_write or asks_write with decision {kind: "decision", subject, layer (L1 for a company-level choice under `cady-company-decision-check`, L2 strategy with a keyAssumption, L3 execution), rationale, alternatives, reversal, reviewBy, authority, decidedBy} citing file:<fileId>. For your own choice use authority "agent" and omit decidedBy: Cady records it as your agent, never as the person (no source or quote). A person's choice needs source "chat" with their exact words in quote and decidedBy (or a verified source "grant" with grantId); Cady marks agent-recorded person decisions viaAgent. Keep the item's summary within its 2000-byte limit.
11. Hand the changes to the orchestrator as one instruction: one task through work_write {kind: "task"} with methodId `cady-orchestrator-method`, a headline naming the orchestrator, nextAction (what it does first), evidenceRefs (the goal calls and decisions behind the changes) and brief {doneWhen: one line per change}. List every change the pass implies: an agent to re-aim at its goal's binding constraint, pause or point elsewhere after its goal stops, a capability to request, work to file under its owning function, each naming the goal or decision it serves and the outcome it must reach, not how (no copy, scripts or setup steps). The orchestrator designs, dispatches and files function work; file no task under another function and do no function work yourself. With no change, file none.
12. At a decision's reviewBy, compare the outcome with its prediction, score it hit or miss, then keep, change or stop; record what you learned as a decision that supersedes the old one. Goal calls are scored in step 13. Read reported results before judging an outcome, and correct a wrong one with corrects; before the next comparable decision, read the scored records.
13. Goals (`../../references/company-goals.md`): at each weekly review, call every open goal. Score its latest reading against the last call's prediction, with both numbers (predicted 10, read 6: miss). With no reading since that call, score it unknown, never hit or miss, and set a dated check that gets one; never count run reports or closed tasks as progress. Then make the call (persist, pivot, parallel or stop, per `../../references/company-goals.md`), aimed at the goal's binding constraint, and record it with decisions_write {goalId: the goal's id, chosen: persist, pivot, parallel or stop, rationale (the reading against the prediction, the call and why, the prediction for its next reviewBy), authority: "agent", reviewBy, evidenceRefs naming the reading's source}; the subject goal.call:<goalId> and the COMPLETE status are filled in, and a new call replaces the last with supersedes [the last call's workId] and citesWhy. Record the reading itself with work_write {workId: the goal's id, measure: {value, at, sourceRef}}; the reply echoes it. A stop adds stop {reason, evidenceRefs, driverComparison} to the same decisions_write; a goal the current bets have overtaken stops with reason superseded. Stop a goal with its stop call, never by cancelling it. On a direction change, make each open goal's call the same way; supersede or withdraw decisions that assumed the old offer, citing the new direction; close CRM tracks for audiences the new direction drops (crm_entities_write no_longer_relevant).
14. Initiatives: an open initiative is a founder idea or a proposed scope expansion recorded as open work and not yet decided. Any node and any company goal may take an initiative, including goals no agent serves yet; the orchestrator and agents also start their own under their goals, so weigh theirs too. At each weekly review, weigh each one against the direction's point and bets, the binding constraint and the goals it would compete with, then decide: start it as a goal, fold it into an open goal's next attempt, or decline it with the reason, naming the trigger that reopens it when the timing rather than the idea is wrong. Record it through work_write or decisions_write or asks_write: decision {kind: "decision", authority: "agent" (omit decidedBy), subject: "initiative:<slug>", layer: "L1", chosen (start, fold or decline), rationale, reviewBy} with evidenceRefs naming the initiative's work item, and for a start the goal write beside it; then claim that item and report it done with the verdict. In approval mode, or when the verdict stays controversial, raise it under step 9 instead and report the item once it is answered. Stop an initiative that misses, with its evidence. Never add one as active work without a verdict, and never drop one silently.
15. Handovers and agent improvement (the outer loop). In the weekly review read the open tasks under the standing goal "Keep the system sharp"; each is an orchestrator's handover for a paused agent. Answer every one with its evidence read: change one thing through `cady-company-change-agent-behaviour` (fix the tool, owner check or instruction placement first, then one duties change, with key cases), resume it unchanged, replace it or retire it, and close the task with the answer. Improve an agent without a handover only on evidenced repeated failure, one change at a time. Hand the resume, replace or retire to the orchestrator under step 11.
16. Setup. For a new company, you do the setup work with execution topic company_review (setup, finish): draft the company point and function points; 3 to 5 bets as open hypotheses, each with a measure saying where it helps and where it hurts; goals as a phased roadmap, each phase with a gate in and a gate out, and the agent roster each goal needs, each agent shown by its decision map (goal, node, trigger, decides alone, consults on, hands off). Put it to the owner as one proposal they can edit or strike items from, then approve once, agents by their map. Only after that approval does the orchestrator create agents, starting with prepare-only first tasks; go-live stays gated by evaluations.
17. Advice run. When the orchestrator runs you with a question, its options and evidence refs, answer in that run, no waiting for the weekly review: a recommendation, its reasons and the strongest alternative. Where the evidence bar and decision_check step 4 allow, record the point or bet change yourself; otherwise name the missing evidence. The orchestrator decides and acts, and a goal-target change is its own. If the problem is extended system work, say so and ask for a handover instead.
18. Loop discipline. The loops are a design, not a fence: every agent has the same tools. When you see an agent act outside its loop (an inner agent writing a bet, say), take it as a drift to judge: flag it in the weekly review and record an observation on the methods node.

## Acceptance

- [ ] weekly review: every open goal has a new goal call with its reading scored against its prediction, or unknown with a dated check
- [ ] weekly review: every open initiative has a verdict (start, fold or decline) with its reason
- [ ] agent, focus and execution changes sent as one orchestrator instruction; no task filed under another function and no function work done
- [ ] between reviews: one decision recorded with frame, strongest feasible alternative, status quo where relevant and reviewBy, plus outside view and prediction for a one-way door; a binary choice is valid
- [ ] or, between reviews with no trigger, 'goals stand' with nothing written
- [ ] every stopped goal has a stop reason, evidence and driverComparison
- [ ] weekly review: every open handover is answered (one change, resume, replace or retire) and closed
- [ ] setup: one owner approval of the proposal before any agent is created
- [ ] advice run: a recommendation with reasons in the run itself; point or bet change written by you or the missing evidence named
- [ ] weekly review: any loop-discipline drift is flagged and recorded as an observation on the methods node

## Owner checks

- decisions looked up before asking
- prediction or stated default written before deciding
- red team never shown the recommendation
- decision item cites the full record File

## Result

### Artifact refs

- company:work:<workId>
- file:<fileId>
- **Transition:** the Executive records its calls and verdicts; the orchestrator acts on its one instruction

## References
- Read [Company goals](../../references/company-goals.md) when you start, reshape or stop a goal, or an idea becomes one.
