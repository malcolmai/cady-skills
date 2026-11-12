---
name: "cady-product-manage"
description: "Product management and discovery. Use when: Decide what to build and why; run discovery; plan each release and its go/no-go; run a goal to done. Not for: Engineering execution (use `cady-engineering-method`), QA runs (use `cady-qa-method`) or GTM campaigns (use `cady-gtm-method`)."
license: "MPL-2.0"
compatibility: "Requires Cady (app.cadyworks.com/mcp)"
metadata:
  cady-id: "skill.product.manage"
  version: "e38584ba8f75a1bf3d7b"
  library: "6501d292ae359b43"
  function: "product"
---
# Product management and discovery

**Point:** Decide what to build from evidence and run each goal to a live, measured result, because plans are not outcomes.

**Company context:** `cady_read {"search": {"query": "<what you are about to do, in one sentence>"}}`

**Bets** (where this differs from the default):
- Start with one offering, one assumed ICP and problem assumption with its disproof, and one first-value goal; defer everything else. Instead of: Build the full product model first: personas, roadmap, dimensions, research and stories.
- Rank with the lightest frame that separates the options, labelling each estimate measured, evidence-based or guess. Instead of: Score every item with RICE or a weighted matrix.
- Decide product calls yourself and record them; ask the owner only a call still controversial after testing, or a fact only they hold. Instead of: Ask the founder to approve each product choice before building.
- When no ready item remains, review the system against the goal; only a review with no material finding ends the roadmap. Instead of: Report done when the backlog is empty.
- End a goal only with a reading from its own source and the release live; delivered work with the target unmet keeps the goal open. Instead of: Close the goal when its items ship or the release goes out.

Decide what to build and why; run discovery; plan each release and its go/no-go; run a goal to done.

**Not for:** Engineering execution (use `cady-engineering-method`), QA runs (use `cady-qa-method`) or GTM campaigns (use `cady-gtm-method`).

**Unit of work:** one product outcome, assumption or release work item. **Kind:** strategy. **Parallel:** no. 

## Inputs

### Evidence refs

- company direction
- current decisions and assumptions
- file:<fileId> research, notes and observations
- crm:party:<partyId> and interactions
- release work item

### Work fields

- outcome or assumption
- customer group
- acceptance or test
- decision needed

## Procedure

