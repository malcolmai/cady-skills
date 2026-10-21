---
name: "cady-engineering-system-cycle"
description: "Recurring system cycle: map, dimensions, routed motions. Use when: Clear a product's engineering backlog in recurring cycles from its goal map, system dimensions and state-routed motions. Not for: One bounded change with clear acceptance (use `cady-engineering-method`) or deciding what to build and for whom (use `cady-product-manage`)."
license: "MPL-2.0"
compatibility: "Requires Cady (app.cadyworks.com/mcp)"
metadata:
  cady-id: "skill.engineering.system_cycle"
  version: "1e5e7f0848d9190f8f38debf7e04f8cdc9a392375d97e177b0b775f51829e3b7"
  library: "cf93c1d9ce44e1ac"
  function: "engineering"
---
# Recurring system cycle: map, dimensions, routed motions

**Company context:** `get_cady_context({"area": "product/<productId>/engineering", "task": "<what you are about to do, in one sentence>", "knownMethods": {"skill.engineering.system_cycle": "1e5e7f0848d9190f8f38debf7e04f8cdc9a392375d97e177b0b775f51829e3b7"}})`

Clear a product's engineering backlog in recurring cycles from its goal map, system dimensions and state-routed motions.

**Not for:** One bounded change with clear acceptance (use `cady-engineering-method`) or deciding what to build and for whom (use `cady-product-manage`).

**Unit of work:** one cycle of one product: its map, dimension register and the review, build and hunt motions. **Kind:** execution. **Parallel:** yes. **Can release:** no. 

See [Always](references/always.md).
## Procedure

1. Map once, update in place. Keep one system map beside the product's source (a File for non-software): journey goals as user outcomes in lifecycle order and architecture as one simple diagram. Features and implementation choices are decisions, not goals. Read get_company_direction and current get_company_work decisions first; never restate what a decision already holds.
2. Name high-level, mutually exclusive, collectively exhaustive dimensions that every goal crosses, each with one question, owner and boundary. Keep authentication separate from permissions, and agent action/tool authority separate from user/data access; give agent management its own dimension. Name the commercial category a buyer would compare. Label each differentiating or not. A label is a product choice under subject product.choice:dimension:<slug>; use the current decision or raise a missing/changed one to Product as a BLOCKED decision with your recommendation.
3. Depth follows the label. A non-differentiating dimension takes the most reliable widely used approach with the least custom code; deviation needs a named reason. A differentiating dimension gets a research layer and a reviewed architecture. Research names the exact problem space (often adjacent to the need, not identical), who does the best work in it now and their latest published method, and maps that to the dimension's goal as concise guidance with exact do and don't examples for each layer in its scope; the gap is the current design against that. Group differentiating dimensions N to 1 into research tracks where their commercial solutions are linked, and scan each track weekly with `cady-product-research-technology` and `cady-product-research-competition` for material improvements since the last scan; keep the scan as a File cited from the track's work item, and test any promising idea with `cady-company-experiment` before it changes the architecture. A scan with nothing material says so in one line.
4. Test depth follows the change and design comes before tests. Plan bug fixes with root cause, owner and blast radius; test features against the touched dimensions and architecture changes with core end-to-end tests after research and any needed experiment. Run checks once per revision, record unrun evidence as unrun, and fix the root cause across instances. Test each dimension's contract and key edge cases beside its owner, then each journey goal through real interfaces; results are findings, not gates.
5. Route each pass from current state; motions are conditions, not a fixed rotation. Review when there is no ranked direction, when the goals, a dimension label or a research scan changed since it was written, or when findings contradict it. Engineer when the direction is current and ready items exist, under the engineering role card. Test and iterate automatically for narrow pieces: when a dimension-scoped item lands, the same lane runs that dimension's tests and fixes until they pass. Hunt, under the QA role card and by an agent that did not build what it hunts, after a dimension closes, across seams after the end-to-end tests (step 7), or when the finding list is empty or stale. With a short queue one agent reviews and engineers in the same pass, and its diffs still get the engineering role's independent review; give a motion its own agent only when its queue justifies it, and never let two agents share a claim.
6. Review once from Product (journey goals, user alternative, best in class) and Engineering (dimension architecture, research gaps, size, lifecycle and ownership). Give every touched dimension and the whole a verdict (right, right but over-built, or wrong shape), best alternative, gap and deletion; check that numbers and structures have a principled need. Extend the last review rather than redo it, checkpoint the verdict, and return ranked direction to Product, whose scope decisions stand. Report only the highest-level changes, their journey goals, cross-product tradeoffs and any decision needed. Update each touched dimension's goal and acceptance, and deduplicate hunting findings against open items.
7. Dimensions first, then the whole. Test, fix and review each dimension until its narrow tests pass and the review finds nothing material; dimensions may run in tandem. Then run the core end-to-end tests and an overall hunt across dimension seams. A failure there that a dimension test should have caught gets that dimension test added.
8. Record each motion's result as a checkpoint on the cycle's work item: findings as Projects items citing the dimension, journey goal and evidence; delivered items with the reviewed commit; the review with its scores and ranked direction. Persist each dimension and end-to-end run as a File cited from that work item (dimension, test, failure signature, commit, date), deduplicated by signature; a result is evidence for its commit only. A signature that persists across three runs or three days becomes an architecture finding for the next review, not a test to re-run until its work lands. Schedule recurring motions with `cady-core-scheduling` under an owner binding; this skill grants no schedule, send or spend authority.

## Acceptance

- [ ] one map holds journey goals and architecture, each as one simple diagram
- [ ] the dimension register is MECE and authentication is separate from permissions
- [ ] each dimension passes its narrow tests and review before the overall end-to-end hunt
- [ ] each review gives every touched dimension a design verdict, and a recurring failure signature becomes an architecture finding rather than a rerun
- [ ] each pass names why it reviewed, engineered or hunted, and ends with a checkpoint: ranked review, reviewed delivery or a deduplicated finding list
- [ ] each review reports its top changes with the goal each serves, cross-product tradeoffs with why each lasts, and the decision needed

See [Owner checks](references/owner-checks.md).
