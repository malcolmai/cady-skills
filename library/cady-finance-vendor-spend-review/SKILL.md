---
name: "cady-finance-vendor-spend-review"
description: "Vendor spend review: new purchase or renewal. Use when: Decide whether to buy, trial, renew or cancel a paid tool or vendor: cost, actual use, alternatives and commitment. Not for: Bookkeeping, a finance ledger, payment, provider billing changes, supplier order execution or technical qualification; use `cady-finance-budget-review` for the current budget plan."
license: "MPL-2.0"
compatibility: "Requires Cady (app.cadyworks.com/mcp)"
metadata:
  cady-id: "skill.finance.vendor_spend_review"
  version: "6d5ca131937a778d78437c8d697de430911fbb1e8cce77b87bf7afdbb56c61a2"
  library: "6950bdef5dfadc81"
  function: "finance"
---
# Vendor spend review: new purchase or renewal

**Company context:** `get_cady_context({"area": "finance/plan", "task": "<what you are about to do, in one sentence>", "knownMethods": {"skill.finance.vendor_spend_review": "6d5ca131937a778d78437c8d697de430911fbb1e8cce77b87bf7afdbb56c61a2"}})`

Decide whether to buy, trial, renew or cancel a paid tool or vendor: cost, actual use, alternatives and commitment.

**Not for:** Bookkeeping, a finance ledger, payment, provider billing changes, supplier order execution or technical qualification; use `cady-finance-budget-review` for the current budget plan.

**Unit of work:** one work item per vendor and plan or purchase decision. **Kind:** strategy. **Parallel:** yes. **Can release:** no. 

## Inputs

### Evidence refs

- crm:party:<vendorPartyId>
- dated contract, invoice, message or File refs
- current company need and Finance plan
- dated offers, terms, usage and existing-tool evidence

### Statement fields

- vendor and plan
- review horizon
- decision sought
- outcome sought
- decision date and useful life
- requesting owner and proposed vendor

## Procedure

1. Name the decision: a new purchase, or a renewal, trial end or cancellation. Follow the matching reference (`../../references/vendor-purchase.md` or `../../references/vendor-renewal.md`) for evidence, comparison and commitment. Route provider capability, security, access and credential fit to Integrations or the relevant owner. Reuse a current value review for unchanged need, vendor, terms and usage; a small covered request needs a scope/limit check, not another vendor study.
2. Keep cost views distinct: annualized run-rate, full-term commitment and period cash timing. Unknown amount is not zero; annual equivalent is not booked spend; a register line is evidence, not a reservation.
3. Continue authorized research and preparation. For any dependent paid effect without an applicable verified scoped user grant and permitted executor, checkpoint a BLOCKED Projects item with exact vendor, amount, currency, term, decision owner, terms and next action. A future delegated envelope needs owner-enforced limits, reservation, expiry and receipt; do not claim it exists now. Reuse unchanged valid exact authority without another ask. No cancellation is sent and no money is reserved from this skill.
4. Report the recommendation or register and dated next action with transition_company_work(action: 'report_result') after CRM and work readback. A sent notice is not vendor acknowledgement; an acknowledged future effective end is not ended service. Keep work open for dated outcome evidence.

## Acceptance

- [ ] one justified recommendation and a credible cheaper or no-buy alternative
- [ ] full commitment, annualized cost and cash timing are distinct
- [ ] unsupported spend is held with an exact handoff
- [ ] the vendor party and renewal are read back
- [ ] a linked commitment has fields, dates and unknowns
- [ ] notice work is dated and cancellation remains unsent

## Owner checks

- dated price and term sources
- current entitlement and applicable executor authority
- separate provider/access/security checks
- no payment or contract effect from advisory method
- WORK_NOT_FOUND
- METHOD_NOT_CURRENT
- CRM provider role and renewal receipt
- dated evidence and notice recheck
- exact user review before any cancellation effect

## Result

### Artifact refs

- company:work:<workId>
- crm:party:<vendorPartyId>
- **Transition:** decision recommendation or blocked exact authority handoff

## References
- [New purchase review](../../references/vendor-purchase.md)
- [Renewal, trial or cancellation](../../references/vendor-renewal.md)
