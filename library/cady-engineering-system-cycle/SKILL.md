---
name: "cady-engineering-system-cycle"
description: "Recurring system cycle: map, dimensions, routed motions. Use when: Clear a product's engineering backlog in recurring cycles from its goal map, system dimensions and state-routed motions. Not for: One bounded change with clear acceptance (use `cady-engineering-method`) or deciding what to build and for whom (use `cady-product-manage`)."
license: "MPL-2.0"
compatibility: "Requires Cady (app.cadyworks.com/mcp)"
metadata:
  cady-id: "skill.engineering.system_cycle"
  version: "87a029b14d6da8cdf1cd"
  library: "d7882682aac57260"
  function: "engineering"
---
# Recurring system cycle: map, dimensions, routed motions

**Point:** Route each pass to review, build or hunt from current state, so work tracks the goal, not a rotation.

**Company context:** `cady_read {"search": "<what you are about to do, in one sentence>"}`

**Bets** (where this differs from the default):
- Choose the motion from current state: review when direction is stale, engineer when ready items exist, hunt after a dimension closes. Instead of: Run a fixed rotation of review, build and test phases each cycle.
- Label each dimension differentiating or not; take the standard approach on the rest and give the differentiators reviewed design and research. Instead of: Give every part of the system the same review and research depth.
- Group several issues into families by architectural cause and fix each family at the lowest owner that can hold the target. Instead of: Fix each reported issue on its own, in the order filed.
- A failure signature that persists across three runs or three days becomes an architecture finding, not another rerun. Instead of: Keep rerunning the failing check until it passes.
- Hunt with an agent that did not build what it hunts. Instead of: Let the building agent test its own work at the end of the pass.

Clear a product's engineering backlog in recurring cycles from its goal map, system dimensions and state-routed motions.

**Not for:** One bounded change with clear acceptance (use `cady-engineering-method`) or deciding what to build and for whom (use `cady-product-manage`).

**Unit of work:** one cycle of one product: its map, dimension register and the review, build and hunt motions. **Kind:** execution. **Parallel:** yes. 

## Always

- Journey goals are user outcomes, not features or implementation decisions.
- Development tests find and prove; this cycle adds no gate. CI gates follow the company's recorded stage, and an exposed security, isolation or authority defect still blocks its path.
- Before starting a lane, search open Cady work and open PRs (`gh pr list` plus file overlap) for the same thing; extend or coordinate rather than duplicate.

## Inputs

### Evidence refs

- company direction and current decisions
- the product's product map and dimensions page (the File named by the map clause of decision product:offering-<key>)
- open findings and the last review checkpoint
- file:<fileId> research notes

### Work fields

- cycle scope (dimensions or overall)
- motion
- ranked findings or delivered items
- next owner action

## Procedure