1. Objective. Decide what to build, for whom and why, from evidence, and keep one record per decision. The minimum is an offering, an assumed ICP with a problem assumption and one goal; everything else waits for a decision that needs it.
2. Read cady_read company:direction, then cady_read changes {kind: strategy} for its current decisions, bets and assumptions (cady_read decision:<subject> reads one). Read the Files and CRM evidence they cite before judging; unknown stays unknown. On a direction change, make each open goal's call; replace or rule out bets and decisions that assumed the old offer, citing the new direction; close CRM tracks for audiences the new direction drops (crm_interactions_set: the motion's closing stage, the reason as the note).
3. Minimum first session: (a) if the company has no product, name it and record the offering with decisions_set (subject product:offering-<productId>, headline exactly "Offering <productId>: <name>"); goals, tasks, stories and product decisions must name a defined productId. (b) If no customer has given direction (no accepted ICP in direction, no current assumption, no customer evidence in CRM), do not wait or treat a guess as validated: state one assumed ICP and one problem assumption, with what would prove it wrong, record it as a hypothesis bet (decisions_set, basis hypothesis, with its measure), and tell the person it is an assumption they can replace. (c) Then one goal record with brief.target under `../../references/company-goals.md`, as `cady-company-executive-review` step 13 defines; for a product people use, make it a first-value goal read from a blind walk of one story on the deployed product. Defer dimensions, maps, other stories, research and module choices until a decision needs them, except on the crux. The first-session and run-to-done reference holds the record fields.
4. Record assumptions as `cady-company-decision-questions` step 3 does. Get evidence for the assumption with that skill (route) and `cady-company-experiment` (pre-registered tests), as Projects work bound to the assumption (evidenceRefs company:work:<hypothesisId>); run interviews with `cady-product-customer-interview`. If the evidence needs calls and no pipeline is getting the ICP onto calls, hand it to the Executive as the binding constraint and continue independent product work under the Product card’s depth judgement.
5. Keep evidence tied to the offering. Keep interview notes, observations and raw source material in Files through files_set mode begin_upload and files_set mode complete_upload, citing each as file:<fileId> from the assumption or work item. Put curated Competition or Technology analysis in the Research library with `cady-product-research`; preserve and link existing direction, decisions and work context rather than replacing it. Never paste evidence into direction or a work headline, or create another record to hold learning.
6. When a shipped goal missed its measure or users showed no interest, read it by the "Separate causes before concluding no demand" bet in `cady-company-experiment`. When evidence settles an assumption, validate or replace its bet with decisions_set. A product choice about behaviour goes to the product map or a test, not a decision; one that moves resources between products or functions is a bet, written with decisions_set (`cady-company-decision-check` step 6). Any other product call goes in the work result. Raise a choice reserved to the founder as an ask (asks_set) to the owner with the question; it reaches them on Needs you (cady_read view work.needs_you). Write an accepted ICP or bet with decisions_set.
7. Scope from the ranked gap list against the bar; subtract before adding. Rank with the lightest frame that separates the options: for a few items, cost of delay (what each week of waiting loses in revenue, risk, learning or a deadline) divided by effort, highest first; RICE (reach x impact x confidence / effort) only for a longer list with comparable reach data. Label each estimate measured, evidence-based or guess, and never let precise-looking scores hide guesses; a fixed deadline or a blocker on a critical path overrides the score. Record the ranking rationale on the work item. Bind product work to the offering with the company product owner and productId. Plan each release as a work item with release {stage, buildBy, qaDays, thresholds}, per the release plan (`../../references/release-plan.md`).
8. Check release thresholds against exact QA, engineering and customer evidence on the release work item. Go: record the go on that work (work_set {id, note: the go, with evidence refs}, then {id, next: 'ready to release'}); keep release stage 'qa'. No-go: status blocked with the unmet threshold and next action (work_set {id, status: blocked, result, next}) when you hold the claim. Stage 'released' is set by the agent that owns the release, once the deploy receipt reads back the deployed artifact and target, citing the receipt; whoever deployed.
9. When the requested analysis includes validation work, create a scoped Projects item with its acceptance and next action. After verifying a specific successor or confirming the action is complete, update or clear the existing next action with work_set {id, next} when allowed; do not leave a superseded action current or create unrequested follow-on work.
10. Dimension maps: use the map recipe in the product card.
11. Run to done (the loop for a goal owner; only f ends it). a) Work the goal's ranked items (step 7) through Engineering and QA. b) Raise each call that stays controversial after testing and review, or owner-only fact, the roadmap needs once in this run, each with options, your recommendation, unlocks and `blocks` naming its own item (run sequence step 5); decide the rest yourself and record it, and build what does not depend on it. c) When no ready item remains, run the `cady-engineering-system-cycle` review against the goal's doneWhen and the dimension register: findings become ranked items and you return to a; only a review with no material finding ends the roadmap, recorded as a checkpoint. d) Release per policy (read policy:release and grant.release:<company>, `cady-company-decision-check` step 2): under a covering grant, promote through the company's release route yourself; where the policy names who deploys, prepare the exact release (SHA, checks, rollback) and raise one approval ask to that person; with no policy, raise one ask recommending one. Never widen a grant. e) Verify by reading the live target back; cite the deploy receipt and set the release stage (step 8). f) Close the goal only from a reading you took of its target source, never a count you did not read: stop it as met only when the release is live, doneWhen holds and the target count is met; otherwise keep it open and make driving the target the next ranked item. The first-session and run-to-done reference holds the release routes and the close.

## Acceptance

- [ ] with no offering, the offering, then an assumed ICP and problem assumption, then one goal are created in that order and a test is planned
- [ ] each bet names its basis, measure and the item it replaces
- [ ] observations are files linked from work, never a new store
- [ ] each release has an explicit go or no-go on its own work item with evidence
- [ ] requested validation work is recorded, and superseded next actions are updated only by a work_set on the exact current work

## Owner checks

- current direction and decisions read before judging
- assumption recorded as a hypothesis bet, not in direction
- evidence held as Files and cited by ref
- go/no-go recorded on the release work item
- offering exists before product-area calls; later structure waits for a decision that needs it

## Result

### Artifact refs

- company:work:<workId>
- file:<fileId>
- **Transition:** the claim holder reports the decision, assumption or release verdict and its evidence

## References
- Read [Product first session and run to done](../../references/product-manage-detail.md) when you run a product's first session (offering, assumption, first goal), or run a goal through release, verification and close.
- Read [Release plan](../../references/release-plan.md) when you plan a release or run its go/no-go.
