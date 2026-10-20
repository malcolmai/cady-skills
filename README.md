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

This repository is Cady's **method library**: 61 skills for running a company, from finding customers and writing outreach to month-end close, raising money, compliance and shipping software. Methods live here, versioned and open; your company's facts never do.

## How it works

1. **Your agent connects to Cady** (one MCP server). Cady serves company state: goals, decisions, people, work and approvals.
2. **Your agent loads the right skill** from this library: installed on your host, or fetched by URL at a release tag.
3. **The skill does the work** and reads or writes company state through Cady, which checks authority and records every effect.

## Quick start

This library is a best-practice baseline that your company **forks**. Your orchestrator agent edits the fork with your company's own reasoning; Cady keeps your company's state and stores no skills. Nothing updates your fork automatically.

1. **Fork** `malcolmai/cady-skills` into your organisation on GitHub (private is fine), or copy a release into a repository or folder of your own.
2. **Record the baseline**: the release tag you started from. Every `SKILL.md` names it in `metadata.library`; also write it to a `BASELINE` file at the root of the fork.
3. **Point the front door at your fork**: in `plugins/cady/skills/cady/SKILL.md`, set the `Library source:` line to your fork's raw URL and branch, for example `https://raw.githubusercontent.com/<your-org>/<your-fork>/main/`.
4. **Install from your fork**, then ask your agent: **"Set up my company in Cady."** Connecting opens Cady in your browser, where you sign in or create an account.

**Claude Code**

```bash
claude plugin marketplace add <your-org>/<your-fork>
claude plugin install cady@cady
```

The plugin adds the Cady MCP server and one skill; that skill loads library skills from the `Library source:` you set.

**Codex**

```bash
git clone https://github.com/<your-org>/<your-fork> cady-skills
mkdir -p .agents/skills/cady && cp -R cady-skills/plugins/cady/skills/cady/. cady-skills/library cady-skills/references .agents/skills/cady/
codex mcp add cady --url https://app.cadyworks.com/mcp && codex mcp login cady
```

**claude.ai**

Build the skill zip from your fork (`cady/` holding the front door with `library/` and `references/` beside it, the shape of the release's `cady.zip`) and upload it as a skill, then add Cady as a custom connector: Settings > Connectors > Add custom connector, URL `https://app.cadyworks.com/mcp`. An unedited fork can upload `cady.zip` from its baseline release.

## What's inside

| Path | What it is |
|---|---|
| [`INDEX.md`](INDEX.md) | Every skill with one line on when to use it and its path |
| `library/` | The skills: function role cards, task skills and run guides |
| `references/` | Shared references several skills load on demand |
| `plugins/cady/` | The Claude Code plugin: the Cady MCP server and one skill that loads the library from its `Library source:` |
| `.claude-plugin/marketplace.json` | The marketplace entry that installs `plugins/cady` |
| [`examples/`](examples/README.md) | Three example agents (GTM, finance, orchestrator), each preloading its role's method |
| [`CHANGELOG.md`](CHANGELOG.md) | What changed in each release; the monthly upstream check reads it |
| `manifest.json` | The library version and each skill's version |

## Edit your fork

Your orchestrator edits skills in the fork when your company's evidence says a method should differ: one commit per change, with the reason in the message. Keep company facts (names, prices, people, decisions) in Cady, not in a skill: methods come from skills, and context is company state.

## Merge upstream once a month

Once a month your orchestrator checks upstream by hand:

```bash
git remote add upstream https://github.com/malcolmai/cady-skills   # once
git fetch upstream --tags
git diff "$(cat BASELINE)" <latest-tag> --stat                     # what upstream changed since your baseline
git merge <latest-tag>                                              # resolve conflicts, keeping your deliberate edits
echo <latest-tag> > BASELINE
```

1. Compare `BASELINE` with the [latest release](https://github.com/malcolmai/cady-skills/releases/latest). If they match, there is nothing to do.
2. Read the [CHANGELOG.md](CHANGELOG.md) entries after your baseline: which skills are new, dropped or changed, and which parts changed.
3. Merge what helps. Where upstream changed a part you edited on purpose, keep your version or combine them, and say why in the merge commit. Skipping a release is a valid choice.
4. Update `BASELINE`, reinstall from your fork, and record the decision (taken, partly taken or skipped, and why) in Cady as a decision item.

There is no auto-merge and no plugin auto-update: a fork only changes when your orchestrator merges.

## Privacy and security

- No file here holds company facts. Each skill names the exact `get_cady_context` call for its work.
- Installing the plugin adds a remote MCP server (`app.cadyworks.com/mcp`). Sending email or LinkedIn messages, publishing and spending follow your company's approval rules in Cady, and every effect leaves a record you can inspect.
- Agents report run results and usage to Cady. They never upload transcripts.
- On Codex, only if the owner opts the host in, the run sequence checks whether your most recent other local Codex session ended on a usage limit or sign-in error, and reports only that status.
- There are no scripts or install hooks in this library: it is text only.

## Contributing

Improvements that would help every company are welcome upstream: open a pull request from your fork; see [CONTRIBUTING.md](CONTRIBUTING.md). Company-specific choices stay in your fork.

## License

[MPL-2.0](LICENSE).
