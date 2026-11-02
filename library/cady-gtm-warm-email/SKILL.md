---
name: "cady-gtm-warm-email"
description: "Warm email and follow-ups. Use when: Write email follow-ups, engaged notes, or partner, organiser and supplier business messages, including first approaches. Not for: A customer cold first touch, a reply in a live thread, or LinkedIn. Missing history is not proof that a party is cold."
license: "MPL-2.0"
compatibility: "Requires Cady (app.cadyworks.com/mcp)"
metadata:
  cady-id: "skill.gtm.warm_email"
  version: "c72f6d86d782c639ba56"
  library: "76da591f0f251280"
  function: "gtm"
---
# Warm email and follow-ups

**Point:** Maintain the real relationship respectfully, subtly make clear what we do, and follow up on strong buying or interest signals.

**Company context:** `context_read({"area": "gtm/outreach", "task": "<what you are about to do, in one sentence>", "knownMethods": {"skill.gtm.warm_email": "c72f6d86d782c639ba56@76da591f0f251280"}})`

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

1. The scheduled pass is `cady-gtm-pipeline-pass`. Partner and organiser approaches use this skill even without prior engagement: record the partner purpose and sourced relationship facts, without claiming a prior exchange. Supplier business messages use it too; for a cancellation, order or commitment obtain the exact user review `cady-finance-vendor-spend-review` requires (a standing outreach grant does not substitute). Use a work item bound to `cady-gtm-warm-email` and claim it before preparation.
2. For an engaged route, confirm engagement from a readable thread or CRM interaction and state it; for a first partner approach, state that no exchange is evidenced; missing history is not proof the party is cold. File external clicks with crm_interactions_create.
3. For an existing exchange, read it with crm_communications_find and crm.get_communication. For a product link, check sign-up first with records_read party:<partyId>; if they signed up, respond to that.
4. For a customer message: When you plan, rank prospects or write customer copy, start from the persona's profile and insight (`cady-gtm-persona-profile`; write it there first if none) and write in its words, not the company's; the company's records and calendar describe the sender, not the buyer. A profile not yet checked by a fresh helper is marked unchecked in the held review before copy uses it. Name the persona's profile in the review's justification with any inferred or unknown line the message leans on; that line becomes the message's question, never a claim about the recipient. Each recipient is a member of the persona who passes its disqualifiers, reached by a private route; someone who sells to the persona is not a member of it, so its copy and evidence do not apply, but may be a candidate persona of their own, approached only as a partner or competitor, with that purpose; a public comment, reply or post is publishing, not outreach. Write as the named sender; if only a company name is known, say so in the review. A message to one person meets them where they are in that profile, from their own record or thread, not a company fact plus a shared pitch. Run the draft check (message rules) before the taste check. For a follow-up, name which one this is and apply the follow-up rule (message rules, follow_up). Recheck permission before every review. Judge it with the taste check (../../references/taste-check.md, message part) before review.
5. Each note gives them something useful or new, makes what we do clear in a natural clause, not a pitch, and meets a buying or interest signal (a question, sign-up, stated need) with one concrete next step.
6. Before any follow-up run the outcome check (message rules, outcome_check), then read records_read party:<partyId>. Preparation: RECIPIENTS_EXCLUDED for destination_invalid, opted_out, suppressed; held by skill_required, claim_required, claim_expired, CAP_REACHED, TRACKED_LINKS_OFF. Not held by no_basis, platform_paused, company_paused, SENDING_ACCOUNT_NOT_CONFIRMED, sender_missing, destination_unverified, deferred, recent_contact, replied_since_release, already_sent_in_cycle, executor_unavailable. Prepare with crm_outreach_review_prepare (a follow-up carries followUp {delayDays, nonRepliersOnly: true}), read records_read review:outreach/<subjectId>, then follow release.

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
