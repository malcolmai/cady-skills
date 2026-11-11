---
name: "cady-gtm-warm-email"
description: "Warm email and follow-ups. Use when: Write email follow-ups, engaged notes, or partner, organiser and supplier business messages, including first approaches. Not for: A customer cold first touch, a reply in a live thread, or LinkedIn. Missing history is not proof that a party is cold."
license: "MPL-2.0"
compatibility: "Requires Cady (app.cadyworks.com/mcp)"
metadata:
  cady-id: "skill.gtm.warm_email"
  version: "bae6fda89bef8717ef76"
  library: "921dfb8c2c658fd5"
  function: "gtm"
---
# Warm email and follow-ups

**Point:** Keep each relationship moving with a useful email and a next step paced to the person.

**Company context:** `cady_read {"search": {"query": "<what you are about to do, in one sentence>"}}`

**Bets** (where this differs from the default):
- Establish the relationship from evidence first; missing history is not proof a party is cold. Instead of: Treat anyone without a logged thread as cold and send a cold pitch.
- Before a trial nudge, check whether they signed up and respond to what they did. Instead of: Send the scheduled nudge to everyone who received the link.
- Say what we do in a natural clause inside a note about them, not a pitch. Instead of: Paste the company pitch paragraph into each warm note.
- Pass motion on the prepare call when the person is new to every board. Instead of: Leave the relationship type to inference.

Write email follow-ups, engaged notes, or partner, organiser and supplier business messages, including first approaches.

**Not for:** A customer cold first touch, a reply in a live thread, or LinkedIn. Missing history is not proof that a party is cold.

**Unit of work:** one work item per person. **Kind:** execution. **Parallel:** yes. 

## Inputs

### Evidence refs

- crm:party:<partyId>
- readable communication or relationship-track ref, or sourced partner/supplier purpose for a first approach
- profileRef
- governing decision ref for a partner or supplier purpose

### Work fields

- senderLabel
- relationship type
- next action
- grant ref
- voice and brand pack subjects
- doneWhen
- stopIf

## Procedure

1. One named person and a plain purpose (a thanks, a proposed time, an answer) needs only the party (crm_read) and voice:me before the draft: prepare at step 4. Otherwise read the party and its record or thread to establish the relationship: confirm engagement or an introduction from evidence; a partner or supplier first approach may proceed even without prior engagement using its sourced purpose, without claiming an exchange.
2. For a follow-up, a trial nudge or a reply, read the existing exchange with crm_read mode interactions and cady_read communication:<id>. Before a trial nudge about a product link, check sign-up with cady_read party:<partyId> and respond to it. Ask the owner for a price, commitment, availability or relationship call. For a supplier cancellation, order or commitment, obtain the exact user review required by `cady-finance-vendor-spend-review`; an outreach grant does not substitute.
3. For a follow-up, say which follow-up this is (first or second), run the outcome check (`../../references/outreach-release.md`, Outcome check) first, then apply `../../references/outreach-release.md`, Follow up. For an introduction request, use `../../references/intro-request.md`. File external clicks with crm_interactions_set; a human click nudge uses the warm_email copy reference.
4. Draft one message per person, meeting them where they are in their own record or thread. Use `../../references/outreach-drafting.md`, Brief, Sender voice, Framing, Truth and grounding, Claims, Format, Easy yes, Booking and Unknowns; the relationship type carried by the review decides the lane. Run the draft check in `../../references/outreach-drafting.md` before `../../references/taste-message.md`.
5. Prepare the review (its reply carries it once) and act on each hold; show the person the message and, when they approve in their own words, record it with quoted_approval, which sends it (an ask cannot approve it); then report the review and the track update. To send a file, pass fileIds (email only, up to 5 files, 2 MiB in all; the person approves the exact versions and the recipient keeps a copy Cady cannot revoke); a larger file, or any other channel, goes as a dataroom share (datarooms_shares_set) linked in the message.
6. Stop: on any condition in `../../references/agent-stop.md`, stop and report as it says.

## Acceptance

- [ ] (check) readable evidence supports the relationship or sourced partner/supplier purpose, and sign-up is checked before a trial nudge
- [ ] (check) each recipient has one personal message and next step grounded in their record or thread
- [ ] (check) a follow-up has an outcome check and follows `../../references/outreach-release.md`, Follow up
- [ ] (check) the review carries the relationship type and the track stage and next action are evidence-backed
- [ ] (person) release follows `../../references/outreach-release.md`, Release

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
- Read [Warm email copy](references/warm-email-copy.md) when drafting a warm email or click nudge.
- Read [Agent stop](../../references/agent-stop.md) when throughout the run.
- Read [Introduction request](../../references/intro-request.md) when asking for an introduction.
- Read [Outreach drafting](../../references/outreach-drafting.md) when before drafting beyond one plain note to a named person.
- Read [Outreach release](../../references/outreach-release.md) when before releasing or checking outreach and before follow-ups; preparing one note needs no read first.
- Read [Taste check: message](../../references/taste-message.md) when after the draft check and before review.
