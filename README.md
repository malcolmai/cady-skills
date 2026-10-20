# Cady skills

Requires a Cady account. Without Cady, these skills do nothing useful because company context and approvals live there.

## Install

**Claude Code**

    claude plugin marketplace add malcolmai/cady-skills
    claude plugin install cady@cady

**Codex**

    git clone https://github.com/malcolmai/cady-skills
    mkdir -p .agents/skills/cady && cp -R cady-skills/skills/cady/. cady-skills/library cady-skills/references .agents/skills/cady/
    codex mcp add cady --url https://app.cadyworks.com/mcp
    codex mcp login cady

**claude.ai**

Upload `cady.zip` from the repository's Releases page as a skill, then add Cady as a custom connector (Settings > Connectors > Add custom connector, URL `https://app.cadyworks.com/mcp`).

## First task

After connecting, ask your agent: "Set up my company in Cady." It opens Cady in your browser to sign in or create an account.

## Connect

Connecting opens Cady in your browser; create an account there (email code or passkey) if you don't have one.

## What is here

- `skills/cady`: the registered front door.
- `library/`: 62 skills: function methods with role cards, task skills and run guides; `INDEX.md` lists them with when to use each.
- `references/`: shared references linked from several skills.
- `examples/agents/`: two example agent files the orchestrator installs.
- `manifest.json`: Cady id, version and file digests.

## Update

Updates are manual and led by your orchestrator (or you): `claude plugin update cady@cady`; re-copy the folders for Codex, or re-upload the zip for claude.ai.

Cady may tell an agent that a newer version of a skill exists; that notice is informational and the installed version keeps working. Plugin auto-update is not relied on.

## Evaluate

`evals/discovery/` holds routing cases: does the right skill load, and does Cady stay quiet on unrelated requests.
From a clone run `claude plugin eval . --trust-plugin --tag discovery --ablation none --runs 3 --max-cost-usd 15`; runs bill your own Claude usage.
Task-quality cases need a Cady test company with seeded records, so they run in Cady's own qualification harness, not here.

## Company content stays in Cady

No file here holds a company's facts. Each skill ends with the exact `get_cady_context` call for its
work, and Cady checks authority, approvals and receipts on every write.

## Privacy

Installing the plugin adds a remote MCP server (`app.cadyworks.com/mcp`). After you approve them in Cady, your agent can send email and LinkedIn messages for your company; agents report run results and usage to Cady; they never upload transcripts. On Codex, the run sequence also checks whether your most recent other local Codex session ended on a usage limit or sign-in error and reports only that status.

## Contributing and license

Pull requests are welcome; see `CONTRIBUTING.md`. Licensed under MPL-2.0; see `LICENSE`.
