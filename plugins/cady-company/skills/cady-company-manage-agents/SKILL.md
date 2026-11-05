---
name: "cady-company-manage-agents"
description: "Manage company agents. Use when: Create and bind, schedule, review or retire a company agent: whether one is warranted, its design and first task. Not for: Native helpers, subagents, one-off work items and agents on a host that is in contact."
license: "MPL-2.0"
compatibility: "Requires Cady (app.cadyworks.com/mcp)"
metadata:
  cady-id: "skill.company.manage_agents"
  version: "90d541c104f48f8d3bc7"
  library: "fd2ce869bc7d467d"
  function: "company"
---
# Manage company agents

**Point:** One agent per ongoing responsibility nobody owns, proven on a first task; grants only on the person's approval.

**Company context:** `context_read({"area": "ops/agents", "task": "<what you are about to do, in one sentence>", "knownMethods": {"skill.company.manage_agents": "90d541c104f48f8d3bc7@fd2ce869bc7d467d"}})`

**Bets** (where this differs from the default):
- An agent is one recurring responsibility tied to one goal; reuse or update the agent that owns the outcome before creating one. Instead of: Create a new agent for each new need or parallel stream of work.
- Class risk by reach and reversibility, and make the first task one real cycle at its finish line; a critical agent runs it prepare-only through every effect path. Instead of: Class agents by how important their work is, and start with a trivial smoke task or go live directly.
- Authority comes only from the person's approval or a grant; never write approval limits into an agent's text and treat them as control. Instead of: Write the limits into the agent's instructions and trust it to stay inside them.
- Count a schedule, pause or retirement as real only after reading the host scheduler back. Instead of: Treat the agent record in Cady, or a successful create call, as the schedule's state.
- Judge an agent by what it changed for its goal and the rigour of its decisions; fix the tool, check or placement before its duties. Instead of: Judge by runs completed and records written, and rewrite the agent's prompt when it fails.

Create and bind, schedule, review or retire a company agent: whether one is warranted, its design and first task.

**Not for:** Native helpers, subagents, one-off work items and agents on a host that is in contact.

**Unit of work:** one company agent and one judged goal. **Kind:** execution. **Parallel:** no. **Can release:** no. 

## Inputs

### Authority

- verified member credential
- host identity from the current Cady connection
- omit decisionId and nonce (the server fills them) unless retrying an exact call
- expectedRevision null for a new agent or run, else the current revision
- current targetAgentId for changes

### Design

- agent name and function
- one goal
- risk class (critical or standard)
- measure and its data (on the goal it serves)
- cadence or trigger, with why
- approval limits
- tool pack
- owner member
- first task, its checks and evaluation criteria
- end or escalation condition

## Procedure

