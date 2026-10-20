---
name: "cady-gtm-offer-and-segments"
description: "Offer and segments. Use when: Before a cold cycle and at its review, and whenever evidence may change the offer, segment or message angle. Not for: Preparing or releasing a message; use `cady-gtm-cold-email-cycle`, `cady-gtm-warm-email`, `cady-gtm-reply` or `cady-gtm-linkedin-message`."
license: "MPL-2.0"
compatibility: "Requires Cady (app.cadyworks.com/mcp)"
metadata:
  cady-id: "skill.gtm.offer_and_segments"
  version: "a913308ddc676a999369bea2ceade204a9458d0abf1d4e1e473df9d6f3b7bd49"
  function: "gtm"
---
# Offer and segments

Before a cold cycle and at its review, and whenever evidence may change the offer, segment or message angle.

**Not for:** Preparing or releasing a message; use `cady-gtm-cold-email-cycle`, `cady-gtm-warm-email`, `cady-gtm-reply` or `cady-gtm-linkedin-message`.

**Unit of work:** one work item per cycle review. **Kind:** strategy. **Parallel:** no. **Can release:** no. 

## Inputs

### Evidence refs

- core:direction ref
- current company and customer evidence refs

### Statement fields

- cycle
- current bet
- open decision

## Procedure

1. Claim this work item with transition_company_work(action: 'claim') (the server fills attemptId and claimProof). Stop on CONFLICT.
2. Read get_company_direction and relevant accepted work. Keep a hypothesis register (offer, segment, trigger) as hypothesis decisions with subject hypothesis:gtm.<key> (get_company_work decisions {state: "current", subjectPrefix: "hypothesis:gtm."}; continue, never duplicate) and carry the current ones into the direction revision. Each hypothesis: statement; status (open, supported, weakened, rejected); evidence for and against, each with type and strength on the direction_rule ladder; the next cheapest test; the reversal or kill condition. Find the evidence that could most change the decision, desk evidence first; run the test that could most change the decision with `cady-company-experiment` and frame questions with `cady-company-decision-questions` rather than repeating them here.
3. Define segments by pain or buying trigger as hypotheses. For each state fit, evidence for and against, exclusion and what would change the choice. Do not require a dated trigger. Never use a weakly supported hypothesis as a filter, stop rule or fact; no sign of the claimed pain counts against it.
4. Choose a few distinct angles and compare them with angles already prominent in current direction and work. Avoid repeating an overused angle without a reason.
5. Inventory real customer proof. Use relevant, permissioned proof of the same problem or outcome; prefer the closest comparable customer unless competition or confidentiality rules it out, then use the nearest non-competing one. Omit proof when none fits.
6. Use crm.update_party to record company_name, industry and proof approval on their owner records. Read current permission and engagement with crm.get_party; record engagement evidence with crm.record_interactions, never as a free label.
7. Treat shares as guidance: favor variety early and concentrate only after a winner holds across two cycles. Do not claim statistical certainty from small samples. Use the caps and review rules in `cady-gtm-cold-email-cycle`. If the company wants volume beyond those caps, its owner must choose a sender and authorize it separately. Read its sending mailbox through the host connector because crm.find_communications does not show new replies. Match the released review and record replies, bounce with bounceType hard or soft and destination, and opt_out through crm.record_interactions.
8. Prepare the recommended direction revision with update_company_direction, including evidence, alternatives and the reversal condition. Read the accepted direction with get_company_direction before treating it as current.

## Acceptance

- [ ] a hypothesis register with status, evidence for and against by ladder type, next cheapest test and kill condition
- [ ] no weakly evidenced hypothesis used as a filter, stop rule or fact
- [ ] real proof is cited or omitted
- [ ] direction revision is prepared without claiming acceptance

## Owner checks

- WORK_NOT_FOUND
- METHOD_NOT_CURRENT
- direction review and acceptance remain separate

## Result

### Artifact refs

- company:direction review
- **Transition:** the claim holder reports the prepared revision

**Company context:** `get_cady_context({"area": "gtm/strategy", "task": "<what you are about to do, in one sentence>", "knownMethods": {"skill.gtm.offer_and_segments": "a913308ddc676a999369bea2ceade204a9458d0abf1d4e1e473df9d6f3b7bd49"}})`
