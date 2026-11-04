---
name: "cady-sales-deal-motion"
description: "Deal motion: discovery to close and handoff. Use when: Work one opportunity: discovery call, light qualification, proposal, close plan, handoff to success or loss review. Not for: A scheduled pass over many due tracks (`cady-gtm-pipeline-pass`), call sheets and call records (`cady-gtm-calls`), message copy (`cady-gtm-reply` or `cady-gtm-warm-email`), or offer and price strategy (`cady-gtm-offer-and-segments`)."
license: "MPL-2.0"
compatibility: "Requires Cady (app.cadyworks.com/mcp)"
metadata:
  cady-id: "skill.sales.deal_motion"
  version: "5c89727bd8e50ad2b292"
  library: "584f400834f42c35"
  function: "sales"
---
# Deal motion: discovery to close and handoff

**Point:** Move one deal on buyer evidence and dated mutual steps, so real deals close and non-fits end fast.

**Company context:** `context_read({"area": "sales/deals", "task": "<what you are about to do, in one sentence>", "knownMethods": {"skill.sales.deal_motion": "5c89727bd8e50ad2b292@584f400834f42c35"}})`

**Bets** (where this differs from the default):
- Use discovery to learn whether a problem worth solving now exists; the buyer talks most and either side may conclude no fit. Instead of: Use the first call to demo the product and pitch its features.
- A fast no is a good result: close or pause a deal with no problem, owner or timing. Instead of: Keep a stalled deal open and nurture it in case it revives.
- Send terms only after the buyer agrees the problem and asks for them, and walk through them live. Instead of: Email a proposal after a good first call to keep momentum.
- Work back from the buyer's needed date with steps each side owns; ask about a missed buyer date once, directly. Instead of: Chase with repeated follow-ups and create urgency with deadlines or discounts.

Work one opportunity: discovery call, light qualification, proposal, close plan, handoff to success or loss review.

**Not for:** A scheduled pass over many due tracks (`cady-gtm-pipeline-pass`), call sheets and call records (`cady-gtm-calls`), message copy (`cady-gtm-reply` or `cady-gtm-warm-email`), or offer and price strategy (`cady-gtm-offer-and-segments`).

**Unit of work:** one work item per opportunity: one customer party and its track. **Kind:** execution. **Parallel:** yes. **Can release:** no. 

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

1. Claim this work item with work_write(action: 'claim') (the server fills attemptId and claimProof); on CONFLICT stop and report the holder. Start one with work_write or decisions_write or asks_write if none is bound to this opportunity.
2. Read the deal: records_read party:<partyId>, its customer track via crm.list_parties mode tracks, crm_interactions_read, and earlier checkpoints with work_read. Work out which step below the deal is at and start there; skip what is already done.
3. Discovery call (use `cady-gtm-calls` for the sheet and the call record). The aim is to learn whether a problem worth solving now exists, not to pitch. Open with a short upfront contract: the time, the purpose, and that either side may conclude there is no fit. Ask about the situation and how they handle it today, what it costs them in their own numbers, why now, who else is affected or decides, and how they buy (security, legal, procurement, budget cycle). The buyer talks most. Show only the part of the product that meets the problem they named. End with a dated next step agreed on the call, not "I'll follow up".
4. Qualify lightly with four questions, each answered from the buyer's words or marked unknown: problem (real and costly to them?), priority (why now; what happens if nothing changes?), power (who signs, who else must agree?), path (the steps and dates to a decision). Unknowns become the next conversation's questions; never fill them by inference. Enthusiasm, a demo request or a trial sign-up is a signal, not qualification. No problem, owner or timing: say so and close it with crm_entities_write outcome disqualified or paused with recontact. A fast no is a good result.
5. Stages: propose a stage change with the buyer action behind it and set it only when the user states or confirms it: crm_entities_write for a first start, crm_entities_write for an existing track. Stages need not move in listed order. Reasonable exits: discovery once a discovery call is booked; qualified when the four answers are known; trial when an agreed evaluation starts; proposal when the buyer asked for terms; negotiation when scope is accepted and terms are discussed; won when signed; lost when they decline or the close plan lapses without a reply. Every touch sets nextAction and nextActionDueAt.
6. Proposal: only after the buyer agrees the problem and asks for terms; walk through it live when you can rather than emailing it cold. One or two pages: their situation and goal in their words; the outcome and how both sides will measure it; scope in and out; price from the accepted offer, at most three options with one recommended; timeline to first value; what you need from them; validity date and payment terms. A discount or non-standard term is the owner's decision; trade it for something real (term, timing, reference), never give it to get a reply. Save with files_create and read it back with files.read_text; send it through `cady-gtm-reply` or `cady-gtm-warm-email`. Before sending terms, run `cady-company-operations-contract-checks` (plan, customer contract) for payment, liability, data and tax terms. For accompanying message copy, use `../../references/outreach-drafting.md`, draft_check before `../../references/taste-message.md`; route preparation and release through `../../references/outreach-release.md`.
7. Mutual close plan: work back from the date the buyer needs the result, with dated steps each side owns (technical check, security review, legal, procurement, signature, kickoff). Agree it with the buyer's champion; save it with files_create. A missed buyer-owned date is the earliest sign of a stalled deal: ask about it directly, once, instead of chasing. No invented deadlines, exploding offers or pressure on a champion to skip their own process.
8. Won: close it with one crm_entities_write call, stage won, reason (why they bought, in their words), reasonKind (pain_fit, referral, timing, price or other) and evidence (a short quote, or the crm:interaction ref of the order recorded with crm_interactions_write kind note, sourceRef the order or invoice ref, no document text); name source (other:<how they came>) only when Cady never sent to them. Set role customer with renewalDate in its own crm_entities_write call. Write a handoff note with files_create: why they bought and how they will judge success, in their words; scope and anything promised beyond standard; people and champion; first-value date; open risks and objections; contract start, renewal and notice dates. Start the customer work item bound to `cady-customer-success-lifecycle` with work_write or decisions_write or asks_write. Anything sold that the product cannot yet do goes to the product owner now, not at kickoff. Then run `cady-company-operations-contract-checks` (act, customer contract).
9. Lost: close it with one crm_entities_write call, stage lost, reason in the buyer's words (mark it inferred when it is yours), reasonKind (price, timing, no_fit, competitor, no_need, went_quiet, champion_left or other), optional evidence, and recontact 'unless_changed' or a date the buyer gave; no_fit records disqualified, any other kind no_longer_relevant. Correct a close with the same call and expectedRevision. Ask the buyer once, without pressure, what would have needed to be different, and keep their words apart from your inference. Note the stage it died at. Three or more losses with one reason are a proposed change for `cady-gtm-offer-and-segments`; one loss is not a pivot.
10. Small self-serve deals skip the proposal and close plan: confirm sign-up and activation, then hand straight to `cady-customer-success-lifecycle`. Report with work_write once the track, files and next action read back.

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
- contact permission under `../../references/outreach-release.md`, permission before any message

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
- Read [Taste check: message](../../references/taste-message.md) when judging a message draft before review.
