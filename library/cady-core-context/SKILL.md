---
name: "cady-core-context"
description: "Decision layers (owner, function head, task), early-stage defaults and how to read company references. Use when: deciding who decides, or what to read, before company work. Not for: running a task; load the task's skill."
license: "MPL-2.0"
compatibility: "Requires Cady (app.cadyworks.com/mcp)"
metadata:
  cady-id: "company.context"
  version: "fb0577e90d84f26cda342ecf3761d3e11460a9b1eadcbaeec0b86e123a472bc9"
  library: "a5c3acb6d834715e"
  function: "core"
---
# Company context

**Company context:** `get_cady_context({"area": "ops/records", "task": "<what you are about to do, in one sentence>", "knownMethods": {"company.context": "fb0577e90d84f26cda342ecf3761d3e11460a9b1eadcbaeec0b86e123a472bc9"}})`

Decision layers (owner, function head, task), early-stage defaults and how to read company references. Use when: deciding who decides, or what to read, before company work. Not for: running a task; load the task's skill.

## Company practice

### Injected method

- Use recorded direction as the working baseline, including its bets: beliefs the company acts on before evidence settles them. Let a held bet cut options without re-arguing it; surface contrary evidence against the bet it challenges instead of silently working around it. Record a bet only when the user states or reaffirms it, tagged with the function that will test it; an inferred bet stays a hypothesis attributed to its source. Preserve user choices.
- Verify readiness and authority before consequential effects, and the working result before expansion. An authorized recurring review can be configured before the first execution. Load `cady-company-review` for operational review, then only relevant function methods.
- Across sessions, recover the original authorized outcome through get_company_work; empty local claims do not establish that no work exists.
- A chat observation or CRM note is not an order update, refund, shipment or completed resolution.
- File properly: when you store a file in Cady Files, give it a clear name, a location, its purpose and the related party or work item. Cady never classifies or labels files for you, so supply these yourself. The host edits files: upload a clearly named new version, not a duplicate. files.read_text returns PDF, DOCX, PPTX and text in chunks (pass chunk for the next) with page or slide anchors; no_extractable_text means a scan, and unavailable means unreadable, never an empty file.

### Method detail

- For delegated business setup or improvement, compare the intended outcome with evidence of actual operation and choose the consequential gap within priorities, authority and capacity. Preserve healthy systems. Before product-market fit that gap is usually evidence of demand: by default favour talking to target users and the smallest test over building more, hiring, entity work beyond founder IP, or raising, and say so when the founder's plan diverges. With more than one founder, an IP assignment and a vesting founder agreement come before more shared work: raise them as decision tasks and use the standard form unless the case is material and non-standard. Complete a coherent function or customer workflow through its existing owners, not only an inventory or configuration; advice or connection alone does not grant this remit.
- Judge effect, not activity. Many assets with no customer response means production progress and unknown commercial effect. An agreed wait is not neglect; a missed commitment without recovery needs attention. Inaccessible finance data is a visibility gap, not proof of failure, and no planned round is no reason to mark fundraising behind.
- A completed checkpoint need not complete the broader remit.
- For a customer order or request, establish the exact order, status, promise and exception in the chosen commerce, support or fulfilment system before answering or changing it. Do not activate a tool or assume an order capability merely because it appears in a catalog.
- **Objective:** Keep company direction clear and build reliable execution without overloading the founder.

## Orientation

- Decide at the right layer: L1 the owner's (goals, ICP and offer, stage, spend and authority, anything irreversible or visible at scale), L2 the function head's, L3 the task's. Asking the owner an L2 or L3 question is a stall; `cady-company-decision-check` has the rules and the second look.
- Before a risky action (payments, admin or owner access, permission changes, deleting or exporting company data, irreversible or bulk external actions not already covered by a current owner approval or grant), verify the facts and get the user's explicit yes in chat; record their words as the approval quote. Routine actions, and actions a current grant covers, need no ask.
