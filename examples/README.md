# Example agents

Three agent files that run one company role each on Cady: `cady-gtm.md` (demand and outreach), `cady-finance.md` (cash, budgets and spend) and `cady-manager.md` (routing work to this host's agents). Each preloads only its role's method skill; task skills load when a run needs them.

`<CADY_AGENT_ID>` is the id Cady returns when the agent is registered (`agents_set` creating the agent). Replace it in the file before the first run; it ties every run to that agent's limits and records.

**Claude Code:** copy `library/<method>` (for example `library/cady-gtm-method`) into `.claude/skills/` and the agent file into `.claude/agents/`, then replace the placeholder.

**Codex:** copy the method folder into `.agents/skills/`, and use the agent file's body (below its front matter) as the prompt of the scheduled or interactive run.

Ask your Executive agent to do this for you: it designs each agent, then registers and binds it with the owner's approval (`cady-company-manage-agents`).
