---
name: "cady-gtm-warm-email"
description: "Warm email and follow-ups. Use when: Write a follow-up email (to a non-replier or an engaged contact) or the next note in an engaged relationship. Not for: A first touch to a cold party, a reply in a live thread, or LinkedIn. Missing history is not proof that a party is cold."
license: "MPL-2.0"
compatibility: "Requires Cady (app.cadyworks.com/mcp)"
metadata:
  cady-id: "skill.gtm.warm_email"
  version: "0cf26a7c2158f9d28f9ddc2fbe10ae3015cf62da67eca185c179d13ce57b173b"
  library: "b1e7050435d28aef"
  function: "gtm"
---
# Warm email and follow-ups

**Company context:** `get_cady_context({"area": "gtm/outreach", "task": "<what you are about to do, in one sentence>", "knownMethods": {"skill.gtm.warm_email": "0cf26a7c2158f9d28f9ddc2fbe10ae3015cf62da67eca185c179d13ce57b173b"}})`

Write a follow-up email (to a non-replier or an engaged contact) or the next note in an engaged relationship.

**Not for:** A first touch to a cold party, a reply in a live thread, or LinkedIn. Missing history is not proof that a party is cold.

**Unit of work:** one work item per party or small cohort. **Kind:** execution. **Parallel:** yes. **Can release:** yes. 

## Inputs

### Evidence refs

- crm:party:<partyId>
- readable communication or relationship-track ref

### Statement fields

- senderLabel
- relationship evidence
- next action

## Procedure

1. Read the shared message rules (`../../references/outreach-message-rules.md`) first: voice pack, consent, release.
2. The scheduled pass is `cady-gtm-pipeline-pass`. Vendor, supplier and partner messages use this skill too: a CRM role vendor or partner, a business purpose, and for a cancellation, order or commitment the exact user review `cady-finance-vendor-spend-review` requires (a standing outreach grant does not substitute).
3. Confirm engagement from a readable thread or CRM interaction and state it; missing history is not proof the party is cold. Attribution links record human and non-human clicks separately and only human clicks count as engagement; file external clicks with crm.record_interactions.
4. Read the exchange with crm.find_communications and crm.get_communication. For a product link, check sign-up first with crm.get_party; if they signed up, respond to that.
5. Draft following the copy rules. Name which follow-up this is and apply the follow-up rule (message rules, follow_up): a follow-up to an unengaged non-replier is at most 2, at least 3 days apart and counted toward the cold email quota; one to an engaged recipient is paced to the thread's tempo, not counted and never dropped. Each adds something useful and new. Recheck permission before every review.
6. Before any follow-up run the outcome check (message rules, outcome_check), then read crm.get_party. Preparation: RECIPIENTS_EXCLUDED for no_basis, destination_unverified, destination_invalid, opted_out, suppressed, deferred, recent_contact; held by SENDING_ACCOUNT_NOT_CONFIRMED, skill_required, claim_required, claim_expired, REPLIED_SINCE_RELEASE, CAP_REACHED, TRACKED_LINKS_OFF. Not held by platform_paused, company_paused, executor_unavailable. Prepare with crm.prepare_outreach_review (a follow-up carries followUp {delayDays, nonRepliersOnly: true}), read crm.get_outreach_review, then follow release.

## Acceptance

- [ ] readable CRM evidence supports the warm route
- [ ] one personal next step is prepared per recipient
- [ ] track stage and next action remain evidence-backed

## Owner checks

- WORK_NOT_FOUND
- METHOD_NOT_CURRENT
- SKILL_CHANNEL_MISMATCH
- readable engagement evidence
- product sign-up checked before a trial nudge
- current contact permission
- COPY_RULE_FAILED

## Result

### Artifact refs

- crm:outreach_review:<approvalId>
- crm:relationship_track:<trackId>
- **Transition:** the claim holder reports prepared reviews and track updates

## References
- [Copy](references/copy.md)
- [Outreach message rules](../../references/outreach-message-rules.md)
