---
name: "cady-company-manage-agents"
description: "Manage company agents. Use when: Create and bind, schedule, review or retire a company agent: whether one is warranted, its design and first task. Not for: Native helpers, subagents, one-off work items and agents on a host that is in contact (step 12 covers a silent one)."
license: "MPL-2.0"
compatibility: "Requires Cady (app.cadyworks.com/mcp)"
metadata:
  cady-id: "skill.company.manage_agents"
  version: "5021d010ae7457e92675"
  library: "a9ede08c00c06027"
  function: "company"
---
# Manage company agents

**Company context:** `get_cady_context({"area": "ops/agents", "task": "<what you are about to do, in one sentence>", "knownMethods": {"skill.company.manage_agents": "5021d010ae7457e92675@a9ede08c00c06027"}})`

Create and bind, schedule, review or retire a company agent: whether one is warranted, its design and first task.

**Not for:** Native helpers, subagents, one-off work items and agents on a host that is in contact (step 12 covers a silent one).

**Unit of work:** one company agent and one judged goal. **Kind:** execution. **Parallel:** no. **Can release:** no. 

## Inputs

### Authority

- verified member credential
- host identity from the current Cady connection
- omit decisionId and nonce (the server fills them) unless retrying an exact call
- expectedRevision null for a new agent or run, or the current revision for a change
- current targetAgentId for changes

### Design

- agent name and function
- one goal
- risk class (critical or standard)
- measure and its data (the target and readings live on the goal it serves)
- cadence or trigger, with why
- approval limits
- tool pack
- owner member
- first task, its checks and evaluation criteria
- end or escalation condition

## Procedure

