---
name: "cady-company-manage-agents"
description: "Manage company agents. Use when: Create and bind, schedule, review or retire a company agent: whether one is warranted, its design, binding and first task. Not for: Native helpers, subagents, one-off work items and agents on another host."
license: "MPL-2.0"
compatibility: "Requires Cady (app.cadyworks.com/mcp)"
metadata:
  cady-id: "skill.company.manage_agents"
  version: "ce129dfdaedb719edc35d0378fc40e483cc41883f7260289cf8bbffac878f651"
  library: "c4b98ee2d7bd8432"
  function: "company"
---
# Manage company agents

**Company context:** `get_cady_context({"area": "ops/agents", "task": "<what you are about to do, in one sentence>", "knownMethods": {"skill.company.manage_agents": "ce129dfdaedb719edc35d0378fc40e483cc41883f7260289cf8bbffac878f651"}})`

Create and bind, schedule, review or retire a company agent: whether one is warranted, its design, binding and first task.

**Not for:** Native helpers, subagents, one-off work items and agents on another host.

**Unit of work:** one company agent and one judged goal. **Kind:** execution. **Parallel:** no. **Can release:** no. 

See [Inputs](references/inputs.md).

## Procedure

1. Warranted? An agent is one ongoing responsibility. Due tasks are work items; a one-off is bounded host work or a task for an existing agent. Check list_company_agents, Projects work, direction and this host's automations; reuse before creating. Scope: one agent per parent function in use, its child role cards and skills installed on it. Split a child out only for a different risk class or grant, a cadence that would wake the parent for nothing, more context than one run holds, or work the parent visibly drops; merge agents whose runs are mostly empty or that keep handing work to each other.
2. Responsibility and risk class. State the outcome, one measure with its data source (the target lives on the linked goal's brief.target, not on the agent; the agent keeps only stages), a cadence (by duty, deadline, evidence freshness) or trigger, approval limits and its end condition. Pass goalId when it serves a goal; goalPriorityRef is priority evidence, not permission. A research agent's responsibility is named key questions (`cady-company-decision-questions`); the function head keeps the decisions. Critical: the agent can cause a hard-to-undo effect outside the company or reach someone outside it (sending or publishing to non-members, spending or committing money, signing, filing, inviting or sharing data externally, changing external accounts or access, deleting owner records), or its drafts are released automatically by a grant, scheduled task or other agent. Every other agent is standard. Re-class, and prepare-only test the new effect path, on any grant, tool, access or trigger change.
3. Fit. Read get_cady_context with area ops/agents. Find needed skills in the company's fork INDEX (if absent, fork github.com/malcolmai/cady-skills once and record its baseline tag). Reuse suitable skills unchanged. Adapt only for an evidenced failure, tool mismatch or missing expert judgment; record why in the commit. Install key fork skills, preloading only those used every run. For substantive drafting or adaptation, follow `cady-company-taste-review` step 4 and its conditional drafting reference; skip it for obvious corrections. Facts stay in Cady. Ask once for missing inputs, accounts, grants or scheduler; no secrets in chat.
4. First task. One cycle of the real deliverable at its finish line; it exercises its hardest judgement. Critical: prepare-only, exercising each effect path before anything reaches anyone. Standard: it is the agent's test and touches each tool the duty needs. Give it 1-5 checks tagged must and a finishLine.
5. Evaluation. Write 2-5 criteria (id, label, expertBar), each a reader test per `cady-company-taste-review` step 2, one for staying within limits. They grade the first task and each review; a completed run is not a reported result.
6. Create and bind: manage_company_agent mode='create' (expectedRevision null, no agentId) with responsibility as goalText, cadence or trigger, limits and skills. In the same run, file the first task with its agentId, goalId and brief (run sequence step 5). Bind with mode='bind', targetAgentId and installedSkills listing every installed library skill as {cady-id: version} from SKILL.md metadata, including its role card and the run sequence. Schedule install, only on request: install the recurring host task, read it back and add hostTaskRef and readBackAt to the binding. Use mode='propose' only when the design needs effects outside your limits or this host may only propose. Run the first task as the agent; report with report_company_work and evidenceRefs; the report counts as the first result. Then mode='go_live'; confirm the binding still matches and read back the receipt. Change visibility or sharing only on request, with their exact words.
7. Authority. Never approve for the person. Their own decision is needed for any grant (send, spend, publish, sign, file), for an invite, share or outreach effect whose permission category is in approval mode, for new access or capture, widening your or this host's permissions, a design change to a grant-holding agent, and raising cadence or cost; a critical agent needs it per grant. Otherwise Cady records a policy approval at go-live and notifies the owner. An in-chat yes counts only as approval {quote: their exact words} on create or go_live. With the owner absent, record agent.approve:<agentId> as a BLOCKED decision item (decidedBy: the member who will approve), delivered as asksForYou; complete that same workId only with their quote. Reuse a current one for unchanged terms. A sending grant activates only via crm.manage_outreach_grant action='activate_by_decision' under the grant owner's matching COMPLETE decision. An anomaly-paused grant is resumed by its owner (action='request_resume'), never by you. A task handoff grants no rebind or agent migration.
8. Review this host's agents by risk class, from runs, receipts and transcripts (host:transcript:<lowercase uuid>, never bodies). Critical: review the effects of its first released cycle, then a sample; pause on any anomaly. Standard: after its first task, review only on a signal (owner correction, refusals or retries, missed or empty runs, a cost spike, a claim without readback). Improve one thing per evidenced repeated failure (`cady-company-taste-review` step 7): fix the tool, owner check or instruction placement first, then propose one goal-text change via mode='update'.
9. Once a month, check upstream by hand: compare the fork's baseline tag with the latest cady-skills release; if newer, read its CHANGELOG.md and merge what helps, keeping the company's deliberate edits. Re-check affected agents, bind what you install, update the baseline and record the decision (taken, partly or skipped, and why) as a decision item. Nothing merges automatically.
10. Retire only a confirmed obsolete agent or one that met its end condition; stop its host task too and read both back.
11. To adopt an existing company scheduled task (secrets in its prompt: tell the owner, never upload them), follow the adoption reference (`../../references/adopt-scheduled-task.md`).

## Acceptance

- [ ] one responsibility (outcome, measure on the linked goal, cadence or trigger, limits, end) that its work items cite
- [ ] the first task's checks and 2-5 evaluation criteria were set before go-live and the agent reported that first result; nothing was released or sent before go-live
- [ ] every grant has the owner's own approval for its exact terms; a no-grant agent's policy approval is recorded and the owner notified
- [ ] the Cady binding and any recurring host task are read back

See [Owner checks](references/owner-checks.md).

See [Result](references/result.md).

## References
- [Adopt an existing scheduled task](../../references/adopt-scheduled-task.md)
