---
name: "cady-company-operations-inbox-follow-through"
description: "Inbox follow-through: group, triage, track commitments. Use when: Bounded inbox maintenance or thread triage for follow-through, marketing handling or commitments needing tracking. Not for: Executing a prospect reply (`cady-gtm-reply`), sending or drafting outreach, or reading mail Cady is not given: only the host's connector reads mail. Thread triage remains in scope."
license: "MPL-2.0"
compatibility: "Requires Cady (app.cadyworks.com/mcp)"
metadata:
  cady-id: "skill.company_operations.inbox_follow_through"
  version: "81d846ccd04fb438c243"
  library: "591145ab2187b638"
  function: "company_operations"
---
# Inbox follow-through: group, triage, track commitments

**Company context:** `get_cady_context({"area": "ops/inbox", "task": "<what you are about to do, in one sentence>", "knownMethods": {"skill.company_operations.inbox_follow_through": "81d846ccd04fb438c243@591145ab2187b638"}})`

Bounded inbox maintenance or thread triage for follow-through, marketing handling or commitments needing tracking.

**Not for:** Executing a prospect reply (`cady-gtm-reply`), sending or drafting outreach, or reading mail Cady is not given: only the host's connector reads mail. Thread triage remains in scope.

**Unit of work:** the requested thread or bounded mailbox sweep; reuse existing work or an adequate native reminder, adding commitment metadata only when later due, waiting, deduplication or source-linked fulfillment needs it. **Kind:** execution. **Parallel:** no. **Can release:** no. 

## Inputs

### Evidence refs

- crm:party:<partyId> for known senders
- crm:interaction:<interactionId> or the provider message id
- current inbox.suppress: decisions

### Statement fields

- mail account and window
- what counts as urgent
- user's time zone

## Procedure

