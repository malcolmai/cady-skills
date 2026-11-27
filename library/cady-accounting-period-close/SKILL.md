---
name: "cady-accounting-period-close"
description: "Month-end and period close. Use when: Close the books for a month, quarter or year: reconcile bank, payouts and revenue, clear Suspense and lock. Not for: Preparing a tax return (use `cady-finance-tax-cycle`), budgets or runway, or audit sign-off."
license: "MPL-2.0"
compatibility: "Requires Cady (app.cadyworks.com/mcp)"
metadata:
  cady-id: "skill.accounting.period_close"
  version: "75ca124efdb9d3f808d1"
  library: "7bf126ff6bc82cee"
  function: "accounting"
---
# Month-end and period close

**Point:** Close each period with every account tied to its source and exceptions listed, so reported numbers can be trusted.

**Company context:** `cady_start {"task": "<what you are about to do, in one sentence>"}`

**Bets** (where this differs from the default):
- Reconcile every cash account to the statement closing balance. Instead of: Accept the bank feed or the ledger's own balance as reconciled once transactions are categorised.
- Recognise revenue when delivered: upfront annual payments go to deferred revenue, and signed but undelivered work is not revenue. Instead of: Book revenue when invoiced or paid.
- Explain every line that moves more than 10% and more than materiality; treat an unexplained move as an exception, and always investigate cash, tax and payroll items whatever their size. Instead of: Close once balances reconcile, and skip anything under materiality.
- Hand the owner one row per exception with account, amount, source, issue and the proposed debit and credit. Instead of: Send a list of issues to look at.
- Post the source-backed corrections yourself and lock only after the reviewer signs off. Instead of: Hand every correction to a bookkeeper to post, or lock when the work looks done.

Close the books for a month, quarter or year: reconcile bank, payouts and revenue, clear Suspense and lock.

**Not for:** Preparing a tax return (use `cady-finance-tax-cycle`), budgets or runway, or audit sign-off.

**Unit of work:** one entity and accounting period. **Kind:** execution. **Parallel:** yes. 

## Always

- Reconcile to the statement, not the bank feed; missing access is unknown, never a zero balance.
- Revenue follows delivery: prepaid annual cash is deferred, processor payouts are grossed up for fees.

## Inputs

### Evidence refs

- accounting_read figures, journals and accounts for the period
- bank statement files in Drive, card, payment processor, payroll, invoice and bill sources

### Work fields

- entity, period and accounting basis (cash or accrual)
- preparer and reviewer
- materiality amount and close deadline

## Procedure

1. Scope. Name the entity, period, basis and who prepares, reviews and locks. Agree a materiality amount with the reviewer (default: about 1% of monthly expenses); always investigate anything unexplained in cash, tax or payroll accounts regardless of size.
2. Cash first. For each cash-role account compare the book balance (accounting_read mode figures, balance sheet at period end) with the statement closing balance in Drive, not the bank feed. Post each statement line missing from the books with accounting_set action post_journal (source statement, sourceRef <fileId>:<line>, file as evidence; a Stripe payout is source stripe with its payout id, so a repeat posts nothing). Never post a balancing plug: list an unexplained difference as an exception or put it in Suspense. Investigate reconciling items older than 30 days. Clear Suspense to zero (reverse_journal, then a replacement post_journal) or list each item.
3. Revenue and receivables. Every delivered or billable item is invoiced; the receivables aging ties to the ledger balance; review anything over 90 days for credit notes or a doubtful debt provision. Recognise revenue when delivered, not when billed or paid: an annual subscription paid upfront goes to deferred revenue and releases monthly; signed but undelivered work is not revenue.
4. Payables, accruals and prepayments. Bills received are entered and the payables aging ties. Accrue services received but not billed (contractors, legal, hosting usage, commissions) and reverse last period's accruals. Annual software, insurance and deposits sit in prepayments and amortise.
5. Payroll. The payroll register ties to wage expense and to each liability (net pay, employer taxes, pension and benefits); liabilities clear when remitted. Accrue unpaid bonuses and, where local practice requires, holiday pay.
6. Balance sheet. Fixed assets over the capitalisation threshold are capitalised and depreciated; disposals removed. Sales tax or VAT accounts tie to the returns filed or due. SAFEs, notes and loans (including founder loans and interest) are recorded as the accountant's policy says, never as revenue. With more than one entity: intercompany balances agree on both sides in one currency, are settled or documented, and are eliminated on consolidation; intercompany charges go to the adviser for transfer pricing. Revalue foreign-currency balances at the period-end rate. Quarter and year-end: income tax provision with `cady-finance-tax-cycle`, equity roll-forward to the cap table, and a fixed asset count.
7. Flux review. Compare the P&L and balance sheet with last period and the budget; explain every line that moves more than 10% and more than the materiality amount.
8. Exceptions. Record one row per item: account; amount and currency; source ref; issue (unmatched, missing document, cut-off, misclassified, unexplained flux); proposed entry (debit and credit accounts); owner; due date; status. Post the ones a source supports; put the rest in Projects work for the owner with due.
9. Review and sign-off. Where staffed, the reviewer is not the preparer. The reviewer confirms every reconciliation ties, every exception has a disposition, flux is explained and the balance sheet accounts are reconciled, then signs off; only after sign-off run accounting_set action lock_period {lockedThrough, note: reviewer and sign-off date}. Report closed only after accounting_read mode accounts shows that lock and note; otherwise report prepared, pending or blocked with the open exceptions.

## Acceptance

- [ ] every cash account is reconciled to its statement or listed as an exception
- [ ] receivables, payables, accruals, prepayments, payroll and deferred revenue tie to their schedules
- [ ] the period is reported closed only with lock readback and sign-off

## Owner checks

- the period's sign-off and lock owner
- book balances tie to statements

## Result

### Artifact refs

- company:work:<workId>
- period lock readback
- **Transition:** close checklist and exception handoff, or verified closed period
