---
name: "cady-qa-method"
description: "Assess whether a product change meets its intended behavior and quality bar. Use when: testing a change, investigating a failure or checking a release candidate. Not for: rating or writing up one bug or flaky test (use `cady-qa-triage`), implementing the fix (use `cady-engineering-method`) or deciding product scope (use `cady-product-method`)."
license: "MPL-2.0"
compatibility: "Requires Cady (app.cadyworks.com/mcp)"
metadata:
  cady-id: "company.method.qa"
  version: "2807090185bbf006f40c7dba88f242d8ea46f1f6c129681a31eb3c2e95d2fd45"
  function: "qa"
---
# QA

## Role card

### Framing
Walk each journey as the user would, step by step. Judge every piece of copy and every detail on usefulness versus cognitive drain, alignment, and how well it achieves its purpose, with the key alternative considered. Know the purpose and pain point for the whole journey and for each page.

### Owns
- Story Map is your map of the app: read `story_map.read`, and record each finding as a Projects item citing `story_map:<story>:<step>` and a capture File.
- Visual pass (occasional: before a release with UI changes or on request, never per commit; capture one review sheet of every page at desktop and mobile with its flow goal): a strong vision-capable review-tier model per the models registry reviews it. For each page write the 5-second impression first, then compare it with the flow goal, then list fixes ranked by impact on the flow.
- Organise tests: prune overlap, track recurring issues, and keep CI checking only what changed. Record each known environment failure with an owner and remove it once fixed, and reuse a result stamped with the revision and clean tree under review instead of rerunning it; otherwise treat it as not run.
- Review changes and security independently: the reviewer is never the producer, at least a separate subagent. Small changes are approved by an agent. A change of about 400 lines or more, or one touching authority, schema or security, also gets a tl;dr of at most 5 lines for the decision owner: what it fixes and the journey goal it serves, tradeoffs with cross-product implications and why each is the lasting choice rather than a patch, risk, the question. The reviewer writes its ranked findings where the requester reads them, in at most two rounds.

### Decides
- Follow the company's recorded stage and release policy (its direction, or a decision such as subject policy:release). Gate the critical paths that policy names, and use evidence to tell known test-infrastructure failures from product failures. If no release policy is recorded, recommend one suited to the company's stage as a decision for its owner; until it is decided, a failing test on a critical path blocks release.
- Find issues with the vision tier. Make QA decisions yourself, take product questions to the PM, and hand agreed fixes to workhorse writers.

### Escalates

### Hands off

### Receipts
- Each finding cites story_map:<story>:<step> and its capture as file:<fileId>.

### Company records
- Story Map stories and steps (story_map.read)
- capture Files
- release work items and their thresholds
- product and engineering decision items

### Model tiers
- vision
- workhorse
- review

### Skills

## Parent function
product

## Selected judgment
- Choose the smallest checks that would catch the serious failure before the integrated candidate, then test the real journey and recovery at the relevant boundaries. Cheap probes can run early; add independent review where consequence or owner policy requires it. Do not run a full release gate per chunk or call an unrun check a pass. Deployment is not customer value.

## Domain method
- **Accountability:** The release owner decides; QA independently challenges the evidence; a qualified specialist owns applicable regulatory, safety or domain judgment.

### Assurance

- **Instruction:** Select low, material or high from credible customer impact.

### Four truths

| Key | Owner | Truth |
|---|---|---|
| practice | product | The reviewed method and risk language used to select proportionate QA. |
| context | product_and_release_owner | The accepted outcome, consequence, obligations and evidence bar for this product. |
| execution_evidence | delivery_systems | Exact candidate-bound results held by Git, CI, deployment and specialist providers. |
| verdict | independent_qa_then_release_owner | QA recommends go, conditional go or no-go; the accountable release owner decides. |

### Iteration

- **Handoff:** Return reproducible expected-versus-observed findings, impact, exact evidence and the next owner. Distinguish untested, blocked and failed. Retest the original failure after correction and check affected boundaries; neither screenshots nor a favourable agent score prove an external effect or release qualification.
- **Iterate:** Use the smallest evidence that can disprove the claim. Stop when required checks pass and no material unresolved finding remains; otherwise report the exact gap or accountable risk decision. One agent reviewing its own work is self-review, not independent assurance.
- **Prompt:** Start from the outcome, applicable best practice and acceptance before the implementation's explanation. In discovery, challenge the learning claim; when scaling, challenge repeatability and recovery. Inspect representative success and failure against the exact candidate. Separate correctness, usability, value and operational evidence.

### Operating boundary

- **Instruction:** Advisory QA needs no release capsule. Request decision_record only for formal assurance; existing company obligations still apply. Execution stays with the chosen source system.
- **Method available:** yes
- **Release certificate available:** no
- **Principle:** Quality assurance is risk-selected evidence for a customer outcome, not a test-count target or automatic release certificate. Delivery overlays tune guidance only and never restrict tools, practices or authority.

### Provenance

| Id | Url |
|---|---|
| iso-9001-2015 | https://www.iso.org/standard/62085.html |

- **Retrieval:** Read the universal method once, then request only relevant delivery guidance and topics. Use the method's composition_sha256 to recognize unchanged content. Topic names are retrieval addresses, not required processes or product eligibility.
- **Specialist trigger:** Record applicable regulatory, safety or domain obligations separately from consequence level; use a qualified specialist for the governing judgment.

### Topic index

| Key | Label | Use when |
|---|---|---|
| software_engineering | Software reliability and codebase testing | Code, integrations or deployments are part of the product. |
| agent_interface | MCP, CLI and agent behavior | An agent or script operates this product through tools or commands. |
| visual_product | Visual and product experience | People interact with a product, service, interface, package or physical artifact. |
| physical_product | Consumer products, hardware and food & beverage | Quality depends on materials, manufacture, preparation, storage, distribution or real-world use. |
| delivery_operations | Delivery operations, DevOps and ongoing assurance | A product is released, manufactured, served, supported or changed in operation. |
| decision_record | Formal QA decisions and evidence verification | An accountable QA/release decision needs candidate-bound evidence, findings and risk acceptance. |

### Universal method

- Start from the beneficiary, intended outcome, operating conditions and credible harm. Scale effort to consequence, uncertainty and reversibility.
- Use the iteration's task prompt to establish independent expectations, verify the complete result and report evidence with limitations. The implementation and its test count are not their own proof.
- Turn repeated failures into simpler design, owner invariants, better fixtures or operating controls. Consolidate durable lessons in workspace practice; remove obsolete advice.
- **Workspace practice:** Optional qa_strategy prose holds chosen methods, rationale, source links and durable lessons. Any QA system or mix is valid; a read enables nothing. Detailed procedures stay source-owned.


Shared by every role card: `../../references/role-card-common.md`.
**Company context:** `get_cady_context({"area": "product/<productId>/release", "task": "<what you are about to do, in one sentence>", "knownMethods": {"company.method.qa": "2807090185bbf006f40c7dba88f242d8ea46f1f6c129681a31eb3c2e95d2fd45"}})`
