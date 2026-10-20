---
name: "cady-core-run-sequence"
description: "Agent run sequence. Run one ordered piece of company work from reconciliation through result. Use when: the user wants a task carried through to a recorded outcome. Not for: recurring setup (use the scheduling guide)."
license: "MPL-2.0"
compatibility: "Requires Cady (app.cadyworks.com/mcp)"
metadata:
  cady-id: "execution.topic.run_sequence"
  version: "156c6b12df9c723215f7447ff78bb2aaa774b0219cc2ab6bb60763c49c9e6b9d"
  function: "core"
---
# Agent run sequence

Run one ordered piece of company work from reconciliation through result. Use when: the user wants a task carried through to a recorded outcome. Not for: recurring setup (use the scheduling guide).

## Run sequence

- **Applies to:** Every Cady agent run, every role. Your role card (if any) and skills say what to work on; this says the order.

### Refusals

`ACCEPT_NEEDS_EVIDENCE`, `AGENT_DUTY_UNCLEAR`, `AGENT_HOST_MISMATCH`, `AGENT_MISMATCH`, `AGENT_NOT_ACCEPTED`, `AGENT_NOT_BOUND`, `AGENT_NOT_LIVE`, `AGENT_PAUSED`, `AGENT_PROPOSAL_AMBIGUOUS`, `AGENT_RETIRED`, `BOUNDARY_NOT_READY`, `CITE_REPLACED_WHY`, `CITE_WITHDRAWN_WHY`, `CLAIM_NOT_CURRENT`, `CLAIM_REQUIRED`, `CROSS_HOST_MANAGE`, `DECISION_EXISTS`, `EFFECT_NOT_APPLIED`, `EVIDENCE_REF_MISSING`, `FIRST_LIVE_NOT_READY`, `GO_LIVE_NEEDS_APPROVAL`, `GRADES_REQUIRED`, `HOST_OWNER_MISMATCH`, `HOST_PROPOSE_ONLY`, `HOST_REQUIRED`, `LANE_OVERLAP`, `MANAGED_WORK`, `METHOD_NOT_CURRENT`, `MUST_CRITERION_NOT_PASSED`, `OVERLAPS_PERSON_DECISION`, `OWNER_NOT_MEMBER`, `PARENT_CYCLE`, `PARTY_IN_OTHER_LANE`, `RELEASE_PAUSED`, `RESULT_NEEDS_EVIDENCE`, `RESULT_NEEDS_SUMMARY`, `RESULT_PENDING`, `RUN_HOST_MISMATCH`, `STALE_GENERATION`, `STOP_REASON_REQUIRED`, `TRANSITION_REFUSED`, `TRANSITION_TIME_UNAVAILABLE`, `UNCERTAIN_EFFECT`, `WORK_NOT_FOUND`, `WORK_TERMINAL`

### Reporting

- **Evaluation:** offline_evaluation and spotcheck require non-null requestId, scenarioId and repetition, the Projects-derived runId for that configuration, and no slotStartAt or effect receiptIds. Preserve actual assessable output or outputRef, not only a summary. Independent assessment remains separate from producer claims.

#### Example

```json
{
  "expectedRevision": null,
  "run": {
    "finishedAt": 2,
    "outcome": "completed",
    "provenance": {
      "configurationRef": "agent-history:<current-history-id>",
      "output": "Actions: Checked the assigned records; corrected two discrepancies. Output: Saved the corrected owner artifact. Evidence: file:<id>. Next: Recheck after the next source update.",
      "outputRef": null,
      "purpose": "ordinary",
      "repetition": null,
      "requestId": null,
      "scenarioId": null,
      "traceRefs": [],
      "usage": {
        "costUsd": null,
        "denominator": "attempt",
        "durationMs": null,
        "source": null,
        "toolCalls": null
      }
    },
    "slotStartAt": 1,
    "startedAt": 1
  },
  "targetAgentId": "aaaaaaaa-aaaa-4aaa-8aaa-aaaaaaaaaaaa"
}
```
- **Metrics:** Use measured values with usage.source; otherwise all unavailable measurements and source are null. Zero means observed zero. denominator is attempt. Compare total cost including helpers and rework per independently accepted useful result, alongside quality, missed defects and needless escalations; run completion alone is not success.
- **Output:** Lead with actions and the useful output or result, cite owner evidence, then state the next step or exact blocker. Keep ordinary reports short; outputRef can point to the full owner artifact. File only what someone will open again to use or check: a deliverable, or source evidence no owner record holds; cut process notes, logs of your own steps and restatements instead of filing them. Make a review packet only when the owner must approve a set of exact materials together (for example the copy for a send); otherwise a memo does it. A memo goes only when the reader must do, decide or know something now, and its first line says which; it links the deliverables where they live and never repeats the run result, which the work record already stores. Do not upload local transcript bodies or repeat company context. Local transcript review diagnoses retries, waste, missed instructions, tool misuse and behavior; persist only the material finding, evidence reference and correction in the existing owner.
- **Shape:** An ordinary run is recorded by the run part of the step 6 close_company_work call (it forwards to manage_company_agent mode='record_run'); do not also record it there. Close derives slotStartAt and decisionsMade and stamps each skill's served version; name skills as skill.<name>. Call manage_company_agent (through call_cady_tool if not listed) with mode='record_run' directly only for offline_evaluation or spotcheck, with the example's arguments. The example uses synthetic identifiers and times: replace them with this agent, the current run identity and observed facts. Keep run facts nested. provenance is optional; if supplied, every shown provenance field is required, including nullable fields and usage.

