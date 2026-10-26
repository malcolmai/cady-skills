---
name: "cady-product-manage"
description: "Product management and discovery. Use when: Decide what to build and why; run discovery; plan each release and its go/no-go; run a goal to done. Not for: Engineering execution (use `cady-engineering-method`), QA runs (use `cady-qa-method`) or GTM campaigns (use `cady-gtm-method`)."
license: "MPL-2.0"
compatibility: "Requires Cady (app.cadyworks.com/mcp)"
metadata:
  cady-id: "skill.product.manage"
  version: "873f59a285395157e1f2"
  library: "23f51ba2f726595e"
  function: "product"
---
# Product management and discovery

**Company context:** `get_cady_context({"area": "product/<productId>/scope", "task": "<what you are about to do, in one sentence>", "knownMethods": {"skill.product.manage": "873f59a285395157e1f2@23f51ba2f726595e"}})`

Decide what to build and why; run discovery; plan each release and its go/no-go; run a goal to done.

**Not for:** Engineering execution (use `cady-engineering-method`), QA runs (use `cady-qa-method`) or GTM campaigns (use `cady-gtm-method`).

**Unit of work:** one product outcome, hypothesis or release work item. **Kind:** strategy. **Parallel:** no. **Can release:** no. 

## Inputs

### Evidence refs

- company direction
- current decisions and hypotheses
- file:<fileId> research, notes and observations
- crm:party:<partyId> and interactions
- release work item

### Statement fields

- outcome or hypothesis
- customer group
- acceptance or test
- decision needed

## Procedure

