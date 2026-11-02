---
name: "cady-gtm-warm-email"
description: "Warm email and follow-ups. Use when: Write email follow-ups, engaged notes, or partner, organiser and supplier business messages, including first approaches. Not for: A customer cold first touch, a reply in a live thread, or LinkedIn. Missing history is not proof that a party is cold."
license: "MPL-2.0"
compatibility: "Requires Cady (app.cadyworks.com/mcp)"
metadata:
  cady-id: "skill.gtm.warm_email"
  version: "caae526041e911295cc8"
  library: "0a992a8af46752b9"
  function: "gtm"
---
# Warm email and follow-ups

**Company context:** `context_read({"area": "gtm/outreach", "task": "<what you are about to do, in one sentence>", "knownMethods": {"skill.gtm.warm_email": "caae526041e911295cc8@0a992a8af46752b9"}})`

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
3. For an engaged route, confirm engagement from a readable thread or CRM interaction and state it; for a first partner approach, state that no exchange is evidenced; missing history is not proof the party is cold. Attribution links record human and non-human clicks separately and only human clicks count as engagement; file external clicks with crm_interactions_create.
4. For an existing exchange, read it with crm_communications_find and crm.get_communication. For a product link, check sign-up first with records_read party:<partyId>; if they signed up, respond to that.
5. For a customer message: When you plan, rank prospects or write customer copy, start from the segment's customer record (`cady-gtm-offer-and-segments` step 2; write it there first if there is none) and write in its words, not the company's terms; the company's own records and calendar describe the sender, not the buyer. Name the record in the review's justification, with any assumed line the message leans on; an assumed need makes the message a test, not a pitch. Each recipient is a member of the segment who passes its disqualifiers, reached by a private route; someone who sells to the segment (a coach, agency or tool) is a partner or competitor, approached only as one and with that purpose; a public comment, reply or post is publishing, not outreach. Write as the named sender; if only a company name is known, say so in the review rather than writing "I'm <company>". A message to one person meets them where they are in that record, from their own record or thread; a fact about their company plus a shared pitch does not. Before review, reread each draft's first sentence: if it is about you, praises them, claims a reaction or shared experience you have no record of, or asks what their own page already answers, rewrite it. Then draft following the copy rules. For a follow-up, name which one this is and apply the follow-up rule (message rules, follow_up): a follow-up to an unengaged non-replier is at most 2, at least 3 days apart and counted toward the cold email quota; one to an engaged recipient is paced to the thread's tempo, not counted and never dropped. Each adds something useful and new. Recheck permission before every review. Judge it with the taste check (../../references/taste-check.md, message part) before review.
6. Before any follow-up run the outcome check (message rules, outcome_check), then read records_read party:<partyId>. Preparation: RECIPIENTS_EXCLUDED for destination_invalid, opted_out, suppressed; held by skill_required, claim_required, claim_expired, CAP_REACHED, TRACKED_LINKS_OFF. Not held by no_basis, platform_paused, company_paused, SENDING_ACCOUNT_NOT_CONFIRMED, sender_missing, destination_unverified, deferred, recent_contact, replied_since_release, already_sent_in_cycle, executor_unavailable. Prepare with crm_outreach_review_prepare (a follow-up carries followUp {delayDays, nonRepliersOnly: true}), read crm.get_outreach_review, then follow release.

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
