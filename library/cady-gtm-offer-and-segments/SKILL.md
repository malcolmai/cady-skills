---
name: "cady-gtm-offer-and-segments"
description: "Offer and segments. Use when: Choose or revise the target segment, offer or message angle from evidence, before a cold cycle and at its review. Not for: Preparing or releasing a message; use `cady-gtm-cold-email-cycle`, `cady-gtm-warm-email`, `cady-gtm-reply` or `cady-gtm-linkedin-message`."
license: "MPL-2.0"
compatibility: "Requires Cady (app.cadyworks.com/mcp)"
metadata:
  cady-id: "skill.gtm.offer_and_segments"
  version: "2751efeac6451efd7157712350be95ab465bebfb97ae4dfe34190de659c4062d"
  library: "9a524e526102a3c5"
  function: "gtm"
---
# Offer and segments

**Company context:** `get_cady_context({"area": "gtm/strategy", "task": "<what you are about to do, in one sentence>", "knownMethods": {"skill.gtm.offer_and_segments": "2751efeac6451efd7157712350be95ab465bebfb97ae4dfe34190de659c4062d"}})`

Choose or revise the target segment, offer or message angle from evidence, before a cold cycle and at its review.

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

1. Read read_cady company:direction and relevant accepted work. Keep a hypothesis register (offer, segment, trigger) as hypothesis decisions with subject hypothesis:gtm.<key> (get_company_work decisions {state: "current", subjectPrefix: "hypothesis:gtm."}; continue, never duplicate) and carry the current ones into the direction revision. Each hypothesis: statement; status (open, supported, weakened, rejected); evidence for and against, each with type and strength on the direction_rule ladder; the next cheapest test; the reversal or kill condition. Find the evidence that could most change the decision, desk evidence first; run the test that could most change the decision with `cady-company-experiment` and frame questions with `cady-company-decision-questions` rather than repeating them here.
2. State the ICP with at least two disqualifiers (who it is not for and why) and its hypothesis status. Define segments by pain or buying trigger as hypotheses. For each state fit, evidence for and against, exclusion and what would change the choice. Do not require a dated trigger. Never use a weakly supported hypothesis as a filter, stop rule or fact; no sign of the claimed pain counts against it.
3. Choose a few distinct angles and compare them with angles already prominent in current direction and work. Avoid repeating an overused angle without a reason.
4. Inventory real, permissioned customer proof by problem and outcome; how proof is chosen for a message is in the cold email copy rules (`cady-gtm-cold-email-cycle`). Omit proof when none fits.
5. Use crm.update_party to record company_name, industry and proof approval on their owner records. Read current permission and engagement with crm.get_party; record engagement evidence with crm.record_interactions, never as a free label.
6. Variant shares and the cold email quota are in `cady-gtm-cold-email-cycle`; do not claim statistical certainty from small samples. Volume beyond the quota needs a sender the owner chooses and authorizes separately; its outcomes are recorded as the outcome check says.
7. Prepare the recommended direction revision with update_company_direction, including evidence, alternatives and the reversal condition. Read the accepted direction with read_cady company:direction before treating it as current.

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
