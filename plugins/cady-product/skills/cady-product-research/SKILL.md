---
name: "cady-product-research"
description: "Research. Use when: Write or update a research file (research/<title>.md) on competitors and alternatives, or on a technology. Not for: Product plans, roadmaps, architecture implementation plans, task reports or company policy; keep these with Product and Company Work. Raw notes belong in Files linked from work. Use `cady-product-manage` for product strategy; Research supports it with evidence. Vendor choice for the company's own tools: `cady-engineering-integrations` (vendor reference)."
license: "MPL-2.0"
compatibility: "Requires Cady (app.cadyworks.com/mcp)"
metadata:
  cady-id: "skill.product.research"
  version: "a15c6369014b4c0788bc"
  library: "810d92568a814141"
  function: "product"
---
# Research

**Point:** Gather dated, attributable evidence on alternatives or technology so an owner can decide without redoing the analysis.

**Company context:** `cady_read {"search": {"query": "<what you are about to do, in one sentence>"}}`

**Bets** (where this differs from the default):
- Count manual workarounds, doing nothing and staying put as alternatives, scoped to the customer's job and circumstance. Instead of: List the named competitors in the category and compare their features.
- Compare a technology against the no-build and existing-capability baseline, measured at the real workload. Instead of: Compare candidate vendors with each other from their published benchmarks and demos.
- Update the same-question piece and keep it short; research is an intermediate record that feeds a decision. Instead of: Write a new, comprehensive report for each request.
- End with the implication for the decision and the next test that could change the choice. Instead of: End with a neutral summary of what was found.

Write or update a research file (research/<title>.md) on competitors and alternatives, or on a technology.

**Not for:** Product plans, roadmaps, architecture implementation plans, task reports or company policy; keep these with Product and Company Work. Raw notes belong in Files linked from work. Use `cady-product-manage` for product strategy; Research supports it with evidence. Vendor choice for the company's own tools: `cady-engineering-integrations` (vendor reference).

**Unit of work:** one research question and its evolving research file. **Kind:** strategy. **Parallel:** no. 

## Inputs

### Evidence refs

- company question or decision
- existing research file
- dated source references

### Work fields

- question
- scope
- product relevance

## Procedure

1. State the question, scope, audience and product relevance in a sentence. Research the decision-relevant uncertainty; keep the piece a useful second-layer evidence source rather than a new decision record or policy.
2. Search Files for the same question and dimension (cady_read search kinds ["file"], query research/ plus the topic). Update that file when it exists, preserving its history and useful structure; create another only for a distinct question or dimension.
3. Competition (who the alternatives are and how they price, position and win) or Technology (a product use case and technical feasibility)? Read the matching reference before gathering evidence; both apply the steps below.
4. Prefer attributable primary evidence close to the claim: product documentation, customer or user evidence, standards, filings, datasets, technical reports or direct measurements. Date each source and identify what it supports. Treat vendor claims as claims until independently measured or corroborated; note credible contrary evidence and missing coverage.
5. Separate sourced observations, interpretation and recommendations. Mark estimates, assumptions and inference explicitly; state uncertainty where it could change the conclusion. Recommendations are analysis for the relevant owner, never policy or authority.
6. Write Markdown with useful headings and real tables. Include question, scope, evidence, counterevidence and implications where useful; omit empty sections. Cite customer quotes as quote:<id> (research.write records and checks a quote against its public page) and sources by URL or file:<id>. Do not delay useful evidence for formatting.
7. A research piece is a File named research/<title>.md: create it with files_set mode save_text (text up to 24576 bytes; split longer pieces by question), and revise the same file with files_set mode patch at its expectedGeneration after reading it with cady_read file:<id>. Discover their current schemas and generation rules with find_cady_tools before writing. Never assume operation names or claim a write succeeded without its receipt and readback. Customer interviews and observations stay in Files linked from work, with a CRM interaction. Use only authorized provider reads; research does not authorize signup, payment, contact, access changes or other external effects.

## Acceptance

- [ ] (check) the piece cites dated sources for each claim and the file's write receipt and readback are on the work item
- [ ] (fresh) a reader who sees only the piece can compare the alternatives on the stated dimension, or the technology against its no-build baseline, and find the decision-relevant implication or open gap
- [ ] (fresh) claims separate observed evidence from vendor claims and inference; scope, uncertainty and counterevidence are visible; the piece adds evidence without becoming policy

## Owner checks

- same-question piece checked
- sources dated and attributable
- source, inference and recommendation distinguishable
- current operation schema and file generation checked
- alternatives are real for the scoped customer choice, or the baseline and no-build path are explicit
- counterevidence and limits included; implications conditional rather than policy

## Result

### Artifact refs

- research file reference (file:<id>)
- source references
- **Transition:** updated research file with verified owner receipt

## References
- Read [Competition](references/competition.md) when the question is about competitors, alternatives, pricing or positioning.
- Read [Technology](references/technology.md) when the question is about choosing or assessing a technology, vendor, library or approach for a product use case.
- Read [Competitor profile](../../references/competitor-profile.md) when you profile, compare or keep a competitor or alternative analysis current.
