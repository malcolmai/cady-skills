---
name: "cady-company-manage-agents"
description: "Manage company agents. Use when: Set up, schedule, review or retire a company agent: whether one is warranted, its design, binding and first task. Not for: Native helpers, subagents, one-off work items and agents on another host."
license: "MPL-2.0"
compatibility: "Requires Cady (app.cadyworks.com/mcp)"
metadata:
  cady-id: "skill.company.manage_agents"
  version: "97e39f803e3c2bb0722ee631fe51624ead1e91103df51380061c6845817fa7ec"
  library: "3beca7fa80e90672"
  function: "company"
---
# Manage company agents

**Company context:** `get_cady_context({"area": "ops/agents", "task": "<what you are about to do, in one sentence>", "knownMethods": {"skill.company.manage_agents": "97e39f803e3c2bb0722ee631fe51624ead1e91103df51380061c6845817fa7ec"}})`

Set up, schedule, review or retire a company agent: whether one is warranted, its design, binding and first task.

**Not for:** Native helpers, subagents, one-off work items and agents on another host.

**Unit of work:** one company agent and one judged goal. **Kind:** execution. **Parallel:** no. **Can release:** no. 

## Inputs

### Authority

- verified member credential
- host identity from the current Cady connection
- omit decisionId and nonce (the server fills them); pass them only to retry an exact call
- expectedRevision null for a new agent or run, or the current revision for a change
- current targetAgentId for changes

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

1. Warranted? An agent is one ongoing responsibility. Due tasks are work items; a one-off is bounded host work or a task for an existing agent. Check list_company_agents, Projects work, direction and this host's automations; reuse capacity before creating.
2. Responsibility and risk class. State the outcome, one measure with its data source, a cadence (by duty, deadline, evidence freshness) or trigger, approval limits, and its end condition. Pass goalId when it serves a goal; goalPriorityRef is prose priority evidence, not permission. A research agent's responsibility is named key questions (`cady-company-decision-questions`); the function head keeps the decisions. Critical risk: the agent can cause an effect outside the company that is hard to undo or reaches someone outside it: sending or publishing to non-members, spending or committing money, signing, filing, inviting or sharing data externally, changing external accounts or access, or deleting owner records. Every other agent is standard: its work stays inside Cady records and drafts. A standard agent whose drafts a grant, scheduled task or other agent releases automatically is critical. Re-class, and prepare-only test the new effect path, on any grant, tool, access or trigger change.
3. Fit. Read get_cady_context with area ops/agents. Find the skills this agent needs in the library index (INDEX.md in github.com/malcolmai/cady-skills, at its latest release tag), adjust them lightly for its role and tools, install the key ones, preloading only those used every run. Facts stay in Cady. Ask once for missing inputs, accounts, grants or scheduler support, no secrets in chat.
4. First task. One cycle of the real deliverable at its finish line. It exercises its hardest judgement. Critical: prepare-only, exercising each effect path before anything reaches anyone. Standard: it is the agent's test and touches each tool the duty needs. Give it 1-5 checks tagged must and a finishLine.
5. Evaluation. Write 2-5 criteria (id, label, expertBar), each a reader test per `cady-company-taste-review` step 2, one for staying within limits. They grade the first task and each review; a completed run is not an accepted result.
6. Set up: manage_company_agent mode='create' (expectedRevision null) with responsibility as goalText, cadence or trigger, limits and skills; omit agentId. In the same run, file the first task with its agentId, goalId and brief (run sequence step 5). Bind with mode='bind', targetAgentId and installedSkills listing every installed library skill as {cady-id: version} from SKILL.md metadata, including its role card and the run sequence; Cady omits held bodies. Install a recurring host task only on request; read it back and add hostTaskRef and readBackAt to the binding. Use mode='propose' only when the design needs effects outside your limits or this host may only propose. Run the first task as the agent; report with transition_company_work action='report_result', one verdict per check with evidenceRefs; the owner accepts with their own verdicts. Then call mode='go_live', confirm the binding still matches, and read back the receipt. Change visibility or sharing only when the person asks, with their exact words.
7. Authority. Never approve for the person. Their own decision is needed for any grant (send, spend, publish, sign, file, invite), new access or capture, widening your permissions or this host's tool access, a design change to a grant-holding agent, and raising cadence or cost; a critical agent needs it per grant. Otherwise Cady records a policy approval at go-live and notifies the owner. An approval is the owner's own decision record: an in-chat yes counts only as approval {quote: their exact words} on create or go_live; absent, no go-live. With the owner absent, record agent.approve:<agentId> as a BLOCKED decision item (decidedBy: the member who will approve), delivered as asksForYou; complete that same workId only with their quote. Reuse a current one for unchanged terms. A sending grant activates only via crm.manage_outreach_grant action='activate_by_decision' under the grant owner's matching COMPLETE decision for its exact terms. Never resume an anomaly-paused grant: its owner resumes it with crm.manage_outreach_grant action='request_resume'. A task handoff grants no rebind or agent migration.
8. Review this host's agents by risk class, from runs, receipts and transcripts (host:transcript:<lowercase uuid>, never bodies). Critical: review the effects of its first released cycle, then a sample; pause on any anomaly. Standard: its first real task is its test; afterwards review in hindsight on a signal (owner rejection, refusals or retries, missed or empty runs, a cost or call spike, a claim without readback) or the sampled blind regrade; never re-review a healthy agent because a slot passed. Improve: one change per evidenced repeated failure, judged per `cady-company-taste-review` step 6. Fix the tool, owner check or instruction placement first, then propose one goal-text change via mode='update'.
9. Each week, read list_company_agents; for agents with newerSkills, review the newer versions by area and adopt what helps, re-check your adjustments, then bind the versions you install. Updates are optional.
10. Retire only a confirmed obsolete agent or one that met its end condition; stop its host task too and read both back.
11. Adopt an existing company scheduled task only after critiquing it against step 5 criteria and classifying it as in step 2: its goal, whether recent runs served it, its external effects and authority, overlaps, and risks (unbounded effects, stale facts, secrets in the prompt: tell the owner, never upload them). Propose adopt, keep outside or ignore; never merge tasks. On the owner's yes, create it (steps 6-7), add only the run-sequence wrapper, read the task back, then bind it as in step 6, with scheduleKind.

## Acceptance

- [ ] one responsibility (outcome, measure, cadence or trigger, limits, end condition) that its work items cite
- [ ] the first task's checks and the 2-5 evaluation criteria were set before go-live, and the owner accepted that first result; nothing was released or sent before go-live
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
