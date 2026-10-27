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

This repository is Cady's **method library**: 63 skills for running a company, from finding customers and writing outreach to month-end close, raising money, compliance and shipping software. Methods live here, versioned and open; your company's facts never do.

## How it works

1. **Your agent connects to Cady** (one MCP server). Cady serves company state: goals, decisions, people, work and approvals.
2. **Your agent loads the right skill** from this library: installed on your host, or fetched by URL at a release tag.
3. **The skill does the work** and reads or writes company state through Cady, which checks authority and records every effect.

## Quick start

Install straight from upstream; no fork is needed. Then ask your agent: **"Set up my company in Cady."** Connecting opens Cady in your browser, where you sign in or create an account.

**Claude Code**

```bash
claude plugin marketplace add malcolmai/cady-skills
claude plugin install cady@cady
claude plugin install cady-core@cady
```

`cady` adds the Cady MCP server and the front door skill. Each `cady-<group>` plugin ships that group's skills, so install `cady-core`, then only the groups your agents use (cady-company, cady-gtm, cady-finance, cady-product, cady-engineering) with `claude plugin install <group>@cady`: every installed skill's description joins the host's skill list.

**Codex**

```bash
git clone --depth 1 https://github.com/malcolmai/cady-skills ~/.codex/cady-skills
mkdir -p ~/.codex/skills/cady && cp -R ~/.codex/cady-skills/plugins/cady/skills/cady/. ~/.codex/cady-skills/library ~/.codex/cady-skills/references ~/.codex/skills/cady/
codex mcp add cady --url https://app.cadyworks.com/mcp && codex mcp login cady
```

**claude.ai**

Upload `cady.zip` from the latest release as a skill (`cady/` holding the front door with `library/` and `references/` beside it), then add Cady as a custom connector: Settings > Connectors > Add custom connector, URL `https://app.cadyworks.com/mcp`.

## Update

Cady's first answer in a run says whether your skills match the release it serves and, when they do not, names the command for your host. You can run it any time. Starting a new session or conversation also refreshes the connection's instructions.

**Claude Code**

```bash
claude plugin marketplace update cady && claude plugin update cady@cady && claude plugin update cady-core@cady
```

Also run `claude plugin update <group>@cady` for each group plugin you installed.

Then: Restart Claude Code.

**Codex**

```bash
git -C ~/.codex/cady-skills pull --ff-only && rm -rf ~/.codex/skills/cady && mkdir -p ~/.codex/skills/cady && cp -R ~/.codex/cady-skills/plugins/cady/skills/cady/. ~/.codex/cady-skills/library ~/.codex/cady-skills/references ~/.codex/skills/cady/
```

Then: Start a new Codex session.

**claude.ai**

Download cady.zip from github.com/malcolmai/cady-skills/releases/latest and upload it again as the cady skill.

Then: Start a new conversation.

**Other hosts**: Reinstall from github.com/malcolmai/cady-skills (README, Update).

If Claude Code reports your skills are newer than Cady's release (after a rollback), reinstall instead:

```bash
claude plugin uninstall cady@cady && claude plugin install cady@cady
```

Also uninstall and reinstall each group plugin you installed (`claude plugin install <group>@cady`).

## Customise for your company (fork)

Optional. Fork when you want company-specific methods; the library is a best-practice baseline, your orchestrator agent edits the fork with your company's own reasoning, and Cady keeps your company's state and stores no skills. Nothing updates your fork automatically.

1. **Fork** `malcolmai/cady-skills` into your organisation on GitHub (private is fine), or copy a release into a repository or folder of your own.
2. **Record the baseline**: the release tag you started from. Every `SKILL.md` names it in `metadata.library`; also write it to a `BASELINE` file at the root of the fork.
3. **Point the front door at your fork**: in `plugins/cady/skills/cady/SKILL.md`, set the `Library source:` line to your fork's raw URL and branch, for example `https://raw.githubusercontent.com/<your-org>/<your-fork>/main/`.
4. **Install from your fork** with the commands above, replacing `malcolmai/cady-skills` and the clone URL with `<your-org>/<your-fork>`. For claude.ai, build the skill zip from your fork in the shape of the release's `cady.zip`.

## What's inside

| Path | What it is |
|---|---|
| [`INDEX.md`](INDEX.md) | Every skill with one line on when to use it and its path |
| `library/` | The skills: function role cards, task skills and run guides |
| `references/` | Shared references several skills load on demand |
| `plugins/cady/` | The Claude Code plugin: the Cady MCP server and the front door skill |
| `plugins/cady-<group>/` | One Claude Code plugin per skill group, each shipping its skills and the references they link |
| `.claude-plugin/marketplace.json` | The marketplace entries for `plugins/cady` and the group plugins |
| [`examples/`](examples/README.md) | Three example agents (GTM, finance, orchestrator), each preloading its role's method |
| [`CHANGELOG.md`](CHANGELOG.md) | What changed in each release; the monthly upstream check reads it |
| `manifest.json` | The library version and each skill's version |

## Edit your fork

Your orchestrator edits skills in the fork when your company's evidence says a method should differ: one commit per change, with the reason in the message. Keep company facts (names, prices, people, decisions) in Cady, not in a skill: methods come from skills, and context is company state.

## Merge upstream once a month

Once a month your orchestrator checks upstream by hand. Add the upstream remote once, then fetch, look at what changed since your baseline with `git diff`, merge the latest tag (resolve conflicts, keeping your deliberate edits) and record it as the new baseline:

```bash
git remote add upstream https://github.com/malcolmai/cady-skills
git fetch upstream --tags
git diff "$(cat BASELINE)" <latest-tag> --stat
git merge <latest-tag>
echo <latest-tag> > BASELINE
```

1. Compare `BASELINE` with the [latest release](https://github.com/malcolmai/cady-skills/releases/latest). If they match, there is nothing to do.
2. Read the [CHANGELOG.md](CHANGELOG.md) entries after your baseline: which skills are new, dropped or changed, and which parts changed.
3. Merge what helps. Where upstream changed a part you edited on purpose, keep your version or combine them, and say why in the merge commit. Skipping a release is a valid choice.
4. Update `BASELINE`, reinstall from your fork, and record the decision (taken, partly taken or skipped, and why) in Cady as a decision item.

There is no auto-merge and no plugin auto-update: a fork only changes when your orchestrator merges.

## Privacy and security

- No file here holds company facts. Each skill names the exact `get_cady_context` call for its work.
- In Claude Code the plugin also adds the Cady MCP server (`app.cadyworks.com/mcp`), so do not also run `claude mcp add`, and switch off the claude.ai Cady connector inside Claude Code so Cady is not connected twice. In other apps, connect Cady once as a connector. Sending email or LinkedIn messages, publishing and spending follow your company's approval rules in Cady, and every effect leaves a record you can inspect.
- Agents report run results and usage to Cady. They never upload transcripts.
- On Codex, only if the owner opts the host in, the run sequence checks whether your most recent other local Codex session ended on a usage limit or sign-in error, and reports only that status.
- There are no scripts or install hooks in this library: it is text only.

## Contributing

Improvements that would help every company are welcome upstream: open a pull request from your fork; see [CONTRIBUTING.md](CONTRIBUTING.md). Company-specific choices stay in your fork.

## License

[MPL-2.0](LICENSE).
