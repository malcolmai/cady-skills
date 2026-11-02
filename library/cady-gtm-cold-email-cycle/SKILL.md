---
name: "cady-gtm-cold-email-cycle"
description: "Cold email cycle. Use when: Write and send cold email to people not yet contacted, one template per segment; fix bounces, spam or deliverability. Not for: Engaged parties, partner or organiser business approaches, replies in a live thread, and every follow-up; use `cady-gtm-warm-email` for partner approaches and follow-ups, or `cady-gtm-reply` for inbound replies. Missing verification holds release, not held preparation."
license: "MPL-2.0"
compatibility: "Requires Cady (app.cadyworks.com/mcp)"
metadata:
  cady-id: "skill.gtm.cold_email_cycle"
  version: "308af8c15f27c8211159"
  library: "9c2ba6e6a0d1e0d3"
  function: "gtm"
---
# Cold email cycle

**Point:** Earn replies from strangers with one honest, segment-true reason, learning each cycle what works, without harming sender reputation.

**Company context:** `context_read({"area": "gtm/outreach", "task": "<what you are about to do, in one sentence>", "knownMethods": {"skill.gtm.cold_email_cycle": "308af8c15f27c8211159@9c2ba6e6a0d1e0d3"}})`

Write and send cold email to people not yet contacted, one template per segment; fix bounces, spam or deliverability.

**Not for:** Engaged parties, partner or organiser business approaches, replies in a live thread, and every follow-up; use `cady-gtm-warm-email` for partner approaches and follow-ups, or `cady-gtm-reply` for inbound replies. Missing verification holds release, not held preparation.

**Unit of work:** one work item per segment and cycle, 50 or fewer Recipients. **Kind:** execution. **Parallel:** yes. **Can release:** yes. 

## Inputs

### Evidence refs

- crm:list:<listId> or crm:party:<partyId> (50 or fewer)
- core:direction ref

### Work fields

- cycleKey
- segmentKey
- senderLabel
- reason or offer

## Procedure

