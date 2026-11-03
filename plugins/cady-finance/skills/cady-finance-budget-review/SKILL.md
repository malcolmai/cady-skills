---
name: "cady-finance-budget-review"
description: "Budget and cost review. Use when: Draft or update a budget or spend allocation, or review last month's spend against it. Not for: Burn, runway and when to cut, posting ledger entries, reserving money or authorizing payment; use `cady-accounting-method` for close work."
license: "MPL-2.0"
compatibility: "Requires Cady (app.cadyworks.com/mcp)"
metadata:
  cady-id: "skill.finance.budget_review"
  version: "217fc7b0bbcb01f66203"
  library: "f4537fc893b29278"
  function: "finance"
---
# Budget and cost review

**Point:** Allocate money to the few drivers that change a decision, from dated actuals, so spend follows what works.

**Company context:** `context_read({"area": "finance/plan", "task": "<what you are about to do, in one sentence>", "knownMethods": {"skill.finance.budget_review": "217fc7b0bbcb01f66203@f4537fc893b29278"}})`

**Bets** (where this differs from the default):
- Budget the few drivers that move cash (payroll, usage-based services, paid acquisition) at a depth set by stage and the decision at hand. Instead of: Build a full line-item budget by department and month.
- Rest the return on any allocation only on existing or secured revenue; forecasts stay scenarios, and a cost without one is the owner's call with no return claim. Instead of: Justify an allocation with a forecast ROI.
- Raise in the monthly review only what can change a decision: the largest movers, renewals inside their notice window, metered lines against ceiling, overdue receivables. Instead of: Walk every line of budget against actual each month.
- Report a source with no records as unknown coverage. Instead of: Treat a category with no transactions found as zero spend or available balance.

Draft or update a budget or spend allocation, or review last month's spend against it.

**Not for:** Burn, runway and when to cut, posting ledger entries, reserving money or authorizing payment; use `cady-accounting-method` for close work.

**Unit of work:** one decision horizon, or one monthly cost review, against the current Finance plan. **Kind:** strategy. **Parallel:** no. **Can release:** no. 

## Inputs

### Evidence refs

- current Finance plan and source file
- dated cash, ledger, receivable and obligation sources where available

### Work fields

- decision and horizon
- company scale and material drivers
- currency and source freshness

## Procedure

1. Read current company direction and the current finance plan owner read. Choose planning depth from the company stage, business model, cash pressure and actual obligations; a small company need not maintain a corporate FP&A process. Identify the decision the budget must support and the few drivers that change it.
2. Reconcile dated observed cash and actuals from the chosen sources with committed obligations, any independently evidenced reservations and forecast flows. Keep those four categories distinct; missing records mean unknown coverage, never zero spend or available balance. Identify currency, period, tax and timing differences before adding figures.
3. Draft a baseline with explicit driver assumptions and material upside/downside or timing sensitivity. Include collections, payments, inventory, payroll, tax or capital only when relevant. Take cash, burn and runway from `cady-finance-runway` rather than recomputing them; state what would change the decision.
4. Review at two levels. First why: does the work serve the purpose one level up? Ask why until you reach a recorded goal, direction or decision, and list each assumption with its evidence or mark it unsupported. A why that is missing goes back to the requester as a question. A why that evidence contradicts is a blocker even when the details are sound. A why that conflicts with an owner's recorded decision goes to that owner; you do not reverse it. Then review the details. An obviously purposeful small fix needs one line on why. The detail level is the figures, allocation and trigger below. Recommend a proportionate allocation, stop/review trigger and owner. Attach a plan file only if one exists. Keep exact evidence refs in the company's chosen records. If authorized, update through the authorized finance plan owner write and read back the resulting plan. Omitted file, source, objective, allocation and horizon fields carry forward from the expected active revision; send null to remove the file, source or horizon, or an empty objective or allocation list to clear it, and inspect retained details on readback. A plan allocation is decision context, not a reservation or executable spending grant. Rest the return on any spend only on existing or secured revenue, never on projected revenue; forecasts stay scenarios.
5. Monthly cost review, when that is the unit: compare last month's actuals with the plan and name the few largest movers and their cause; list renewals inside their notice window (`cady-finance-vendor-spend-review` decides each); for metered lines (cloud, AI APIs, ads) compare usage with the ceiling and name who owns the provider-side alert, since a ceiling is a review trigger, not a hold; and read the receivables aging, routing any chaser through the customer's existing reviewed outreach. Raise only what changes a decision.
6. Report the dated baseline, assumptions, unresolved sources, decision and next review trigger. Prepare independent follow-up in Projects; hold any dependent spend until an applicable current executor verifies exact scoped user authority or a future owner-enforced envelope.

## Acceptance

- [ ] a usable source-linked budget or plan update matches company scale
- [ ] actual, committed, reserved and forecast amounts remain distinct
- [ ] unknown coverage and next trigger are explicit
- [ ] a cost review names movers, renewals in their notice window, metered lines against ceiling and overdue receivables, or says which source was unavailable

## Owner checks

- current Finance plan and company direction
- source dates and category separation
- plan readback
- spend authority belongs to an applicable current owner

## Result

### Artifact refs

- company:plan:finance_plan
- company:work:<workId>
- **Transition:** return a recommendation or verified plan update; spending remains separate
