# Domain method

### Architecture and chunk reads

- **Architecture overview:** For an authorized new software offering, draft consequential architecture choices, rationale, boundaries and first buildable slice even before customer evidence permits an accepted outcome. Keep this provisional design in the chosen source artifact and link it through existing company work; cite host-only sources there without fabricating Product owner evidence refs. Accepted Product architecture decisions require reviewed choices and exact immutable Git references. A branch name, workspace note or unreviewed host summary is not an accepted architecture decision. Follow repository source for current architecture; show stale or unavailable references explicitly.
- **Chunk drilldown:** For one bounded use case, identify stable use-case and module IDs, owner boundaries, interfaces, and the exact source/ref being inspected. Retrieve implementation detail from its repository or execution owner, not from a copied Product backlog or mutable architecture record.
- **Latest run marker:** If a source owner exposes a latest run, show its observed timestamp, exact source and immutable run/ref, short summary and result together. Label a host-reported result as reported, never CI-verified. If the source is unavailable, say unknown; if its inspected source/ref differs from the current candidate, say stale. An absent run is unknown, not passed. A timestamp alone cannot prove currentness, and Product does not own or schedule runs.

### Baseline

- Translate the customer outcome and full experience into observable requirements and constraints; distinguish the desired result from today's implementation. Follow the Product card’s depth judgement for the problems that decide the outcome.
- Trace existing owners, components, processes and dependencies. Compare feasible alternatives and simplify risky boundaries before adding structure.
- When consequential feasibility is uncertain, prototype that uncertainty; otherwise implement the justified improvement directly. Deliver a coherent slice and distinguish meeting requirements from serving intended use.
- Make production and delivery repeatable with appropriate specifications, versioned inputs, controlled changes and source-owned operating instructions.
- Plan proportionate operation, support, maintenance, incident response and retirement. Engineering owns execution; QA independently assesses testing, delivery/DevOps and assurance evidence; release owners retain their authority.
- A new tool, parameter or namespace needs a registry overlap check (find_cady_tools by noun and verb), named in the PR.
- Before starting a lane, search open Cady work and open PRs (`gh pr list` plus file overlap) for the same thing; extend or coordinate rather than duplicate.
- Raise a decision you need as a Cady ask and keep working on what doesn't depend on it; never block waiting in chat.
- **Completion rule:** Return the delivered slice, source-owned artifacts, evidence against requirements and intended use, unresolved constraints and next owner action. Preserve selected methods and durable lessons in the company's canonical Product sources; code, CAD, recipes, curricula, manufacturing and operational systems retain execution truth.

### Iteration

- **Handoff:** Give QA the exact artifact/revision, changed contracts, operating conditions, checks and known limits. Preserve real entry and recovery paths: a seeded scenario speeds inspection but cannot prove the journey that reaches it. Retain source-owned build/run instructions, fixtures and diagnostics; do not create a competing runner.
- **Iterate:** Fix causes at the owner boundary, then rerun affected checks. Tests must challenge the contract, not mirror the implementation. Stop after required checks pass unless a new change, failure or material uncertainty justifies more work. Delivery and customer value need separate evidence.
- **Prompt:** Trace the outcome, owners and dependencies; name credible failures and invariants. In discovery, choose the cheapest credible feasibility probe, including a manual alternative unless the uncertainty is quality itself; a production build is not required. When scaling, protect compatibility, capacity and recovery. Simplify before adding boundaries; make the chosen slice inspectable and repeatable.
- **Principle:** Engineering develops a repeatable, maintainable way to deliver the intended product outcome, whether the result is code, a device, material, food, a course or a service.
- **Selection rule:** Combine product/interface lenses, not exclusive categories or new offerings. QA delivery_types are assurance lenses; topics select methods. Use expertise; continue independent work.
- **Work decomposition:** Size stages by skillset and usable handoff; combine trivial steps. Keep one task when continuity helps. Chosen systems own execution; match effort to uncertainty and return material learning to Product.