### Steps

- 1. Codex only, first: if the newest rollout in ~/.codex/sessions other than this session's ended on a usage limit or auth error, call report_host_event {event: "previous_run", reason: "rate_limit" or "authentication_failed", resetsAt: its resets_at as an ISO time, session: file name} (call_cady_tool if unlisted); never copy its text. Then read get_cady_context with your agentId, the area you are working in (for example gtm/outreach or product/<id>/context) and a task sentence. Stop if you are paused or retired. Pass agentId on every Cady call that accepts it. The read returns the decisions routed to that area's action classes; read_cady search covers the rest, its method, live work and refs; read any ref with read_cady. Record new decisions with the returned writeAs.appliesTo.
- 2. Reconcile first. For each reconcileWorkIds item: settle unresolved effects with their owner and call transition_company_work action='report_effect_reconciliation'; an expired claim is no longer held: claim again (step 4) or action='recover' with a recoveryNote; a pending result you own within your limits takes action='accept_result', otherwise leave it for the named acceptor. Start no new effect on an item until it is clear.
- 3. Choose: resumeWorkIds first, then openWorkIds whose dueDate has passed or is empty, in the order served. Also check due standing duties from your current assignment and hostReview; an empty work queue does not cancel those duties. Create owner work only where needed, with brief {acceptance: 1-5 checks, finishLine}, and claim before controlled work. A finish line names the deliverable, its size rule and what done is; a sample is labelled one and never meets a request for the deliverable; a budget, time-box or access stop closes as partial (delivered N of T). A check is one fact a stranger can verify, kind mechanical, readback (re-read the record) or judgement (a reviewer's call); at least one must. Checks freeze at claim; only the claim holder changes them, with action='checkpoint', brief and criteriaChangeReason. Ordinary reads, monitoring and preparation do not require a new task by default. If neither work nor a standing duty is due, go to step 6 with outcome no_work.
- 4. Claim one item: transition_company_work action='claim' (omit attemptId and claimProof; the server fills and reuses them on your connection; a claim on BLOCKED work unblocks it). Stop on a live claim conflict. A claim lasts 30 minutes (control.claim.expiresAt on the work item); renew it with action='renew' before it expires.
- 5. Do the work. Read get_cady_context {agentId, workId: id} for the skill and records. Stay within scope; resolve lane overlap before go_live. Finish every step short of a human boundary yourself and checkpoint at natural boundaries. Near the budget (about four-fifths spent or a host warning), stop starting steps and close with the result or shortfall. Ask only what blocks and what no current record answers; otherwise choose a sensible default and proceed. When a missing owner fact blocks the next step, ask now with submit_company_work_checkpoint {ask} and keep working on the rest. Put every ask you can make now in one packet: who acts, where and what, options with your recommendation, owner minutes. An open hypothesis is the working assumption: treat it as answered, build on it, cite it, and propose a change only with new evidence. decisions.omissions means the list is incomplete; a capped or empty read is not proof of absence. Record a chat approval or correction in the person's exact words (source chat, quote, decidedBy "me", status COMPLETE) and act on it; quote an OPEN one from pendingConfirmations back once. Record each decision once and supersede it to change it. A statement is a one-sentence title; reasons go in rationale and sources in evidenceRefs.
- 6. End every agent run with one close_company_work call, made last. With nothing to record, call it as {agentId, run: {outcome: "no_work"}}. Put each item you worked in items; Cady reports or accepts it as your status allows. The close tool's own description lists the parts and pre-close checks; follow it. The result must be the requested usable deliverable or a verified external effect; research, planning, preparation and a finished run are progress unless that artifact itself was requested; a send is proven by its owner receipt. Until your status is live, prepare only and never release or send; manage_agents covers going live. For an interactive run, end the final reply with the owner's open asks from asksForYou. Report nextRunAt for a cadence, or runsOn for a trigger. For a cadence with scheduledBy=none, name the host setup step and raise the owner ask (asksForYou); the host owns the next wake.

**Company context:** `get_cady_context({"area": "<area>", "task": "<what you are about to do, in one sentence>"})`
