---
name: "cady-gtm-linkedin-message"
description: "LinkedIn message. Use when: Prepare a connection note, a first message to a connection, or its single follow-up. Not for: Email or an active email thread; replies in a live thread use `cady-gtm-reply`, and cold email uses `cady-gtm-cold-email-cycle`."
license: "MPL-2.0"
compatibility: "Requires Cady (app.cadyworks.com/mcp)"
metadata:
  cady-id: "skill.gtm.linkedin_message"
  version: "a0d1bc80a9c5a17557f92e1646e0fc90dbaaec74a4be9364792cbe35e8db0243"
  function: "gtm"
---
# LinkedIn message

Prepare a connection note, a first message to a connection, or its single follow-up.

**Not for:** Email or an active email thread; replies in a live thread use `cady-gtm-reply`, and cold email uses `cady-gtm-cold-email-cycle`.

**Unit of work:** one work item per cohort of 20 or fewer. **Kind:** execution. **Parallel:** yes. **Can release:** yes. 

## Always

- Read the sender's voice pack first (crm.manage_voice_pack, mode read) and write in it.
- On LinkedIn and WhatsApp write as people chat: a few short messages, one thought each; never split one thought or merge replies. A connection note is one message.
- In a review body, put a line with only --- between messages.

## Inputs

### Evidence refs

- crm:list:<listId> or crm:party:<partyId>
- profile or shared-context refs

### Statement fields

- relationship state
- senderLabel
- what is new

## Procedure

1. Work this item under the run sequence (claim, checkpoint, close); read `cady-core-run-sequence` if it is not in your context.
2. Read the profile and available context. Use genuine common ground such as a shared event, past employer, school or interest in their posts. Mention a mutual connection only when they have identified it. Never invent closeness.
3. A connection note gives one honest reason to connect, with no pitch, ask or company name. For a first message to an existing connection, use a subtle personal note about what you are working on, why it may be relevant, and that you would be glad to chat sometime. Avoid product names and links.
4. Read crm.get_party for every recipient. Exclude and explain a recorded opt-out or destination suppression; never overwrite it.
5. Pace like a person: about 20 connection requests a day at most, spread across working hours, inside LinkedIn's weekly invitation limit; tell the owner which invitations have been pending over three weeks so they can withdraw them; a falling acceptance rate means the targeting or note is wrong, not that volume should rise.
6. Preparation: RECIPIENTS_EXCLUDED for no_basis, destination_unverified, destination_invalid, opted_out, suppressed, deferred, recent_contact; held by SENDING_ACCOUNT_NOT_CONFIRMED, skill_required, claim_required, claim_expired, REPLIED_SINCE_RELEASE, CAP_REACHED, TRACKED_LINKS_OFF. Not held by platform_paused, company_paused, executor_unavailable. Prepare one body per recipient with crm.prepare_outreach_review and read it with crm.get_outreach_review; keep connection notes, first messages and follow-ups in distinct cohorts. Then follow release.
7. Allow one follow-up only, with something new. Anyone who replies leaves follow-up and moves to `cady-gtm-reply`. Recheck permission and suppression before preparing.
8. Stop rule: a security challenge (verify identity, CAPTCHA, forced sign-in), a restriction or warning notice, a weekly-limit or rate-limit message, or an unusual-activity prompt stops all work on that account at once. Prepare and release nothing more on it, pause any active grant with crm.manage_outreach_grant action 'pause', and do not retry, wait it out, or switch tool, account or browser automation. Tell the owner what appeared and when; resume only after the owner confirms the account is clear.

## Acceptance

- [ ] copy uses real common ground without invented familiarity
- [ ] connection note has no pitch, ask or company name
- [ ] at most one new follow-up is prepared
- [ ] any challenge, restriction or limit notice stopped all work on the account and the owner was told

## Owner checks

- WORK_NOT_FOUND
- METHOD_NOT_CURRENT
- SKILL_CHANNEL_MISMATCH
- current contact permission
- COPY_RULE_FAILED

## Result

### Artifact refs

- crm:outreach_review:<approvalId>
- **Transition:** the claim holder reports the prepared review

## References
- [Outcome check](../../references/outcome-check.md)
- [Permission](../../references/permission.md)
- [Release](../../references/release.md)
- [Shared core](../../references/shared-core.md)

**Company context:** `get_cady_context({"area": "gtm/outreach", "task": "<what you are about to do, in one sentence>", "knownMethods": {"skill.gtm.linkedin_message": "a0d1bc80a9c5a17557f92e1646e0fc90dbaaec74a4be9364792cbe35e8db0243"}})`