1. Use a work item bound to `cady-gtm-cold-email-cycle`. If starting one, call work_create with this methodId, its current methodVersion, segment, cycle and evidence refs.
2. Read direction and List; the review's Recipients come from reachable Candidates and a grant’s scope is its Audience. Run the outcome check on prior releases (message rules, outcome_check) and read records_read party:<partyId>. Exclude opted-out, suppressed, engaged contacts, prior touches and missing names, each with a reason. Keep no_basis, deferred and unverified destinations visible as held Recipients under the CRM preparation readiness rules. List hygiene: verify every address before its first send (message rules, permission); keep catch-all a small share of the Recipients; skip role inboxes (info, sales, support); never buy a list; re-verify data older than about 90 days.
3. Check the sender before the first release and after any change, as the deliverability reference says (`../../references/cold-deliverability.md`): a secondary sending domain, SPF, DKIM and DMARC passing on a test send, and a warmed-up mailbox. Cady cannot see DNS or reputation, so the user or host checks and you record what was shown. Missing mailbox or verification holds release; continue native review preparation. The company quota below still binds.
4. When you plan, rank prospects or write customer copy, start from the persona's profile and insight (`cady-gtm-persona-profile`; write it there first if none) and write in its words, not the company's; the company's records and calendar describe the sender, not the buyer. A profile not yet checked by a fresh helper is marked unchecked in the held review before copy uses it. Name the persona's profile in the review's justification with any inferred or unknown line the message leans on; that line becomes the message's question, never a claim about the recipient. Each recipient is a member of the persona who passes its disqualifiers, reached by a private route; someone who sells to the persona is not a member of it, so its copy and evidence do not apply, but may be a candidate persona of their own, approached only as a partner or competitor, with that purpose; a public comment, reply or post is publishing, not outreach. Write as the named sender; if only a company name is known, say so in the review. A message to one person meets them where they are in that profile, from their own record or thread, not a company fact plus a shared pitch. Run the draft check (message rules) before the taste check. From what starts their search (profile part 4), draft two or three framings of why this may matter to them now, then write one plain template with an easy_yes ask. An offer is optional. In cold_template mode the reason belongs to the persona, so people who share it get their own segmentKey (the persona_key). Plain text, no images or attachments, at most one link. Judge it with the taste check (../../references/taste-check.md, message part) before review.
5. Choose one to three variants. Shares are guidance: about 40/30/30 early; consider 70/20/10 only after a winner holds for two cycles. Small arms are underpowered; favor large reason or angle differences and qualitative reply learning.
6. Preparation: RECIPIENTS_EXCLUDED for destination_invalid, opted_out, suppressed; held by skill_required, claim_required, claim_expired, CAP_REACHED, TRACKED_LINKS_OFF. Not held by no_basis, platform_paused, company_paused, SENDING_ACCOUNT_NOT_CONFIRMED, sender_missing, destination_unverified, deferred, recent_contact, replied_since_release, already_sent_in_cycle, executor_unavailable. Prepare crm_outreach_review_prepare with mode 'cold_template', cycleKey, segmentKey, variants, proof and listId or partyIds. For a linked template, include trackedLink {destination: '<final https>'}. Do not provide recipientBodies. Cold first touch follows the shared 30-day release cycle per party and channel; cycleKey groups results only. Follow-ups never go in the cycle (the follow-up rule). The company cold email quota is 100 recipients per rolling day and 500 per rolling week, with no lifetime total; above it, use a sender the owner chooses and authorizes and record its outcomes as outcome_check says.
7. Read crm.get_outreach_review(approvalId); check samples, exclusions and remaining cap; fix refusals and prepare again.
8. At mid-cycle and end, read crm.get_outreach_review({cycleKey}). Each variant, segment and channel row counts sends to closed parties as touched and advancing (a definitive result followed before the next send), plus won and lost parties; these are counts, not shares. Decide keep, scale or kill by variant with denominators, underpowered flags and receipts on this work item; never scale on small samples or reply noise.
9. Release: RELEASE_PAUSED for platform_paused, company_paused; held by SENDING_ACCOUNT_NOT_CONFIRMED, skill_required, claim_required, claim_expired, NO_CONTACT_BASIS, QUOTE_UNVERIFIED, SENDER_MISSING, DESTINATION_UNVERIFIED, CONTACT_DEFERRED, RECENT_CONTACT, REPLIED_SINCE_RELEASE, ALREADY_SENT_IN_CYCLE, CAP_REACHED, APPROVAL_EXPIRED, GRANT_NOT_ACTIVE, TRACKED_LINKS_OFF. Release as in release: a release is first contact and creates the Prospect track if missing. Server and device executors add each recipient's tracked link and unsubscribe header; never edit them. Sending with your own connector (route A), put the minted link from crm.get_outreach_review in the email with descriptive anchor text. Record learning before next cycle.
10. Pause rules: stop cold sending from the affected mailbox at once, and pause any active grant with crm_outreach_grants_update action 'pause', when a send shows hard bounces above 2%, spam complaints above 0.1% (0.3% is the large mailbox providers' ceiling, not a target), provider blocks, a blocklist listing or a low reputation reading; then follow the recovery in `../../references/cold-deliverability.md`. Never switch to a fresh domain or mailbox to keep sending the same list.

## Acceptance

- [ ] (check) one exact cold-template review is prepared and readable, with an easy yes
- [ ] (fresh) a reader who sees only the template and the profile's quoted words can say what is asked, why now and how to answer, and recognises the words as the customer's own
- [ ] (check) the template passes Cady's copy check, with one ask and at most one sourced reason, and the review's justification names the persona's profile and any assumed line it leans on
- [ ] (check) the domain passes SPF, DKIM and DMARC on a test send, the mailbox is warmed up, complaints stay under 0.3% (pause above 0.1%) and no pause rule is tripped
- [ ] (check) every excluded party has a reason
- [ ] (check) the cycle and assigned variant are visible for each recipient
- [ ] (person) nothing is released before the person, or a grant covering the exact text, has approved it

## Owner checks

- permission, engagement, cycle and cap rechecked by CRM
- opt-out line on every rendered body

## Result

### Artifact refs

- crm:outreach_review:<approvalId>
- crm:outreach_cycle:<cycleKey>
- **Transition:** the claim holder reports the review, cycle results and next direction decision

## References
- Read [Copy](references/copy.md) when you write the cold template.
- Read [Cold email deliverability](../../references/cold-deliverability.md) when before the first cycle, after a sender change, or when bounces, complaints or blocks appear.
- Read [Outreach message rules](../../references/outreach-message-rules.md) when you draft, review or prepare any message (read first).
- Read [Taste check](../../references/taste-check.md) when judging a draft or design before review.
