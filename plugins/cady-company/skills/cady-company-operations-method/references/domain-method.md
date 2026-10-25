# Domain method

### Method detail

- To change the company profile (name, website, description, logo) read get_cady_context for company.profileRevision, save a logo (PNG or JPEG, small) through files.upload with mode "image" and base64 bytes you fetched yourself, or mode "begin" and "complete" for a larger file, then call company.profile.update with expectedRevision; omit idempotencyKey (server-filled). A refusal carries reason, message and recovery and nothing was saved: for a field refusal such as DESCRIPTION_TOO_LONG fix the field and omit the key; for REVISION_CONFLICT re-read, reapply and retry; for ACCESS_DENIED_COMPANY_ADMIN hand the change to an owner or admin or have them reconnect the agent.

### Operations topics

- **Boundary:** Methods guide the host; external systems own operational records. For entity or filing work, check the applicable legal entity and actual obligation; use crm.manage_company_records(action='set_entity'), action='list' or action='get' for entity facts where authorized. Finance tax-cycle work uses Projects dueDate and dependsOn for preparation before separately sourced filing and payment deadlines; Operations oversees operational risk and follow-through, while Finance retains financial controls. Retain evidence references, not file bodies. When a result, run close or goal call changes what the company already records (a goal's acceptance, a bet, a system map, a plan, an agent's binding), update that record in place and cite the evidence; open no parallel record and log no routine chat.
- **Content hash:** 139eb0e37434eda0b51cb995cc0febed66e85da9ca526fce9089587c6a3801bf
- **Owner:** company_operations

#### Pending

| Missing owner | Need |
|---|---|
| Canonical spending reservation and executor qualification | Operations can prepare a vendor decision, but Finance advice and agent prose cannot approve payment or a contract; use an applicable checked current route or hold the effect. |

- **Read:** the installed `cady-core-context` skill for company practice

#### Routing

- **Finance:** Use the current Finance plan and `cady-finance-vendor-spend-review` for material budget and vendor value judgment; Operations owns supplier delivery and operational-risk oversight. Keep embedded financial controls with Finance and verify any exact financial effect with its owner.
- **Gtm:** Use Sales for customer commitments and demand evidence, and Customer Success for customer outcomes and recovery. Keep accepted promises separate from unconfirmed demand.
- **Operations:** Procure, manage vendor delivery, replenish, allocate, fulfil and recover delivery of the accepted offering. The host agent reasons and acts through the company's chosen systems within current authority.
- **Product:** Use Product to define or change the offering, specifications, customer promise or delivery experience. Building a new planning application is Product/Engineering work; using or improving an ordering model for current operations stays here.
