---
name: "cady-gtm-warm-email"
description: "Warm email. Use when: Continue an engaged relationship, or follow up a released cold touch that got no reply. Not for: A first cold touch (use `cady-gtm-cold-email-cycle`), or unverified engagement. Do not treat missing history as proof that a party is cold."
license: "MPL-2.0"
compatibility: "Requires Cady (app.cadyworks.com/mcp)"
metadata:
  cady-id: "skill.gtm.warm_email"
  version: "89862c7ff86559d0aec393bf2b94a4240deb8a0bbf2302719afb00c2fce9270e"
  library: "3beca7fa80e90672"
  function: "gtm"
---
# Warm email

**Company context:** `get_cady_context({"area": "gtm/outreach", "task": "<what you are about to do, in one sentence>", "knownMethods": {"skill.gtm.warm_email": "89862c7ff86559d0aec393bf2b94a4240deb8a0bbf2302719afb00c2fce9270e"}})`

Continue an engaged relationship, or follow up a released cold touch that got no reply.

**Not for:** A first cold touch (use `cady-gtm-cold-email-cycle`), or unverified engagement. Do not treat missing history as proof that a party is cold.

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
2. The scheduled pass is `cady-gtm-pipeline-pass`.
3. Confirm engagement from a readable thread or CRM interaction and state it; missing history is not proof the party is cold. Attribution links record human and non-human clicks separately and only human clicks count as engagement; file external clicks with crm.record_interactions.
4. Read the exchange with crm.find_communications and crm.get_communication. For a product link, check sign-up first with crm.get_party; if they signed up, respond to that.
5. Draft following the copy rules. A follow-up comes after the previous touch, adds something useful and new, and stops on a reply, no, opt-out or suppression; an engaged, interested lead has no count limit and is never dropped. A non-responder to a cold touch gets 1-2 follow-ups only, within the grant's followUps (delayDays 3 or more), only after outcome_check finds no reply, counted in the cold daily cap. Recheck permission before every review.
6. Scan replies via crm.list_parties mode interactions; read crm.get_party. Preparation: RECIPIENTS_EXCLUDED for no_basis, destination_unverified, destination_invalid, opted_out, suppressed, deferred, recent_contact; held by SENDING_ACCOUNT_NOT_CONFIRMED, skill_required, claim_required, claim_expired, REPLIED_SINCE_RELEASE, CAP_REACHED, TRACKED_LINKS_OFF. Not held by platform_paused, company_paused, executor_unavailable. Prepare with crm.prepare_outreach_review, read crm.get_outreach_review, then follow release.

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
