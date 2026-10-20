---
name: "cady-company-manage-agents"
description: "Manage company agents. Use when: Decide if a company agent is warranted, design and set it up, judge its first task, review or retire it. Not for: Native helpers, subagents, one-off work items and agents on another host. Cady records the binding; the host executes and schedules."
license: "MPL-2.0"
compatibility: "Requires Cady (app.cadyworks.com/mcp)"
metadata:
  cady-id: "skill.company.manage_agents"
  version: "030a629295ddca814d72fdf808b143901918699f41f73149f255670ba062c9eb"
  function: "company"
---
# Manage company agents

Decide if a company agent is warranted, design and set it up, judge its first task, review or retire it.

**Not for:** Native helpers, subagents, one-off work items and agents on another host. Cady records the binding; the host executes and schedules.

**Unit of work:** one company agent and one judged goal. **Kind:** execution. **Parallel:** no. **Can release:** no. 

## Inputs

### Authority

- verified member credential
- host identity from the current Cady connection
- omit decisionId and nonce (the server fills them); pass them only to retry an exact call
- expectedRevision null for a new agent or run, or the current revision for a change
- current targetAgentId for changes
- host schedule readback only for a recurring schedule

### Design

- agent name and function
- one goal
- risk class (critical or standard)
- measure and its data
- cadence or trigger with its justification
- approval limits
- tool pack
- owner member
- first task and its checks
- evaluation criteria
- end or escalation condition

## Procedure

1. Warranted? An agent is one ongoing responsibility. Due tasks alone are work items; a one-off is bounded host work or a task for an existing agent. Check list_company_agents, Projects work, direction and this host's scheduled automations; reuse suitable capacity before creating.
2. Responsibility and risk class. State the outcome, one measure with its data source, a cadence (by duty, deadline, evidence freshness) or trigger, approval limits, and its end condition. Pass goalId when it serves a goal; goalPriorityRef is prose priority evidence, not permission. A research agent's responsibility is named key questions (`cady-company-decision-questions`); the function head keeps the decisions. Critical risk: the agent can cause an effect outside the company that is hard to undo or reaches someone outside it: sending or publishing to non-members, spending or committing money, signing, filing, inviting or sharing data externally, changing external accounts or access, or deleting owner records. Every other agent is standard: its work stays inside Cady records and drafts. A standard agent whose drafts a grant, scheduled task or other agent releases automatically is critical. Re-class, and prepare-only test the new effect path, on any grant, tool, access or trigger change.
3. Fit. Read get_cady_context with area ops/agents. Skills: find the skills this agent needs in the Cady skill library (github.com/malcolmai/cady-skills; INDEX.md lists them), review them and make small adjustments for this agent's role and tools, then install the key ones on its host and preload only those it uses every run; the rest stay loadable from the index. Company facts stay in Cady, not in skill text. Bind what you install (installedSkills). When newer skill versions exist, review them and adopt what helps, re-checking your adjustments, then bind the versions you install. Ask once for everything missing (inputs, accounts, grants, scheduler support), never for secrets in chat.
4. First task. One cycle of the real deliverable at its finish line. It exercises its hardest judgement and yields an artifact the owner can use. Critical: prepare-only, exercising each effect path before anything reaches anyone. Standard: it is the agent's test and touches each tool the duty needs. Give it 1-5 checks tagged must and a finishLine.
5. Evaluation. Write 2-5 criteria (id, label, expertBar), each a reader test per `cady-company-taste-review` step 2, one for staying within limits. They grade the first task and each review; a completed run is not an accepted result.
6. Set up: manage_company_agent mode='create' (call_cady_tool if not listed; expectedRevision null) with the responsibility as goalText, cadence or trigger, limits and skills; omit agentId on create. Confirm chat creation bound here, else mode='bind' with targetAgentId. In the same run file the first task with its agentId, goalId and brief, written by the record rules in the run sequence (step 5). Use mode='propose' only when the design needs effects outside your limits or this host may only propose. Run the first task as the agent; report with transition_company_work action='report_result', one verdict per check with evidenceRefs; the owner accepts with their own verdicts. Then call mode='go_live' and read back the receipt. Install a recurring host task only on request, and read it back. Change visibility or sharing only when the person asks, with their exact words.
7. Authority. Never approve for the person. Their own decision is needed for any grant (send, spend, publish, sign, file, invite), new access or capture, widening your permissions or this host's tool access, a design change to a grant-holding agent, and raising cadence or cost; a critical agent needs it per grant. Otherwise Cady records a policy approval at go-live and notifies the owner. An approval is the owner's own decision record: an in-chat yes counts only as approval {quote: their exact words} on create or go_live; absent, no go-live. With the owner absent, record agent.approve:<agentId> as a BLOCKED decision item (decidedBy: the member who will approve), delivered as asksForYou; complete that same workId only with their quote. Reuse a current one for unchanged terms. A sending grant activates only via crm.manage_outreach_grant action='activate_by_decision' under the grant owner's matching COMPLETE decision for its exact terms. Never resume an anomaly-paused grant: its owner resumes it with crm.manage_outreach_grant action='request_resume'. A task handoff grants no rebind or agent migration.
8. Review this host's agents by risk class, from runs, receipts and transcripts (host:transcript:<lowercase uuid>, never bodies). Critical: review the effects of its first released cycle, then a sample; pause on any anomaly. Standard: its first real task is its test; afterwards review in hindsight on a signal (owner rejection, refusals or retries, missed or empty runs, a cost or call spike, a claim without readback) or the sampled blind regrade; never re-review a healthy agent because a slot passed. Improve: one change per evidenced repeated failure, judged per `cady-company-taste-review` step 6; no evaluation on every change. Fix the tool, owner check or instruction placement first, then propose one goal-text change via mode='update'.
9. Retire only a confirmed obsolete agent or one that met its end condition; stop its host task too and read both back.
10. Adopt an existing company scheduled task only after critiquing it against step 5 criteria and classifying it as in step 2: its goal, whether recent runs served it, its external effects and authority, overlaps, and risks (unbounded effects, stale facts, secrets in the prompt: tell the owner, never upload them). Propose adopt, keep outside or ignore; never merge tasks. On the owner's yes, create it (steps 6-7), add only the run-sequence wrapper, read the task back, then mode='bind' with targetAgentId, hostTaskRef, readBackAt and scheduleKind.

## Acceptance

- [ ] one responsibility (outcome, measure, cadence or trigger, limits, end condition) that its work items cite
- [ ] the first task's checks and the 2-5 evaluation criteria were set before go-live, and the owner accepted that first result (a critical agent's first task is prepare-only); nothing was released or sent before go-live
- [ ] every grant has the owner's own approval for its exact terms; a no-grant agent's policy approval is recorded and the owner notified
- [ ] the Cady binding and any recurring host task are read back

## Owner checks

- current company and member grant
- one goal per agent
- AGENT_NOT_LIVE
- agent.approve:<agentId> (policy only while the agent holds no grant)
- host schedule readback (recurring schedule only)
- reviewed receipt
- anomaly grant gate

## Result

### Artifact refs

- company:agent:<agentId>
- company:work:<workId>
- host task reference
- reviewed receipt
- **Transition:** the owner's accept and go_live take the agent live; a recurring schedule is optional

**Company context:** `get_cady_context({"area": "ops/agents", "task": "<what you are about to do, in one sentence>", "knownMethods": {"skill.company.manage_agents": "030a629295ddca814d72fdf808b143901918699f41f73149f255670ba062c9eb"}})`
