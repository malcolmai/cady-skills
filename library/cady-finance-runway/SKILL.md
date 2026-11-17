---
name: "cady-finance-runway"
description: "Burn and runway. Use when: Work out burn, runway months and default alive or dead from actual cash, then decide when to cut and what first. Not for: Drafting a budget or allocation (use `cady-finance-budget-review`), deciding a raise (use `cady-fundraise-raise-plan`), approving spend or moving money."
license: "MPL-2.0"
compatibility: "Requires Cady (app.cadyworks.com/mcp)"
metadata:
  cady-id: "skill.finance.runway"
  version: "9b37e8457f3040b56b88"
  library: "8f1b82867a8ae070"
  function: "finance"
---
# Burn and runway

**Point:** Show when cash runs out and whether growth gets there first, so cuts or a raise start in time.

**Company context:** `cady_start {"task": "<what you are about to do, in one sentence>"}`

**Bets** (where this differs from the default):
- Derive cash, burn and runway from the ledger's cash accounts at read time. Instead of: Type cash and burn into the plan and read them back.
- Measure burn from bank cash out and net it of cash collected, excluding unfunded SAFEs, undrawn credit and tax collected but owed. Instead of: Compute burn from the P&L as expenses minus booked revenue, and count signed or available money as cash.
- Report runway to a floor of about three months of gross burn, plus the date the raise must start (floor minus 9 to 12 months). Instead of: Report months to zero as cash divided by burn.
- When burn is changing, build a month-by-month cash table for 18 to 24 months with hires, annual bills, payroll runs and tax payments in the months they are paid. Instead of: Divide cash by an average monthly burn.
- Answer default alive or dead: hold expenses, grow collections at the trailing rate, state the growth rate needed and the concentration and recurrence behind it. Instead of: Report runway months alone, or grow revenue at the plan's assumed rate.
- Cut once, deep enough to reach default alive or 18 months: tools, agencies and unmeasured spend first, hires and founder pay next, headcount last, protecting what brings in cash. Instead of: Make a series of small cuts as runway shrinks.

Work out burn, runway months and default alive or dead from actual cash, then decide when to cut and what first.

**Not for:** Drafting a budget or allocation (use `cady-finance-budget-review`), deciding a raise (use `cady-fundraise-raise-plan`), approving spend or moving money.

**Unit of work:** one company cash position at one as-of date. **Kind:** strategy. **Parallel:** no. 

## Always

- Unpaid receivables, unfunded commitments and collected sales tax are not cash.
- Burn comes from cash-account movements; annual prepayments, payroll and tax land in the month they are paid.

## Inputs

### Evidence refs

- accounting_read figures; bank statement files in Drive, last 3 to 6 months
- payroll register, signed contracts, committed hires and known annual or quarterly bills

### Work fields

- as-of date and reporting currency
- decision the runway figure informs

## Procedure

1. Objective. Answer one question for the person who decides spend and hiring: how long the cash lasts, whether the company is default alive, and if not when to cut and what first. If cash cannot be tied to statements, say so and give a labelled estimate.
2. Cash. accounting_read mode figures with asOn gives cash per currency from the cash-role accounts, converted at a stated rate; noCashAccount or cashPartial means cash is unknown, not zero. Cash is money in the bank, not: unpaid receivables, undrawn credit or venture debt (show as a separate line), signed but unfunded SAFEs or term sheets, restricted deposits, or sales tax and VAT collected but owed.
3. Burn from cash, not the P&L. Net burn is the figures burn: operating cash out less cash collected, trailing 3-month average, equity and loan flows left out; burnPartial true means the newest days read do not reach back three months, so burn and runway are withheld: sum the cash-account journals for those months; partialWindow true means the books start inside the window and the average reads low. Gross burn is all cash out (fully loaded payroll, contractors and every other operating cost), summed from journals on cash accounts. Remove one-offs (raise legal fees, a deposit); spread annual bills over 12 months for the trend only.
4. Forward view. When burn is changing, build a month-by-month cash table for 18 to 24 months instead of dividing once. Put each committed hire at its start month and loaded cost, each annual or quarterly bill in the month it is actually paid, payroll on its real dates (a month with three pay runs, bonuses, a 13th month), and tax payments on their due dates (VAT or sales tax remittance, payroll tax, corporate estimates). Collections follow actual payment terms and the receivables aging, not invoice dates.
5. Runway. Report two dates: cash at zero, and cash below a floor (default: 3 months of gross burn, enough to close a raise or wind down in order with payroll, notice and final taxes paid). Runway in months is to the floor unless the person asks for zero. A month with positive net cash flow does not end burn; keep the table running.
6. Scenarios, each with the same as-of cash. Base: committed spend and hires, collections at the trailing growth rate. Cut: the specific cuts in step 8 applied from next month, with notice and severance costs. Raise delay: the planned raise closes 6 months late, or not at all. For each, give the zero date, the floor date and the raise-start date (floor date minus 9 to 12 months).
7. Default alive or dead. Hold expenses at the current plan and grow collections at the trailing 3-month month-on-month rate: if monthly collections reach monthly expenses before cash hits the floor, the company is default alive. State the growth rate that would be needed and how sensitive the answer is; Read collections for quality: name customer concentration (the share from the largest one to three customers) and how much is recurring, contracted or one-off; a default-alive result resting on one customer or one-off revenue says so. For recurring revenue, also show the burn multiple (net burn divided by net new ARR over the same period; under 1 is efficient, above 2 needs a reason).
8. When to cut and what first. Cut when default dead with under 12 months to the floor and no credible raise path (term sheets in hand, not first meetings), or at once under 9 months. Cut once, deep enough to reach default alive or 18 months; repeated small cuts cost more trust than one clear one. Order: unused or duplicate software, agencies and contractors, unmeasured marketing, travel and events, office; then open and planned hires; then pay (founders first); headcount last. Protect what produces collections and the next milestone. Also pull cash forward: collect overdue receivables, offer annual prepay, renegotiate vendor terms. Route any people change to `cady-company-operations-people-lifecycle` for local employment rules.
9. Report the as-of date, sources, cash, gross and net burn, both runway dates, the three scenarios, the alive or dead result and the next review trigger (default monthly, weekly under 6 months). Nothing is written back: figures derive from the ledger. A cut list is a recommendation; any contract, payment or people effect stays with its owner.

## Acceptance

- [ ] cash, gross burn, net burn and both runway dates carry as-of date and source
- [ ] three scenarios with stated assumptions and a raise-start date
- [ ] default alive or dead with the growth rate it depends on
- [ ] any cut list is ordered, costed and marked as a recommendation

## Owner checks

- cash ties to bank statements at the as-of date
- net burn ties to bank outflows less collections
- figures read at the as-of date

## Result

### Artifact refs

- company:work:<workId>
- **Transition:** return the runway view and recommendation; spending and people changes remain separate
