<div align="center">

<img src="assets/cady.webp" alt="Cady" width="720">

# Cady skills

**Your company. Your AI team.**

Run your whole company across Claude and ChatGPT. These are the skills your agents use to do the work, with Cady keeping the company's goals, owners, decisions and records.

[![License: MPL-2.0](https://img.shields.io/badge/license-MPL--2.0-blue.svg)](LICENSE)
[![Release](https://img.shields.io/github/v/release/malcolmai/cady-skills?label=library)](https://github.com/malcolmai/cady-skills/releases)
[![Requires Cady](https://img.shields.io/badge/requires-Cady-111.svg)](https://cadyworks.com)

[Website](https://cadyworks.com) · [Skill index](INDEX.md) · [Releases](https://github.com/malcolmai/cady-skills/releases) · [Contributing](CONTRIBUTING.md)

</div>

> **Requires a Cady account.** The skills hold the methods; Cady holds your company's state, approvals and records. Without Cady they do nothing useful.

## What is Cady?

Cady is your agent orchestrator. Connect your Claude Code, Codex, Claude or ChatGPT account once, keep asking for work in the same chat you use today, and Cady gives your agent your company's goals, owners and context, plus the tools to do company work. Your ChatGPT and a colleague's Claude work from the same company, goals and records, so work handed between them needs no explaining again.

This repository is Cady's **method library**: 77 skills for running a company, from finding customers and writing outreach to month-end close, raising money, compliance and shipping software. Methods live here, versioned and open; your company's facts never do.

## How it works

1. **Your agent connects to Cady** (one MCP server). Cady serves company state: goals, decisions, people, work and approvals.
2. **Your agent loads the right skill** from this library: installed on your host, or fetched by URL at a release tag.
3. **The skill does the work** and reads or writes company state through Cady, which checks authority and records every effect.

## Quick start

Clone this library once and adopt the agents you run. Then ask your agent: **"Set up my company in Cady."** Connecting opens Cady in your browser, where you sign in or create an account.

**Claude Code**

```bash
claude plugin marketplace add malcolmai/cady-skills
claude plugin install cady@cady
git clone --depth 1 https://github.com/malcolmai/cady-skills "$HOME/.cady-skills"
python3 "$HOME/.cady-skills/install.py" --host claude-code
```

`cady` adds the Cady MCP server and the front door skill. The last command copies, into this project's `.claude/`, the company system (the Executive and the orchestrator) and the core skills every agent reads. Once setup has designed your agents, adopt each one with `python3 "$HOME/.cady-skills/install.py" --host claude-code --add <agent>` (`--list` names them, `--stage <creator|bootstrap|deep_tech>` adds a stage's usual agents): it copies that agent's role card, its function's skills and the skills the card lists, and never overwrites a folder you already have. Only installed skills join the host's skill list.

**Codex**

```bash
git clone --depth 1 https://github.com/malcolmai/cady-skills "${CODEX_HOME:-$HOME/.codex}/cady-skills"
python3 "${CODEX_HOME:-$HOME/.codex}/cady-skills/install.py" --host codex
codex mcp add cady --url https://app.cadyworks.com/mcp && codex mcp login cady
```

The install copies the front door, the company system (the Executive and the orchestrator) and the core skills into `${CODEX_HOME:-$HOME/.codex}/skills`; adopt each agent setup designs with `python3 "${CODEX_HOME:-$HOME/.codex}/cady-skills/install.py" --host codex --add <agent>` (`--list` names them, `--stage <creator|bootstrap|deep_tech>` adds a stage's usual agents). A folder you already have is never overwritten.

**claude.ai**

Upload `cady.zip` from the latest release as a skill (`cady/` holding the front door, with its `library/` folder beside it), then add Cady as a custom connector: Settings > Connectors > Add custom connector, URL `https://app.cadyworks.com/mcp`.

## Update

Pull your clone of this library (the commands below) to see what is new. Your Executive reads [CHANGELOG.md](CHANGELOG.md) since its last agent review and adopts what helps: to take a newer skill, delete its old folder from your host's `skills/` folder and add its agent again. Skills you have not re-added stay exactly as they are. Starting a new session or conversation also refreshes the connection's instructions.

**Claude Code**

```bash
claude plugin marketplace update cady && claude plugin update cady@cady && git -C "$HOME/.cady-skills" pull --ff-only
```

Then: Restart Claude Code.

On a host with a shell and the Cady CLI, run `cady usage read --host claude-code --session <current session when known> --started-at <run start ISO>` at close and report usage only when `cady usage read` exits 0; otherwise omit run.usage. Never reconstruct missing usage.

**Codex**

```bash
git -C "${CODEX_HOME:-$HOME/.codex}/cady-skills" pull --ff-only
```

Then: Start a new Codex session.

On a host with a shell and the Cady CLI, run `cady usage read --host codex --session <current session when known> --started-at <run start ISO>` at close and report usage only when `cady usage read` exits 0; otherwise omit run.usage. Never reconstruct missing usage.

**claude.ai**

Download cady.zip from github.com/malcolmai/cady-skills/releases/latest and upload it again as the cady skill.

Then: Start a new conversation.

**Other hosts**: Reinstall from github.com/malcolmai/cady-skills (README, Update).

## Customise for your company

The skills you adopt are copied into your host and are your company's own: edit them in place and record why. Your Executive decides which library changes to take, from [CHANGELOG.md](CHANGELOG.md).

## What's inside

| Path | What it is |
|---|---|
| [`INDEX.md`](INDEX.md) | Every skill with one line on when to use it and its path |
| `library/` | The skills: function role cards, task skills and run guides, each folder self-contained with its own `references/` |
| `plugins/cady/` | The Claude Code plugin: the Cady MCP server and the front door skill |
| `install.py`, `roster.json` | The adopt helper: copies the agents you choose (role card and the skills it lists) and the core skills into your host |
| `.claude-plugin/marketplace.json` | The marketplace entry for `plugins/cady` |
| [`examples/`](examples/README.md) | Three example agents (GTM, finance, orchestrator), each preloading its role's method |
| [`CHANGELOG.md`](CHANGELOG.md) | The material changes in each release; your Executive reads it |
| `manifest.json` | The library version and each skill's version |

## Privacy and security

- No file here holds company facts. Each skill names the exact `cady_read` call for its work.
- In Claude Code the plugin also adds the Cady MCP server (`app.cadyworks.com/mcp`), so do not also run `claude mcp add`, and switch off the claude.ai Cady connector inside Claude Code so Cady is not connected twice. In other apps, connect Cady once as a connector. Sending email or LinkedIn messages, publishing and spending follow your company's approval rules in Cady, and every effect leaves a record you can inspect.
- Agents report run results and usage to Cady. They never upload transcripts.
- On Codex, only if the owner opts the host in, the run sequence checks whether your most recent other local Codex session ended on a usage limit or sign-in error, and reports only that status.
- The only script is `install.py`: it copies skill folders from your clone of this library into your host's skills folder and never overwrites one that is there. It fetches nothing, runs no hooks and sends nothing anywhere.

## Contributing

Improvements that would help every company are welcome upstream: open a pull request; see [CONTRIBUTING.md](CONTRIBUTING.md). Company-specific choices stay in your own skills.

## License

[MPL-2.0](LICENSE).
