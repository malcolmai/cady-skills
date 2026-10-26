---
name: "cady-gtm-reply"
description: "Reply in a live thread. Use when: Answer an inbound reply in a live thread: a question, interest, objection, referral, not now or stop. Not for: First touches (use `cady-gtm-cold-email-cycle` or `cady-gtm-linkedin-message`) and follow-ups to someone who has not replied (email: `cady-gtm-warm-email`; LinkedIn: `cady-gtm-linkedin-message`)."
license: "MPL-2.0"
compatibility: "Requires Cady (app.cadyworks.com/mcp)"
metadata:
  cady-id: "skill.gtm.reply"
  version: "55943c284093822a422b"
  library: "58091c89f54a2355"
  function: "gtm"
---
# Reply in a live thread

**Company context:** `get_cady_context({"area": "gtm/outreach", "task": "<what you are about to do, in one sentence>", "knownMethods": {"skill.gtm.reply": "55943c284093822a422b@58091c89f54a2355"}})`

Answer an inbound reply in a live thread: a question, interest, objection, referral, not now or stop.

**Not for:** First touches (use `cady-gtm-cold-email-cycle` or `cady-gtm-linkedin-message`) and follow-ups to someone who has not replied (email: `cady-gtm-warm-email`; LinkedIn: `cady-gtm-linkedin-message`).

**Unit of work:** one work item per thread. **Kind:** execution. **Parallel:** yes. **Can release:** yes. 

## Always

- In a review body, put a line with only --- between messages.

## Inputs

### Evidence refs

- crm:party:<partyId>
- the communication ref being answered

### Statement fields

- channel
- senderLabel

## Procedure

1. Read the shared message rules (`../../references/outreach-message-rules.md`) first: voice pack, consent, release.
2. Read the actual inbound thread through its authorized connector and crm.get_party; for Cady-held email, use the outcome check and crm.find_communications/crm.get_communication. Keep the same channel and recipient. Other channels use route A or the approved device route, never a Cady email account. Exclude anything permission rules block. A channel-specific stop that Cady cannot store remains an explicit no-send hold in the task; do not silently discard it or broaden its scope.
3. Triage the newest inbound message before drafting anything. Pick one class; when several apply, stop wins, then wrong person, then objection over positive. File it with crm.record_interactions (sourceRef the provider message id) if outcome_check has not.

