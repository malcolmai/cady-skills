---
name: "cady-gtm-linkedin-message"
description: "Social direct message. Use when: Draft a first social DM or one no-reply follow-up on any non-email channel; LinkedIn connection notes too. Not for: Public posts, email, or a reply in a live thread (`cady-gtm-reply`); cold email uses `cady-gtm-cold-email-cycle`."
license: "MPL-2.0"
compatibility: "Requires Cady (app.cadyworks.com/mcp)"
metadata:
  cady-id: "skill.gtm.linkedin_message"
  version: "3b60d6eb09950b0eac62"
  library: "d3edf78d7249b663"
  function: "gtm"
---
# Social direct message

**Company context:** `context_read({"area": "gtm/outreach", "task": "<what you are about to do, in one sentence>", "knownMethods": {"skill.gtm.linkedin_message": "3b60d6eb09950b0eac62@d3edf78d7249b663"}})`

Draft a first social DM or one no-reply follow-up on any non-email channel; LinkedIn connection notes too.

**Not for:** Public posts, email, or a reply in a live thread (`cady-gtm-reply`); cold email uses `cady-gtm-cold-email-cycle`.

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
3. For a customer message: When you plan, rank prospects or write customer copy, start from the segment's customer record (`cady-gtm-offer-and-segments` step 2; write it there first if there is none) and write in its words, not the company's terms; the company's own records and calendar describe the sender, not the buyer. Name the record in the review's justification, with any assumed line the message leans on; an assumed need makes the message a test, not a pitch. Each recipient is a member of the segment who passes its disqualifiers, reached by a private route; someone who sells to the segment (a coach, agency or tool) is a partner or competitor, approached only as one and with that purpose; a public comment, reply or post is publishing, not outreach. Write as the named sender; if only a company name is known, say so in the review rather than writing "I'm <company>". A message to one person meets them where they are in that record, from their own record or thread; a fact about their company plus a shared pitch does not. Before review, reread each draft's first sentence: if it is about you, praises them, claims a reaction or shared experience you have no record of, or asks what their own page already answers, rewrite it. A LinkedIn connection note gives one honest reason to connect, with no pitch, ask or company name. For a first direct message, use a subtle personal note about what you are working on, why it may matter where they are now, and that you would be glad to chat sometime. Avoid product names and links. Judge it with the taste check (../../references/taste-check.md, message part) before review.
4. Read records_read party:<partyId> for every recipient. Exclude and explain a recorded opt-out or destination suppression; never overwrite it.
5. Pace like a person within existing channel caps: 20 messages per rolling day and 100 per rolling week, spread across working hours; host sends keep that count too. On LinkedIn, tell the owner which invitations have been pending over three weeks so they can withdraw them; a falling acceptance rate means the targeting or note is wrong, not that volume should rise.
6. Preparation: RECIPIENTS_EXCLUDED for destination_invalid, opted_out, suppressed; held by skill_required, claim_required, claim_expired, CAP_REACHED, TRACKED_LINKS_OFF. Not held by no_basis, platform_paused, company_paused, SENDING_ACCOUNT_NOT_CONFIRMED, sender_missing, destination_unverified, deferred, recent_contact, replied_since_release, already_sent_in_cycle, executor_unavailable. Prepare one body per recipient with crm_outreach_review_prepare and read it with crm.get_outreach_review; keep connection notes, first messages and follow-ups in distinct cohorts. Give prepare a one-line justification (why this send now). Then follow release.
7. Social send with your own connector, in order: prepare; confirm it (self-approve in notify mode with crm.outreach.confirm, an active grant, or the person's review); only then send exactly the approved text with your own channel connector, never before and never to a party the confirmed review does not cover; record each explicit outreachOutcome with crm_interactions_create by following readiness.nextAction as outreach_release says, then schedule the follow-up with crm_tracks_set so it shows in the due follow-ups view. Honor the returned holds and the 20 a day, 100 a week pacing. With no channel connector, run crm_outreach_release with executor device and the user's `cady exec <ticket>` sends instead.
8. Allow one follow-up only, with something new, under the follow-up rule (message rules, follow_up), after the outcome check has read the thread. Anyone who replies leaves follow-up and moves to `cady-gtm-reply`. Recheck permission and suppression before preparing.
9. Stop rule: a security challenge (verify identity, CAPTCHA, forced sign-in), a restriction or warning notice, a weekly-limit or rate-limit message, or an unusual-activity prompt stops all work on that account at once. Prepare and release nothing more on it, pause any active grant with crm_outreach_grants_update action 'pause', and do not retry, wait it out, or switch tool, account or browser automation. Tell the owner what appeared and when; resume only after the owner confirms the account is clear.

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
