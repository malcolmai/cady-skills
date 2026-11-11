---
name: "cady-company-manage-agents"
description: "Manage company agents. Use when: Create and bind, schedule, review or retire a company agent: whether one is warranted, its design and first task. Not for: Native helpers, subagents, one-off work items and agents on a host that is in contact."
license: "MPL-2.0"
compatibility: "Requires Cady (app.cadyworks.com/mcp)"
metadata:
  cady-id: "skill.company.manage_agents"
  version: "1a4128cdcf0657d45910"
  library: "24d354b05663abe0"
  function: "company"
---
# Manage company agents

**Point:** One agent per ongoing responsibility nobody owns, proven on a first task; grants only on the person's approval.

**Company context:** `cady_read {"search": {"query": "<what you are about to do, in one sentence>"}}`

**Bets** (where this differs from the default):
- An agent is one recurring responsibility tied to one goal; reuse or update the agent that owns the outcome before creating one. Instead of: Create a new agent for each new need or parallel stream of work.
- Class risk by reach and reversibility, and make the first task one real cycle at its finish line; a critical agent runs it prepare-only through every effect path. Instead of: Class agents by how important their work is, and start with a trivial smoke task or go live directly.
- Authority comes only from the person's approval or a grant; never write approval limits into an agent's text and treat them as control. Instead of: Write the limits into the agent's instructions and trust it to stay inside them.
- Count a schedule, pause or retirement as real only after reading the host scheduler back. Instead of: Treat the agent record in Cady, or a successful create call, as the schedule's state.
- Judge an agent by what it changed for its goal and the rigour of its decisions; fix the tool, check or placement before its duties. Instead of: Judge by runs completed and records written, and rewrite the agent's prompt when it fails.

Create and bind, schedule, review or retire a company agent: whether one is warranted, its design and first task.

**Not for:** Native helpers, subagents, one-off work items and agents on a host that is in contact.

**Unit of work:** one company agent and one judged goal. **Kind:** execution. **Parallel:** no. 

## Inputs

### Authority

- verified member credential
- host identity from the current Cady connection
- decisionId and nonce are the server's: to retry, repeat the exact call
- expectedRevision null for a new agent or run, else the current revision
- current agentId for changes

### Design

- agent name and function
- one goal
- risk class (critical or standard)
- measure and its data (on the goal it serves)
- cadence or trigger, with why
- approval limits
- skills
- owner member
- first task, its checks and evaluation criteria
- end or escalation condition

## Procedure

1. An agent is one ongoing responsibility; due tasks are work items and a one-off is a helper run. Read agents_read, Projects work (work_read), direction and this host's automations first: if an agent already owns the outcome (same goal, area, function) and no safety-isolation exception applies, reuse it or change it with agents_set (rebind if its host changed) and stop. Create only when none owns it or a safety-isolation exception applies: one recurring agent per goal or sub-goal; parallel sessions and subagents are runs of that agent, not new agents. Split a child agent out only for a different risk class or grant, or a different cadence or host.
2. Responsibility and risk class. State the outcome, one measure with its data source, a cadence or trigger, approval limits and end condition; pass goal when it serves a goal. Critical: a hard-to-undo effect or reach outside the company, or drafts released automatically; every other agent is standard. Re-class and prepare-only test a new path on any grant, tool, access or trigger change.
3. Fit. Read agents_read and cady_read company:map, and find needed skills in the installed library's INDEX, reused unchanged; adapt only for an evidenced failure, tool mismatch or missing expert judgment.
4. First task. One cycle of the real deliverable at its finish line; it exercises its hardest judgement, and a critical agent runs it prepare-only through every effect path before anything reaches anyone. Its decision map, for approval: goal, node, trigger, decides alone, consults on, hands off.
5. Evaluation. The criteria live on the first task, not the agent record: brief.doneWhen holds 2-5 reader tests tagged (check), (fresh) or (person), and brief.stopIf the early-stop limit; a completed run is not a reported result.
6. Create, bind, prove, go live with agents_set (host {action: bind}, then status live), then report the first task with work_write; a returned schedule stays configured_unconfirmed until a host readback. Change visibility or sharing only on request; it applies at once and the owner is told.
7. Authority. Read the company's permission modes first (cady_read company:map values, the permission modes line). Effects follow `cady-company-decision-check` step 2. No mode lets you send without that approval or a grant; limits text is not enforcement. Never approve for the person: their own decision covers every grant (send, spend, publish, sign, file), an invite, share or outreach effect in approval mode, new access or capture, widening permissions, a design change to a grant-holding agent and raising cadence or cost; per grant when critical. An in-chat yes counts only as approval {quote: their exact words} on create or go_live. An absent owner's approval: agent design, setup, review and retirement reference.
8. Review this host's agents by risk class, with evidence from runs, receipts, cady_read changes {kind: agents} and transcripts (never bodies). Pause one that is not up to scratch (step 9) and hand over to the Executive; never rewrite its brief, methods or skills.
9. Retire or pause an agent only when it is confirmed obsolete or met its end condition, and adopt an existing company scheduled task only on the owner's yes: read the agent design, setup, review and retirement reference (it confirms an unscheduled task with agents_set host {action: removed}).

## Acceptance

- [ ] one responsibility that its work items cite
- [ ] the first task carries its evaluation criteria and stopIf before go-live and the agent reported its result; nothing was released before go-live
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
- Read [Agent host tasks, library and silent hosts](../../references/agent-hosts.md) when you install, change or review a recurring host task, install or update the skill library, or check hosts for agents whose host went silent.
- Read [Agent design, setup, review and retirement](../../references/agent-lifecycle.md) when you design an agent or change its responsibility, create, bind or take an agent live, review an agent or judge a reported result, pause or retire an agent, adopt a scheduled task, or install the baseline roster.
- Read [Execution agent brief](../../references/execution-agent-brief.md) when you set up a channel execution agent.
