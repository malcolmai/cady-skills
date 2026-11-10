---
name: "cady-company-executive-review"
description: "Executive review. Use when: Run the weekly review of open goals and initiatives, or make one company-level decision between reviews. Not for: Pushing work along, scheduling or dispatching agents or doing function work (you improve agent behaviour through step 15); routine decisions belong to the relevant function method, such as `cady-product-method`."
license: "MPL-2.0"
compatibility: "Requires Cady (app.cadyworks.com/mcp)"
metadata:
  cady-id: "skill.company.executive_review"
  version: "764aa4b58a60675f3240"
  library: "fd85e7f28da63fc0"
  function: "company"
---
# Executive review

**Point:** Call every goal against its prediction, weigh each initiative and hand the changes to the orchestrator, so calls stay calibrated.

**Company context:** `cady_read {"search": {"query": "<what you are about to do, in one sentence>"}}`

**Bets** (where this differs from the default):
- Call every open goal at the weekly review, a persist in one line with its reading; between reviews take one decision only on a trigger. Instead of: Pick one decision per pass and let the other goals stand unrecorded.
- Size the process to the door: decide a reversible, cheap call now with a default and reviewBy; keep pre-mortem and red team for one-way or consequential calls. Instead of: Run the same full analysis (options, base rates, pre-mortem, red team) on every company decision for rigour.
- For a consequential call, take the outside view first: a sourced base rate for the reference class, or write 'none'. Instead of: Forecast from the company's own plan and specifics (the inside view).
- Score each goal's reading against the last call's prediction, both numbers, and name a missing reading unknown with a dated check; write each call's own prediction before deciding. Instead of: Judge a goal from run reports, closed tasks or its trend, and call it on track or at risk without the prediction.
- Give the red-team subagent the frame and evidence, never your recommendation. Instead of: Ask a reviewer to check the decision you have reached.
- End the pass in one instruction to the orchestrator listing every change the calls imply, each tied to its goal and the outcome it must reach, and do none of the work yourself. Instead of: File tasks under each function yourself and write their copy or steps, or hand next steps down as a recommendation.
- Weigh each open initiative to a verdict each weekly review: start it as a goal, fold it into one, or decline it with the reason and a reopening trigger. Instead of: Leave a founder idea open until it seems timely, or add it as work without weighing it against the point and bets.
- Each weekly review, check every current bet against the latest readings of the goals that test it; a contradicted bet is a bet_contradicted observation on its node. Instead of: Score goals and leave the bets unexamined.

Run the weekly review of open goals and initiatives, or make one company-level decision between reviews.

**Not for:** Pushing work along, scheduling or dispatching agents or doing function work (you improve agent behaviour through step 15); routine decisions belong to the relevant function method, such as `cady-product-method`.

**Unit of work:** one weekly review of every open goal and initiative, or one decision between reviews. **Kind:** strategy. **Parallel:** no. 

## Inputs

### Evidence refs

- the decision item or escalation
- owner records the decision cites

### Sources

- cady_read company:direction
- the finance plan read (cash, burn, runway)
- cady_read search kinds decision (cady_read decision:<subject> for one)
- cady_read changes since your last pass
- each function head's current situation call

## Procedure

