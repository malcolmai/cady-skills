---
name: "cady-company-operations-inbox-follow-through"
description: "Inbox follow-through: group, triage, track commitments. Use when: Review a mailbox window or a specific thread for material follow-through and commitments that need tracking. Not for: Replying to a prospect's thread (`cady-gtm-reply`), sending or drafting outreach, or reading mail Cady is not given: only the host's connector reads mail."
license: "MPL-2.0"
compatibility: "Requires Cady (app.cadyworks.com/mcp)"
metadata:
  cady-id: "skill.company_operations.inbox_follow_through"
  version: "8c905a4299180a4c7957340e5c2c7c2174fa7b3851565d98d2ae0e662b95b67d"
  library: "725c50982aeed34b"
  function: "company_operations"
---
# Inbox follow-through: group, triage, track commitments

**Company context:** `get_cady_context({"area": "ops/records", "task": "<what you are about to do, in one sentence>", "knownMethods": {"skill.company_operations.inbox_follow_through": "8c905a4299180a4c7957340e5c2c7c2174fa7b3851565d98d2ae0e662b95b67d"}})`

Review a mailbox window or a specific thread for material follow-through and commitments that need tracking.

**Not for:** Replying to a prospect's thread (`cady-gtm-reply`), sending or drafting outreach, or reading mail Cady is not given: only the host's connector reads mail.

**Unit of work:** the requested thread or bounded mailbox sweep; reuse existing work or an adequate native reminder, adding commitment metadata only when later due, waiting, deduplication or source-linked fulfillment needs it. **Kind:** execution. **Parallel:** no. **Can release:** no. 

See [Inputs](references/inputs.md).
## Procedure

1. For mailbox maintenance, read the current inbox.suppress: decisions and relevant recent communication references, then read only headers (sender and domain, List-Id, List-Unsubscribe, Precedence: bulk, subject, To versus BCC, reply-to, attachment flag) through the host's own mail connector. For a one-thread request, read only that thread and the owner records it needs. If the required connector or account is unavailable, stop and say so; never read mail through Cady.
2. Group and sample only to maintain mailbox handling rules. Key: sender domain or List-Id plus the subject template. A message joins a bulk group only with List-Unsubscribe or Precedence: bulk, or the user in BCC or a large To list. Never group a known CRM party with an open track or promise, anyone the user has written to, or a thread the user is on: read those individually, even when sent from a newsletter tool. A one-thread request needs only the applicable thread steps; do not perform a mailbox sweep.
3. For homogeneous low-consequence groups, sample about three messages (newest, oldest and one random; all of a small group). This and the 2% audit are operating defaults, not proof that the rest are safe. Samples must share a template and show no personal address, question, deadline, money or contract aimed at the user. Read mixed or consequential messages individually; narrow a group only where its members are genuinely alike. Resample a changed sender/template or a rule 30 days old. If the connector cannot scan outliers with credible coverage, do not suppress unread messages.
4. Scan unsampled group members for outliers before applying a suppression rule: the user's name or address in the body, a different reply-to, an attachment, invoice, contract, deadline, overdue, cancel, urgent, renewal or signature. Read each hit individually and count it as pulledOut.
5. Triage each individually read message on separate fields, never one score: type (question, request, promise, receipt, invoice, notice, social), action (none, reply, do, decide, wait), owner, deadline (absolute date and the zone written in) and importance (the user's own priority). Archive or label only what is no action and low importance; keep anything with a deadline, money or a contract.
6. Record only material communication evidence with crm.record_interactions (kind email-like reply or note, provider message id as sourceRef, sender party, time and one-line outcome). Never put body, subject or attachments in Cady. Resolve an unknown sender using authorized CRM/source evidence; if identity remains unknown, do not invent a party or permission. Create a party through crm.update_party mode=create only when identity is sufficiently evidenced and durable CRM identity is useful; otherwise ask only if the ambiguity changes a consequential next action.
7. Reuse the existing task or an adequate native reminder for a promised outcome; do not create duplicate work for metadata. Add obligation metadata only when it helps later retrieval, waiting, due-date queries, deduplication or source-linked fulfillment. Preserve the source-backed terms and certainty; never infer a promisor, deadline or fulfillment. Use the supported reporting or focused-update route. See [Commitment updates and takeaway routing](../../references/inbox-follow-through-details.md) for the conditional owner routes.
8. Reconcile due awaiting commitments before a sweep, even when no new mail arrived. Record who acts next and a justified chase date; awaiting is not blocked or Needs-you without a person action. Keep unfinished outcomes open, completed work terminal on replay, and cancellation distinct from fulfillment. Correct prior errors through the supported owner route. Stop a denied mutation and continue independent work.
9. Write only material takeaways, once, to their owner. Routine mail writes nothing. A reported fact is not a verified identity update, a hedge is not a decision, and never set an unstated stage. See [Commitment updates and takeaway routing](../../references/inbox-follow-through-details.md) for CRM-specific routes and distinctions.
10. For mailbox maintenance, audit a random 2% of previously suppressed mail (at least 5, or all if fewer). This default is not proof of safety. One that needed action is a misfile: demote that group to read-individually, pull the message out, handle it, and count it as misfiled.
11. A rule that archives or hides without reading is a company decision: submit_company_work_checkpoint decision subject inbox.suppress:<sender-or-list-slug>, the group key, sample evidence, layer L2, authority "agent", reviewBy at most 30 days away, superseding the current one. Without a current decision the group is read individually.
12. Report: what needs the user (type, owner, deadline, due first), what is owed by and to them, and what you wait on. Put these counts in the run output: groups, sampled, pulledOut, suppressed, audited, misfiled, obligations written, superseded and refused.

## Acceptance

- [ ] no message was suppressed from headers alone: every suppressed group was sampled and outlier-scanned
- [ ] known parties, people the user has written to and threads the user is on were read individually
- [ ] material commitments remain findable through suitable existing work or reminders; optional terms preserve source, known promisor and supplied date precision without duplicating the outcome
- [ ] an awaiting obligation carries waitingOn and chaseAt and is not in Needs-you
- [ ] completed work stays terminal on replay; genuinely new commitments use explicit successor lineage, while an erroneous completion follows the supported correction route
- [ ] takeaways reach their owner only when important: routine mail writes nothing to the CRM or context; a deferral is a track, a stop is a permission, an owner decision is a quoted decision

See [Owner checks](references/owner-checks.md).
## References
- [Commitment updates and takeaway routing](../../references/inbox-follow-through-details.md)