| Class | Next action | Timing | Permission effect |
|---|---|---|---|
| Positive or question | Answer exactly what was asked. Offer one dated next step only if they signalled one ("happy to talk", "send times"). | The first run that finds it | Recorded reply makes the party engaged and holds follow-ups; set no stage the user has not stated; a party with no track needs motion customer and a user-stated stage before any crm.set_track |
| Objection | Answer it with the objection step below; one question at most. | The next run | None |
| Referral ("talk to X") | Thank them in one line; ask whether they will introduce you (double opt-in, `../../references/intro-request.md`) or you may mention them. | The first run that finds it | X is a new party with no permission of their own: cold rules apply unless the referrer introduces you in a thread (kind intro) |
| Not now | One short line acknowledging it; no pitch, no "just in case" material. | Once, then hold | crm.set_track outcome paused, recontact on their date, else '3m' |
| No or not a fit | Optional one-line thanks if they wrote more than a word; no rebuttal. | Once or not at all | crm.set_track outcome disqualified with outcomeReason, recontact 'unless_changed' |
| Out of office or auto-reply | Send nothing. Note any return date; a named alternative contact is a referral. | No reply | File as kind note, not reply: it is not engagement and does not hold the follow-up |
| Wrong person or left the company | One line: thank them, ask who owns the problem. If they left, the address is dead. | The first run that finds it | Filing it as a reply holds follow-ups; a later bounce is filed as a hard bounce; the named owner is a referral |
| Stop, unsubscribe, remove me, complaint | Send nothing, not even a confirmation. | Immediately | kind opt_out on the channel they named, else all; optOutReason complaint if hostile or a spam report; tell the owner |
4. Commitments in the thread: keep a simple next step in existing work text when structure adds no useful retrieval. Reuse the existing task or adequate native reminder for the same outcome; do not duplicate it to add metadata, and keep independently fulfilled promises distinct. Keep workKind=task and the existing outcome in the title and optional brief. Add optional obligation metadata only when useful for later retrieval, waiting, due-date queries, deduplication or source-linked fulfillment. Preserve conditions and stated/inferred certainty without upgrading a hedge. Record the source and exact counterparty when supported; a known promisor is distinct from executor, and an unknown promisor stays unknown. A date-only commitment uses the canonical task dueDate; never invent a time or timezone. Use report_company_work for material work reporting with optional obligation/brief on the item; for a focused update to already-owned work, use the exact managed checkpoint route with current revision, generation and claim proof. If the same obligation already exists, read the existing work and attach/update the same id. A reply, acknowledgement, delay or partial delivery does not fulfill an owed guide or contract; keep its remainder open. Close only when evidence meets the actual promised outcome; a requested confirmation can be completed by that confirmation. An acknowledged cancellation stops execution but does not fulfill, release or waive the promise. The reply still waits for review approval. Route other material takeaways to their owners; do not infer a stage or role.
5. Objections: acknowledge in their words, ask the one question that tells a brush-off from a real blocker, answer with evidence, offer one low-effort next step, and accept a second no. "Send me info": send the one item that fits what they said, not a deck. "We use X" or "we built it": ask what works and what does not; name one difference only if it meets that gap. "Too expensive" or "no budget": find whether it is price, value, timing or authority; quote only the accepted offer, and a discount or pilot is the owner's decision. "Not a priority": treat as not now. "Not my call": ask who decides and offer a short summary they can forward. Security, compliance or certification: answer only from company evidence; say you will check rather than guess. "How did you get my address?": state the real source and offer to stop. Never use false urgency, guilt, invented scarcity, a fake "closing your file" email or another ask after a clear no.
6. Draft one reply following the copy rules: shorter than their message where possible, one question at most, no re-pitch of the cold email, and keep everyone they copied. Judge it with the taste check (../../references/taste-check.md, message part) before review.
7. Preparation: RECIPIENTS_EXCLUDED for no_basis, destination_unverified, destination_invalid, opted_out, suppressed, deferred, recent_contact; held by SENDING_ACCOUNT_NOT_CONFIRMED, skill_required, claim_required, claim_expired, REPLIED_SINCE_RELEASE, CAP_REACHED, TRACKED_LINKS_OFF. Not held by platform_paused, company_paused, executor_unavailable. Prepare with crm.prepare_outreach_review on the thread's channel, one recipient and lane "non_marketing", read it with crm.get_outreach_review, then follow release.
8. Act versus ask: follow `cady-company-operations-inbox-follow-through`.

## Acceptance

- [ ] (check) a positive reply or question is answered in the first run that finds it, and an objection in the next run; an agent has one cadence, so its replies are no faster than its next run, which the owner was told when the cadence was set
- [ ] (check) the reply class, its next action and any permission effect are stated for this thread
- [ ] (check) a stop request or auto-reply gets no reply; a stop is filed as opt_out
- [ ] (check) one review prepared and readable for this thread
- [ ] (fresh) a reader who sees only the thread and the reply finds that it answers what was asked and no more
- [ ] (person) nothing is sent before the person, or a grant covering the exact text, has approved the review
- [ ] (check) material commitments remain findable across runs; an ordinary dated next step may stay in the existing work text

## Owner checks

- permission recheck at prepare

## Result

### Artifact refs

- crm:outreach_review:<approvalId>
- **Transition:** the claim holder reports the result

## References
- Read [Copy](references/copy.md) when you draft the reply.
- Read [Outreach message rules](../../references/outreach-message-rules.md) when you draft, review or prepare any message (read first).
- Read [Taste check](../../references/taste-check.md) when judging a draft or design before review.
