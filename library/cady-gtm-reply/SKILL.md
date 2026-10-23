---
name: "cady-gtm-reply"
description: "Reply in a live thread. Use when: Answer an inbound reply in a live email, LinkedIn or host-connected message thread: a question, interest, objection, referral, not now or stop. Not for: First touches (use `cady-gtm-cold-email-cycle` or `cady-gtm-linkedin-message`) and follow-ups to someone who has not replied (email: `cady-gtm-warm-email`; LinkedIn: `cady-gtm-linkedin-message`)."
license: "MPL-2.0"
compatibility: "Requires Cady (app.cadyworks.com/mcp)"
metadata:
  cady-id: "skill.gtm.reply"
  version: "a8ace37ca26987f645e1b7f481cf3be8d4cb8e281ab255feecf15e1500a7221c"
  library: "d9d01922e6210604"
  function: "gtm"
---
# Reply in a live thread

**Company context:** `get_cady_context({"area": "gtm/outreach", "task": "<what you are about to do, in one sentence>", "knownMethods": {"skill.gtm.reply": "a8ace37ca26987f645e1b7f481cf3be8d4cb8e281ab255feecf15e1500a7221c"}})`

Answer an inbound reply in a live email, LinkedIn or host-connected message thread: a question, interest, objection, referral, not now or stop.

**Not for:** First touches (use `cady-gtm-cold-email-cycle` or `cady-gtm-linkedin-message`) and follow-ups to someone who has not replied (email: `cady-gtm-warm-email`; LinkedIn: `cady-gtm-linkedin-message`).

**Unit of work:** one work item per thread. **Kind:** execution. **Parallel:** yes. **Can release:** yes. 

See [Always](references/always.md).
## Procedure

1. Read the shared message rules (`../../references/outreach-message-rules.md`) first: voice pack, consent, release.
2. Read the actual inbound thread through its authorized connector and crm.get_party; for Cady-held email/LinkedIn, use the outcome check and crm.find_communications/crm.get_communication. Keep the same channel and recipient. Other channels use the approved host or device route, never a Cady email account. Exclude anything permission rules block. A channel-specific stop that Cady cannot store remains an explicit no-send hold in the task; do not silently discard it or broaden its scope.
3. Triage the newest inbound message before drafting anything. Pick one class; when several apply, stop wins, then wrong person, then objection over positive. File it with crm.record_interactions (sourceRef the provider message id) if outcome_check has not.

| Class | Next action | Timing | Permission effect |
|---|---|---|---|
| Positive or question | Answer exactly what was asked. Offer one dated next step only if they signalled one ("happy to talk", "send times"). | Same business day, ideally within a few hours | Recorded reply makes the party engaged and holds follow-ups; set no stage the user has not stated; a party with no track needs motion customer and a user-stated stage before any crm.set_track |
| Objection | Answer it with the objection step below; one question at most. | Within one business day | None |
| Referral ("talk to X") | Thank them in one line; ask whether they will introduce you (double opt-in, `../../references/intro-request.md`) or you may mention them. | Same day | X is a new party with no permission of their own: cold rules apply unless the referrer introduces you in a thread (kind intro) |
| Not now | One short line acknowledging it; no pitch, no "just in case" material. | Once, then hold | crm.set_track outcome paused, recontact on their date, else '3m' |
| No or not a fit | Optional one-line thanks if they wrote more than a word; no rebuttal. | Once or not at all | crm.set_track outcome disqualified with outcomeReason, recontact 'unless_changed' |
| Out of office or auto-reply | Send nothing. Note any return date; a named alternative contact is a referral. | No reply | File as kind note, not reply: it is not engagement and does not hold the follow-up |
| Wrong person or left the company | One line: thank them, ask who owns the problem. If they left, the address is dead. | Same day | Filing it as a reply holds follow-ups; a later bounce is filed as a hard bounce; the named owner is a referral |
| Stop, unsubscribe, remove me, complaint | Send nothing, not even a confirmation. | Immediately | kind opt_out on the channel they named, else all; optOutReason complaint if hostile or a spam report; tell the owner |
4. Commitments in the thread: keep a simple next step in existing work text when structure adds no useful retrieval. Reuse the existing task or adequate native reminder for the same outcome; do not duplicate it to add metadata, and keep independently fulfilled promises distinct. Keep workKind=task and the existing outcome in the title and optional brief. Add optional obligation metadata only when useful for later retrieval, waiting, due-date queries, deduplication or source-linked fulfillment. Preserve conditions and stated/inferred certainty without upgrading a hedge. Record the source and exact counterparty when supported; a known promisor is distinct from executor, and an unknown promisor stays unknown. A date-only commitment uses the canonical task dueDate; never invent a time or timezone. Use close_company_work for material work reporting with optional obligation/brief on the item; for a focused update to already-owned work, use the exact managed checkpoint route with current revision, generation and claim proof. On OBLIGATION_EXISTS, read the existing work and attach/update the same id. A reply, acknowledgement, delay or partial delivery does not fulfill an owed guide or contract; keep its remainder open. Close only when evidence meets the actual promised outcome; a requested confirmation can be completed by that confirmation. An acknowledged cancellation stops execution but does not fulfill, release or waive the promise. The reply still waits for review approval. Route other material takeaways to their owners; do not infer a stage or role.
5. Objections: acknowledge in their words, ask the one question that tells a brush-off from a real blocker, answer with evidence, offer one low-effort next step, and accept a second no. "Send me info": send the one item that fits what they said, not a deck. "We use X" or "we built it": ask what works and what does not; name one difference only if it meets that gap. "Too expensive" or "no budget": find whether it is price, value, timing or authority; quote only the accepted offer, and a discount or pilot is the owner's decision. "Not a priority": treat as not now. "Not my call": ask who decides and offer a short summary they can forward. Security, compliance or certification: answer only from company evidence; say you will check rather than guess. "How did you get my address?": state the real source and offer to stop. Never use false urgency, guilt, invented scarcity, a fake "closing your file" email or another ask after a clear no.
6. Draft one reply following the copy rules: shorter than their message where possible, one question at most, no re-pitch of the cold email, and keep everyone they copied.
7. Preparation: RECIPIENTS_EXCLUDED for no_basis, destination_unverified, destination_invalid, opted_out, suppressed, deferred, recent_contact; held by SENDING_ACCOUNT_NOT_CONFIRMED, skill_required, claim_required, claim_expired, REPLIED_SINCE_RELEASE, CAP_REACHED, TRACKED_LINKS_OFF. Not held by platform_paused, company_paused, executor_unavailable. Prepare with crm.prepare_outreach_review on the thread's channel, one recipient and lane "non_marketing", read it with crm.get_outreach_review, then follow release.
8. Act versus ask: follow `cady-company-operations-inbox-follow-through`.

## Acceptance

- [ ] a positive reply or question is answered the same business day; an objection within one business day
- [ ] the reply class, its next action and any permission effect are stated for this thread
- [ ] a stop request or auto-reply gets no reply; a stop is filed as opt_out
- [ ] one review prepared and readable for this thread
- [ ] nothing sent before the review is approved
- [ ] material commitments remain findable across runs; an ordinary dated next step may stay in the existing work text

See [Owner checks](references/owner-checks.md).
See [Result](references/result.md).
See [References](references/references.md).
