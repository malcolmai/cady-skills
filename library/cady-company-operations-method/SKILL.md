---
name: "cady-company-operations-method"
description: "Handle the company's practical operating requirements, records and obligations. Use when: setting up or maintaining compliance, people processes or operating requirements. Not for: finance planning (use `cady-finance-method`) or product and sales decisions."
license: "MPL-2.0"
compatibility: "Requires Cady (app.cadyworks.com/mcp)"
metadata:
  cady-id: "company.method.company_operations"
  version: "c78cf62d686b89550c6d44ddd1096e908eba5dd88bc6fd776a015ff99e5b5462"
  function: "company_operations"
---
# Company Operations

## Parent function
company

## Selected judgment
- Start with the service or obligation outcome. Compare demand, capacity, commitments, vendor handoffs and exception recovery; the chosen external system owns operational truth. Verify completion there, including obligations after an initial handoff.
- For an actual vendor or inventory decision, start from fresh discovery and the chosen system's current records. A recommendation, source-system draft and submitted order or accepted vendor commitment are distinct states; reconcile the exact returned source state.
- Company operations guidance is general information, not legal advice; identify the applicable jurisdiction. Never adopt a service, tool or adviser because other companies use one. Map the workflow and find the work points with the most impact. Material and non-standard (our case departs from the standard process): bring in a specialist. A standard process and a standard case: do it AI-driven from official guidance and standard forms. Immaterial: the simplest thing that works.

## Domain method

### Method detail

- To change the company profile (name, website, description, logo) read get_cady_context for company.profileRevision, save a logo (PNG or JPEG, small) through files.upload with mode "image" and base64 bytes you fetched yourself, or mode "begin" and "complete" for a larger file, then call company.profile.update with expectedRevision; omit idempotencyKey (server-filled). A refusal carries reason, message and recovery and nothing was saved: for a field refusal such as DESCRIPTION_TOO_LONG fix the field and omit the key; for REVISION_CONFLICT re-read, reapply and retry; for ACCESS_DENIED_COMPANY_ADMIN hand the change to an owner or admin or have them reconnect the agent.

### Operations topics

- **Boundary:** Methods guide the host; external systems own operational records. For entity or filing work, check the applicable legal entity and actual obligation; use crm.manage_company_records(action='set_entity'), action='list' or action='get' for entity facts where authorized. Finance tax-cycle work uses Projects dueDate and dependsOn for preparation before separately sourced filing and payment deadlines; Operations oversees operational risk and follow-through, while Finance retains financial controls. Retain evidence references, not file bodies. When a result, run close or goal call changes what the company already records (a goal's acceptance, a bet, a system map, a plan, an agent's setup), update that record in place and cite the evidence; open no parallel record and log no routine chat.
- **Content hash:** 139eb0e37434eda0b51cb995cc0febed66e85da9ca526fce9089587c6a3801bf
- **Owner:** company_operations

#### Pending

| Missing owner | Need |
|---|---|
| Canonical spending reservation and executor qualification | Operations can prepare a vendor decision, but Finance advice and agent prose cannot approve payment or a contract; use an applicable checked current route or hold the effect. |

#### Read

#### Arguments

- **Function:** company_operations
- **Mode:** practice
- **Tool:** get_execution_guide

#### Routing

- **Finance:** Use the current Finance plan and finance.vendor_spend_review for material budget and vendor value judgment; Operations owns supplier delivery and operational-risk oversight. Keep embedded financial controls with Finance and verify any exact financial effect with its owner.
- **Gtm:** Use Sales for customer commitments and demand evidence, and Customer Success for customer outcomes and recovery. Keep accepted promises separate from unconfirmed demand.
- **Operations:** Procure, manage vendor delivery, replenish, allocate, fulfil and recover delivery of the accepted offering. The host agent reasons and acts through the company's chosen systems within current authority.
- **Product:** Use Product to define or change the offering, specifications, customer promise or delivery experience. Building a new planning application is Product/Engineering work; using or improving an ordering model for current operations stays here.


Shared by every role card: `../../references/role-card-common.md`.
**Company context:** `get_cady_context({"area": "ops/records", "task": "<what you are about to do, in one sentence>", "knownMethods": {"company.method.company_operations": "c78cf62d686b89550c6d44ddd1096e908eba5dd88bc6fd776a015ff99e5b5462"}})`
