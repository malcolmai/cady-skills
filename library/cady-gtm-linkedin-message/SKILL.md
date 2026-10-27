---
name: "cady-gtm-linkedin-message"
description: "LinkedIn message. Use when: Draft a LinkedIn connection note or direct message to one person, or its one follow-up; pacing and invitation limits. Not for: Public LinkedIn posts, email, or a reply in a live thread; cold email uses `cady-gtm-cold-email-cycle`."
license: "MPL-2.0"
compatibility: "Requires Cady (app.cadyworks.com/mcp)"
metadata:
  cady-id: "skill.gtm.linkedin_message"
  version: "7ed58946267f43b8e780"
  library: "a9ede08c00c06027"
  function: "gtm"
---
# LinkedIn message

**Company context:** `get_cady_context({"area": "gtm/outreach", "task": "<what you are about to do, in one sentence>", "knownMethods": {"skill.gtm.linkedin_message": "7ed58946267f43b8e780@a9ede08c00c06027"}})`

Draft a LinkedIn connection note or direct message to one person, or its one follow-up; pacing and invitation limits.

**Not for:** Public LinkedIn posts, email, or a reply in a live thread; cold email uses `cady-gtm-cold-email-cycle`.

**Unit of work:** one work item per cohort of 20 or fewer. **Kind:** execution. **Parallel:** yes. **Can release:** yes. 

## Always

- In a review body, put a line with only --- between messages.

## Inputs

### Evidence refs

- crm:list:<listId> or crm:party:<partyId>
- profile or shared-context refs

### Work fields

- relationship state
- senderLabel
- what is new

## Procedure

1. Read the shared message rules (`../../references/outreach-message-rules.md`) first: voice pack, consent, release.
2. Read the profile and available context. Use genuine common ground such as a shared event, past employer, school or interest in their posts. Mention a mutual connection only when they have identified it. Never invent closeness.
3. A connection note gives one honest reason to connect, with no pitch, ask or company name. For a first message to an existing connection, use a subtle personal note about what you are working on, why it may be relevant, and that you would be glad to chat sometime. Avoid product names and links. Judge it with the taste check (../../references/taste-check.md, message part) before review.
4. Read crm.get_party for every recipient. Exclude and explain a recorded opt-out or destination suppression; never overwrite it.
5. Pace like a person within the company's LinkedIn caps: 20 connection requests per rolling day, and 100 per rolling week, spread across working hours (the review holds anything over them); tell the owner which invitations have been pending over three weeks so they can withdraw them; a falling acceptance rate means the targeting or note is wrong, not that volume should rise.
6. Preparation: RECIPIENTS_EXCLUDED for destination_invalid, opted_out, suppressed; held by skill_required, claim_required, claim_expired, CAP_REACHED, TRACKED_LINKS_OFF. Not held by no_basis, platform_paused, company_paused, SENDING_ACCOUNT_NOT_CONFIRMED, sender_missing, destination_unverified, deferred, recent_contact, replied_since_release, already_sent_in_cycle, executor_unavailable. Prepare one body per recipient with crm.prepare_outreach_review and read it with crm.get_outreach_review; keep connection notes, first messages and follow-ups in distinct cohorts. Give prepare a one-line justification (why this send now). Then follow release.
7. LinkedIn send with your own connector, in order: prepare; confirm it (self-approve in notify mode with crm.outreach.confirm, an active grant, or the person's review); only then send exactly the approved text with your own LinkedIn connector, never before and never to a party the confirmed review does not cover; note each send with crm.record_interactions (kind note, approvalId) then schedule the follow-up with crm.set_track so it shows in the due follow-ups view; details as outreach_release says. Cady keeps no release ledger or cap count here, so hold the 20 a day, 100 a week pacing yourself. With no LinkedIn connector, run crm.execute_approved_outreach with executor device and the user's `cady exec <ticket>` sends instead.
8. Allow one follow-up only, with something new, under the follow-up rule (message rules, follow_up), after the outcome check has read the thread. Anyone who replies leaves follow-up and moves to `cady-gtm-reply`. Recheck permission and suppression before preparing.
9. Stop rule: a security challenge (verify identity, CAPTCHA, forced sign-in), a restriction or warning notice, a weekly-limit or rate-limit message, or an unusual-activity prompt stops all work on that account at once. Prepare and release nothing more on it, pause any active grant with crm.manage_outreach_grant action 'pause', and do not retry, wait it out, or switch tool, account or browser automation. Tell the owner what appeared and when; resume only after the owner confirms the account is clear.

## Acceptance

- [ ] (fresh) copy uses real common ground without invented familiarity
- [ ] (check) connection note has no pitch, ask or company name
- [ ] (check) at most one new follow-up is prepared
- [ ] (check) any challenge, restriction or limit notice stopped all work on the account and the owner was told
- [ ] (person) nothing is released before the person, or a grant covering the exact text, has approved it

## Owner checks

- current contact permission

## Result

### Artifact refs

- crm:outreach_review:<approvalId>
- **Transition:** the claim holder reports the prepared review

## References
- Read [Outreach message rules](../../references/outreach-message-rules.md) when you draft, review or prepare any message (read first).
- Read [Taste check](../../references/taste-check.md) when judging a draft or design before review.
