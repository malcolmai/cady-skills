---
name: "cady-engineering-system-cycle"
description: "Recurring system cycle: map, dimensions, routed motions. Use when: Clear a product's engineering backlog in recurring cycles from its goal map, system dimensions and state-routed motions. Not for: One bounded change with clear acceptance (use `cady-engineering-method`) or deciding what to build and for whom (use `cady-product-manage`)."
license: "MPL-2.0"
compatibility: "Requires Cady (app.cadyworks.com/mcp)"
metadata:
  cady-id: "skill.engineering.system_cycle"
  version: "bcf07ba454b58418091ca7b603b7dd1bd6825741b44b0b2c2cf7554a65b04387"
  function: "engineering"
---
# Recurring system cycle: map, dimensions, routed motions

Clear a product's engineering backlog in recurring cycles from its goal map, system dimensions and state-routed motions.

**Not for:** One bounded change with clear acceptance (use `cady-engineering-method`) or deciding what to build and for whom (use `cady-product-manage`).

**Unit of work:** one cycle of one product: its map, dimension register and the review, build and hunt motions. **Kind:** execution. **Parallel:** yes. **Can release:** no. 

## Always

- Journey goals are user outcomes, not features or implementation decisions.
- Development tests find and prove; this cycle adds no gate. CI gates follow the company's recorded stage, and an exposed security, isolation or authority defect still blocks its path.

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