1. Objective. Clear the product's engineering backlog by the motion its current state calls for: review, engineer or hunt, routed from current state, not a fixed rotation. Review when there is no ranked direction, when the goals, a dimension label or a research scan changed since it was written, or when findings contradict it. Engineer when the direction is current and ready items exist, under the engineering role card. Hunt, under the QA role card and by an agent that did not build what it hunts, after a dimension closes, across seams after the end-to-end tests (step 7), or when the finding list is empty or stale. With a short queue one agent reviews and engineers in the same pass, its diffs still getting the engineering role's independent review; give a motion its own agent only when its queue justifies it, and never let two agents share a claim.
2. Map once, update in place. Keep one product map, with its dimensions page, at its single writer: the repo for software, a Notion page or HTML template otherwise. Publish it as one Markdown Cady File, named by the `map [file:<id>]` clause of the product's Offering line (decision product:offering-<key>); product-area context serves it as `Product map (<key>): file:<id>`. Whoever merges a change to the map then runs `cady product map publish <path> --product <key>` from the merged source: the first run attaches the File (pass `--writer <url>` then), and once it is attached every run adds a version, keeps the writer and records no decision. The system_map reference holds the template and the drafting steps. On the map: journey goals as user outcomes in lifecycle order and architecture as one simple diagram. Features and implementation choices are decisions, not goals. Read the current decisions (cady_read search kinds decision) first; never restate what a decision already holds.
3. Name high-level, mutually exclusive, collectively exhaustive dimensions that every goal crosses, each with one question, owner and boundary. Before users or revenue, name only the 3 to 5 a goal actually crosses. With users, expect 8 to 14. For a product you build in code, every code area has exactly one owner, including a module’s SQL, pages and tests; do not register qualities such as cost, isolation, verification or efficiency as owners (`references/quality-classes.md`). Keep only what has its own owner, question and test. Label each differentiating or not on the map's Dimensions page; only a real choice becomes a decision. The dimensions reference holds the rest of the register rules.
4. Depth follows the label. A non-differentiating dimension takes the most reliable widely used approach with the least custom code; deviation needs a named reason. A differentiating dimension gets a reviewed architecture (apply the Product card’s depth judgement on the decisive problem from the first session, including before users or revenue) and, only after the first users or revenue, a weekly research scan with `cady-product-research`; test a promising idea with `cady-company-experiment` before it changes the architecture; before then, research only where that judgement calls for it. The dimensions reference holds the research rules.
5. Test depth follows the change and design comes before tests. Plan bug fixes with root cause, owner and blast radius; for a product you build in code, add only the classes crossed, usually in one line. For its features and architecture, name touched owners, adjacent loops and layers; route about four questions from `references/quality-classes.md` and recurring owner cells, and answer them in the writer brief; a small fix follows the trail into adjacent logic instead; a change to method or agent-behaviour text follows `cady-company-change-agent-behaviour`; test features against the touched dimensions and architecture changes with core end-to-end tests after research and any needed experiment. Record unrun evidence as unrun, and fix the root cause across instances.
6. Every plan ends with the engineering card's map review. Beyond that, select Product and Engineering review to match the risk and open questions, not as mandatory model calls or serial phases. Product judges journey goals, user alternatives and scope; Engineering judges architecture, research gaps, size, lifecycle and ownership. Consider a further plan review when unresolved design choices could cause costly rework, especially for authority, schema, several owners or a differentiating owner. An architecture review of several issues, by default, groups them into families by architectural cause and ends in ordered fix slices; the review reference holds the method. A cycle records the map review's result as a verdict for each touched dimension and the whole (right, right but over-built, or wrong shape), with best alternative, gap and deletion. Extend the last review, checkpoint the verdict, and return ranked direction to Product, whose scope decisions stand. Update affected goals and acceptance; deduplicate hunting findings against open items.
7. Integrate meaningful work as it arrives and check affected dimensions, journeys and seams at a depth selected for risk. Hunt where its findings can change the next action, not as a fixed phase. A failure that a dimension test should have caught gets that test added. Apply cady-engineering-independent-review to reuse review and evidence. Ready independently useful scope need not wait for unrelated branches; keep a coupled refactor in one consolidated PR.
8. Record each motion's result as a checkpoint on the cycle's work item: findings as Projects items citing the dimension, journey goal and evidence; for a product you build in code, place whole-outcome failures under the journey, and each other finding in exactly one owner × quality class cell using `references/quality-classes.md`. When findings recur under the same owner and quality class, assess whether they share an architectural cause; use that evidence to update the owner’s planning defaults. Record delivered items with the reviewed commit; the review with its scores and ranked direction. Schedule recurring motions with `cady-company-manage-agents` under an owner binding; this skill grants no schedule, send or spend authority. End each cycle's checkpoint with the two lines of execution topic company_review close. The review reference holds the checkpoint's citation rules.
9. Data paths. For a material data path (import, transformation, reconciliation or migration), identify the authoritative source and record identity, decide replay/backfill and schema-drift behavior, and reconcile the result against the business outcome. Reuse `cady-engineering-integrations` for provider idempotency. The review reference holds the rest.

## Acceptance

- [ ] one product map, published as the File the product's Offering line names, holds journey goals and one simple architecture diagram
- [ ] the dimension register is MECE
- [ ] each review gives every touched dimension a design verdict, and a recurring failure signature becomes an architecture finding rather than a rerun
- [ ] each pass ends with a checkpoint: ranked review, reviewed delivery or a deduplicated finding list, ending with the close's two lines
- [ ] each review reports its top changes with the goal each serves, cross-product tradeoffs with why each lasts, and the decision needed

## Owner checks

- current direction and decisions read before mapping
- every dimension has one owner, one question and a label on the map's Dimensions page; a real choice is decided or raised to Product
- differentiating dimensions have a reviewed design and decision-relevant research; recurring scans follow step 4
- findings are deduplicated against open items before filing

## Result

### Artifact refs

- company:work:<workId>
- file:<fileId>
- **Transition:** each motion's claim holder checkpoints its result on the cycle work item

## References
- Read [Engineering cycle dimension register and research](references/engineering-cycle-dimensions.md) when you name, label or change the dimension register, or scan research for a differentiating dimension.
- Read [Software quality classes](references/quality-classes.md) when planning a change or placing a finding for a product you build in code.
- Read [Engineering cycle review, checkpoint and data paths](references/engineering-cycle-review.md) when you run an architecture review of several issues, write a motion's checkpoint, or check a material data path.
- Read [Product map template and drafting](references/engineering-system-map.md) when you draft, restructure or publish a product's product map.
