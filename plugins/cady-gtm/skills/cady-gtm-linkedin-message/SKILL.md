---
name: "cady-gtm-linkedin-message"
description: "Social direct message. Use when: Draft a first social DM or one no-reply follow-up on any non-email channel; LinkedIn connection notes too. Not for: Public posts, email, or a reply in a live thread (`cady-gtm-reply`); cold email uses `cady-gtm-cold-email-cycle`."
license: "MPL-2.0"
compatibility: "Requires Cady (app.cadyworks.com/mcp)"
metadata:
  cady-id: "skill.gtm.linkedin_message"
  version: "6e2160f798ac6cd6d6f3"
  library: "9c2ba6e6a0d1e0d3"
  function: "gtm"
---
# Social direct message

**Point:** Open a real conversation on a social channel with one honest reason, paced so the account stays safe.

**Company context:** `context_read({"area": "gtm/outreach", "task": "<what you are about to do, in one sentence>", "knownMethods": {"skill.gtm.linkedin_message": "6e2160f798ac6cd6d6f3@9c2ba6e6a0d1e0d3"}})`

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

1. Read the profile and available context. Use only common ground that is real and that they would recognise. Mention a mutual connection only when they have identified it. Never invent closeness.
2. For a customer message: When you plan, rank prospects or write customer copy, start from the persona's profile and insight (`cady-gtm-persona-profile`; write it there first if none) and write in its words, not the company's; the company's records and calendar describe the sender, not the buyer. A profile not yet checked by a fresh helper is marked unchecked in the held review before copy uses it. Name the persona's profile in the review's justification with any inferred or unknown line the message leans on; that line becomes the message's question, never a claim about the recipient. Each recipient is a member of the persona who passes its disqualifiers, reached by a private route; someone who sells to the persona is not a member of it, so its copy and evidence do not apply, but may be a candidate persona of their own, approached only as a partner or competitor, with that purpose; a public comment, reply or post is publishing, not outreach. Write as the named sender; if only a company name is known, say so in the review. A message to one person meets them where they are in that profile, from their own record or thread, not a company fact plus a shared pitch. Run the draft check (message rules) before the taste check. A LinkedIn connection note gives one honest reason to connect, with no pitch, ask or company name. For a first direct message, use a subtle personal note about what you are working on, why it may matter where they are now, and that you would be glad to chat sometime. Avoid product names and links. Judge it with the taste check (../../references/taste-check.md, message part) before review.
3. Read records_read party:<partyId> for every recipient. Exclude and explain a recorded opt-out or destination suppression; never overwrite it.
4. Pace like a person within existing channel caps: 20 messages per rolling day and 100 per rolling week, spread across working hours; host sends keep that count too. On LinkedIn, tell the owner which invitations have been pending over three weeks so they can withdraw them. A falling acceptance rate means revising the targeting or note, never raising volume.
5. Preparation: RECIPIENTS_EXCLUDED for destination_invalid, opted_out, suppressed; held by skill_required, claim_required, claim_expired, CAP_REACHED, TRACKED_LINKS_OFF. Not held by no_basis, platform_paused, company_paused, SENDING_ACCOUNT_NOT_CONFIRMED, sender_missing, destination_unverified, deferred, recent_contact, replied_since_release, already_sent_in_cycle, executor_unavailable. Prepare one body per recipient with crm_outreach_review_prepare and read it with crm.get_outreach_review; keep connection notes, first messages and follow-ups in distinct cohorts. Give prepare a one-line justification (why this send now). Then follow release.
6. Social send with your own connector, in order: prepare; confirm it (self-approve in notify mode with crm.outreach.confirm, an active grant, or the person's review); only then send exactly the approved text with your own channel connector, never before and never to a party the confirmed review does not cover; record each explicit outreachOutcome with crm_interactions_create by following readiness.nextAction as outreach_release says, then schedule the follow-up as outreach_release says. Honor the returned holds and the 20 a day, 100 a week pacing. With no channel connector, run crm_outreach_release with executor device and the user's `cady exec <ticket>` sends instead.
7. Allow one follow-up only (account safety; the two-follow-up allowance is for email), with something new, under the follow-up rule (message rules, follow_up), after the outcome check has read the thread. Anyone who replies leaves follow-up and moves to `cady-gtm-reply`. Recheck permission and suppression before preparing.
8. Stop rule: a security challenge (verify identity, CAPTCHA, forced sign-in), a restriction or warning notice, a weekly-limit or rate-limit message, or an unusual-activity prompt stops all work on that account at once. Prepare and release nothing more on it, pause any active grant with crm_outreach_grants_update action 'pause', and do not retry, wait it out, or switch tool, account or browser automation. Tell the owner what appeared and when; resume only after the owner confirms the account is clear.

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
