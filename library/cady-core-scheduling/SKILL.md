---
name: "cady-core-scheduling"
description: "Recurring work setup and recovery. Set up recurring work with the right context, host and recovery. Use when: the user wants a scheduled or repeatable task. Not for: one run (use `cady-core-run-sequence`)."
license: "MPL-2.0"
compatibility: "Requires Cady (app.cadyworks.com/mcp)"
metadata:
  cady-id: "execution.topic.scheduling"
  version: "bc9a0f9666653b5b884280e81d97076ed6f8420f33672fbc835c010efb297772"
  library: "6950bdef5dfadc81"
  function: "core"
---
# Recurring work setup and recovery

**Company context:** `get_cady_context({"area": "ops/agents", "task": "<what you are about to do, in one sentence>", "knownMethods": {"execution.topic.scheduling": "bc9a0f9666653b5b884280e81d97076ed6f8420f33672fbc835c010efb297772"}})`

Set up recurring work with the right context, host and recovery. Use when: the user wants a scheduled or repeatable task. Not for: one run (use `cady-core-run-sequence`).

## Company scheduling

- **Cadence:** Reuse the authorized cadence and actual host or spend limits; otherwise fit cadence to evidence freshness and deadlines without inventing a time quota. Actionable work continues until accepted or an actual limit; waiting work checks near the expected reply or deadline and backs off empty checks; with no ready work, stop the run and keep the next useful trigger. Coalesce or skip missed runs; never replay a backlog of external effects.
- **Models:** The host owns model and effort selection. Preserve explicit user settings and use supported host controls; when selection is unavailable, use the configured executor.
- **Principle:** Wake for a useful action or signal, not to keep an agent busy. The host schedules and executes; Cady runs no scheduler and holds the work, checkpoints and results. Only host readback establishes a configured recurrence, and only a reported result proves a run.
- **Run:** Every run of every agent follows `cady-core-run-sequence`. Waiting work records nextAction and a dueDate and relies on the host's next wake; there is no separate wake mechanism.
- **Runtime:** Choose the lightest capable runtime: a script for deterministic work, a supported native host schedule for periodic work, an always-on external agent only when response time justifies its cost and security burden. Verify the actual host's scheduler, persistence and tools before promising unattended work; local execution cannot run while the machine is off.
- **Setup:** Install, bind and review agents with `cady-company-manage-agents`. Dated reminders (renewals, notice deadlines, filings) are due items in company work, read by the bound agent through get_company_work, never a separate reminder, calendar file or schedule.
- **Since last pass:** Since your last pass: read list_recent_changes from the time saved on your work item, paging back with its cursor; after a complete pass save this pass's start time, overlapping the boundary and deduplicating change ids. A change pointer is a reason to re-check, never a completion verdict.

## Shared execution sections

Read these sections of `cady-core-execution`: Execution guidance.
