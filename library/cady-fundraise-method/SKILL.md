---
name: "cady-fundraise-method"
description: "Plan financing choices and prepare evidence-backed materials for a company's raise. Use when: deciding whether to raise, preparing investor materials or organizing financing evidence. Not for: building an investor pool (use `cady-fundraise-investor-list`) or issuing shares."
license: "MPL-2.0"
compatibility: "Requires Cady (app.cadyworks.com/mcp)"
metadata:
  cady-id: "company.method.fundraise"
  version: "066ed8732e725c516d1d48e25ff7046509ecec3608c89d0027ccc8c125a8cb27"
  function: "fundraise"
---
# Fundraise

## Parent function
finance

## Selected judgment
- Compare capital needed for specific milestones with lower-capital alternatives and timing. Assess investor fit, evidence, diligence readiness and the exact relationship before authorized communication. No active round is not an overdue round; preparation does not authorize launch or investor contact.
- Size scenarios against cash timing, milestone proof and the cost of delay. Distinguish the internal round objective, investor thesis, materials, pipeline and external launch; evidence can support preparation without establishing terms or send authority.
- Produce the smallest useful investor or materials result with source-backed claims and exact owner references. Record the next decision and accountable checkpoint where authorized; verify any saved result and keep uncertain investor responses separate from commitments.

## Domain method
- **Integrate:** Read each result with get_company_work and inspect the exact CRM list or Files refs before transition_company_work(action: 'accept_result'). Send the helper one corrected prompt on a miss. Present investor contact or update copy as unsent until its separate owner review and authority are satisfied. Before recording shares, list recent share issues and verify the investment against its evidence document. A SAFE is not issued shares. Issues are automatic plus notify; report issuance only after the receipt. Suspected duplicates are refused unless distinctReason explains a separate issuance. Correct only with a void entry.
- **Job:** Help the company decide whether, when and how much capital to raise for named milestones. Read get_company_direction first; distinguish internal strategy, investor fit, materials and contact authority. Manage entities, rounds and issued-share records with crm.manage_company_records(action='set_entity'), crm.manage_company_records(action='set_round'), crm.manage_company_records(action='record_share_issue'), crm.manage_company_records(action='void_share_issue'), crm.manage_company_records(action='list'), crm.manage_company_records(action='get'); crm.set_track and crm.list_parties with mode "tracks" accept roundId.
- **Plan into work:** Turn each commissioned investor list or material into one Projects work item with submit_company_work_checkpoint: a new workId, expectedRevision null, current skill_index methodId and methodVersion, source refs, statement, acceptance and next action. Do not create an unrequested round or bundle of materials.


Shared by every role card: `../../references/role-card-common.md`.
**Company context:** `get_cady_context({"area": "gtm/strategy", "task": "<what you are about to do, in one sentence>", "knownMethods": {"company.method.fundraise": "066ed8732e725c516d1d48e25ff7046509ecec3608c89d0027ccc8c125a8cb27"}})`
