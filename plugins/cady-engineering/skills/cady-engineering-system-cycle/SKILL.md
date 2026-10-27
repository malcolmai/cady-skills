---
name: "cady-engineering-system-cycle"
description: "Recurring system cycle: map, dimensions, routed motions. Use when: Clear a product's engineering backlog in recurring cycles from its goal map, system dimensions and state-routed motions. Not for: One bounded change with clear acceptance (use `cady-engineering-method`) or deciding what to build and for whom (use `cady-product-manage`)."
license: "MPL-2.0"
compatibility: "Requires Cady (app.cadyworks.com/mcp)"
metadata:
  cady-id: "skill.engineering.system_cycle"
  version: "18886d2fb851a888d396"
  library: "9f22976155458e5f"
  function: "engineering"
---
# Recurring system cycle: map, dimensions, routed motions

**Company context:** `get_cady_context({"area": "product/<productId>/engineering", "task": "<what you are about to do, in one sentence>", "knownMethods": {"skill.engineering.system_cycle": "18886d2fb851a888d396@9f22976155458e5f"}})`

Clear a product's engineering backlog in recurring cycles from its goal map, system dimensions and state-routed motions.

**Not for:** One bounded change with clear acceptance (use `cady-engineering-method`) or deciding what to build and for whom (use `cady-product-manage`).

**Unit of work:** one cycle of one product: its map, dimension register and the review, build and hunt motions. **Kind:** execution. **Parallel:** yes. **Can release:** no. 

## Always

- Journey goals are user outcomes, not features or implementation decisions.
- Development tests find and prove; this cycle adds no gate. CI gates follow the company's recorded stage, and an exposed security, isolation or authority defect still blocks its path.
- Before starting a lane, search open Cady work and open PRs (`gh pr list` plus file overlap) for the same thing; extend or coordinate rather than duplicate.

## Inputs

### Evidence refs

- company direction and current decisions
- your system map and dimension register, kept beside the product's source
- open findings and the last review checkpoint
- file:<fileId> research notes

### Statement fields

- cycle scope (dimensions or overall)
- motion
- ranked findings or delivered items
- next owner action

## Procedure

1. Objective. Clear the product's engineering backlog by the motion its current state calls for: review, engineer or hunt. Route each pass from current state; motions are conditions, not a fixed rotation. Review when there is no ranked direction, when the goals, a dimension label or a research scan changed since it was written, or when findings contradict it. Engineer when the direction is current and ready items exist, under the engineering role card. Hunt, under the QA role card and by an agent that did not build what it hunts, after a dimension closes, across seams after the end-to-end tests (step 7), or when the finding list is empty or stale. With a short queue one agent reviews and engineers in the same pass, and its diffs still get the engineering role's independent review; give a motion its own agent only when its queue justifies it, and never let two agents share a claim.
2. Map once, update in place. Keep one system map beside the product's source (a File for non-software): journey goals as user outcomes in lifecycle order and architecture as one simple diagram. Features and implementation choices are decisions, not goals. Read read_cady company:direction and current get_company_work decisions first; never restate what a decision already holds.
3. Name high-level, mutually exclusive, collectively exhaustive dimensions that every goal crosses, each with one question, owner and boundary. Before users or revenue, name only the 3 to 5 a goal actually crosses (typically data and tenancy; identity and authority; the core workflow's integrations; runtime and release) and fold the rest into them as decisions. With users, seed from: data model and storage; tenancy and isolation; identity; agent action authority; user and data access; runtime and deployment; integration and connectivity; testing and release; observability and recovery; cost; expect 8 to 14. Scope, ICP and pricing live in direction and decisions, not the register. Keep only what has its own owner, question and test; add one only for a new subsystem, region, provider or buyer category. Draw the map as the product card's map recipe says. Keep authentication separate from permissions, and agent action/tool authority separate from user/data access; give agent management its own dimension. Name the commercial category a buyer would compare. Raise agent draft labels as one batched ask, never a "Draft:" decision. Label each differentiating or not. A label is a product choice under subject product.choice:dimension:<slug>; use the current decision or raise a missing/changed one to Product as a BLOCKED decision with your recommendation.
4. Depth follows the label. A non-differentiating dimension takes the most reliable widely used approach with the least custom code; deviation needs a named reason. A differentiating dimension gets a reviewed architecture; add the research layer and weekly scans only after the first users or revenue, and before then skip them. Research names the problem space, who does the best work in it now and their latest published method, and maps it to the dimension's goal as concise do and don't guidance; the gap is the current design against that. Group differentiating dimensions N to 1 into research tracks where their commercial solutions are linked, and scan each track weekly with `cady-product-research` (its technology and competition references) for material improvements since the last scan; keep the scan as a File cited from the track's work item, and test any promising idea with `cady-company-experiment` before it changes the architecture.
5. Test depth follows the change and design comes before tests. Plan bug fixes with root cause, owner and blast radius; test features against the touched dimensions and architecture changes with core end-to-end tests after research and any needed experiment. Run checks once per revision, record unrun evidence as unrun, and fix the root cause across instances. Test each dimension's contract and key edge cases beside its owner, then each journey goal through real interfaces.
6. Review once from Product (journey goals, user alternative, best in class) and Engineering (dimension architecture, research gaps, size, lifecycle and ownership). Give every touched dimension and the whole a verdict (right, right but over-built, or wrong shape), best alternative, gap and deletion. Extend the last review rather than redo it, checkpoint the verdict, and return ranked direction to Product, whose scope decisions stand. Update each touched dimension's goal and acceptance, and deduplicate hunting findings against open items.
7. Dimensions first, then the whole. Test, fix and review each dimension until its narrow tests pass and the review finds nothing material; dimensions may run in tandem. Then run the core end-to-end tests and an overall hunt across dimension seams. A failure there that a dimension test should have caught gets that dimension test added.
8. Record each motion's result as a checkpoint on the cycle's work item: findings as Projects items citing the dimension, journey goal and evidence; delivered items with the reviewed commit; the review with its scores and ranked direction. Persist each dimension and end-to-end run as a File cited from that work item (dimension, test, failure signature, commit, date), deduplicated by signature. A signature that persists across three runs or three days becomes an architecture finding for the next review, not a test to re-run until its work lands. Schedule recurring motions with `cady-company-manage-agents` (reference scheduling) under an owner binding; this skill grants no schedule, send or spend authority.
9. Data paths. For a material data path (import, transformation, reconciliation or migration), identify the authoritative source and record identity; decide replay/backfill and schema-drift behavior; then reconcile the result against the business outcome and relevant quality or freshness limits. Reuse `cady-engineering-integrations` for provider idempotency. Product or the domain owner defines metric meaning; Engineering owns pipeline correctness and reports unresolved drift.

## Acceptance

- [ ] one map holds journey goals and architecture, each as one simple diagram
- [ ] the dimension register is MECE
- [ ] each review gives every touched dimension a design verdict, and a recurring failure signature becomes an architecture finding rather than a rerun
- [ ] each pass ends with a checkpoint: ranked review, reviewed delivery or a deduplicated finding list
- [ ] each review reports its top changes with the goal each serves, cross-product tradeoffs with why each lasts, and the decision needed

## Owner checks

- current direction and decisions read before mapping
- every dimension has one owner, one question and a label that is decided or raised to Product
- differentiating dimensions have a dated research scan and a reviewed design
- findings are deduplicated against open items before filing

## Result

### Artifact refs

- company:work:<workId>
- file:<fileId>
- **Transition:** each motion's claim holder checkpoints its result on the cycle work item
