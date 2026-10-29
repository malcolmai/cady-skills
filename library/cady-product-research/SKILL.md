---
name: "cady-product-research"
description: "Research. Use when: Create or update a company-library research piece on competitors and alternatives, or on a technology approach. Not for: Product plans, roadmaps, architecture implementation plans, task reports or company policy; keep these with Product and Company Work. Raw notes belong in Files linked from work. Use `cady-product-manage` for product strategy; Research supports it with evidence. Vendor choice for the company's own tools: `cady-engineering-integrations` (vendor reference)."
license: "MPL-2.0"
compatibility: "Requires Cady (app.cadyworks.com/mcp)"
metadata:
  cady-id: "skill.product.research"
  version: "ab07147ecb781f43d983"
  library: "3cff3ea9351c22bc"
  function: "product"
---
# Research

**Company context:** `get_cady_context({"area": "product/<productId>/scope", "task": "<what you are about to do, in one sentence>", "knownMethods": {"skill.product.research": "ab07147ecb781f43d983@3cff3ea9351c22bc"}})`

Create or update a company-library research piece on competitors and alternatives, or on a technology approach.

**Not for:** Product plans, roadmaps, architecture implementation plans, task reports or company policy; keep these with Product and Company Work. Raw notes belong in Files linked from work. Use `cady-product-manage` for product strategy; Research supports it with evidence. Vendor choice for the company's own tools: `cady-engineering-integrations` (vendor reference).

**Unit of work:** one research question and its evolving library piece. **Kind:** strategy. **Parallel:** no. **Can release:** no. 

## Inputs

### Evidence refs

- company question or decision
- existing research piece
- dated source references

### Work fields

- question
- scope
- product relevance

## Procedure

1. State the question, scope, audience and product relevance in a sentence. Research the decision-relevant uncertainty; keep the piece a useful second-layer evidence source rather than a new decision record or policy.
2. Search the relevant Competition or Technology category for the same question and dimension. Update that piece when it exists, preserving its history and useful structure; create another only for a distinct question or dimension.
3. Competition (who the alternatives are and how they price, position and win) or Technology (a product use case and technical feasibility)? Read the matching reference before gathering evidence; both apply the steps below.
4. Prefer attributable primary evidence close to the claim: product documentation, customer or user evidence, standards, filings, datasets, technical reports or direct measurements. Date each source and identify what it supports. Treat vendor claims as claims until independently measured or corroborated; note credible contrary evidence and missing coverage.
5. Separate sourced observations, interpretation and recommendations. Mark estimates, assumptions and inference explicitly; state uncertainty where it could change the conclusion. Recommendations are analysis for the relevant owner, never policy or authority.
6. Write semantic HTML or Markdown with useful headings and real tables, styled by the preset described in the research.write tool description (do not restate or replace it). Include question, scope, evidence, counterevidence and implications where useful; omit empty sections. Do not delay useful evidence or require a rewrite just for formatting.
7. Find the same-question piece in the research namespace (find_cady_tools), read it with read_cady research:<id> (with its revision) and research.write (create or update) through find_cady_tools; check their current schemas and revision rules before writing. Customer evidence (interviews, observations) is not a library piece yet: keep it in Files and record a CRM interaction until a customer category exists. Never assume operation names or claim a write succeeded without its receipt/readback. Use only authorized provider reads; research does not authorize signup, payment, contact, access changes or other external effects.

## Acceptance

- [ ] (check) the piece cites dated sources for each claim and its write receipt and readback are on the work item
- [ ] (fresh) a reader who sees only the piece can compare the alternatives on the stated dimension, or the technology against its no-build baseline, and find the decision-relevant implication or open gap
- [ ] (fresh) claims separate observed evidence from vendor claims and inference; scope, uncertainty and counterevidence are visible; the piece adds evidence without becoming policy

## Owner checks

- same-question piece checked
- sources dated and attributable
- source, inference and recommendation distinguishable
- current operation schema and write revision checked
- alternatives are real for the scoped customer choice, or the baseline and no-build path are explicit
- counterevidence and limits included; implications conditional rather than policy

## Result

### Artifact refs

- research piece reference
- source references
- **Transition:** updated library piece with verified owner receipt

## References
- Read [Competition](references/competition.md) when the question is about competitors, alternatives, pricing or positioning.
- Read [Technology](references/technology.md) when the question is about choosing or assessing a technology, vendor, library or approach for a product use case.
- Read [Competitor profile](../../references/competitor-profile.md) when you profile, compare or keep a competitor or alternative analysis current.
