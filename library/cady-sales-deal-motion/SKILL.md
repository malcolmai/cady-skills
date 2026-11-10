---
name: "cady-sales-deal-motion"
description: "Deal motion: discovery to close and handoff. Use when: Work one opportunity: discovery call, light qualification, proposal, close plan, handoff to success or loss review. Not for: A scheduled pass over many due tracks (`cady-gtm-pipeline-pass`), call sheets and call records (`cady-gtm-calls`), message copy (`cady-gtm-reply` or `cady-gtm-warm-email`), or offer and price strategy (`cady-gtm-offer-and-segments`)."
license: "MPL-2.0"
compatibility: "Requires Cady (app.cadyworks.com/mcp)"
metadata:
  cady-id: "skill.sales.deal_motion"
  version: "1066499f93eecae82edc"
  library: "3e67725c10e93707"
  function: "sales"
---
# Deal motion: discovery to close and handoff

**Point:** Move one deal on buyer evidence and dated mutual steps, so real deals close and non-fits end fast.

**Company context:** `cady_read {"search": {"query": "<what you are about to do, in one sentence>"}}`

**Bets** (where this differs from the default):
- Use discovery to learn whether a problem worth solving now exists; the buyer talks most and either side may conclude no fit. Instead of: Use the first call to demo the product and pitch its features.
- A fast no is a good result: close or pause a deal with no problem, owner or timing. Instead of: Keep a stalled deal open and nurture it in case it revives.
- Send terms only after the buyer agrees the problem and asks for them, and walk through them live. Instead of: Email a proposal after a good first call to keep momentum.
- Work back from the buyer's needed date with steps each side owns; ask about a missed buyer date once, directly. Instead of: Chase with repeated follow-ups and create urgency with deadlines or discounts.

Work one opportunity: discovery call, light qualification, proposal, close plan, handoff to success or loss review.

**Not for:** A scheduled pass over many due tracks (`cady-gtm-pipeline-pass`), call sheets and call records (`cady-gtm-calls`), message copy (`cady-gtm-reply` or `cady-gtm-warm-email`), or offer and price strategy (`cady-gtm-offer-and-segments`).

**Unit of work:** one work item per opportunity: one customer party and its track. **Kind:** execution. **Parallel:** yes. 

## Inputs

### Evidence refs

- crm:party:<partyId>
- crm:relationship_track:<trackId>
- accepted offer and price
- call notes, communication and file refs

### Work fields

- buyer's problem in their words
- stage the user stated
- next step and date

## Procedure

1. Claim this work item with work_write {id, status: working}; if someone else holds it, stop and report the holder. Start one with work_write {kind: task} if none covers this opportunity.
2. Read the deal: cady_read party:<partyId>, its customer track via crm_read mode stages, crm_read mode interactions, and earlier checkpoints with work_read. Find the step below the deal is at and start there; skip what is done.
3. Discovery call (sheet and record: `cady-gtm-calls`). The aim is to learn whether a problem worth solving now exists, not to pitch: open with an upfront contract, let the buyer talk most, and end with a dated next step. The stages reference holds the questions.
4. Qualify lightly with four questions, each answered from the buyer's words or marked unknown: problem, priority, power, path. Never fill unknowns by inference; enthusiasm, a demo request or a trial sign-up is a signal, not qualification. No problem, owner or timing: close it with crm_interactions_set: an interaction with motion customer and stage lost, its note the reason, and due the re-contact date when there is one. A fast no is a good result.
5. Stages: propose a stage change with the buyer action behind it and set it only when the user states or confirms it: crm_interactions_set, an interaction with motion and stage, for a first start or an existing track. Stages need not move in listed order. Exits: discovery once a discovery call is booked; qualified when the four answers are known; trial when an agreed evaluation starts; proposal when the buyer asked for terms; negotiation when scope is accepted and terms are discussed; won when signed; lost when they decline or the close plan lapses without a reply. Every touch records an interaction whose note is the next action and due its date.
6. Proposal: only after the buyer agrees the problem and asks for terms. Price comes from the accepted offer; a discount or non-standard term is the owner's decision. Save with files_set, read back with cady_read file:<id>; send it through `cady-gtm-reply` or `cady-gtm-warm-email`. Before sending terms, run `cady-company-operations-contract-checks` (plan, customer contract). For accompanying message copy, use `../../references/outreach-drafting.md`, draft_check before `../../references/taste-message.md`; route preparation and release through `../../references/outreach-release.md`. The stages reference holds the proposal contents.
7. Mutual close plan: work back from the date the buyer needs the result, with dated steps each side owns, agreed with the buyer's champion and saved with files_set. A missed buyer-owned date is the earliest sign of a stalled deal: ask once, directly, instead of chasing; invent no deadlines or pressure.
8. Won: close it with one crm_interactions_set call (the order's interaction with motion customer, stage won, the reason and its kind as the note, evidence), set role customer with renewalDate in its own crm_set call, write a handoff note with files_set, start the customer work item with work_write {kind: task} (`cady-customer-success-lifecycle` runs it), send anything sold that the product cannot yet do to the product owner now, run `cady-company-operations-contract-checks` (act, customer contract). The stages reference holds the fields and the handoff note.
9. Lost: close it with one crm_interactions_set call: motion customer, stage lost, the note the reason in the buyer's words (or marked inferred when it is yours; keep their words apart from your inference) and its kind, due a re-contact date; correct a close with another interaction that moves the stage. Three or more losses with one reason are a proposed change for `cady-gtm-offer-and-segments`; one loss is not a pivot. The stages reference holds the fields.
10. Small self-serve deals skip the proposal and close plan: confirm sign-up and activation, then hand to `cady-customer-success-lifecycle`. Report with work_write once track, files and next action read back.

## Acceptance

- [ ] (check) the deal's step is named with the buyer evidence behind it; unknowns are listed, not filled
- [ ] (check) the track has a dated next action
- [ ] (check) a proposal or close plan, when made, is saved in Files and uses only the accepted offer and price
- [ ] (check) a won deal has a handoff note and a customer success work item; a lost deal has a reason in the buyer's words or marked inferred
- [ ] (fresh) a buyer reading only the proposal can state their problem, the price and what happens next
- [ ] (check) nothing is sent from this skill
- [ ] (person) every stage change was stated or confirmed by the user

## Owner checks

- exact CRM party and track
- user-stated stage
- accepted offer and price
- Files readback
- contact permission before any message (`../../references/outreach-release.md`)

## Result

### Artifact refs

- crm:relationship_track:<trackId>
- file:<fileId>
- crm:interaction:<interactionId>
- company:work:<workId>
- **Transition:** the claim holder reports the deal step, track readback and next action

## References
- Read [Outreach drafting](../../references/outreach-drafting.md) when preparing customer message copy.
- Read [Outreach release](../../references/outreach-release.md) when checking permission or routing a customer message for preparation and release.
- Read [Deal motion stage detail](../../references/deal-motion-stages.md) when you run a discovery call, qualify, write a proposal or close plan, or close the deal won or lost.
- Read [Taste check: message](../../references/taste-message.md) when judging a message draft before review.
