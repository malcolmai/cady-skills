---
name: "cady-gtm-offer-and-segments"
description: "Offer and persona. Use when: Choose or revise the target persona, offer or message angle from evidence, before a cold cycle and at its review. Not for: Preparing or releasing a message; use `cady-gtm-cold-email-cycle`, `cady-gtm-warm-email`, `cady-gtm-reply` or `cady-gtm-linkedin-message`."
license: "MPL-2.0"
compatibility: "Requires Cady (app.cadyworks.com/mcp)"
metadata:
  cady-id: "skill.gtm.offer_and_segments"
  version: "fe32e4a1cf5136893ca0"
  library: "921dfb8c2c658fd5"
  function: "gtm"
---
# Offer and persona

**Point:** Turn the persona profile into the right offer, checking first that we understand the customer well enough.

**Company context:** `cady_read {"search": {"query": "<what you are about to do, in one sentence>"}}`

**Bets** (where this differs from the default):
- Write the promise as the customer would say it, against what they do today; keep a sender term only where they use it. Instead of: Write the value proposition in the company's language: category, mechanism, 'AI-powered platform'.
- Where the product does not yet beat today's alternative, the promise is a test to run, not a claim to make. Instead of: Claim the advantage the roadmap or pitch deck promises.
- With no proof this reader already respects, claim nothing and show one specific, true observation about their situation. Instead of: Borrow credibility: 'trusted by', rounded numbers, logos or press used without permission.
- Let a fresh reader given only the customer's quotes pick the promise that sounds like them. Instead of: Pick the promise the writer or founder likes best.
- If the profile cannot yet support an offer, go back to understanding the customer before positioning. Instead of: Position from the founder's view and fill the gaps with assumptions.

Choose or revise the target persona, offer or message angle from evidence, before a cold cycle and at its review.

**Not for:** Preparing or releasing a message; use `cady-gtm-cold-email-cycle`, `cady-gtm-warm-email`, `cady-gtm-reply` or `cady-gtm-linkedin-message`.

**Unit of work:** one work item per cycle review. **Kind:** strategy. **Parallel:** no. 

## Inputs

### Evidence refs

- core:direction ref
- current company and customer evidence refs

### Work fields

- cycle
- current bet
- open decision

## Procedure

1. Read cady_read company:direction and relevant accepted work. Read current assumptions (the hypothesis bets in your context read's orchestrator.bets, and the question tasks from cady-company-decision-questions step 3), continue them rather than duplicate, and carry them into the direction revision. Each has a statement, status, evidence for and against handled as in `cady-gtm-persona-profile`, the next cheapest test (`cady-company-experiment`) and the reversal condition. Each kept piece of evidence carries its link or ref (URL, File id or interview note id) next to it.
2. First check the profile supports an offer; if thin, use cady-gtm-persona-profile first. This skill does no customer research of its own. That check covers an insight that holds widely enough, their words, what they use now and its cost, and the unknowns that could change the offer. State the ICP with at least two disqualifiers (who it is not for and why) and its assumption status. Propose each persona with an assumption; ask the owner to approve the ICP, promise and disqualifiers before recording them with crm_personas_set (personaKey = slug). Make a persona narrow enough that one message reads as written to each person in it; split it rather than generalise the copy.
3. Position from the profile's insight. Write the promise as the customer would say it: what they get, in their words, against what they use now, with why it beats that for them; promise only what the product does now, and where it does not yet beat the alternative, the promise is a test, not a claim. For a home-sewing pattern tool, "turn any idea, inspiration or photograph into a pattern, fitted to your body", not "we use AI to help you make dresses". Write two or three distinct promises and compare them with those already prominent in direction, brand packs and work; keep a sender term (the category, the mechanism, "AI", "platform") only where the customer uses it. A fresh reader given only the profile's quotes and the promises picks the one that sounds like the customer. Propose the promise and alternatives for owner approval; after approval record them on the persona's assumption, which a brand pack's positioning cites. Next to each piece of evidence the offer leans on, say where it was read (the File id, the interview or note, or the URL), and how widely it holds in one phrase; a reliability label or a count is not a substitute.
4. Inventory credibility for the persona (whom they trust): only what is real, current, permitted and checkable by the reader, such as customers or partners they would recognise, awards or press they respect, the founder's relevant record, or a sourced number. What counts is what this reader already respects. Unearned proof (an inflated number, a name or logo used without permission, "trusted by", an implied endorsement) reads as fake and costs more than none. With nothing that fits, claim nothing and show the work instead: one specific, true observation about their situation. How proof enters a message is in the cold email copy rules (`cady-gtm-cold-email-cycle`).
5. Prepare the recommended ICP and offer as a bet (we do X, not Y, because W, with its basis: owner decided with their words, or a hypothesis with its accept, reject and after-doing lines) with decisions_write (`cady-company-decision-check` step 6), including evidence, alternatives and the reversal condition. When the chosen audience needs sourcing, carry the requested size and identity of the List into cady-gtm-tam-map and execute it alongside the open assumption test.

## Acceptance

- [ ] an assumption register with status, evidence handled as in `cady-gtm-persona-profile`, next cheapest test and reversal condition
- [ ] each persona's profile was checked as good enough to craft the offer, or the work returned to it; the chosen promise is in the customer's words and a credibility inventory is kept; unearned proof is omitted
- [ ] direction revision and persona choice are proposed for owner approval; record the choice only after approval
- [ ] (check) the promise names what they do today and marks any unproven advantage as a test

## Owner checks

- direction review and acceptance remain separate

## Result

### Artifact refs

- company:direction review
- **Transition:** the claim holder reports the prepared revision