1. Objective. Decide what to build, for whom and why, from evidence, and keep one record per decision. The minimum is an offering, an assumed ICP with a problem hypothesis and one goal; everything else waits for a decision that needs it.
2. Read read_cady company:direction, then get_cady_context for recent decisions and get_company_work with decisions {state: "current"} for every current decision and hypothesis. Read the Files and CRM evidence they cite before judging; unknown stays unknown.
3. Minimum first session: (a) if the company has no offering, create it first (confirm none exists with get_cady_context), then manage_company_product with expectedRevision null and links []; the product area needs the productId only it creates. (b) Discovery is part of the job: if no customer has given direction (no accepted ICP in direction, no current hypothesis, no customer evidence in CRM), do not wait and do not build on a guess. State one assumed ICP (who, circumstance, observable signals) and one problem hypothesis (the job, current alternative, what they pay in money, time or risk), with what would prove it wrong. Record it with submit_company_work_checkpoint: statement is the hypothesis, status OPEN, decision {kind: "hypothesis", subject: "hypothesis:product.<slug>", rationale, authority: "agent" and no decidedBy}, evidenceRefs to the sources used. Tell the person it is an assumption they can replace. (c) Then one goal with brief.target. Defer dimensions, maps, stories, research and module choices until a decision needs them.
4. Record hypotheses as `cady-company-decision-questions` step 3 does. Get evidence for the hypothesis with that skill (route) and `cady-company-experiment` (pre-registered tests), as Projects work bound to the hypothesis (evidenceRefs company:work:<hypothesisId>); run interviews with `cady-product-customer-interview`. If the evidence needs calls and no pipeline is getting the ICP onto calls, hand it to the Executive as the binding constraint rather than adding product work.
5. Keep evidence tied to the offering. Keep interview notes, observations and raw source material in Files through files.upload with mode "begin" and files.upload with mode "complete", citing each as file:<fileId> from the hypothesis or work item. Put curated Competition or Technology analysis in the Research library with `cady-product-research`; preserve and link existing direction, decisions and work context rather than replacing it. Never paste evidence into direction or a work statement, or create another record to hold learning.
6. When evidence settles a hypothesis or product choice, use subject hypothesis.outcome:<function>.<slug> or product.choice:<slug> respectively. Record it with submit_company_work_checkpoint: statement is the decision, status COMPLETE, decision {kind: "decision", subject, rationale, authority, decidedBy, supersedes: [the hypothesis or earlier decision workIds]}. For your own choice use authority "agent" and omit decidedBy, source and quote; for a person use their exact words as source "chat" and quote, or a verified source "grant" with grantId. Raise a choice reserved to the founder as a BLOCKED decision item addressed to the owner, with the question as nextAction; it reaches them as asksForYou. Propose an accepted ICP or bet for direction only through update_company_direction.
7. Scope from the ranked gap list against the bar; subtract before adding. Rank with the lightest frame that separates the options: for a few items, cost of delay (what each week of waiting loses in revenue, risk, learning or a deadline) divided by effort, highest first; RICE (reach x impact x confidence / effort) only for a longer list with comparable reach data. Label each estimate measured, evidence-based or guess, and never let precise-looking scores hide guesses; a fixed deadline or a blocker on a critical path overrides the score. Record the ranking rationale on the work item. Bind product work to the offering with the company product owner and productId. Plan each release as a work item with release {stage, buildBy, qaDays, thresholds}, per the release plan (`../../references/release-plan.md`).
8. Check release thresholds against exact QA, engineering and customer evidence on the release work item. Go: record the go decision there under subject release.go:<workId>, with evidence refs and nextAction 'ready to release'; keep release stage 'qa'. No-go: status BLOCKED with the unmet threshold and next action, through transition_company_work(action: 'checkpoint', status: 'BLOCKED', nextAction) when you hold the claim. Stage 'released' is set by the agent that owns the release, once the deploy receipt reads back the deployed artifact and target, citing the receipt; whoever deployed.
9. When the requested analysis includes validation work, create a scoped Projects item with its acceptance and next action. After verifying a specific successor or confirming the action is complete, update or clear the existing nextAction through its supported current-revision owner transition when allowed; do not leave a superseded action current or create unrequested follow-on work.
10. Dimension maps: link one top-level map on the offering by the recipe in the product card.
11. Run to done (the loop for a goal owner; only f ends it). a) Work the goal's ranked items (step 7) through Engineering and QA. b) Raise every owner decision the rest of the roadmap needs in this run, one ask per decision, each with options, your recommendation, unlocks and `blocks` naming its own item (run sequence step 5), and build what does not depend on it. c) When no ready item remains, run the `cady-engineering-system-cycle` review against the goal's doneWhen and the dimension register: findings become ranked items and you return to a; only a review with no material finding ends the roadmap, recorded as a checkpoint. d) Release per policy: read policy:release and grant.release:<company> (`cady-company-decision-check` step 2). Under a covering grant, promote through the company's release route yourself; where the policy names who deploys, prepare the exact release (SHA, checks, rollback) and raise one approval ask to that person; with no policy, raise one ask recommending one. Never widen a grant. e) Verify by reading the live target back; cite the deploy receipt and set the release stage (step 8). f) Close the goal: read the target's source (its definition or sourceRef, for example a usage report) and record a reading from it (measure {value, at, sourceRef}); never record a count you did not read. If the release is live, doneWhen holds and the goal's target count is met: the goal call stop {reason: met, evidenceRefs: [review checkpoint, release receipt]}; confirm no OPEN or BLOCKED own items or unresolved effects remain; raise one ask 'Goal <name> is done and live. What next?' with options, and end the run reporting the goal done. The agent is then idle. If the release is live and doneWhen holds but the target count is not yet met: keep the goal open, report the release done, and make driving the target (users, sends, the unit the target counts) the next ranked item; do not stop the goal as met.

## Acceptance

- [ ] with no offering, the offering, then an assumed ICP and problem hypothesis, then one goal are created in that order and a test is planned
- [ ] each decision names rationale, authority and the items it supersedes
- [ ] observations are files linked from work, never a new store
- [ ] each release has an explicit go or no-go on its own work item with evidence
- [ ] requested validation work is recorded, and superseded next actions are updated only through a supported owner transition

## Owner checks

- current direction and decisions read before judging
- hypothesis recorded as a Projects decision item, not in direction
- evidence held as Files and cited by ref
- go/no-go recorded on the release work item
- offering exists before product-area calls; later structure waits for a decision that needs it

## Result

### Artifact refs

- company:work:<workId>
- file:<fileId>
- **Transition:** the claim holder reports the decision, hypothesis or release verdict and its evidence

## References
- Read [Release plan](../../references/release-plan.md) when you plan a release or run its go/no-go.
