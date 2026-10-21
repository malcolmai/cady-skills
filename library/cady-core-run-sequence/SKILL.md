---
name: "cady-core-run-sequence"
description: "Agent run sequence. Run one ordered piece of company work from reconciliation through result. Use when: the user wants a task carried through to a recorded outcome. Not for: setting up recurring work."
license: "MPL-2.0"
compatibility: "Requires Cady (app.cadyworks.com/mcp)"
metadata:
  cady-id: "execution.topic.run_sequence"
  version: "e98b6a82d47dd8344387e309d2a6b5c9061e224f94e7184a6765415f158ec29f"
  library: "f4e8ca47d12d38e8"
  function: "core"
---
# Agent run sequence

**Company context:** `get_cady_context({"area": "ops/records", "task": "<what you are about to do, in one sentence>", "knownMethods": {"execution.topic.run_sequence": "e98b6a82d47dd8344387e309d2a6b5c9061e224f94e7184a6765415f158ec29f"}})`

Run one ordered piece of company work from reconciliation through result. Use when: the user wants a task carried through to a recorded outcome. Not for: setting up recurring work.

## Run sequence

- **Applies to:** Every Cady agent run, every role. Your role card (if any) and skills say what to work on; this says the order.
- **Previous run check:** Only when the owner has opted this host in (a current decision with subject host:previous_run_check): on Codex, before step 1, if the newest rollout in ~/.codex/sessions other than this session's ended on a usage limit or auth error, call report_host_event {event: "previous_run", reason: "rate_limit" or "authentication_failed", resetsAt: its resets_at as an ISO time, session: file name} (call_cady_tool if unlisted); never copy its text.

### Steps

- 1. Read get_cady_context with your agentId, the area you are working in (for example gtm/outreach or product/<id>/context) and a task sentence. Stop if you are paused or retired. Pass agentId on every Cady call that accepts it. The read returns the decisions routed to that area's action classes; read_cady search covers the rest, its method, live work and refs; read any ref with read_cady. Record new decisions with the returned writeAs.appliesTo.
- 2. Reconcile first. For each reconcileWorkIds item: settle unresolved effects with their owner and call transition_company_work action='report_effect_reconciliation'; an expired claim is no longer held: claim again (step 4) or action='recover' with a recoveryNote; a pending result you own within your limits takes action='accept_result', otherwise leave it for the named acceptor. Start no new effect on an item until it is clear.
- 3. Choose: resumeWorkIds first, then openWorkIds whose dueDate has passed or is empty, in the order served. Also check due standing duties from your current assignment and hostReview; an empty work queue does not cancel those duties. Create owner work only where needed, with brief {acceptance: 1-5 checks, finishLine}, and claim before controlled work. A finish line names the deliverable, its size rule and what done is; a sample is labelled one and never meets a request for the deliverable; a budget, time-box or access stop closes as partial (delivered N of T). A check is one fact a stranger can verify, kind mechanical, readback (re-read the record) or judgement (a reviewer's call); at least one must. Checks freeze at claim; only the claim holder changes them, with action='checkpoint', brief and criteriaChangeReason. Ordinary reads, monitoring and preparation do not require a new task by default. If neither work nor a standing duty is due, go to step 6 with outcome no_work.
- 4. Claim one item: transition_company_work action='claim' (omit attemptId and claimProof; the server fills and reuses them on your connection; a claim on BLOCKED work unblocks it). Stop on a live claim conflict. A claim lasts 30 minutes (control.claim.expiresAt on the work item); renew it with action='renew' before it expires.
- 5. Do the work. Read get_cady_context {agentId, workId: id} for the skill and records. Stay within scope; resolve lane overlap before go_live. Finish every step short of a human boundary yourself and checkpoint at natural boundaries. Near the budget (about four-fifths spent or a host warning), stop starting steps and close with the result or shortfall. Ask only what blocks and what no current record answers; otherwise choose a sensible default and proceed. When a missing owner fact blocks the next step, ask now with submit_company_work_checkpoint {ask} and keep working on the rest. Put every ask you can make now in one packet: who acts, where and what, options with your recommendation, owner minutes. An open hypothesis is the working assumption: treat it as answered, build on it, cite it, and propose a change only with new evidence. decisions.omissions means the list is incomplete; a capped or empty read is not proof of absence. Record a chat approval or correction in the person's exact words (source chat, quote, decidedBy "me", status COMPLETE) and act on it; quote an OPEN one from pendingConfirmations back once. Record each decision once and supersede it to change it. A statement is a one-sentence title; reasons go in rationale and sources in evidenceRefs.
- 6. End every agent run with one close_company_work call, made last. With nothing to record, call it as {agentId, run: {outcome: "no_work"}}. Put each item you worked in items; Cady reports or accepts it as your status allows. The close tool's own description lists the parts and pre-close checks; follow it. The result must be the requested usable deliverable or a verified external effect; research, planning, preparation and a finished run are progress unless that artifact itself was requested; a send is proven by its owner receipt. Until your status is live, prepare only and never release or send; manage_agents covers going live. For an interactive run, end the final reply with the owner's open asks from asksForYou. Report nextRunAt for a cadence, or runsOn for a trigger. For a cadence with scheduledBy=none, name the host setup step and raise the owner ask (asksForYou); the host owns the next wake.

## References

- [Refusal codes](references/refusals.md)
- [Reporting a run](references/reporting.md)
