---
name: "cady-product-research-shared"
description: "Research craft. Use when: Create or update a company-library research piece in Competition or Technology. Not for: Setting company policy, deciding strategy on behalf of an owner, or executing provider actions; use `cady-product-manage` for product strategy."
license: "MPL-2.0"
compatibility: "Requires Cady (app.cadyworks.com/mcp)"
metadata:
  cady-id: "skill.product.research_shared"
  version: "3e153209da3d4ee557799c8a9bcd66e21f25c949f550b5d164c4c9cad4780d47"
  library: "cf93c1d9ce44e1ac"
  function: "product"
---
# Research craft

**Company context:** `get_cady_context({"area": "product/<productId>/scope", "task": "<what you are about to do, in one sentence>", "knownMethods": {"skill.product.research_shared": "3e153209da3d4ee557799c8a9bcd66e21f25c949f550b5d164c4c9cad4780d47"}})`

Create or update a company-library research piece in Competition or Technology.

**Not for:** Setting company policy, deciding strategy on behalf of an owner, or executing provider actions; use `cady-product-manage` for product strategy.

**Unit of work:** one research question and its evolving library piece. **Kind:** strategy. **Parallel:** no. **Can release:** no. 

## Inputs

### Evidence refs

- company question or decision
- existing research piece
- dated source references

### Statement fields

- question
- scope
- product relevance

## Procedure

1. State the question, scope, audience and product relevance in a sentence. Research the decision-relevant uncertainty; keep the piece a useful second-layer evidence source rather than a new decision record or policy.
2. Search the relevant Competition or Technology category for the same question and dimension. Update that piece when it exists, preserving its history and useful structure; create another only for a distinct question or dimension.
3. Prefer attributable primary evidence close to the claim: product documentation, customer or user evidence, standards, filings, datasets, technical reports or direct measurements. Date each source and identify what it supports. Treat vendor claims as claims until independently measured or corroborated; note credible contrary evidence and missing coverage.
4. Separate sourced observations, interpretation and recommendations. Mark estimates, assumptions and inference explicitly; state uncertainty where it could change the conclusion. Recommendations are analysis for the relevant owner, never policy or authority.
5. Write a flexible semantic HTML fragment with a clear title and useful headings, concise prose, lists or tables as appropriate. Include the question and scope, key evidence, counterevidence, implications and update date as useful; omit empty sections. No navbar/header, scripts or remote embeds.
6. Before writing, discover the current research operation schemas and revision rules. Never assume operation names or claim a write succeeded without its receipt/readback. Use only authorized provider reads; research does not authorize signup, payment, contact, access changes or other external effects.

## Acceptance

- [ ] A company reader can trace claims to dated sources
- [ ] scope, uncertainty and counterevidence are visible
- [ ] piece adds evidence without becoming policy

## Owner checks

- same-question piece checked
- sources dated and attributable
- source, inference and recommendation distinguishable
- current operation schema and write revision checked

## Result

### Artifact refs

- research piece reference
- source references
- **Transition:** updated library piece with verified owner receipt
