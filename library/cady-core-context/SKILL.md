---
name: "cady-core-context"
description: "Decision layers (owner, function head, task), early-stage defaults and how to read company references. Use when: deciding who decides, or what to read, before company work. Not for: running a task; load the task's skill from the front door."
license: "MPL-2.0"
compatibility: "Requires Cady (app.cadyworks.com/mcp)"
metadata:
  cady-id: "company.context"
  version: "8d88b9eabaa2f2b48011f85f0cbce6a0fd7b94732c82aaef8e28047be572481d"
  function: "core"
---
# Company context

Decision layers (owner, function head, task), early-stage defaults and how to read company references. Use when: deciding who decides, or what to read, before company work. Not for: running a task; load the task's skill from the front door.

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

- Find the decision's layer. L1, the owner's: goals with a target and date, ICP and offer, stage and quality bar, spend and authority envelope, anything irreversible or externally visible at scale. Propose it with options and a recommendation as one batched ask, and keep working on everything that does not wait on it.
- L2, yours if you head the function: how the function pursues an L1 goal. Restate the outcome one level up from the parent goal, company direction and current decisions (get_company_work decisions; filter by subject when known), choose, and record a decision with alternatives, the key assumption and what would reverse it; for an important one, take a fresh second look (`cady-company-decision-check`) and note it in rechecked. L3, any agent's: how one task is done; take the decided change narrowly, with the owner's exact constraints and finish line, and flag evidence it is wrong rather than reopen it. Asking the owner an L2 or L3 question is a stall, not caution; decisions that conflict at L2 or L3 are yours to resolve by recording a decision that cites both, and only a conflict touching an L1 item becomes one ask while work continues on everything else.
- Why: owner time is the scarcest input and wrong agent decisions compound; layers put each choice with the cheapest competent decider, and the check catches oversimplification before it spreads. Current owner records, not this static guidance, decide L1 direction; an L2 choice that contradicts or extends an L1 one is an L1 question.
- Before a risky action (payments, admin or owner access, permission changes, deleting or exporting company data, irreversible or bulk external actions not already covered by a current owner approval or grant), verify the facts and get the user's explicit yes in chat; record their words as the approval quote. Routine actions, and actions a current grant covers, need no ask.

## Reference

- **Tool:** get_execution_guide
- **Use when:** Execution/model choice by topic: selected_delivery, independent_review, company_review, executive, company_launch, gtm_launch, run_sequence, integrations (also any vendor or paid-tool choice), scheduling; omit for all.

**Company context:** `get_cady_context({"area": "<area>", "task": "<what you are about to do, in one sentence>"})`
