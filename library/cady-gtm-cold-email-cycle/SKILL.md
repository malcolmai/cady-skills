---
name: "cady-gtm-cold-email-cycle"
description: "Cold email cycle. Use when: Write and send cold email to people not yet contacted, using one template per segment. Not for: Engaged parties, partner or organiser business approaches, replies in a live thread, and every follow-up; use `cady-gtm-warm-email` for partner approaches and follow-ups, or `cady-gtm-reply` for inbound replies. Missing verification holds release, not preparation."
license: "MPL-2.0"
compatibility: "Requires Cady (app.cadyworks.com/mcp)"
metadata:
  cady-id: "skill.gtm.cold_email_cycle"
  version: "b251c7aa11ae16a849e7"
  library: "9d1a473c6ff7b8ff"
  function: "gtm"
---
# Cold email cycle

**Point:** Earn replies from strangers with one honest, segment-true reason, without harming sender reputation.

**Company context:** `cady_read {"search": {"query": "<what you are about to do, in one sentence>"}}`

**Bets** (where this differs from the default):
- Open with the recipient's situation in their words; never a self-introduction, praise or an invented reaction. Instead of: Open with 'I'm X from Y' or a compliment on their recent post.
- An inferred or unknown line becomes the message's question, never a claim about the recipient. Instead of: State the guessed pain as fact ('you're struggling with X').
- Size the ask to the evidence: with only title and company size, ask for a one-word reply or offer a link, not a call. Instead of: Ask every cold prospect for a 15-minute call.
- Protect the sending domain before volume: verify addresses, keep catch-all small, never buy a list. Instead of: Send to a bought or scraped list and clean up bounces afterwards.
- Give each candidate a one-line reason for inclusion or exclusion. Instead of: Exclude or include candidates without explaining the decision.
- Pass motion 'customer' on the prepare call. Instead of: Leave the relationship type to inference.

Write and send cold email to people not yet contacted, using one template per segment.

**Not for:** Engaged parties, partner or organiser business approaches, replies in a live thread, and every follow-up; use `cady-gtm-warm-email` for partner approaches and follow-ups, or `cady-gtm-reply` for inbound replies. Missing verification holds release, not preparation.

**Unit of work:** one work item per segment and cycle, 50 or fewer Recipients. **Kind:** execution. **Parallel:** yes. 

## Inputs

### Evidence refs

- profileRef: checked persona File
- crm:list:<listId> or crm:party:<partyId> (50 or fewer)
- governing decision, grant, voice:me and brand pack refs

### Work fields

- cycleKey
- segmentKey
- angle and variants with shares
- senderLabel
- doneWhen
- stopIf

## Procedure

1. Use the work item for this cycle. If starting one, call work_set {kind: task, headline, next, path: the channel's node, brief {segment, cycle}, evidenceRefs}. Read the brief refs (`../../references/outreach-drafting.md`, Brief). If profileRef is unchecked, stop and report to the brief’s author; draft nothing.
2. Read the List or parties and cady_read party:<partyId>; apply `../../references/outreach-release.md`, Permission. Exclude opted-out, suppressed, engaged parties (route to warm or reply), prior touches, missing names and role inboxes. Give every candidate, in or out, a one-line reason in words, not a code. Keep unverified destinations visible as held. Verify addresses before first send; keep catch-all a small share, never buy a list and re-verify data older than 90 days.
3. Before the first cycle or after a sender change, check and record the sender as `../../references/cold-deliverability.md`, setup says.
4. In cold_template mode the reason belongs to the persona, so people who share it get their own segmentKey (the persona_key). Use the brief’s angle, variants and shares and its segmentKey to write one plain cold_template per variant in the profile’s words; apply `../../references/outreach-drafting.md` (Brief, Unknowns). No images or attachments and at most one link. Run the draft check (the draft check part of `../../references/outreach-drafting.md`) before the taste check (`../../references/taste-message.md`). Use at most one proof item from the credibility inventory, with only CRM-approved customer names. Fields marked templatable use {{field.key|fallback}}. With only title and company size as evidence, ask for a one-word reply or offer a link, not a call.
5. Prepare the review (crm_outreach (no id)), then read it back (cady_read review:outreach/<approvalId>), following `../../references/outreach-release.md`. Use crm_outreach (no id) (relationship type customer: a persona segmentKey puts each recipient on the customer board as Prospect) with cycleKey, segmentKey, variants, proof and listId or partyIds; include trackedLink {destination: "<final https>"} for a linked template, never recipientBodies. Check samples, exclusions and remaining cap. Pass motion 'customer' on the prepare call.
6. The company cold quota is 100 recipients per rolling day and 500 per rolling week. Release only as `../../references/outreach-release.md`, Release says.
7. At cycle end report the cycle's outreach review rows (cady_read review:outreach/<approvalId>) with denominators, including sends and replies by variant, and each variant’s silence evidence (silence.byReason: bounced, complained, opted out, clicked without replying, scanner click only, no signal, which means unexplained, not ignored; opens and reply sentiment are not recorded, so say unknown, never infer them), on this work item for the brief’s author (channel strategy). Read send results for bounces, complaints and blocks (`../../references/agent-stop.md`).
8. Stop: on any condition in `../../references/agent-stop.md`, stop and report as it says.

## Acceptance

- [ ] (check) one exact cold-template review is prepared and readable, with an easy yes
- [ ] (fresh) a reader recognises the profile’s quoted words as the customer’s own and can say what is asked, why now and how to answer
- [ ] (check) the draft check and message taste check pass; the review names the profile and any assumed line it leans on
- [ ] (check) every excluded party has a reason, unverified parties remain visible as held, and the sender check is recorded
- [ ] (check) the cycle and assigned variant are visible for each recipient
- [ ] (person) release follows `../../references/outreach-release.md`, Release

## Owner checks

- permission, engagement, cycle and cap rechecked by CRM
- opt-out line on every rendered body

## Result

### Artifact refs

- crm:outreach_review:<approvalId>
- crm:outreach_cycle:<cycleKey>
- **Transition:** the claim holder reports the review and cycle results for the brief’s author (channel strategy)

## References
- Read [Agent stop](../../references/agent-stop.md) when a stop condition arises.
- Read [Cold email deliverability](../../references/cold-deliverability.md) when before the first cycle or after a sender change.
- Read [Outreach drafting](../../references/outreach-drafting.md) when drafting and checking the template.
- Read [Outreach release](../../references/outreach-release.md) when checking permission, preparing or releasing outreach, or routing follow-ups.
- Read [Taste check: message](../../references/taste-message.md) when judging the template after the draft check.
