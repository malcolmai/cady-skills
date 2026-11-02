---
name: "cady-gtm-reply"
description: "Reply in a live thread. Use when: Answer an inbound reply in a live thread: a question, interest, objection, referral, not now or stop. Not for: First touches and follow-ups to someone who has not replied."
license: "MPL-2.0"
compatibility: "Requires Cady (app.cadyworks.com/mcp)"
metadata:
  cady-id: "skill.gtm.reply"
  version: "793a79112a2809ab161b"
  library: "76da591f0f251280"
  function: "gtm"
---
# Reply in a live thread

**Point:** Learn what they want, honestly judge fit now or later (try; no fit is fine), then follow up without chasing.

**Company context:** `context_read({"area": "gtm/outreach", "task": "<what you are about to do, in one sentence>", "knownMethods": {"skill.gtm.reply": "793a79112a2809ab161b@76da591f0f251280"}})`

Answer an inbound reply in a live thread: a question, interest, objection, referral, not now or stop.

**Not for:** First touches and follow-ups to someone who has not replied.

**Unit of work:** one work item per thread. **Kind:** execution. **Parallel:** yes. **Can release:** yes. 

## Always

- In a review body, put a line with only --- between messages.

## Inputs

### Evidence refs

- crm:party:<partyId>
- the communication ref being answered

### Work fields

- channel
- senderLabel

## Procedure

1. Read the actual inbound thread through its authorized connector and records_read party:<partyId>; for Cady-held email, use the outcome check and crm.find_communications/crm.get_communication. Keep the same channel and recipient. Other channels use route A or the approved device route, never a Cady email account. Exclude anything permission rules block. A channel-specific stop that Cady cannot store remains an explicit no-send hold in the task; do not silently discard it or broaden its scope.
2. Triage the newest inbound message before drafting anything. For every class except stop and auto-reply, first understand what they want and whether we fit now or later; try to fit, and if we do not, say so honestly and note what would change that. Pick one class; when several apply, stop wins, then wrong person, then objection over positive. File it with crm_interactions_create (sourceRef the provider message id) if outcome_check has not.

| Class | Next action | Timing | Permission effect |
|---|---|---|---|
| Positive or question | Answer exactly what was asked. Offer one dated next step only if they explicitly asked for or offered one. | The first run that finds it | Recorded reply makes the party engaged and holds follow-ups; set no stage the user has not stated; a party with no track needs motion customer and a user-stated stage for crm_tracks_set; use crm_tracks_set for existing tracks |
| Objection | Answer it with the objection step below; one question at most. | The next run | None |
| Referral ("talk to X") | Thank them in one line; ask whether they will introduce you (double opt-in, `../../references/intro-request.md`) or you may mention them. | The first run that finds it | X is a new party with no permission of their own: cold rules apply unless the referrer introduces you in a thread (kind intro) |
| Not now | One short line acknowledging it; no pitch, no "just in case" material. | Once, then hold | crm_tracks_set outcome paused, recontact on their date, else '3m' |
| No or not a fit | Optional one-line thanks if they wrote more than a word; no rebuttal. | Once or not at all | crm_tracks_set outcome disqualified with reason, recontact 'unless_changed' |
| Out of office or auto-reply | Send nothing. Note any return date; a named alternative contact is a referral. | No reply | File as kind note, not reply: it is not engagement and does not hold the follow-up |
| Wrong person or left the company | One line: thank them, ask who owns the problem. If they left, the address is dead. | The first run that finds it | Filing it as a reply holds follow-ups; a later bounce is filed as a hard bounce; the named owner is a referral |
| Stop, unsubscribe, remove me, complaint | Send nothing, not even a confirmation. | Immediately | kind opt_out on the channel they named, else all; optOutReason complaint if hostile or a spam report; tell the owner |
3. Commitments in the thread: keep a simple next step in existing work text; reuse the existing task or native reminder for the same outcome, never duplicate it for metadata, and keep independently fulfilled promises distinct. Add obligation metadata only when useful for retrieval, waiting, due dates, deduplication or source-linked fulfillment: preserve conditions and stated/inferred certainty without upgrading a hedge; record the source and exact counterparty when supported, leaving an unknown promisor unknown; a date-only commitment uses the canonical task dueDate, never an invented time or timezone. Report through work_report, or for owned work the managed checkpoint route with current revision, generation and claim proof; if the obligation exists, update that id. A reply, acknowledgement, delay or partial delivery does not fulfill an owed guide or contract; close only when evidence meets the promised outcome. An acknowledged cancellation stops execution but does not fulfill, release or waive the promise. The reply still waits for review approval. Route other takeaways to their owners; infer no stage or role.
4. Objections: acknowledge in their words, ask the one question that tells a brush-off from a real blocker, answer with evidence, offer one low-effort next step, and accept a second no. "Send me info": send the one item that fits what they said, not a deck. "We use X" or "we built it": ask what works and what does not; name one difference only if it meets that gap. "Too expensive" or "no budget": find whether it is price, value, timing or authority; quote only the accepted offer, and a discount or pilot is the owner's decision. "Not a priority": treat as not now. "Not my call": ask who decides and offer a short summary they can forward. Security, compliance or certification: answer only from company evidence; say you will check rather than guess. "How did you get my address?": state the real source and offer to stop. Record what an objection or not-now shows, in the words they used, on the persona's profile against its hypothesis (`cady-gtm-persona-profile`), outside the reply. Never use false urgency, guilt, invented scarcity, a fake "closing your file" email or another ask after a clear no.
5. Draft one reply following the copy rules: shorter than their message where possible, one question at most, no re-pitch of the cold email, and keep everyone they copied. Judge it with the taste check (../../references/taste-check.md, message part) before review.
6. Preparation: RECIPIENTS_EXCLUDED for destination_invalid, opted_out, suppressed; held by skill_required, claim_required, claim_expired, CAP_REACHED, TRACKED_LINKS_OFF. Not held by no_basis, platform_paused, company_paused, SENDING_ACCOUNT_NOT_CONFIRMED, sender_missing, destination_unverified, deferred, recent_contact, replied_since_release, already_sent_in_cycle, executor_unavailable. Prepare with crm_outreach_review_prepare on the thread's channel, one recipient and lane "non_marketing", read it with records_read review:outreach/<subjectId>, then follow release.
7. Act versus ask: follow `cady-company-operations-inbox-follow-through`.

## Acceptance

- [ ] (check) a positive reply or question is answered in the first run that finds it, an objection in the next; replies are no faster than the agent's cadence
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
