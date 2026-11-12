---
name: "cady-fundraise-investor-outreach"
description: "Investor outreach and updates. Use when: Write to investors: a warm intro request, a personalised first note, round follow-ups, or the monthly update send. Not for: Choosing which investors to pitch (use `cady-fundraise-investor-list`), deciding the round (use `cady-fundraise-raise-plan`) or drafting the deck, memo or update (use `cady-fundraise-raise-materials`)."
license: "MPL-2.0"
compatibility: "Requires Cady (app.cadyworks.com/mcp)"
metadata:
  cady-id: "skill.fundraise.investor_outreach"
  version: "9b98a26567bafcb36a50"
  library: "4df067661df56e5b"
  function: "fundraise"
---
# Investor outreach and updates

**Point:** Earn first meetings with fitting investors, warm path first, on one sourced reason and true results, never invented traction.

**Company context:** `cady_read {"search": {"query": "<what you are about to do, in one sentence>"}}`

**Bets** (where this differs from the default):
- Ask for a double opt-in introduction with a forwardable blurb wherever a credible warm path exists; write cold only when none does. Instead of: Cold email the whole ranked list, or ask a contact to forward the deck without checking the investor wants it.
- Write to one partner per firm with a sourced, dated reason for that partner, such as a recent deal. Instead of: Send a firm-wide or multi-partner note citing the fund's general thesis.
- Describe the result so far, not the work; no attachment, and a link only if asked. Instead of: Attach the deck and describe the product, team and effort.
- Send first notes and intro asks so first meetings land together in the round's two to three week window. Instead of: Send each note as each investor is found.
- Pass motion 'investor' on the prepare call. Instead of: Leave the relationship type to inference.

Write to investors: a warm intro request, a personalised first note, round follow-ups, or the monthly update send.

**Not for:** Choosing which investors to pitch (use `cady-fundraise-investor-list`), deciding the round (use `cady-fundraise-raise-plan`) or drafting the deck, memo or update (use `cady-fundraise-raise-materials`).

**Unit of work:** one work item per batch of 20 or fewer investors, or one monthly update send. **Kind:** execution. **Parallel:** yes. 

## Inputs

### Evidence refs

- crm:list:<listId> or crm:party:<partyId> from the ranked investor pool
- the round decision (subject fundraise:round-<slug>, headline "Raising <name>: ..."; the track round tag is that <name>), its file and the accepted raise plan
- file:<fileId> for the blurb, deck or update

### Work fields

- round
- senderLabel
- each investor's stage and warm path

## Procedure

1. Read the accepted raise plan and the round (its fundraise:round-<slug> decision, headline "Raising <name>: ...", and round file; investor tracks with crm_read mode stages and round: <name> exactly). Write only to investors in the ranked pool from `cady-fundraise-investor-list`, leads first; read cady_read party:<partyId> for each before preparing anything.
2. Warm intro first. Where a warm path exists, ask the connector for a double opt-in introduction with a forwardable blurb, as `../../references/intro-request.md` says. Use `../../references/outreach-drafting.md`, Truth and grounding and claims. Write cold only when no credible path exists.
3. First note: one partner per note, using the investor profile and partner record. Give a sourced, dated reason for this partner, such as a recent deal, stated thesis or portfolio fit. Use `../../references/outreach-drafting.md`, Sender voice, framing, Truth and grounding, Claims, Format, Easy yes, Booking and Unknowns; run Draft check before `../../references/taste-message.md` and the investor part of `../../references/taste-check.md`. Describe the result, not the work. No attachment; a link only if asked. Keep the draft with the exact gap visible to the owner outside the message, not as invented or unknown copy.
4. Pace the round from the raise plan: send first notes and intro asks as one batch so first meetings land in its 2 to 3 week window. After a meeting, follow up within a day with the next step and date; for an investor who never replied, use `../../references/outreach-release.md`, Follow up. On a pass, record it with crm_interactions_set (motion investor, stage passed, the reason as the note) and stop. Move each investor's track through its stage with crm_interactions_set (motion investor, stage).
5. Monthly update: send the update drafted with `cady-fundraise-raise-materials` on the plan's fixed send day as one reviewed batch with the same body. Every recipient goes on the marketing lane; use `../../references/outreach-drafting.md`, opt_out. Answer each reply through `cady-gtm-reply`.
6. Prepare each batch with crm_outreach (no id) (recipientBodies, one per investor), using `../../references/outreach-release.md`, Permission, Preparation and Release; read the review with cady_read review:outreach/<approvalId>. Pass motion 'investor' on the prepare call. Sent copy, positive interest, a term sheet, signed documents and money received are distinct states; record replies using `../../references/outreach-release.md`, Outcome check.

## Acceptance

- [ ] (check) each investor had a warm path tried first, or the note states why it is cold
- [ ] (check) every first note names one partner and a sourced reason; apply `../../references/outreach-drafting.md`, Draft check; within Cady’s copy check
- [ ] (fresh) a partner reading only the note can say what the company does and the result so far; apply `../../references/outreach-drafting.md`, Easy yes
- [ ] (check) batches follow the raise plan's pacing and every investor's stage is on its track
- [ ] (person) follow `../../references/outreach-release.md`, Release for outreach mechanics and execution authority's sending rule; sent, interest, commitment and funds stay distinct

## Owner checks

- investor in the ranked pool and the round
- current contact permission

## Result

### Artifact refs

- crm:outreach_review:<approvalId>
- crm:party:<partyId>
- **Transition:** the claim holder reports prepared reviews and track updates

## References
- Read [Introduction request](../../references/intro-request.md) when you ask for a warm introduction.
- Read [Outreach drafting](../../references/outreach-drafting.md) when you draft, review or prepare any message (read first).
- Read [Outreach release](../../references/outreach-release.md) when you prepare, release or check outreach.
- Read [Taste check](../../references/taste-check.md) when judging investor material before review.
- Read [Taste check: message](../../references/taste-message.md) when judging a message draft before review.
