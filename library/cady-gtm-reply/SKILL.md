---
name: "cady-gtm-reply"
description: "Reply in a live thread. Use when: Answer an inbound reply in a live email or LinkedIn thread: a question, interest, objection, referral, not now or stop. Not for: First touches (use `cady-gtm-cold-email-cycle` or `cady-gtm-linkedin-message`) and follow-ups to someone who has not replied (email: `cady-gtm-warm-email`; LinkedIn: `cady-gtm-linkedin-message`)."
license: "MPL-2.0"
compatibility: "Requires Cady (app.cadyworks.com/mcp)"
metadata:
  cady-id: "skill.gtm.reply"
  version: "54cda1e65b37b561c35201ef2fc30893e33582ec5439a5d95e5cc71e84e2dc6f"
  library: "fed32b12fc15ae44"
  function: "gtm"
---
# Reply in a live thread

**Company context:** `get_cady_context({"area": "gtm/outreach", "task": "<what you are about to do, in one sentence>", "knownMethods": {"skill.gtm.reply": "54cda1e65b37b561c35201ef2fc30893e33582ec5439a5d95e5cc71e84e2dc6f"}})`

Answer an inbound reply in a live email or LinkedIn thread: a question, interest, objection, referral, not now or stop.

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
2. Find new replies with the outcome check (message rules, outcome_check); read the thread with crm.find_communications and crm.get_communication, then crm.get_party. Exclude and explain anything the permission rules block.
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
4. Objections: acknowledge in their words, ask the one question that tells a brush-off from a real blocker, answer with evidence, offer one low-effort next step, and accept a second no. "Send me info": send the one item that fits what they said, not a deck. "We use X" or "we built it": ask what works and what does not; name one difference only if it meets that gap. "Too expensive" or "no budget": find whether it is price, value, timing or authority; quote only the accepted offer, and a discount or pilot is the owner's decision. "Not a priority": treat as not now. "Not my call": ask who decides and offer a short summary they can forward. Security, compliance or certification: answer only from company evidence; say you will check rather than guess. "How did you get my address?": state the real source and offer to stop. Never use false urgency, guilt, invented scarcity, a fake "closing your file" email or another ask after a clear no.
5. Draft one reply following the copy rules: shorter than their message where possible, one question at most, no re-pitch of the cold email, and keep everyone they copied.
6. Preparation: RECIPIENTS_EXCLUDED for no_basis, destination_unverified, destination_invalid, opted_out, suppressed, deferred, recent_contact; held by SENDING_ACCOUNT_NOT_CONFIRMED, skill_required, claim_required, claim_expired, REPLIED_SINCE_RELEASE, CAP_REACHED, TRACKED_LINKS_OFF. Not held by platform_paused, company_paused, executor_unavailable. Prepare with crm.prepare_outreach_review on the thread's channel, one recipient and lane "non_marketing", read it with crm.get_outreach_review, then follow release.

## Acceptance

- [ ] a positive reply or question is answered the same business day; an objection within one business day
- [ ] the reply class, its next action and any permission effect are stated for this thread
- [ ] a stop request or auto-reply gets no reply; a stop is filed as opt_out
- [ ] one review prepared and readable for this thread
- [ ] nothing sent before the review is approved

## Owner checks

- WORK_NOT_FOUND
- METHOD_NOT_CURRENT
- COPY_RULE_FAILED
- permission recheck at prepare

## Result

### Artifact refs

- crm:outreach_review:<approvalId>
- **Transition:** the claim holder reports the result

## References
- [Copy](references/copy.md)
- [Outreach message rules](../../references/outreach-message-rules.md)
