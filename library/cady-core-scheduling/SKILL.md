---
name: "cady-core-scheduling"
description: "Recurring work setup and recovery. Set up recurring work with the right context, host and recovery. Use when: the user wants a scheduled or repeatable task. Not for: one run (use the run-sequence guide)."
license: "MPL-2.0"
compatibility: "Requires Cady (app.cadyworks.com/mcp)"
metadata:
  cady-id: "execution.topic.scheduling"
  version: "19b0874ca097a8d249234d02f1957ffa37912ed13ecf41194b49d010a32e24dd"
  function: "core"
---
# Recurring work setup and recovery

Set up recurring work with the right context, host and recovery. Use when: the user wants a scheduled or repeatable task. Not for: one run (use the run-sequence guide).

## Company scheduling

- **Cadence:** Reuse the authorized cadence and actual host or spend limits; otherwise fit cadence to evidence freshness and deadlines without inventing a time quota. Actionable work continues until accepted or an actual limit; waiting work checks near the expected reply or deadline and backs off empty checks; with no ready work, stop the run and keep the next useful trigger. Coalesce or skip missed runs; never replay a backlog of external effects.
- **Models:** Pick models by tier from get_execution_guide(topic="models") and the full guide's scheduled_model_selection; set model and effort explicitly when the host allows it.
- **Principle:** Wake for a useful action or signal, not to keep an agent busy. The host schedules and executes; Cady runs no scheduler and holds the work, checkpoints and results. Only host readback establishes a configured recurrence, and only a reported result proves a run.
- **Run:** Every run of every agent follows `cady-core-run-sequence`. Waiting work records nextAction and a dueDate and relies on the host's next wake; there is no separate wake mechanism.
- **Runtime:** Choose the lightest capable runtime: a script for deterministic work, a supported native host schedule for periodic work, an always-on external agent only when response time justifies its cost and security burden. Verify the actual host's scheduler, persistence and tools before promising unattended work; local execution cannot run while the machine is off.
- **Setup:** Install, bind and review agents with `cady-company-manage-agents`. Dated reminders (renewals, notice deadlines, filings) are due items in company work, read by the bound agent through get_company_work, never a separate reminder, calendar file or schedule.
- **Since last pass:** Since your last pass: read list_recent_changes from the time saved on your work item, paging back with its cursor; after a complete pass save this pass's start time, overlapping the boundary and deduplicating change ids. A change pointer is a reason to re-check, never a completion verdict.

## Shared execution sections

Read these sections of `cady-core-execution`: Execution guidance.

**Company context:** `get_cady_context({"area": "<area>", "task": "<what you are about to do, in one sentence>"})`
