# Domain method

### Method detail

- To change the company profile (name, website, description, currency, logo) or choose the Cady workspaces it uses, call company_setup with any of those fields; no revision or key is needed. For a logo save a PNG or JPEG through files_set (small: mode save_image) and pass its fil-<n> as logo. modules is the full list of Cady workspaces the company uses (crm, files_knowledge, stories, accounting); an external tool is one line in the company workspace AGENTS.md. The reply names next, the first setup phase not done (basics, what already exists, strategy and loops); read all three with cady_read company:setup. A refusal carries reason, message and recovery: a field refusal such as DESCRIPTION_TOO_LONG, fix the field; ACCESS_DENIED names the admin-only fields, so hand those to an admin. After a partial reply repeat the same call.

### Operations topics

- **Boundary:** Methods guide the host; external systems own operational records. For entity or filing work, check the applicable legal entity and actual obligation; record entity facts as decision lines (decisions_set, subject ops:entity:<name>) with the incorporation documents as Files, and read one with cady_read decision:ops:entity:<name> where authorized. Finance tax-cycle work uses Projects due and dependsOn for preparation before separately sourced filing and payment deadlines; Operations oversees operational risk and follow-through, while Finance retains financial controls. Retain evidence references, not file bodies. When a result, run close or goal call changes what the company already records (a goal's acceptance, a bet, a system map, a plan, an agent's binding), update that record in place and cite the evidence; open no parallel record and log no routine chat.
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