1. Warranted? An agent is one ongoing responsibility. Due tasks are work items; a one-off is a bounded helper run or a task for an existing agent. Read agents_read first, then Projects work, direction and this host's automations: if an agent already owns the outcome (same goal, area or function) and no safety-isolation exception applies, reuse it or change it with mode='update' (rebind if its host changed) and stop. Create only when none owns it or a safety-isolation exception applies: one recurring agent per goal or sub-goal; parallel sessions are runs of that agent, not new agents, and so are subagents doing its tasks. Split a child agent out only for a different risk class or grant, or a different cadence or host; parallel work alone is not a reason to split.
2. Responsibility and risk class. State the outcome, one measure with its data source (its target lives on the goal's brief.target), a cadence or trigger, approval limits and the end condition; pass goalId when it serves a goal (goalPriorityRef is priority evidence, not permission). Critical: a hard-to-undo effect or reach outside the company, or drafts released automatically; every other agent is standard. Re-class and prepare-only test a new path on any grant, tool, access or trigger change.
3. Fit. Read context_read area ops/agents and find needed skills in the installed library's INDEX, reused unchanged. A fork is optional and only for a deliberate company edit, with its baseline tag. Install the library as the Library reference says. Adapt only for an evidenced failure, tool mismatch or missing expert judgment, and record why in the commit. For substantive drafting or adaptation, follow `cady-company-taste-review` step 3 and its conditional drafting reference; skip it for obvious corrections. Facts stay in Cady.
4. First task. One cycle of the real deliverable at its finish line; it exercises its hardest judgement, and a critical agent runs it prepare-only through every effect path before anything reaches anyone. Show its decision map for approval: goal, node, trigger, decides alone, consults on, hands off.
5. Evaluation. The criteria live on the first task, not the agent record: brief.doneWhen holds 2-5 reader tests tagged (check), (fresh) or (person), and brief.stopIf the limit that ends the run early; a completed run is not a reported result.
6. Create, bind, prove, go live. Create with mode='create' (expectedRevision null; duties, skills, limits, triggers: [] for on-demand or {kind:'event', on:'<description>'}); Pass goalId separately when it serves a linked goal, and a returned schedule is configured_unconfirmed until a host subscription is read back. Bind with installedSkills listing every installed library skill; Schedule install, only on request, then read the host task back and add hostTaskRef and readBackAt. Report the first task with work_write: it counts as the first result. mode='go_live' once the binding matches; read back the receipt. Use mode='propose' only when the design needs effects outside your limits. Privacy: change visibility or sharing only on request, with their exact words.
7. Authority. Read the company's permission modes first (context_read companyValues, line permission_modes). Effects follow `cady-company-decision-check` step 2. For agents: no mode lets you send without that approval or a grant; limits text is not enforcement. Never approve for the person: their own decision covers every grant (send, spend, publish, sign, file), an invite, share or outreach effect in approval mode, new access or capture, widening permissions, a design change to a grant-holding agent and raising cadence or cost; per grant when critical. Otherwise Cady records a policy approval at go-live. An in-chat yes counts only as approval {quote: their exact words} on create or go_live. With the owner absent, record agent.approve:<agentId> as a BLOCKED decision item (decidedBy: the member who will approve), delivered as asksForYou, and complete that same workId only with their quote; reuse a current one for unchanged terms. A task handoff grants no rebind or agent migration. A grant activates only via crm_interactions_write action='activate_by_decision' under its owner's matching COMPLETE decision; only its owner resumes an anomaly-paused grant (action='request_resume').
8. Review this host's agents by risk class, with evidence, from runs, receipts and transcripts (host:transcript:<lowercase uuid>, never bodies); review a critical agent's first released effects then a sample, a standard one only on a signal. Judge work by what it changed for its goal and by the rigour of its decisions. On an agent that is not up to scratch, pause it (step 9) and file one handover task under the Executive's standing goal "Keep the system sharp" naming the agent, the evidence refs and what was paused; you never rewrite its brief, methods or skills. Resume unchanged only if the cause was external, with evidence. Improving an agent is the Executive's (`cady-company-executive-review` step 15).
9. Retire only a confirmed obsolete agent or one that met its end condition: remove (retire) or pause its host task, read the scheduler back, then confirm with mode=unschedule. Cady runs no scheduler: the record alone stops nothing.
10. To adopt an existing company scheduled task (never upload a secret in its prompt), critique it against step 5 and classify it as in step 2, then propose adopt, keep outside or ignore; only on the owner's yes create, wrap and bind it.

## Acceptance

- [ ] one responsibility (outcome, measure on the linked goal, cadence or trigger, limits, end) that its work items cite
- [ ] the first task's brief holds 2-5 evaluation criteria (doneWhen) and its stopIf, set before go-live, and the agent reported that first result; nothing was released or sent before go-live
- [ ] every grant has the owner's own approval for its exact terms; a no-grant agent's policy approval is recorded and the owner notified
- [ ] the Cady binding and any recurring host task are read back

## Owner checks

- current company and member grant
- one goal per agent
- the agent is live before it takes an outside action
- agent.approve:<agentId> (policy only while no grant is held)
- host schedule readback
- reviewed receipt
- anomaly grant gate

## Result

### Artifact refs

- company:agent:<agentId>
- company:work:<workId>
- host task reference
- reviewed receipt
- **Transition:** the owner's accept and go_live take the agent live

## References
- Read [Agent design](references/agent-design.md) when you design an agent or change its responsibility.
- Read [Agent review](references/agent-review.md) when you review an agent or judge a reported result.
- Read [Agent setup](references/agent-setup.md) when you create, bind or take an agent live.
- Read [Library](references/library.md) when you install or update the skill library, or the company keeps a fork.
- Read [Retiring](references/retiring.md) when you pause or retire an agent, or adopt a scheduled task.
- Read [Scheduling](references/scheduling.md) when you install, change or review a recurring host task.
- Read [Silent hosts](references/silent-hosts.md) when you check other hosts for agents whose host went silent.
- Read [Execution agent brief](../../references/execution-agent-brief.md) when you set up a channel execution agent.
