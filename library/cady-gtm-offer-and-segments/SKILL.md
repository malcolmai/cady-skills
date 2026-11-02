---
name: "cady-gtm-offer-and-segments"
description: "Offer and segments. Use when: Choose or revise the target segment, offer or message angle from evidence, before a cold cycle and at its review. Not for: Preparing or releasing a message; use `cady-gtm-cold-email-cycle`, `cady-gtm-warm-email`, `cady-gtm-reply` or `cady-gtm-linkedin-message`."
license: "MPL-2.0"
compatibility: "Requires Cady (app.cadyworks.com/mcp)"
metadata:
  cady-id: "skill.gtm.offer_and_segments"
  version: "e89257e78af3e7b66e9a"
  library: "c1c41b6e6064f887"
  function: "gtm"
---
# Offer and segments

**Company context:** `context_read({"area": "gtm/strategy", "task": "<what you are about to do, in one sentence>", "knownMethods": {"skill.gtm.offer_and_segments": "e89257e78af3e7b66e9a@c1c41b6e6064f887"}})`

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

1. Read records_read company:direction and relevant accepted work. Keep a hypothesis register (offer, segment, trigger) as hypothesis decisions with subject hypothesis:gtm.<slug> (the convention in `cady-company-decision-questions` step 3) (work_read decisions {state: "current", subjectPrefix: "hypothesis:gtm."}; continue, never duplicate) and carry the current ones into the direction revision. Each hypothesis: statement; status (open, supported, weakened, rejected); evidence for and against, each with type and strength on the direction_rule ladder; the next cheapest test; the reversal or kill condition. Find the evidence that could most change the decision, desk evidence first; run the test that could most change the decision with `cady-company-experiment` and frame questions with `cady-company-decision-questions` rather than repeating them here.
2. State the ICP with at least two disqualifiers (who it is not for and why) and its hypothesis status. Define each segment as a hypothesis by its customer record. Write one customer record per segment before positioning, sourcing or copy, as a Files document cited from the segment's hypothesis decision (hypothesis:gtm.<segment>, evidenceRefs), so later work cites it instead of redoing it. Five parts: (1) job: the situation where it comes up, what they are trying to get done, how often; (2) pain and current alternative: what they do today (a tool, a workaround, a person or nothing) and what that costs them; (3) buying decision: what triggers a search, who uses, decides and pays, the price they compare against and what makes switching risky, found in what they already pay for (price pages, tools they name), "switched from" posts and the ads they respond to; (4) reach and trust: where they look and gather when the trigger hits, and which names, people or communities make a stranger credible to them; (5) their words: 5-15 phrases for the job, the pain and the outcome, copied exactly from a page you read, each said by a member of the segment about their own situation; copy from sellers, coaches, vendors or the company itself is the market's wording, labelled as such, never theirs. Before copy uses a quote, recheck it against its page; one you cannot find again is dropped. Give each line its source (a URL, file: or crm: ref) and its evidence: a conversation about past behaviour, revealed behaviour, desk evidence, or assumed; a part you cannot source says unknown, never a plausible guess. The company's own records and calendar describe the sender, not the buyer. A fresh helper with no drafting context checks a new record before any copy uses it; with no helper available you mark it unchecked in the held review and go on. Evidence of no need stops the work and is recorded against that hypothesis; an assumed need, or an unknown part of the buying decision, makes the work a test of it: the first touch asks about it rather than pitching past it. Make a segment narrow enough that one message reads as written to each person in it (a shared situation, trigger and words); split it rather than generalise the copy. For each segment state fit, evidence for and against, exclusion and what would change the choice. Do not require a dated trigger. Never use a weakly supported hypothesis as a filter, stop rule or fact; no sign of the claimed pain counts against it.
3. Position from the record. Write the promise as the customer would say it: what they get, in their words (part 5), against what they do today (part 2), with why it beats that for them; promise only what the product does now, and where it does not yet beat the alternative, the promise is a test, not a claim. For a home-sewing pattern tool, "turn any idea, inspiration or photograph into a pattern, fitted to your body", not "we use AI to help you make dresses". Write two or three distinct promises and compare them with those already prominent in direction, brand packs and work; keep a sender term (the category, the mechanism, "AI", "platform") only where the customer uses it. A fresh reader given only the record's quotes and the promises picks the one that sounds like the customer. Record the chosen promise and the others on the segment hypothesis; a brand pack's positioning cites it.
4. Inventory credibility for the segment (record part 4): only what is real, current, permitted and checkable by the reader, such as customers, users or partners they would recognise, awards, press or selection they respect, the founder's relevant record, or a number you can source. What counts depends on the reader: a fashion house impresses a dressmaker and means nothing to a founder; a well-known investor is the reverse. Unearned proof (an inflated number, a name or logo used without permission, "trusted by", an implied endorsement) reads as fake and costs more than none. With nothing that fits, claim nothing and show the work instead: one specific, true observation about their situation. How proof enters a message is in the cold email copy rules (`cady-gtm-cold-email-cycle`).
5. Use crm_parties_update or crm_parties_create to record company_name, industry and proof approval on their owner records. Read current permission and engagement with records_read party:<partyId>; record engagement evidence with crm_interactions_create, never as a free label.
6. Variant shares and the cold email quota are in `cady-gtm-cold-email-cycle`; do not claim statistical certainty from small samples. Volume beyond the quota needs a sender the owner chooses and authorizes separately; its outcomes are recorded as the outcome check says.
7. Prepare the recommended direction revision with update_company_direction, including evidence, alternatives and the reversal condition. Read the accepted direction with records_read company:direction before treating it as current. When the chosen audience needs sourcing, carry the GTM plan_into_work identity/List acceptance into `cady-gtm-tam-map` and execute it alongside the open hypothesis test. Map selected recorded segments to a few useful CRM personas with crm_fields_set; keep hypotheses distinct.

## Acceptance

- [ ] a hypothesis register with status, evidence for and against by ladder type, next cheapest test and kill condition
- [ ] no weakly evidenced hypothesis used as a filter, stop rule or fact
- [ ] each segment has a customer record with a source or unknown per line, a promise in the customer's words and a credibility inventory; unearned proof is omitted
- [ ] direction revision is prepared without claiming acceptance

## Owner checks

- direction review and acceptance remain separate

## Result

### Artifact refs

- company:direction review
- **Transition:** the claim holder reports the prepared revision