1. Map once, update in place. Keep one system map, the company's own artifact, beside the product's source (a File for non-software; step 1 creates it if none exists): its journey goals, each a user outcome in lifecycle order, and its architecture in about fifteen boxes, as one simple mermaid diagram each. Features and implementation choices are decisions, not goals. Read get_company_direction and get_company_work decisions {state: "current"} first; never restate what a decision already holds.
2. Name the dimensions. List high-level, mutually exclusive, collectively exhaustive dimensions that every goal crosses, each with the one question it answers, its owner and its boundary. Split what is often blurred, for example who an actor is (authentication) from what it may do (permissions), and, where agents act, their action and tool authority from user and data access. Name for each the commercial product category a buyer would compare. Where agents act through the product, cover their interface and context as both reads and writes, and give agent management (design, approval, schedule, review, retirement) its own dimension. Label each differentiating (users choose the product partly for it) or not. A label is a product choice under subject product.choice:dimension:<slug>: use the current decision; raise a missing or changed one to Product as a BLOCKED decision item with your recommendation, and work on the draft meanwhile.
3. Depth follows the label. A non-differentiating dimension takes the most reliable widely used approach with the least custom code; deviation needs a named reason. A differentiating dimension gets a research layer and a reviewed architecture. Research names the exact problem space (often adjacent to the need, not identical), who does the best work in it now and their latest published method, and maps that to the dimension's goal as concise guidance with exact do and don't examples for each layer in its scope; the gap is the current design against that. Group differentiating dimensions N to 1 into research tracks where their commercial solutions are linked, and scan each track weekly with `cady-product-research-technology` and `cady-product-research-competition` for material improvements since the last scan; keep the scan as a File cited from the track's work item, and test any promising idea with `cady-company-experiment` before it changes the architecture. A scan with nothing material says so in one line.
4. Test depth follows the change, and design comes before dimension tests. A bug fix is planned (root cause, owner, what else it could break) and takes unit tests. A feature takes a design review of the dimensions it touches (step 6), then their narrow tests: a well-tested wrong design is still wrong. An architecture change takes the core end-to-end tests, after research and an evaluated experiment where its dimension is differentiating (step 3). Unit tests run only for what changed (run each check once per revision, record unrun evidence as unrun, and fix by class: the root cause across every instance, not the one that failed); a test's name or one-line docstring says what it proves for which edge case, citing a finding or decision id if one exists. Dimension tests prove each dimension's contract and key edge cases beside its owner; core end-to-end tests run one per journey goal through the real interfaces. Their results are recorded findings, not gates.
5. Route each pass from current state; motions are conditions, not a fixed rotation. Review when there is no ranked direction, when the goals, a dimension label or a research scan changed since it was written, or when findings contradict it. Engineer when the direction is current and ready items exist, under the engineering role card. Test and iterate automatically for narrow pieces: when a dimension-scoped item lands, the same lane runs that dimension's tests and fixes until they pass. Hunt, under the QA role card and by an agent that did not build what it hunts, after a dimension closes, across seams after the end-to-end tests (step 7), or when the finding list is empty or stale. With a short queue one agent reviews and engineers in the same pass, and its diffs still get the engineering role's independent review; give a motion its own agent only when its queue justifies it, and never let two agents share a claim.
6. Review is one pass with two views. Product: journey goals, the user's real alternative and best in class. Engineering: each dimension's architecture, research gaps and size: no layer, option, tool or parameter the goals do not need, the right first call obvious, and cross-dimension logic smallest at one owner. Score each dimension and the whole, giving each touched one a design verdict (right, right but over-built, or wrong shape) with the best alternative, the gap and what to delete; judge a non-differentiating one quickly against the standard approach. Each verdict also asks whether every number or structure the design rests on is principled (a cited limit or need) or a patch, whether it covers its whole lifecycle, and whether competing goals such as completeness and size can both improve rather than trade. The building lane runs this review itself, deeply, when work in a dimension starts (at a task's start for each it spans), extends that dimension's last recorded review rather than redoing it, and checkpoints the verdict, so the owner gives direction rather than corrections. Return a ranked direction with proposed work items to Product, whose scope decisions stand, superseding the last review rather than adding beside it. Report to the person only: the few highest-level changes, each with what it fixes and the journey goal it serves; the tradeoffs with cross-product implications, each with why it is the lasting best-in-class choice rather than a patch and what it implies for the rest of the product; and the decision needed, if any. End review/plan (one step) with Update goals: for each touched dimension, update its goal and acceptance, which clears its stale flag (the goal read shows followThrough.stale when decisions linked to it by goalId are newer than its last update), and record any new decision. Hunting finds without fixing: check open findings first, never re-report one, vary paths and inputs toward unexplored risk, and end with a deduplicated list ranked by user impact.
7. Dimensions first, then the whole. Test, fix and review each dimension until its narrow tests pass and the review finds nothing material; dimensions may run in tandem. Then run the core end-to-end tests and an overall hunt across dimension seams. A failure there that a dimension test should have caught gets that dimension test added.
8. Record each motion's result as a checkpoint on the cycle's work item: findings as Projects items citing the dimension, journey goal and evidence; delivered items with the reviewed commit; the review with its scores and ranked direction. Persist each dimension and end-to-end run as a File cited from that work item (dimension, test, failure signature, commit, date), deduplicated by signature; a result is evidence for its commit only. A signature that persists across three runs or three days becomes an architecture finding for the next review, not a test to re-run until its work lands. Schedule recurring motions with `cady-core-scheduling` under an owner binding; this skill grants no schedule, send or spend authority.

## Acceptance

- [ ] one map holds journey goals and architecture, each as one simple diagram
- [ ] the dimension register is MECE and authentication is separate from permissions
- [ ] each dimension passes its narrow tests and review before the overall end-to-end hunt
- [ ] each review gives every touched dimension a design verdict, and a recurring failure signature becomes an architecture finding rather than a rerun
- [ ] each pass names why it reviewed, engineered or hunted, and ends with a checkpoint: ranked review, reviewed delivery or a deduplicated finding list
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

**Company context:** `get_cady_context({"area": "product/<productId>/engineering", "task": "<what you are about to do, in one sentence>", "knownMethods": {"skill.engineering.system_cycle": "bcf07ba454b58418091ca7b603b7dd1bd6825741b44b0b2c2cf7554a65b04387"}})`
