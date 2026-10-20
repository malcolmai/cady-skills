---
name: "cady-gtm-cold-email-cycle"
description: "Cold email cycle. Use when: Prepare a cold email cycle for parties CRM verifies as cold. Not for: Engaged or unverified parties, replies, and any follow-up (engaged or non-responder); use `cady-gtm-warm-email` or `cady-gtm-reply`."
license: "MPL-2.0"
compatibility: "Requires Cady (app.cadyworks.com/mcp)"
metadata:
  cady-id: "skill.gtm.cold_email_cycle"
  version: "c629350213704352539f8d98c26a563e841f7e22911d28861836cfdfca71a52e"
  function: "gtm"
---
# Cold email cycle

Prepare a cold email cycle for parties CRM verifies as cold.

**Not for:** Engaged or unverified parties, replies, and any follow-up (engaged or non-responder); use `cady-gtm-warm-email` or `cady-gtm-reply`.

**Unit of work:** one work item per segment and cycle, cohort of 50 or fewer parties. **Kind:** execution. **Parallel:** yes. **Can release:** yes. 

## Always

- Read the sender's voice pack first (crm.manage_voice_pack, mode read) and write in it.

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

1. Use a work item bound to `cady-gtm-cold-email-cycle`. If starting one, call submit_company_work_checkpoint with this methodId, its current methodVersion, the segment, cycle and evidence refs. Work this item under the run sequence (claim, checkpoint, close); read `cady-core-run-sequence` if it is not in your context.
2. Read direction and List, scan replies via crm.list_parties mode interactions, read crm.get_party. Exclude opted-out, suppressed, deferred, engaged or unresolved unverified contacts, prior touches and missing names, each with a reason. List hygiene: verify every address before its first send; catch-all stays a small share of a cohort; skip role inboxes (info, sales, support) and never buy a list; re-verify data older than about 90 days, since business addresses decay a few percent a month.
3. Check the sender before the first cycle and after any change; Cady cannot see DNS or mailbox reputation, so the user or host checks and you record what was shown. Domain: cold mail goes from a secondary domain that redirects to the main site, at least two weeks old, so a reputation hit never reaches the main domain's team and product mail. Authentication: SPF lists only the real senders (one record, under 10 lookups); DKIM signs with the From domain (2048-bit); DMARC exists with reporting, p=none first, quarantine once aligned. Verify on a test send to a seed mailbox that SPF, DKIM and DMARC all show pass. Warm-up: a new mailbox sends normal human mail for two to four weeks first, then cold at about 10 a day, rising by about 10 a day each week to 30 to 50 per mailbox at most; add mailboxes rather than push one harder. The company caps below still bind.
4. Draft two or three framings of an honest reason to contact this segment, choose by the shared_core framing and recipient test, then write one plain template with an easy_yes ask. An offer is optional; no trigger, per-person research or AI personalisation; first read about two seconds. Plain text, no images or attachments, at most one link.
5. Choose one to three variants. Shares are guidance: about 40/30/30 early; consider 70/20/10 only after a winner holds for two cycles. Small arms are underpowered; favor large reason or angle differences and qualitative reply learning.
6. Preparation: RECIPIENTS_EXCLUDED for no_basis, destination_unverified, destination_invalid, opted_out, suppressed, deferred, recent_contact; held by SENDING_ACCOUNT_NOT_CONFIRMED, skill_required, claim_required, claim_expired, REPLIED_SINCE_RELEASE, CAP_REACHED, TRACKED_LINKS_OFF. Not held by platform_paused, company_paused, executor_unavailable. Prepare crm.prepare_outreach_review with mode 'cold_template', cycleKey, segmentKey, variants, proof and listId or partyIds. For a linked template, include trackedLink {destination: '<final https>'}. Do not provide recipientBodies. Cold first touch follows the shared 30-day release cycle per party and channel; cycleKey groups results only. followUp is refused in cold_template mode. The shared company email ceilings are 100 recipients per rolling day, 500 per rolling week and 2,000 total. Above that, use a sender such as Instantly and record its outcomes as outcome_check says.
7. Read crm.get_outreach_review(approvalId); check samples, exclusions and remaining cap. Fix refusals and prepare again.
8. At mid-cycle and end, read crm.get_outreach_review({cycleKey}). Decide keep, scale or kill by variant with denominators, underpowered flags and receipts on this work item. Do not scale on small samples or reply noise.
9. Release: RECIPIENTS_EXCLUDED for no_basis, destination_unverified; RELEASE_PAUSED for platform_paused, company_paused; held by SENDING_ACCOUNT_NOT_CONFIRMED, skill_required, claim_required, claim_expired, REPLIED_SINCE_RELEASE, CAP_REACHED, APPROVAL_EXPIRED, GRANT_NOT_ACTIVE, TRACKED_LINKS_OFF. Release as in release. Then read crm.get_outreach_review and put each recipient's minted link in their email, prefixed by the company app origin shown in the tool description. It redirects immediately with UTMs and cref; human and non-human clicks are recorded and reported separately, and only human clicks count as engagement. Use descriptive anchor text, never a raw URL or misleading domain. Record learning before next cycle.
10. Pause rules: stop cold sending from the affected mailbox at once, and pause any active grant with crm.manage_outreach_grant action 'pause', when a send shows hard bounces above 2%, spam complaints above 0.1% (0.3% is the large mailbox providers' ceiling, not a target), provider blocks or rate-limit codes (550 5.7.x, 421 4.7.x), a blocklist listing, or the host's reputation tool showing low or bad. A flagged mailbox: keep only one-to-one replies on it; find the cause (stale list, volume jump, broken authentication, links or images, complaint-prone copy); fix it; wait for one to two weeks of clean normal mail; then ask the owner to resume (action: 'request_resume') at half the previous volume. Never switch to a fresh domain or mailbox to keep sending the same list. Tell the owner what tripped and the evidence.

## Acceptance

- [ ] one exact cold-template review is prepared and readable, with an honest reason and an easy yes, awaiting owner approval
- [ ] sender authentication passes on a test send, the mailbox is past warm-up, and no pause rule is tripped
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
- [Outcome check](../../references/outcome-check.md)
- [Permission](../../references/permission.md)
- [Release](../../references/release.md)
- [Shared core](../../references/shared-core.md)

**Company context:** `get_cady_context({"area": "gtm/outreach", "task": "<what you are about to do, in one sentence>", "knownMethods": {"skill.gtm.cold_email_cycle": "c629350213704352539f8d98c26a563e841f7e22911d28861836cfdfca71a52e"}})`
