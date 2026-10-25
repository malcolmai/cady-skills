---
name: "cady-product-research-technology"
description: "Technology research. Use when: Assess technologies or technical approaches for a concrete product use case. Not for: Technology selection policy, implementation plans without authorization, or vendor summaries; use the installed Cady skill for integration_vendor for company tool choice."
license: "MPL-2.0"
compatibility: "Requires Cady (app.cadyworks.com/mcp)"
metadata:
  cady-id: "skill.product.research_technology"
  version: "b22fc55f4562d15a8cce3707e98ff832e1942823923954a49dcbe34daacb2688"
  library: "e963b3e399742c0d"
  function: "product"
---
# Technology research

**Company context:** `get_cady_context({"area": "product/<productId>/scope", "task": "<what you are about to do, in one sentence>", "knownMethods": {"skill.product.research_technology": "b22fc55f4562d15a8cce3707e98ff832e1942823923954a49dcbe34daacb2688"}})`

Assess technologies or technical approaches for a concrete product use case.

**Not for:** Technology selection policy, implementation plans without authorization, or vendor summaries; use the installed Cady skill for integration_vendor for company tool choice.

**Unit of work:** one product use case and technology question. **Kind:** strategy. **Parallel:** no. **Can release:** no. 

## Inputs

### Evidence refs

- product use case and constraints
- existing Technology pieces
- dated primary sources and measurements

### Statement fields

- user/job
- required outcome
- constraints

## Procedure

1. Apply `cady-product-research-shared`. Define the product use case, users, required outcome, expected scale and material constraints; identify what decision the evidence could inform.
2. Compare credible ways to meet the need: existing capability, buy/use a service, integrate, build, manual operation, defer and no-build where relevant. Describe the baseline so a new technology is not treated as necessary by default.
3. Distinguish independently measured behavior from vendor-published claims and demos. Record version, configuration, workload, date and method for benchmarks; do not generalize a narrow test beyond its conditions.
4. Assess fit, maturity and operational feasibility alongside total cost and constraints: quality at the actual workload, data and integration needs, security/privacy obligations to investigate, reliability, skills, maintenance, scale, portability and dependencies. Mark unsupported areas unknown rather than filling them with generic assumptions.
5. State the evidence-backed tradeoffs, principal failure modes and a bounded next test if it could change the choice. Define observable adoption triggers (for example quality, latency, cost or reliability under a named workload); keep forecasts and future capability conditional. The owner decides whether to adopt or build.

## Acceptance

- [ ] comparison includes a credible no-build or existing path where relevant
- [ ] measurements can be interpreted in their test conditions
- [ ] uncertainty and testable triggers are stated

## Owner checks

- use case and baseline are explicit
- vendor claims separated from measured evidence
- feasibility, maturity, cost and constraints considered
- adoption triggers are observable and conditional

## Result

### Artifact refs

- Technology research piece
- source references
- **Transition:** verified updated or newly scoped library piece

## References
- Apply `cady-product-research-shared` (`../cady-product-research-shared/SKILL.md`).
