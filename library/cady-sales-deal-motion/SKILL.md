---
name: "cady-sales-deal-motion"
description: "Deal motion: discovery to close and handoff. Use when: Work one opportunity: discovery call, light qualification, proposal, close plan, handoff to success or loss review. Not for: A scheduled pass over many due tracks (`cady-gtm-pipeline-pass`), call sheets and call records (`cady-gtm-calls`), message copy (`cady-gtm-reply` or `cady-gtm-warm-email`), or offer and price strategy (`cady-gtm-offer-and-segments`)."
license: "MPL-2.0"
compatibility: "Requires Cady (app.cadyworks.com/mcp)"
metadata:
  cady-id: "skill.sales.deal_motion"
  version: "4a309d523edffee85066e14220a65e109dbc7940efc7cd30a2efa84b2a3b882c"
  library: "c524ef7ffada6715"
  function: "sales"
---
# Deal motion: discovery to close and handoff

**Company context:** `get_cady_context({"area": "gtm/outreach", "task": "<what you are about to do, in one sentence>", "knownMethods": {"skill.sales.deal_motion": "4a309d523edffee85066e14220a65e109dbc7940efc7cd30a2efa84b2a3b882c"}})`

Work one opportunity: discovery call, light qualification, proposal, close plan, handoff to success or loss review.

**Not for:** A scheduled pass over many due tracks (`cady-gtm-pipeline-pass`), call sheets and call records (`cady-gtm-calls`), message copy (`cady-gtm-reply` or `cady-gtm-warm-email`), or offer and price strategy (`cady-gtm-offer-and-segments`).

**Unit of work:** one work item per opportunity: one customer party and its track. **Kind:** execution. **Parallel:** yes. **Can release:** no. 

See [Inputs](references/inputs.md).

## Procedure

1. Claim this work item with transition_company_work(action: 'claim') (the server fills attemptId and claimProof); on CONFLICT stop and report the holder. Start one with submit_company_work_checkpoint if none is bound to this opportunity.
2. Read the deal: crm.get_party, its customer track via crm.list_parties mode tracks, crm.find_communications, and earlier checkpoints with get_company_work. Work out which step below the deal is at and start there; skip what is already done.
3. Discovery call (use `cady-gtm-calls` for the sheet and the call record). The aim is to learn whether a problem worth solving now exists, not to pitch. Open with a short upfront contract: the time, the purpose, and that either side may conclude there is no fit. Ask about the situation and how they handle it today, what it costs them in their own numbers, why now, who else is affected or decides, and how they buy (security, legal, procurement, budget cycle). The buyer talks most. Show only the part of the product that meets the problem they named. End with a dated next step agreed on the call, not "I'll follow up".
4. Qualify lightly with four questions, each answered from the buyer's words or marked unknown: problem (real and costly to them?), priority (why now; what happens if nothing changes?), power (who signs, who else must agree?), path (the steps and dates to a decision). Unknowns become the next conversation's questions; never fill them by inference. Enthusiasm, a demo request or a trial sign-up is a signal, not qualification. No problem, owner or timing: say so and close it with crm.set_track outcome disqualified or paused with recontact. A fast no is a good result.
5. Stages: propose a stage change with the buyer action behind it and set it with crm.set_track only when the user states or confirms it. Stages need not move in listed order. Reasonable exits: discovery once a discovery call is booked; qualified when the four answers are known; trial when an agreed evaluation starts; proposal when the buyer asked for terms; negotiation when scope is accepted and terms are discussed; won when signed; lost when they decline or the close plan lapses without a reply. Every touch sets nextAction and nextActionDueAt.
6. Proposal: only after the buyer agrees the problem and asks for terms; walk through it live when you can rather than emailing it cold. One or two pages: their situation and goal in their words; the outcome and how both sides will measure it; scope in and out; price from the accepted offer, at most three options with one recommended; timeline to first value; what you need from them; validity date and payment terms. A discount or non-standard term is the owner's decision; trade it for something real (term, timing, reference), never give it to get a reply. Save with files.put_text and read it back with files.read_text; send it through `cady-gtm-reply` or `cady-gtm-warm-email`. Before sending terms, run `cady-company-operations-contract-checks` (plan, customer contract) for payment, liability, data and tax terms.
7. Mutual close plan: work back from the date the buyer needs the result, with dated steps each side owns (technical check, security review, legal, procurement, signature, kickoff). Agree it with the buyer's champion; save it with files.put_text. A missed buyer-owned date is the earliest sign of a stalled deal: ask about it directly, once, instead of chasing. No invented deadlines, exploding offers or pressure on a champion to skip their own process.
8. Won: record the signed order with crm.record_interactions kind deal (sourceRef the order or invoice ref, no document text), set role customer with renewalDate in its own crm.update_party call, and crm.set_track stage won with outcome converted. Write a handoff note with files.put_text: why they bought and how they will judge success, in their words; scope and anything promised beyond standard; people and champion; first-value date; open risks and objections; contract start, renewal and notice dates. Start the customer work item bound to `cady-customer-success-lifecycle` with submit_company_work_checkpoint. Anything sold that the product cannot yet do goes to the product owner now, not at kickoff. Then run `cady-company-operations-contract-checks` (act, customer contract).
9. Lost: crm.set_track stage lost, outcome no_longer_relevant (disqualified for a bad fit), outcomeReason, and recontact 'unless_changed' or a date the buyer gave. Ask the buyer once, without pressure, what would have needed to be different, and keep their words apart from your inference. Classify: no decision or status quo, timing, price or value, missing capability, competitor, champion left, poor fit; note the stage it died at. Three or more losses with one reason are a proposed change for `cady-gtm-offer-and-segments`; one loss is not a pivot.
10. Small self-serve deals skip the proposal and close plan: confirm sign-up and activation, then hand straight to `cady-customer-success-lifecycle`. Report with report_company_work once the track, files and next action read back.

## Acceptance

- [ ] the deal's step is named with the buyer evidence behind it; unknowns are listed, not filled
- [ ] every stage change was stated or confirmed by the user and the track has a dated next action
- [ ] a proposal or close plan, when made, is saved in Files and uses only the accepted offer and price
- [ ] a won deal has a handoff note and a customer success work item; a lost deal has a reason in the buyer's words or marked inferred
- [ ] nothing is sent from this skill

## Owner checks

- WORK_NOT_FOUND
- METHOD_NOT_CURRENT
- exact CRM party and track
- user-stated stage
- accepted offer and price
- Files readback
- contact permission before any message

## Result

### Artifact refs

- crm:relationship_track:<trackId>
- file:<fileId>
- crm:interaction:<interactionId>
- company:work:<workId>
- **Transition:** the claim holder reports the deal step, track readback and next action
