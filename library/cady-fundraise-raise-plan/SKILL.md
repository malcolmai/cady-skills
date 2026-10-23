---
name: "cady-fundraise-raise-plan"
description: "Raise plan: amount, instrument, dilution and process. Use when: Decide whether, when and how much to raise (SAFE, note or priced round), model dilution and run the round. Not for: Building the investor list, drafting the deck, memo or update, writing to investors, or legal and tax advice."
license: "MPL-2.0"
compatibility: "Requires Cady (app.cadyworks.com/mcp)"
metadata:
  cady-id: "skill.fundraise.raise_plan"
  version: "a4b9f50c7149fab57c3badf7a08fc868204ea56d9a0c9847ec740a8b94f2a0bc"
  library: "0ff16c1777f932cf"
  function: "fundraise"
---
# Raise plan: amount, instrument, dilution and process

**Company context:** `get_cady_context({"area": "gtm/strategy", "task": "<what you are about to do, in one sentence>", "knownMethods": {"skill.fundraise.raise_plan": "a4b9f50c7149fab57c3badf7a08fc868204ea56d9a0c9847ec740a8b94f2a0bc"}})`

Decide whether, when and how much to raise (SAFE, note or priced round), model dilution and run the round.

**Not for:** Building the investor list, drafting the deck, memo or update, writing to investors, or legal and tax advice.

**Unit of work:** one financing round. **Kind:** strategy. **Parallel:** no. **Can release:** no. 

## Always

- Not legal or tax advice: route instrument choice, material terms and securities filings to counsel.
- Count the option pool and every SAFE and note before stating founder ownership.

## Inputs

### Evidence refs

- current runway view and finance plan
- cap table, existing SAFEs, notes and option pool
- milestone and traction sources

### Statement fields

- next milestone and what it proves
- jurisdiction of the issuing entity

## Procedure

1. If this runs as a Projects work item, claim it with transition_company_work(action: 'claim') (on CONFLICT stop and report the holder); an interactive question needs no claim. Read get_company_direction and the runway view from `cady-finance-runway`.
2. Whether and how much. Name the milestone that makes the next round or profitability possible (revenue level, retention, a shipped product) and the months to reach it. Default amount: planned net burn to that milestone plus 6 months of buffer, usually 18 to 24 months of runway. Compare cheaper routes: revenue and prepayments, grants and R&D credits, a smaller round, and venture debt only alongside equity or revenue. Not raising is a valid answer when the company is default alive.
3. When. Start with at least 9 to 12 months of runway to the floor: a process typically takes 3 to 6 months to cash (unverified). Start just after a milestone proof, not just before it, and avoid launching into local holiday periods.
4. Instrument. SAFE (post-money): fastest and cheapest, no board, no interest or maturity; a valuation cap and optional discount; the holder's share is fixed at purchase amount divided by the post-money cap, so every further SAFE dilutes founders, not earlier holders. Convertible note: debt with interest (often 4 to 8%) and a maturity date (often 18 to 24 months) that gives holders leverage if no round happens; interest converts too. Priced round: sets a price, issues preferred shares, usually adds a board seat and protective provisions, costs more legal time and fees, and is standard from Series A and common at seed with a lead. Local forms differ (in the UK an advance subscription agreement keeps SEIS and EIS eligibility, which a SAFE does not); confirm the instrument with counsel.
5. Dilution maths, written out for this round. Post-money = pre-money + new money; new investors own new money / post-money; price per share = pre-money / pre-money fully diluted shares, and the option pool investors require is counted in the pre-money (the option pool shuffle). Worked example: founders hold 8,000,000 shares, no pool; raise 2M at 8M pre-money (10M post), with a 10% post-money pool. Investors 20%, pool 10%, so founders 70%: fully diluted shares 11,428,571; pool 1,142,857; price 8M / 9,142,857 = 0.875; investors buy 2,285,714 shares. Founders' effective pre-money is 7M, not 8M. If a 500k post-money SAFE at a 5M cap (10%) also converts here at its cap price, and the 8M pre-money includes the converted SAFE shares, founders end at 90% x 70% = 63% and the SAFE at 7%. Model every outstanding SAFE and note before quoting founder ownership; have the cap table tool or counsel run the pro forma.
6. Terms to compare and route to counsel: valuation or cap, discount, most favoured nation, pool size, liquidation preference (1x non-participating is the market default), participation, anti-dilution (broad-based weighted average is standard; full ratchet is off-market), board seats, protective provisions, pro rata, founder vesting and information rights. Back-channel a lead with founders from its portfolio, including ones that struggled.
7. Process: time-boxed and lead-first. Set a start date and a close target before the first meeting (a common shape is 8 to 12 weeks from first meetings to a lead's term sheet; unverified), and take the ranked pool from `cady-fundraise-investor-list` (seed: often 50 to 100 names, unverified), leads first. Track each investor with crm.set_track and its roundId through target, intro, first meeting, partner meeting, diligence, term sheet, docs, closed or passed with the reason. Batch first meetings into 2 to 3 weeks so interest overlaps; follow up within a day with the next step and date; drop investors who stall rather than chase them. Get a lead, then fill the round, then set a close date. Signal check: after about 15 first meetings with no second meetings (unverified), change the story, amount or timing rather than adding volume. Exclusivity after a signed term sheet commonly runs 30 to 45 days (unverified). Record the round with crm.manage_company_records(action='set_round'). Messages to investors go through `cady-fundraise-investor-outreach`.
8. Close. Signed documents and money in the bank are separate states; report closed only when funds are received. Before recording shares, list recent issues with crm.manage_company_records(action='list') and verify each investment against its evidence document; record with crm.manage_company_records(action='record_share_issue') only after that receipt, correct only with crm.manage_company_records(action='void_share_issue'), and never count a SAFE as issued shares. A suspected duplicate is refused unless distinctReason explains a separate issuance. Post-close securities and registry filings go to `cady-company-operations-compliance-register`.
9. Report the recommended amount, instrument, dilution table, timeline, terms needing counsel and the next founder decision; for a work item, use report_company_work. No investor is contacted from this skill.

## Acceptance

- [ ] amount ties to a named milestone and runway
- [ ] instrument choice states its trade-off
- [ ] dilution table reconciles to the cap table
- [ ] material terms are marked for counsel

## Owner checks

- runway view and finance plan
- cap table including SAFEs, notes and pool
- share issue receipts from the CRM owner

## Result

### Artifact refs

- company:work:<workId>
- **Transition:** recommended raise plan or the next founder decision
