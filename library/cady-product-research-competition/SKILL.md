---
name: "cady-product-research-competition"
description: "Competition research. Use when: Find who the competitors and alternatives are and how they price, position and win, for a product or pricing question. Not for: A vendor directory, generic market-size estimate, or policy for how the company must compete; use `cady-product-manage` for product direction."
license: "MPL-2.0"
compatibility: "Requires Cady (app.cadyworks.com/mcp)"
metadata:
  cady-id: "skill.product.research_competition"
  version: "30baea9da8b57632e5fb6e465cf27bb8134eb6d62b7f3977b8412f45eed28081"
  library: "d51b57f8466a2b20"
  function: "product"
---
# Competition research

**Company context:** `get_cady_context({"area": "product/<productId>/scope", "task": "<what you are about to do, in one sentence>", "knownMethods": {"skill.product.research_competition": "30baea9da8b57632e5fb6e465cf27bb8134eb6d62b7f3977b8412f45eed28081"}})`

Find who the competitors and alternatives are and how they price, position and win, for a product or pricing question.

**Not for:** A vendor directory, generic market-size estimate, or policy for how the company must compete; use `cady-product-manage` for product direction.

**Unit of work:** one scoped customer choice and competitive dimension. **Kind:** strategy. **Parallel:** no. **Can release:** no. 

## Inputs

### Evidence refs

- product and customer use case
- existing Competition pieces
- dated primary sources

### Statement fields

- customer and circumstance
- choice being made
- dimension

## Procedure

1. Apply `cady-product-research-shared`. Define the customer, buying/use circumstance, job and boundary of the comparison; name the dimension being examined, such as workflow, capability, price, distribution or switching cost.
2. Identify actual alternatives available in that circumstance: named competitors where evidenced, adjacent substitutes, internal/manual workarounds, and doing nothing or staying put. A company is an alternative only when customers can plausibly choose it for the scoped job.
3. Compare like with like on dated evidence. Prefer observed customer behavior, current product/pricing documentation, filings, direct tests and credible independent sources. Record geography, segment, plan/version and date where they affect comparability. Separate observed fact from vendor positioning and your inference. For alternatives, profile depth, provenance, retrieval and keeping the result current, follow the competitor profile (`../../references/competitor-profile.md`).
4. Include evidence against the leading interpretation: cases where an alternative is not chosen, performs differently, or serves another segment; expose unknowns and source gaps. Do not infer preference from feature counts, web visibility, or market share alone.
5. Close with what the evidence could imply for this product's positioning, differentiation, parity or exposure, and which uncertainty matters next. Keep strategic implications conditional and attributable; the owner makes the decision.

## Acceptance

- [ ] A reader can compare alternatives on the stated dimension
- [ ] claims separate observed evidence from inference
- [ ] the piece identifies a decision-relevant implication or unresolved gap

## Owner checks

- alternatives are real for the scoped customer choice
- comparison dimensions and evidence dates are explicit
- counterevidence and limits included
- implications are conditional rather than policy

## Result

### Artifact refs

- Competition research piece
- source references
- **Transition:** verified updated or newly scoped library piece

## References
- [Competitor profile](../../references/competitor-profile.md)
- Apply `cady-product-research-shared` (`../cady-product-research-shared/SKILL.md`).
