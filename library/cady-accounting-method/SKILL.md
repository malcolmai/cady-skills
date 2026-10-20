---
name: "cady-accounting-method"
description: "Prepare a close from the chosen ledger. Use when: reconciling a period or handing exceptions to the bookkeeper. Not for: finance planning (use `cady-finance-method`) or closing the ledger (use `cady-accounting-period-close`)."
license: "MPL-2.0"
compatibility: "Requires Cady (app.cadyworks.com/mcp)"
metadata:
  cady-id: "company.method.accounting"
  version: "fdf51150151359d5d08e336cfd08f218337288c78aef094a82a60fbfe37ad34d"
  function: "accounting"
---
# Accounting

## Parent function
finance

## Selected judgment
- Use the chosen ledger and reconciliations; identify dated exceptions. Cash observations and a Finance preview do not close a ledger period.
- Hand a source-linked exception list to the authorized bookkeeper or provider owner. Only that owner's posted correction and period status verifies the close. For a consequential interpretation: never adopt a service, tool or adviser because other companies use one. Map the workflow and find the work points with the most impact. Material and non-standard (our case departs from the standard process): bring in a specialist. A standard process and a standard case: do it AI-driven from official guidance and standard forms. Immaterial: the simplest thing that works.

## Domain method
- **Job:** Prepare a qualified period close from the chosen ledger and exact sources; the selected provider or bookkeeper owns posting, lock and close receipt. Use `cady-accounting-period-close`.


Shared by every role card: `../../references/role-card-common.md`.
**Company context:** `get_cady_context({"area": "finance/plan", "task": "<what you are about to do, in one sentence>", "knownMethods": {"company.method.accounting": "fdf51150151359d5d08e336cfd08f218337288c78aef094a82a60fbfe37ad34d"}})`
