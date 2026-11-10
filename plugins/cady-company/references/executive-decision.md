# Executive decision record and handoff

**Point:** Frame a decision to its door, record it whole and hand changes over once, so the orchestrator acts.

- **Frames:** 3. Frame it: the decision in one sentence, the chain from the company goal to it (`cady-company-decision-check` step 3), why now, the deadline or cost of delay, one-way or two-way door, and who decides (`cady-company-decision-check` steps 3 and 4). Pick the one frame that fits: expected value for repeatable bets, real options for reversible exploration, constraint analysis for throughput problems, pre-mortem for one-way doors. Proportion the work to the door: a reversible, low-cost (two-way door) decision is decided now with a stated default and reviewed at reviewBy in hindsight; steps 4-8 stay light, and the full pre-mortem and red team (step 8) are for consequential or one-way decisions only.

4. Compare the strongest feasible alternative and the status quo where relevant. A genuinely binary choice is valid; judge the choice and evidence, not the option count.

5. For a consequential or one-way decision, take the outside view first: the reference class and its base rate with a source, or 'none'.

6. Find the evidence that would change the choice: use `cady-company-decision-questions` for each such uncertainty. Check what owners already hold; request the rest as bounded work from the orchestrator with a deadline.

7. Write the prediction before deciding: for a one-way door a range with a confidence and a kill or reversal condition; for a two-way door the stated default and its reviewBy are enough.

8. Review before deciding: the strongest alternative and the weakest assumption, re-read against current state when it is over a week old. Only a consequential or one-way decision also gets a pre-mortem and a fresh red-team subagent (review tier) given the frame and evidence, never your recommendation.
- **Recording:** Record it: the full record (steps 3-8, the decision and reviewBy) as a File through files_set mode begin_upload then files_set mode complete_upload, and the work result citing file:<fileId> (work_write {id, status: done, result, evidenceRefs}); a strategy result is also a point or a bet with its basis, written with tree_write (`cady-company-decision-check` step 6). For your own choice use authority "agent": Cady records it as your agent, never as the person. A person's choice needs authority manager (admin for an Admin) with their exact words in quote. Keep the result short and the File full.
- **Handoff:** Hand the changes to the orchestrator as one instruction: one task through work_write {kind: task, owner: the orchestrator's agent id, headline naming the orchestrator, next (what it does first), evidenceRefs (the goal calls and decisions behind the changes), brief {doneWhen: one line per change}}. List every change the pass implies: an agent to re-aim at its goal's binding constraint, pause or point elsewhere after its goal stops, a capability to request, work to file under its owning function, each naming the goal or decision it serves and the outcome it must reach, not how (no copy, scripts or setup steps). The orchestrator designs, dispatches and files function work; file no task under another function and do no function work yourself. With no change, file none.