1. Write material internal records without asking. Prepare consequential actions (money, time or an important counterparty) for review; never send without explicit owner approval. Other outside effects use Cady with a one-line justification and self-approval quality check; neither replaces owner, grant or channel checks. Unreadable/403 sources yield no takeaway. Record one interaction per material takeaway and cite its returned ref.
2. For mailbox maintenance, read current inbox.suppress: and inbox:marketing-treatment decisions and relevant recent communication references, then read only headers (sender and domain, List-Id, List-Unsubscribe, Precedence: bulk, subject, To versus BCC, reply-to, attachment flag) through the host's own mail connector. For a one-thread request, read only that thread and the owner records it needs. If the required connector or account is unavailable, stop and say so; never read mail through Cady. The one exception is replies, opt-outs and bounces to mail Cady itself sent: if the company sends outreach from a connected Cady mailbox, start the sweep with crm.record_interactions mode capture; mail it records needs no second filing.
3. Group by sender domain or List-Id plus subject template. Bulk requires List-Unsubscribe, Precedence: bulk, BCC or a large To list. Read known CRM parties with open commitments, prior correspondents, and actual personal exchanges or unresolved requests individually, even if sent through a newsletter tool; mere receipt is not personal. A one-thread request needs no sweep.
4. Sample about three homogeneous, low-consequence messages (newest, oldest, random; all if few). Samples and the 2% audit are defaults, not proof. Read mixed or consequential items individually; never suppress unread messages without credible outlier coverage. See [grouping details](../../references/inbox-follow-through-details.md) for personal-request and sample rules.
5. Scan unsampled members for consequential outliers: a personal request or exchange, different reply-to, attachment, or an actual invoice, contract, deadline, renewal or security action. A name or personalization token alone is not an outlier. Read each hit individually and count it as pulledOut.
6. Triage each individually read message on separate fields, never one score: type (question, request, promise, receipt, invoice, notice, social), action (none, reply, do, decide, wait), owner, deadline (absolute date and the zone written in) and importance (the user's own priority). Preserve each actual obligation, payment, contract or security action, even from a marketing sender. A promotional price or countdown is not an obligation; expired no-action reminders may be archived.
7. For marketing mail, follow the existing inbox:marketing-treatment choice; ask once only for genuinely uncertain useful interest. See [Marketing handling and commitment updates](../../references/inbox-follow-through-details.md) for personalization, archive/unsubscribe separation and exceptional items.
8. Record only material communication evidence with crm.record_interactions (kind reply for an actual response, note for an observation, provider message id as sourceRef (for pasted mail, a stable host reference or deterministic digest, never a raw subject), sender party, time and one-line outcome). Never put body, subject or attachments in Cady. Resolve an unknown sender using authorized CRM/source evidence; if identity remains unknown, do not invent a party or permission. Create a party through crm.update_party mode=create only when identity is sufficiently evidenced and durable CRM identity is useful; otherwise ask only if the ambiguity changes a consequential next action.
9. For material threads, identify outcome and owner/work; check latest counterparty mail against unresolved older requests. Generic status does not complete the goal. Finish useful investigation/preparation within mandate: deliver the assessment or draft, then ask only for the missing decision/approval. No request does not mean done.
10. Reuse existing work or a native reminder; never create per-email or duplicate work. Add obligation metadata only when useful for retrieval or fulfillment. Preserve source, certainty, promisor and date precision; never infer them. Use the supported reporting or focused-update route. See [Commitment updates and takeaway routing](../../references/inbox-follow-through-details.md) for owner routes.
11. Reconcile due awaiting commitments even without new mail: record who acts next and a justified chase date. Awaiting is not blocked or Needs-you without a person action. Keep unfinished outcomes open and completed work terminal; cancellation is not fulfillment. Stop denied mutations and continue independent work. Route material takeaways once; routine mail writes nothing. Use the commitment reference for corrections and CRM-specific routes.
12. For mailbox maintenance, audit a random 2% of previously suppressed mail (at least 5, or all if fewer). This default is not proof of safety. One that needed action is a misfile: demote that group to read-individually, pull the message out, handle it, and count it as misfiled.
13. Unread archive rules remain company decisions under inbox.suppress:<sender-or-list-slug>, with sample evidence and reviewBy at most 30 days away. Marketing keep/ignore policy is a separate inbox:marketing-treatment decision; preserve its existing choice, and ask once only when a relevant item exposes a missing decision.
14. Report user actions (type, owner, deadline, earliest first), owed-by/to items and waits. Include run counters: groups, sampled, pulledOut, suppressed, audited, misfiled, obligations written, superseded, refused.

## Acceptance

- [ ] no message was suppressed from headers alone: every suppressed group was sampled and outlier-scanned
- [ ] known parties, people the user has written to and threads the user is on were read individually
- [ ] material outcomes and dependencies remain open until evidenced complete; work or reminders are reused and optional terms preserve source, known promisor and supplied date precision without duplicating the outcome
- [ ] an awaiting obligation carries waitingOn and chaseAt and is not in Needs-you
- [ ] completed work stays terminal on replay; genuinely new commitments use explicit successor lineage, while an erroneous completion follows the supported correction route
- [ ] takeaways reach their owner only when important: routine mail writes nothing to the CRM or context; a deferral is a track, a stop is a permission, an owner decision is a quoted decision

## Owner checks

- host mail connector only; no mail body, subject or attachment stored in Cady
- existing inbox:marketing-treatment choice; do not ask again for a recorded preference
- exact CRM party before an obligation names a counterparty
- inbox.suppress: decision with reviewBy for every unread archive rule

## Result

### Artifact refs

- company:work:<workId>
- crm:interaction:<interactionId>
- crm:party:<partyId>
- **Transition:** report the useful outcome, material remainder and next owner through report_company_work; include counters only in optional observed run output, never create a run just to hold them

## References
- Read [Commitment updates and takeaway routing](../../references/inbox-follow-through-details.md) when a material inbox outcome, commitment or takeaway needs owner-routed follow-through.
