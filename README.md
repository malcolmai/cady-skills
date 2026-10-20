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

Cady is your agent orchestrator. Connect your Claude, ChatGPT, Gemini or Grok account once, keep asking for work in the same chat you use today, and Cady gives your agent your company's goals, owners and context, plus the tools to do company work. Your ChatGPT and a colleague's Claude work from the same company, goals and records, so work handed between them needs no explaining again.

This repository is Cady's **method library**: 63 skills for running a company, from finding customers and writing outreach to month-end close, raising money, compliance and shipping software. Methods live here, versioned and open; your company's facts never do.

## How it works

1. **Your agent connects to Cady** (one MCP server). Cady serves company state: goals, decisions, people, work and approvals.
2. **Your agent loads the right skill** from this library: installed on your host, or fetched by URL at a release tag.
3. **The skill does the work** and reads or writes company state through Cady, which checks authority and records every effect.

## Quick start

**Claude Code**

```bash
claude plugin marketplace add malcolmai/cady-skills
claude plugin install cady@cady
```

The plugin adds the Cady MCP server and one skill; it loads library skills from this repository by URL at the plugin's release tag.

**Codex**

```bash
git clone https://github.com/malcolmai/cady-skills
mkdir -p .agents/skills/cady && cp -R cady-skills/plugins/cady/skills/cady/. cady-skills/library cady-skills/references .agents/skills/cady/
codex mcp add cady --url https://app.cadyworks.com/mcp && codex mcp login cady
```

**claude.ai**

Upload `cady.zip` from the [latest release](https://github.com/malcolmai/cady-skills/releases) as a skill, then add Cady as a custom connector: Settings > Connectors > Add custom connector, URL `https://app.cadyworks.com/mcp`.

**Any host with web access**

Read the index at `https://raw.githubusercontent.com/malcolmai/cady-skills/<tag>/INDEX.md` and fetch `library/<name>/SKILL.md` at the same tag.

Then ask your agent: **"Set up my company in Cady."** Connecting opens Cady in your browser, where you sign in or create an account.

## What's inside

| Path | What it is |
|---|---|
| [`INDEX.md`](INDEX.md) | Every skill with one line on when to use it and its path |
| `library/` | The skills: function role cards, task skills and run guides |
| `references/` | Shared references several skills load on demand |
| `plugins/cady/` | The Claude Code plugin: the Cady MCP server and one skill that loads the library by URL at this tag |
| `.claude-plugin/marketplace.json` | The marketplace entry that installs `plugins/cady` |
| [`examples/`](examples/README.md) | Three example agents (GTM, finance, orchestrator), each preloading its role's method |
| `manifest.json` | The library version and each skill's version |

## Updating

Updates are manual and optional, led by your orchestrator agent or by you. Each skill records the library version it came from in `metadata.library`. Compare it with the tag in the library index URL the Cady MCP server instructions give; if they give none, use the [latest release](https://github.com/malcolmai/cady-skills/releases/latest). If they differ, update when it helps: `claude plugin update cady@cady`, re-copy the folders for Codex, or re-upload the zip for claude.ai. An older version keeps working.

## Privacy and security

- No file here holds company facts. Each skill names the exact `get_cady_context` call for its work.
- Installing the plugin adds a remote MCP server (`app.cadyworks.com/mcp`). Sending email or LinkedIn messages, publishing and spending follow your company's approval rules in Cady, and every effect leaves a record you can inspect.
- Agents report run results and usage to Cady. They never upload transcripts.
- On Codex, only if the owner opts the host in, the run sequence checks whether your most recent other local Codex session ended on a usage limit or sign-in error, and reports only that status.
- There are no scripts or install hooks in this library: it is text only.

## Contributing

Pull requests are welcome. Edit the skill under `library/` and say what it improves; see [CONTRIBUTING.md](CONTRIBUTING.md). The files are generated from Cady's method source, so maintainers carry accepted changes upstream and credit you.

## License

[MPL-2.0](LICENSE).