1. Warranted? An agent is one ongoing responsibility. Due tasks are work items; a one-off is bounded host work or a task for an existing agent. Read list_company_agents first, then Projects work, direction and this host's automations: if an agent already owns the outcome (same goal, area or function), reuse it or change it with mode='update' (rebind if its host changed) and stop here; a second agent on one goal and one contact list doubles sends and splits records. Create only when none owns it. Scope: one agent per parent function in use, its child role cards and skills installed on it. Split a child out only for a different risk class or grant, a cadence that would wake the parent for nothing, more context than one run holds, or work the parent visibly drops; merge agents whose runs are mostly empty or that keep handing work to each other.
2. Responsibility and risk class. State the outcome, one measure with its data source (the target lives on the linked goal's brief.target, not on the agent; the agent keeps only stages), a cadence (by duty, deadline, evidence freshness) or trigger, approval limits and its end condition. Pass goalId when it serves a goal; goalPriorityRef is priority evidence, not permission. A research agent's responsibility is named key questions (`cady-company-decision-questions`); the function head keeps the decisions. Critical: the agent can cause a hard-to-undo effect outside the company or reach someone outside it (sending or publishing to non-members, spending or committing money, signing, filing, inviting or sharing data externally, changing external accounts or access, deleting owner records), or its drafts are released automatically by a grant, scheduled task or other agent. Every other agent is standard. Re-class, and prepare-only test the new effect path, on any grant, tool, access or trigger change.
3. Fit. Read get_cady_context with area ops/agents. Find needed skills in the installed library's INDEX. A fork is optional: fork github.com/malcolmai/cady-skills only when the company needs a deliberate edit, and then record its baseline tag. Reuse suitable skills unchanged. Adapt only for an evidenced failure, tool mismatch or missing expert judgment; record why in the commit. Install key fork skills, preloading only those used every run. For substantive drafting or adaptation, follow `cady-company-taste-review` step 3 and its conditional drafting reference; skip it for obvious corrections. Facts stay in Cady. Ask once for missing inputs, accounts, grants or scheduler; no secrets in chat.
4. First task. One cycle of the real deliverable at its finish line; it exercises its hardest judgement. Critical: prepare-only, exercising each effect path before anything reaches anyone. Standard: it is the agent's test and touches each tool the duty needs.
5. Evaluation. The criteria live on the first task, not on the agent record: brief.doneWhen holds 2-5 plain lines, each a reader test (a yes/no question a reader without context can answer) and tagged (check), (fresh) or (person) by who can verify it; brief.stopIf holds the limit that ends the run early (staying within approvalLimits is always one). They grade the first task and each later review; a completed run is not a reported result. Agent-level limits stay in approvalLimits and dutyOrder.
6. Create and bind: manage_company_agent mode='create' (expectedRevision null, no agentId) with responsibility as goalText, cadence or trigger, limits and skills. In the same run, file the first task with its agentId, goalId and brief (run sequence step 5). Bind with mode='bind', targetAgentId and installedSkills listing every installed library skill as {id: version} or {id: version@tag}, copied from its SKILL.md header, including its role card and the run sequence. Any spelling resolves to one skill (the skill.* id, function.name shorthand or the library name; the skills field takes the same spellings); an unknown one is refused with the nearest valid id. Schedule install, only on request (reference scheduling): install the recurring host task, read it back and add hostTaskRef and readBackAt to the binding. Use mode='propose' only when the design needs effects outside your limits or this host may only propose. Run the first task as the agent; report with report_company_work and evidenceRefs; the report counts as the first result. Then mode='go_live'; confirm the binding still matches and read back the receipt. Change visibility or sharing only on request, with their exact words. An agent's privacy (private, shared or public; default private) covers its runs, run results, evaluations, cost, refusal log, prompt, design and trigger; its work, results, decisions and notes are company record every member reads, except what is marked sensitive. Admins see private internals only when they turn on See everything.
7. Authority. Read the company's permission modes first (get_cady_context companyValues, line permission_modes; one mode per category: invites, shares, external for outreach and publication, decisions). In approval mode a send waits for a person's approval in the browser; in notify mode you approve it yourself and the owner is only told after, so sends do not wait for them. When the person asks for their approval before sends and the mode is notify, tell them plainly that sends will not wait for them and that only changing the category to approval in company Settings makes them wait; limits written in approvalLimits are not enforcement. Never approve for the person. Their own decision is needed for any grant (send, spend, publish, sign, file), for an invite, share or outreach effect whose permission category is in approval mode, for new access or capture, widening your or this host's permissions, a design change to a grant-holding agent, and raising cadence or cost; a critical agent needs it per grant. Otherwise Cady records a policy approval at go-live and notifies the owner. An in-chat yes counts only as approval {quote: their exact words} on create or go_live. With the owner absent, record agent.approve:<agentId> as a BLOCKED decision item (decidedBy: the member who will approve), delivered as asksForYou; complete that same workId only with their quote. Reuse a current one for unchanged terms. A sending grant activates only via crm.manage_outreach_grant action='activate_by_decision' under the grant owner's matching COMPLETE decision. An anomaly-paused grant is resumed by its owner (action='request_resume'), never by you. A task handoff grants no rebind or agent migration.
8. Review this host's agents by risk class, from runs, receipts and transcripts (host:transcript:<lowercase uuid>, never bodies). Critical: review the effects of its first released cycle, then a sample; pause on any anomaly. Standard: after its first task, review only on a signal (owner correction, refusals or retries, missed or empty runs, a cost spike, a claim without readback). Improve one thing per evidenced repeated failure (`cady-company-change-agent-behaviour`): fix the tool, owner check or instruction placement first, then propose one goal-text change via mode='update'.
9. Keep the library current. An upstream install updates with the host's own update command. If the company keeps a fork, once a month compare its baseline tag with the latest cady-skills release; if newer, read its CHANGELOG.md and merge what helps by hand, keeping the company's deliberate edits. Re-check affected agents, bind what you install, update the baseline and record the decision (taken, partly or skipped, and why) as a decision item. Nothing merges automatically.
10. Retire only a confirmed obsolete agent or one that met its end condition. Cady runs no scheduler, so retiring or pausing an agent does not stop its host task: remove (retire) or pause (pause) that task in the host's scheduler, read the scheduler back, then confirm with manage_company_agent mode=unschedule (targetAgentId, expectedRevision). The agent itself does this on its next wake when its context says stop; this host's orchestrator does it for the triggersToRemove items in its context. On resume the agent shows setUpSchedule: install the task again and bind it with hostTaskRef and readBackAt.
11. To adopt an existing company scheduled task (secrets in its prompt: tell the owner, never upload them), follow the adoption reference (`../../references/adopt-scheduled-task.md`).
12. A silent host's agents. Look at your other hosts at most once a day (list_company_agents: each host's lastContactAt and, for a host silent 72 hours or more, each live agent's moveTo). A host in contact: skip its agents unless you detect and confirm a severe risk (for example an agent sending out poor content); then pause that agent first and tell the owner. A silent host's agent: if moveTo.here is true (moveTo is your host), move it here (mode='move', targetAgentId, expectedRevision), set up its host task at its stored cadence, read it back (mode='bind' with hostTaskRef, readBackAt, scheduleKind) in the same run, and tell the owner in one line; if moveTo is another host, skip it; if moveTo is null, pause it (mode='pause' with a reason) and raise one ask to its owner to pause or retire (moveWhy says why). The server takes a move only from the host moveTo names, which is the target host's orchestrator (that is you when moveTo.here is true); in the web app the owner moves an agent. Retire only an obsolete agent.

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
- Read [Scheduling](references/scheduling.md) when you install, change or review a recurring host task, or choose a cadence, runtime or model for scheduled work.
- Read [Adopt an existing scheduled task](../../references/adopt-scheduled-task.md) when a company's existing host scheduled task is to be brought under Cady.
- Read [GTM agent recipe](../../references/agent-recipe-gtm.md) when the agent is for the gtm function (demand, outreach, posting); it shows one worked design to copy the shape of.
