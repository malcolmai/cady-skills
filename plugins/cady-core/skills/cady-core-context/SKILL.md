---
name: "cady-core-context"
description: "Decision layers (owner, function head, task), early-stage defaults and how to read company references. Use when: deciding who decides, or what to read, before company work. Not for: running a task; load the task's skill."
license: "MPL-2.0"
compatibility: "Requires Cady (app.cadyworks.com/mcp)"
metadata:
  cady-id: "company.context"
  version: "8f3d340f588ec2f15096"
  library: "dbd01ca4ec2c8070"
  function: "core"
---
# Company context

**Company context:** `get_cady_context({"area": "ops/records", "task": "<what you are about to do, in one sentence>", "knownMethods": {"company.context": "8f3d340f588ec2f15096@dbd01ca4ec2c8070"}})`

Decision layers (owner, function head, task), early-stage defaults and how to read company references. Use when: deciding who decides, or what to read, before company work. Not for: running a task; load the task's skill.

## Company practice

### Injected method

- Use recorded direction as the working baseline, including its bets: beliefs the company acts on before evidence settles them. Let a held bet cut options without re-arguing it; surface contrary evidence against the bet it challenges instead of silently working around it. Record a bet only when the user states or reaffirms it, tagged with the function that will test it; an inferred bet stays a hypothesis attributed to its source. Preserve user choices.
- Verify readiness and authority before consequential effects, and the working result before expansion. An authorized recurring review can be configured before the first execution. Load the cady-company-review skill for operational review, then only relevant function methods.
- Across sessions, recover the original authorized outcome through get_company_work; empty local claims do not establish that no work exists.
- A chat observation or CRM note is not an order update, refund, shipment or completed resolution.
- File properly: when you store a file in Cady Files, give it a clear name, a location, its purpose and the related party or work item. Cady never classifies or labels files for you, so supply these yourself. The host edits files: upload a clearly named new version, not a duplicate. files.read_text returns an excerpt of PDF, DOCX, PPTX and text with page or slide anchors (pass chunk for full text, chunk by chunk; nextDownload names the files.get_download call whose 2-minute URL you fetch with plain GET for the raw bytes); no_extractable_text means a scan, and unavailable means unreadable, never an empty file.
- One home per fact: search before creating any record, file, doc or tool and extend the owner; local files are working material, never records.

### Method detail

- For delegated business setup or improvement, compare the intended outcome with evidence of actual operation and choose the consequential gap within priorities, authority and capacity. Preserve healthy systems. Before product-market fit that gap is usually evidence of demand: by default favour talking to target users and the smallest test over building more, hiring, entity work beyond founder IP, or raising, and say so when the founder's plan diverges. Before shared or commissioned work builds up, make sure what is made belongs to the company: with more than one founder, an IP assignment and a vesting founder agreement; with a contractor or agency, an IP assignment in the engagement. Raise them as decision tasks and use the standard form unless the case is material and non-standard; when founder shares are issued or options granted, run `cady-company-operations-contract-checks` (equity) the same day. Complete a coherent function or customer workflow through its existing owners, not only an inventory or configuration; advice or connection alone does not grant this remit.
- Judge effect, not activity. Many assets with no customer response means production progress and unknown commercial effect. An agreed wait is not neglect; a missed commitment without recovery needs attention. Inaccessible finance data is a visibility gap, not proof of failure, and no planned round is no reason to mark fundraising behind.
- A completed checkpoint need not complete the broader remit.
- For a customer order or request, establish the exact order, status, promise and exception in the chosen commerce, support or fulfilment system before answering or changing it. Do not activate a tool or assume an order capability merely because it appears in a catalog.
- Never adopt a service, tool or adviser because other companies use one. Map the workflow and find the work points with the most impact. Material and non-standard (the case departs from the standard process): bring in a specialist. A standard process and a standard case: do it AI-driven from official guidance and standard forms. Immaterial: the simplest thing that works.
- **Objective:** Keep company direction clear and build reliable execution without overloading the founder.

## Orientation

- Before any choice or effect, follow `cady-company-decision-check`: check what is decided and still holds; for an effect, self-approve or use a grant before asking (payments, signatures and filings stay a person's); for a choice, find its layer: L1 goals, offer, stage, bets, hires and grants (an agent decides only in notify mode above a high bar, owner told; otherwise asks), L2 a function's approach (its head, one fresh look), L3 a task (any agent). Asking the owner an L2 or L3 question is a stall.
