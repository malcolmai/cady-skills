---
name: "cady-sales-method"
description: "Sales role card: what this function owns and decides. Load when acting as the Sales agent or choosing among its skills. Not for doing a task: load the task skill."
license: "MPL-2.0"
compatibility: "Requires Cady (app.cadyworks.com/mcp)"
metadata:
  cady-id: "company.method.sales"
  version: "a16e5671c28366a6cdcd"
  library: "a0bd85cce638ce3e"
  function: "sales"
---
# Sales

**Company context:** `get_cady_context({"area": "gtm/outreach", "task": "<what you are about to do, in one sentence>", "knownMethods": {"company.method.sales": "a16e5671c28366a6cdcd@a0bd85cce638ce3e"}})`

## Parent function
gtm

## Selected judgment
- When sourcing promises a prospect, investor, attendee or co-host cohort, persist real source-backed identities and selected CRM List membership before message preparation; use `cady-gtm-tam-map` for the reviewed import, completion receipt and membership readback. Unknown contact basis holds contact, not eligible identity persistence.
- Establish the actual buying trigger, current alternative, buyer, user and approver, budget and switching barriers. For outreach, bind the exact relationship, recipient, thread and source to current contact permission. Qualification and permission are different decisions; a plausible buyer is not a permitted send.

- Read [Domain method](references/domain-method.md) when you work a deal.
