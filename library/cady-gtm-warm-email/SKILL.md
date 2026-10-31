---
name: "cady-gtm-warm-email"
description: "Warm email and follow-ups. Use when: Write email follow-ups, engaged notes, or partner, organiser and supplier business messages, including first approaches. Not for: A customer cold first touch, a reply in a live thread, or LinkedIn. Missing history is not proof that a party is cold."
license: "MPL-2.0"
compatibility: "Requires Cady (app.cadyworks.com/mcp)"
metadata:
  cady-id: "skill.gtm.warm_email"
  version: "5d226c66b198c5c0fc52"
  library: "f7ed85a0f29eb359"
  function: "gtm"
---
# Warm email and follow-ups

**Company context:** `get_cady_context({"area": "gtm/outreach", "task": "<what you are about to do, in one sentence>", "knownMethods": {"skill.gtm.warm_email": "5d226c66b198c5c0fc52@f7ed85a0f29eb359"}})`

Write email follow-ups, engaged notes, or partner, organiser and supplier business messages, including first approaches.

**Not for:** A customer cold first touch, a reply in a live thread, or LinkedIn. Missing history is not proof that a party is cold.

**Unit of work:** one work item per party or small cohort. **Kind:** execution. **Parallel:** yes. **Can release:** yes. 

## Inputs

### Evidence refs

- crm:party:<partyId>
- readable communication or relationship-track ref, or sourced partner/supplier purpose for a first approach

### Work fields

- senderLabel
- relationship or first-approach purpose evidence
- next action

## Procedure

1. Read the shared message rules (`../../references/outreach-message-rules.md`) first: voice pack, consent, release.
2. The scheduled pass is `cady-gtm-pipeline-pass`. Partner and organiser approaches use this skill even without prior engagement: record the partner purpose and sourced relationship facts, without claiming a prior exchange. Supplier business messages use it too; for a cancellation, order or commitment obtain the exact user review `cady-finance-vendor-spend-review` requires (a standing outreach grant does not substitute). Use a work item bound to `cady-gtm-warm-email` and claim it before preparation.
3. For an engaged route, confirm engagement from a readable thread or CRM interaction and state it; for a first partner approach, state that no exchange is evidenced; missing history is not proof the party is cold. Attribution links record human and non-human clicks separately and only human clicks count as engagement; file external clicks with crm.record_interactions.
4. For an existing exchange, read it with crm.find_communications and crm.get_communication. For a product link, check sign-up first with crm.get_party; if they signed up, respond to that.
5. Draft following the copy rules. For a follow-up, name which one this is and apply the follow-up rule (message rules, follow_up): a follow-up to an unengaged non-replier is at most 2, at least 3 days apart and counted toward the cold email quota; one to an engaged recipient is paced to the thread's tempo, not counted and never dropped. Each adds something useful and new. Recheck permission before every review. Judge it with the taste check (../../references/taste-check.md, message part) before review.
6. Before any follow-up run the outcome check (message rules, outcome_check), then read crm.get_party. Preparation: RECIPIENTS_EXCLUDED for destination_invalid, opted_out, suppressed; held by skill_required, claim_required, claim_expired, CAP_REACHED, TRACKED_LINKS_OFF. Not held by no_basis, platform_paused, company_paused, SENDING_ACCOUNT_NOT_CONFIRMED, sender_missing, destination_unverified, deferred, recent_contact, replied_since_release, already_sent_in_cycle, executor_unavailable. Prepare with crm.prepare_outreach_review (a follow-up carries followUp {delayDays, nonRepliersOnly: true}), read crm.get_outreach_review, then follow release.

## Acceptance

- [ ] (check) readable CRM evidence supports the relationship or partner/supplier business route
- [ ] (check) one personal next step is prepared per recipient
- [ ] (fresh) a reader who sees only the draft and the thread can say what is new in it and what next step it asks for
- [ ] (check) track stage and next action remain evidence-backed
- [ ] (person) nothing is released before the person, or a grant covering the exact text, has approved it

## Owner checks

- readable engagement evidence or sourced partner/supplier business purpose
- product sign-up checked before a trial nudge
- current contact permission

## Result

### Artifact refs

- crm:outreach_review:<approvalId>
- crm:relationship_track:<trackId>
- **Transition:** the claim holder reports prepared reviews and track updates

## References
- Read [Copy](references/copy.md) when you draft the follow-up.
- Read [Outreach message rules](../../references/outreach-message-rules.md) when you draft, review or prepare any message (read first).
- Read [Taste check](../../references/taste-check.md) when judging a draft or design before review.
