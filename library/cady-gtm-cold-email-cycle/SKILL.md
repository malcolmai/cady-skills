---
name: "cady-gtm-cold-email-cycle"
description: "Cold email cycle. Use when: Write and send cold email to people not yet contacted, one template per segment; fix bounces, spam or deliverability. Not for: Engaged or unverified parties, replies in a live thread, and every follow-up, which goes as its own review through `cady-gtm-warm-email`."
license: "MPL-2.0"
compatibility: "Requires Cady (app.cadyworks.com/mcp)"
metadata:
  cady-id: "skill.gtm.cold_email_cycle"
  version: "a926735def0c6561af08"
  library: "55ee7488e450b058"
  function: "gtm"
---
# Cold email cycle

**Company context:** `get_cady_context({"area": "gtm/outreach", "task": "<what you are about to do, in one sentence>", "knownMethods": {"skill.gtm.cold_email_cycle": "a926735def0c6561af08@55ee7488e450b058"}})`

Write and send cold email to people not yet contacted, one template per segment; fix bounces, spam or deliverability.

**Not for:** Engaged or unverified parties, replies in a live thread, and every follow-up, which goes as its own review through `cady-gtm-warm-email`.

**Unit of work:** one work item per segment and cycle, cohort of 50 or fewer parties. **Kind:** execution. **Parallel:** yes. **Can release:** yes. 

## Inputs

### Evidence refs

- crm:list:<listId> or crm:party:<partyId> (50 or fewer)
- core:direction ref

### Statement fields

- cycleKey
- segmentKey
- senderLabel
- reason or offer

## Procedure

1. Read the shared message rules (`../../references/outreach-message-rules.md`) first: voice pack, consent, release.
2. Use a work item bound to `cady-gtm-cold-email-cycle`. If starting one, call submit_company_work_checkpoint with this methodId, its current methodVersion, segment, cycle and evidence refs.
3. Read direction and List, run the outcome check on prior releases (message rules, outcome_check) and read crm.get_party. Exclude opted-out, suppressed, deferred, engaged or unresolved unverified contacts, prior touches and missing names, each with a reason. List hygiene: verify every address before its first send (message rules, permission); keep catch-all a small share of a cohort; skip role inboxes (info, sales, support); never buy a list; re-verify data older than about 90 days.
4. Check the sender before the first cycle and after any change, as the deliverability reference says (`../../references/cold-deliverability.md`): a secondary sending domain, SPF, DKIM and DMARC passing on a test send, and a warmed-up mailbox. Cady cannot see DNS or reputation, so the user or host checks and you record what was shown. The company quota below still binds.
5. Draft two or three framings of an honest reason to contact this segment, choose by the shared_core framing and recipient test, then write one plain template with an easy_yes ask. An offer is optional. Personalise at most at the account level, with one sourced reason (a dated, cited fact about the account that explains why now); in cold_template mode that reason belongs to the segment, so give accounts that share it their own segmentKey. No flattery, fake familiarity, person-level trivia or AI personalisation. Plain text, no images or attachments, at most one link.
6. Choose one to three variants. Shares are guidance: about 40/30/30 early; consider 70/20/10 only after a winner holds for two cycles (a practitioner heuristic, unverified). Small arms are underpowered; favor large reason or angle differences and qualitative reply learning.
7. Preparation: RECIPIENTS_EXCLUDED for no_basis, destination_unverified, destination_invalid, opted_out, suppressed, deferred, recent_contact; held by SENDING_ACCOUNT_NOT_CONFIRMED, skill_required, claim_required, claim_expired, REPLIED_SINCE_RELEASE, CAP_REACHED, TRACKED_LINKS_OFF. Not held by platform_paused, company_paused, executor_unavailable. Prepare crm.prepare_outreach_review with mode 'cold_template', cycleKey, segmentKey, variants, proof and listId or partyIds. For a linked template, include trackedLink {destination: '<final https>'}. Do not provide recipientBodies. Cold first touch follows the shared 30-day release cycle per party and channel; cycleKey groups results only. Follow-ups never go in the cycle (the follow-up rule). The company cold email quota is 100 recipients per rolling day and 500 per rolling week, with no lifetime total; above it, use a sender such as Instantly and record its outcomes as outcome_check says.
8. Read crm.get_outreach_review(approvalId); check samples, exclusions and remaining cap; fix refusals and prepare again.
9. At mid-cycle and end, read crm.get_outreach_review({cycleKey}). Decide keep, scale or kill by variant with denominators, underpowered flags and receipts on this work item; never scale on small samples or reply noise.
10. Release: RECIPIENTS_EXCLUDED for no_basis, destination_unverified; RELEASE_PAUSED for platform_paused, company_paused; held by SENDING_ACCOUNT_NOT_CONFIRMED, skill_required, claim_required, claim_expired, REPLIED_SINCE_RELEASE, CAP_REACHED, APPROVAL_EXPIRED, GRANT_NOT_ACTIVE, TRACKED_LINKS_OFF. Release as in release. Server and device executors add each recipient's tracked link and unsubscribe header; never edit them. Sending with your own connector (route A), put the minted link from crm.get_outreach_review in the email with descriptive anchor text. Only human clicks count as engagement. After a send settles, set each recipient's follow-up with crm.set_track (nextActionDueAt = send time plus 4 days) so the due follow-ups view lists it; closing the track (won, lost, not yet) clears that marker. Record learning before next cycle.
11. Pause rules: stop cold sending from the affected mailbox at once, and pause any active grant with crm.manage_outreach_grant action 'pause', when a send shows hard bounces above 2%, spam complaints above 0.1% (0.3% is the large mailbox providers' ceiling, not a target), provider blocks, a blocklist listing or a low reputation reading; then follow the recovery in `../../references/cold-deliverability.md`. Never switch to a fresh domain or mailbox to keep sending the same list.

## Acceptance

- [ ] one exact cold-template review is prepared and readable, with an honest reason and an easy yes
- [ ] the template is under 120 words with one ask and at most one sourced account-level reason
- [ ] the domain passes SPF, DKIM and DMARC on a test send, the mailbox is warmed up, complaints stay under 0.3% (pause above 0.1%) and no pause rule is tripped
- [ ] every excluded party has a reason
- [ ] the cycle and assigned variant are visible for each recipient
- [ ] nothing is released before approval

## Owner checks

- WORK_NOT_FOUND
- METHOD_NOT_CURRENT
- SKILL_CHANNEL_MISMATCH
- COLD_NO_FOLLOW_UP
- COLD_PAUSED
- permission, engagement, cycle and cap rechecked by CRM
- opt-out line on every rendered body

## Result

### Artifact refs

- crm:outreach_review:<approvalId>
- crm:outreach_cycle:<cycleKey>
- **Transition:** the claim holder reports the review, cycle results and next direction decision

## References
- [Copy](references/copy.md)
- [Cold email deliverability](../../references/cold-deliverability.md)
- [Outreach message rules](../../references/outreach-message-rules.md)
