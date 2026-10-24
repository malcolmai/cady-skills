---
name: "cady-product-research-shared"
description: "Research craft. Use when: Create or update a company-library research piece in Competition or Technology. Not for: Product plans, roadmaps, architecture implementation plans, task reports or company policy; keep these with Product and Company Work. Raw notes belong in Files linked from work. Use `cady-product-manage` for product strategy; Research supports it with evidence."
license: "MPL-2.0"
compatibility: "Requires Cady (app.cadyworks.com/mcp)"
metadata:
  cady-id: "skill.product.research_shared"
  version: "e755cc079737590da29b87231e835f92e0df7d5237242d8204dc55988d79c9dc"
  library: "bee76862d99c83e9"
  function: "product"
---
# Research craft

**Company context:** `get_cady_context({"area": "product/<productId>/scope", "task": "<what you are about to do, in one sentence>", "knownMethods": {"skill.product.research_shared": "e755cc079737590da29b87231e835f92e0df7d5237242d8204dc55988d79c9dc"}})`

Create or update a company-library research piece in Competition or Technology.

**Not for:** Product plans, roadmaps, architecture implementation plans, task reports or company policy; keep these with Product and Company Work. Raw notes belong in Files linked from work. Use `cady-product-manage` for product strategy; Research supports it with evidence.

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
5. Write semantic HTML or Markdown with useful headings and real tables, styled by the preset described in the research.write tool description (do not restate or replace it). Include question, scope, evidence, counterevidence and implications where useful; omit empty sections. Do not delay useful evidence or require a rewrite just for formatting.
6. Find the same-question piece in the research namespace (find_cady_tools), read it with read_cady research:<id> (with its revision) and research.write (create or update) through find_cady_tools; check their current schemas and revision rules before writing. Customer evidence (interviews, observations) is not a library piece yet: keep it in Files and record a CRM interaction until a customer category exists. Never assume operation names or claim a write succeeded without its receipt/readback. Use only authorized provider reads; research does not authorize signup, payment, contact, access changes or other external effects.

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
