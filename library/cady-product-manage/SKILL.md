---
name: "cady-product-manage"
description: "Product management and discovery. Use when: Decide what to build, for whom and why; run discovery and hypotheses; plan each release and run its go/no-go. Not for: Engineering execution (use `cady-engineering-method`), QA runs (use `cady-qa-method`) or GTM campaigns (use `cady-gtm-method`)."
license: "MPL-2.0"
compatibility: "Requires Cady (app.cadyworks.com/mcp)"
metadata:
  cady-id: "skill.product.manage"
  version: "2005a053f4560784a28eaa47a2d6daa13025a330828d4b27f5cbfa22e38a9a16"
  library: "b1e7050435d28aef"
  function: "product"
---
# Product management and discovery

**Company context:** `get_cady_context({"area": "product/<productId>/scope", "task": "<what you are about to do, in one sentence>", "knownMethods": {"skill.product.manage": "2005a053f4560784a28eaa47a2d6daa13025a330828d4b27f5cbfa22e38a9a16"}})`

Decide what to build, for whom and why; run discovery and hypotheses; plan each release and run its go/no-go.

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

1. Read get_company_direction, then get_cady_context for recent decisions and get_company_work with decisions {state: "current"} for every current decision and hypothesis. Read the Files and CRM evidence they cite before judging; unknown stays unknown.
2. Discovery is part of the job. If no customer has given direction (no accepted ICP in direction, no current hypothesis and no customer evidence in CRM), do not wait and do not build on a guess. State one assumed ICP (who, circumstance, observable signals) and one problem hypothesis (the job, current alternative, what they pay in money, time or risk), with what would prove it wrong. Record it with submit_company_work_checkpoint: statement is the hypothesis, status OPEN, decision {kind: "hypothesis", subject: "hypothesis:<slug>", rationale, authority: "agent" and no decidedBy}, evidenceRefs to the sources used. Tell the person it is an assumption they can replace.
3. Get evidence for the hypothesis with `cady-company-decision-questions` (route) and `cady-company-experiment` (pre-registered tests), as Projects work bound to the hypothesis (evidenceRefs company:work:<hypothesisId>); run interviews with `cady-product-customer-interview`. If the evidence needs calls and no pipeline is getting the ICP onto calls, hand it to the Executive as the binding constraint rather than adding product work.
4. Keep evidence tied to the offering. Keep interview notes, observations and raw source material in Files through files.upload with mode "begin" and files.upload with mode "complete", citing each as file:<fileId> from the hypothesis or work item. Put curated Competition or Technology analysis in the Research library using the matching specialist card, which includes shared research craft; preserve and link existing direction, decisions and work context rather than replacing it. Never paste evidence into direction or a work statement, or create another record to hold learning.
5. When evidence settles a hypothesis or product choice, use subject hypothesis.outcome:<slug> or product.choice:<slug> respectively. Record it with submit_company_work_checkpoint: statement is the decision, status COMPLETE, decision {kind: "decision", subject, rationale, authority, decidedBy, supersedes: [the hypothesis or earlier decision workIds]}. For your own choice use authority "agent" and omit decidedBy, source and quote; for a person use their exact words as source "chat" and quote, or a verified source "grant" with grantId. Raise a choice reserved to the founder as a BLOCKED decision item addressed to the owner, with the question as nextAction; it reaches them as asksForYou. Propose an accepted ICP or bet for direction only through update_company_direction.
6. Scope from the ranked gap list against the bar; subtract before adding. Rank with the lightest frame that separates the options: for a few items, cost of delay (what each week of waiting loses in revenue, risk, learning or a deadline) divided by effort, highest first; RICE (reach x impact x confidence / effort) only for a longer list with comparable reach data. Label each estimate measured, evidence-based or guess, and never let precise-looking scores hide guesses; a fixed deadline or a blocker on a critical path overrides the score. Record the ranking rationale on the work item. Bind product work to the offering with the company product owner and productId. Plan each release as a work item with release {stage, buildBy, qaDays, thresholds}, per the release plan (`../../references/release-plan.md`).
7. Check release thresholds against exact QA, engineering and customer evidence on the release work item. Go: record the go decision there under subject release.go:<workId>, with evidence refs and nextAction 'ready to release'; keep release stage 'qa'. No-go: status BLOCKED with the unmet threshold and next action, through transition_company_work(action: 'checkpoint', status: 'BLOCKED', nextAction) when you hold the claim. The release owner sets stage 'released' only after verifying the deployed artifact and target, citing the deploy receipt.
8. When the requested analysis includes validation work, create a scoped Projects item with its acceptance and next action. After verifying a specific successor or confirming the action is complete, update or clear the existing nextAction through its supported current-revision owner transition when allowed; do not leave a superseded action current or create unrequested follow-on work.

## Acceptance

- [ ] with no customer direction, an assumed ICP and problem hypothesis is recorded and a test is planned
- [ ] each decision names rationale, authority and the items it supersedes
- [ ] observations are files linked from work, never a new store
- [ ] each release has an explicit go or no-go on its own work item with evidence
- [ ] requested validation work is recorded, and superseded next actions are updated only through a supported owner transition

## Owner checks

- current direction and decisions read before judging
- hypothesis recorded as a Projects decision item, not in direction
- evidence held as Files and cited by ref
- go/no-go recorded on the release work item

## Result

### Artifact refs

- company:work:<workId>
- file:<fileId>
- **Transition:** the claim holder reports the decision, hypothesis or release verdict and its evidence

## References
- [Release plan](../../references/release-plan.md)
