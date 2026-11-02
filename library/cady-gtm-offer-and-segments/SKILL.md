---
name: "cady-gtm-offer-and-segments"
description: "Offer and segments. Use when: Choose or revise the target segment, offer or message angle from evidence, before a cold cycle and at its review. Not for: Preparing or releasing a message; use `cady-gtm-cold-email-cycle`, `cady-gtm-warm-email`, `cady-gtm-reply` or `cady-gtm-linkedin-message`."
license: "MPL-2.0"
compatibility: "Requires Cady (app.cadyworks.com/mcp)"
metadata:
  cady-id: "skill.gtm.offer_and_segments"
  version: "b20f07390363cd28e454"
  library: "bd82e1a78db1644c"
  function: "gtm"
---
# Offer and segments

**Point:** Turn the persona profile into the right offer, checking first that we understand the customer well enough.

**Company context:** `context_read({"area": "gtm/strategy", "task": "<what you are about to do, in one sentence>", "knownMethods": {"skill.gtm.offer_and_segments": "b20f07390363cd28e454@bd82e1a78db1644c"}})`

Choose or revise the target segment, offer or message angle from evidence, before a cold cycle and at its review.

**Not for:** Preparing or releasing a message; use `cady-gtm-cold-email-cycle`, `cady-gtm-warm-email`, `cady-gtm-reply` or `cady-gtm-linkedin-message`.

**Unit of work:** one work item per cycle review. **Kind:** strategy. **Parallel:** no. **Can release:** no. 

## Inputs

### Evidence refs

- core:direction ref
- current company and customer evidence refs

### Work fields

- cycle
- current bet
- open decision

## Procedure

1. Read records_read company:direction and relevant accepted work. Keep the hypothesis register (offer, segment, trigger) as hypothesis decisions with subject hypothesis:persona.<persona_key>. Read any existing hypothesis:gtm.<persona_key> (or hypothesis:<persona_key>) for this persona and continue it under its recorded subject; do not register a second one under persona. (`cady-company-decision-questions` step 3; work_read decisions {state: "current", subjectPrefix: "hypothesis:"}; continue, never duplicate) and carry the current ones into the direction revision. Each has a statement, status, evidence for and against with its reliability and how widely it holds, the next cheapest test (`cady-company-experiment`) and the reversal condition.
2. State the ICP with at least two disqualifiers (who it is not for and why) and its hypothesis status. Define each segment as a persona (crm_fields_set define_persona, key = slug) with a hypothesis. This skill adapts the persona's profile and does no customer research of its own: check the profile supports an offer (an insight that holds widely enough, their words, what they use now and its cost, the unknowns that could change the offer); if it is thin or missing, use `cady-gtm-persona-profile` first. Make a persona narrow enough that one message reads as written to each person in it; split it rather than generalise the copy.
3. Position from the profile's insight. Write the promise as the customer would say it: what they get, in their words (part 2), against what they do today (part 3), with why it beats that for them; promise only what the product does now, and where it does not yet beat the alternative, the promise is a test, not a claim. For a home-sewing pattern tool, "turn any idea, inspiration or photograph into a pattern, fitted to your body", not "we use AI to help you make dresses". Write two or three distinct promises and compare them with those already prominent in direction, brand packs and work; keep a sender term (the category, the mechanism, "AI", "platform") only where the customer uses it. A fresh reader given only the profile's quotes and the promises picks the one that sounds like the customer. Record the chosen promise and the others on the persona's hypothesis; a brand pack's positioning cites it.
4. Inventory credibility for the persona (profile part 4: whom they trust): only what is real, current, permitted and checkable by the reader, such as customers or partners they would recognise, awards or press they respect, the founder's relevant record, or a sourced number. What counts is what this reader already respects. Unearned proof (an inflated number, a name or logo used without permission, "trusted by", an implied endorsement) reads as fake and costs more than none. With nothing that fits, claim nothing and show the work instead: one specific, true observation about their situation. How proof enters a message is in the cold email copy rules (`cady-gtm-cold-email-cycle`).
5. Prepare the recommended direction revision with update_company_direction, including evidence, alternatives and the reversal condition. Read the accepted direction with records_read company:direction before treating it as current. When the chosen audience needs sourcing, carry the GTM plan_into_work identity/List acceptance into `cady-gtm-tam-map` and execute it alongside the open hypothesis test.

## Acceptance

- [ ] a hypothesis register with status, evidence for and against by reliability and how widely it holds, next cheapest test and kill condition
- [ ] each persona's profile was checked as good enough to craft the offer, or the work returned to it; the chosen promise is in the customer's words and a credibility inventory is kept; unearned proof is omitted
- [ ] direction revision is prepared without claiming acceptance

## Owner checks

- direction review and acceptance remain separate

## Result

### Artifact refs

- company:direction review
- **Transition:** the claim holder reports the prepared revision