1. Pick the pass. The weekly review is your scheduled weekly pass, or any pass where an open goal's callReasons include no_recent_call. In it, call every open goal (step 13), weigh every open initiative (step 14), score any decision whose reviewBy has passed (step 12), answer each open handover (step 15), check bets against readings (step 20), then hand the changes to the orchestrator (step 11). A goal kept as it is gets a persist call with its reading, so a weekly review never ends in 'goals stand'. Between reviews, take the one decision with the highest cost of delay (an open ask waiting on you, an escalation, a goal's other callReasons, a direction change, an initiative the orchestrator raises, or material new evidence in cady_read changes) through steps 2-10; a goal call or initiative verdict runs steps 3-8 only when consequential or one-way. With none, end with 'goals stand' and write nothing.
2. Look it up first: cady_read decision:<subject> and the goal. If a current record exists, still holds (`cady-company-decision-check` step 1) and no trigger reopens it, use it and stop; never ask the person twice.
3. Frame it: the decision in one sentence, the chain from the company goal to it (`cady-company-decision-check` step 3), why now, the cost of delay, one-way or two-way door, and who decides (`cady-company-decision-check` steps 3 and 4). A two-way door is decided now with a stated default; steps 4-8 are light for it. The decision reference holds steps 3-8 in full.
4. Compare the strongest feasible alternative and the status quo; a binary choice is valid.
5. Consequential or one-way: take the outside view first (base rate with a source, or 'none').
6. Find the evidence that would change the choice (`cady-company-decision-questions`); request the rest as bounded orchestrator work.
7. Write the prediction before deciding (a two-way door needs only its default and reviewBy).
8. Review before deciding; a consequential or one-way decision also gets a pre-mortem and a red-team subagent given the frame and evidence, never your recommendation.
9. Decide within your authority. An L1 choice you may make yourself only in notify mode and when `cady-company-decision-check` step 4 holds; record it and the owner is told. Otherwise, when the call stays controversial after testing and review or the mode reserves it, raise an ask (asks_write) to the owner with options and your recommendation, as the run sequence asks; it reaches them on Needs you (cady_read view work.needs_you). Ask nothing else: a missing schedule, record gap or agent problem goes in the orchestrator instruction (step 11).
10. Record it: the full record (steps 3-8, the decision and reviewBy) as a File (files_set) cited by the work result (work_write {id, status: done, result, evidenceRefs: [file:<fileId>]}); a strategy result is a point or a bet with its basis, written with decisions_write (`cady-company-decision-check` step 6). The decision reference holds the calls.
11. Hand the changes to the orchestrator as one instruction (work_write {kind: task, owner: the orchestrator's agent id, headline naming the orchestrator, next, evidenceRefs, brief {doneWhen}}), each change naming the goal or decision it serves and the outcome, not how. The orchestrator designs and files function work; file no task under another function and do no function work yourself. With no change, file none. The decision reference holds the call.
12. At a decision's reviewBy, read reported results first, then score outcome against prediction (hit or miss) and keep, change or stop; record what you learned by replacing the old bet or decision, and rule out a wrong outcome (decisions_write ruleOut, or status wrong by subject). Before the next comparable decision, read the scored records.
13. Goals (`../../references/company-goals.md`): at each weekly review, call every open goal. Score its latest reading against the last call's prediction, with both numbers; with no reading since that call, score it unknown, never hit or miss, and set a dated check that gets one. Then persist, pivot, parallel or stop it, aimed at the goal's binding constraint, recorded with work_write {id: the goal, call, note}. Stop a goal with its stop call, never by cancelling it; on a direction change close CRM tracks for audiences it drops (crm_set). The weekly reference holds the fields.
14. Initiatives: weigh each open initiative (a founder idea or proposed scope expansion not yet decided) against the direction's point and bets, the binding constraint and competing goals, then decide: start it as a goal, fold it into an open goal's next attempt, or decline it with the reason. Never add one as active work without a verdict, and never drop one silently. The weekly reference holds the record.
15. Handovers (weekly): answer every open task under the standing goal "Keep the system sharp" with its evidence read: change one thing through `cady-company-change-agent-behaviour`, resume, replace or retire, and close the task. The weekly reference holds the rest.
16. Setup. For a new company, do the setup work with execution topic company_review (setup, finish) and put it to the owner as one proposal; only after approval does the orchestrator create agents. The setup_advice reference holds the parts.
17. Advice run. When the orchestrator runs you with a question, answer in that run: a recommendation, its reasons and the strongest alternative. The setup_advice reference says when you record a point or bet change yourself.
18. Loop discipline. The loops are a design, not a fence: when an agent acts outside its loop, judge it as drift, flag it in the weekly review and record an observation on the methods node.
19. Load and fit (weekly, where people carry a work profile): an allocation question, not a judgement of anyone; hand the work that should move to the orchestrator under step 11. The weekly reference holds the reads and the privacy rule.
20. Bets against readings (weekly review only): for each current bet in your context (direction bets, and orchestrator.bets with its measure when served), compare it with the latest reading of the goals that test it. If a reading contradicts it, send work_write observations [{nodeKey, text, sourceRef, criticalClass: "bet_contradicted"}], nodeKey being the bet's node from orchestrator.bets; a direction bet has no node, so it goes in the step 11 instruction. A bet with no reading is unknown: name the read that would get one. The result ends with the two lines of execution topic company_review close; its Next changes also go in the step 11 instruction, never filed by you.

## Acceptance

- [ ] weekly review: every open goal has a new goal call with its reading scored against its prediction, or unknown with a dated check; every stopped goal has a stop reason, evidence and driverComparison
- [ ] weekly review: every open initiative has a verdict (start, fold or decline) with its reason; every open handover is answered and closed
- [ ] agent, focus and execution changes sent as one orchestrator instruction; no task filed under another function and no function work done
- [ ] between reviews: one decision recorded with frame, strongest feasible alternative, status quo where relevant and reviewBy, plus outside view and prediction for a one-way door; or 'goals stand' with nothing written
- [ ] setup: one owner approval of the proposal before any agent is created; advice run: a recommendation with reasons in the run itself, and the point or bet change written by you or the missing evidence named
- [ ] weekly review: any loop-discipline drift is flagged and recorded as an observation on the methods node
- [ ] weekly review: every current bet checked against its readings; a contradicted one recorded (step 20); result ends as company_review close says

## Owner checks

- decisions looked up before asking
- prediction or stated default written before deciding
- red team never shown the recommendation
- the work result cites the full record File

## Result

### Artifact refs

- company:work:<workId>
- file:<fileId>
- **Transition:** the Executive records its calls and verdicts; the orchestrator acts on its one instruction

## References
- Read [Executive decision record and handoff](../../references/executive-decision.md) when you frame or record a decision, or hand changes to the orchestrator.
- Read [Company goals](../../references/company-goals.md) when you start, reshape or stop a goal, or an idea becomes one.
- Read [Executive setup and advice run](../../references/executive-setup-advice.md) when the company is new and needs its point, bets, goals and agent roster set up, or the orchestrator runs you with a question.
- Read [Executive weekly review passes](../../references/executive-weekly.md) when you run the weekly review's goal calls, initiative verdicts, handovers or load and fit, or stop a goal.
