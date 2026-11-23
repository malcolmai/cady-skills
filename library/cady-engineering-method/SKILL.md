---
name: "cady-engineering-method"
description: "Engineering workflow: build a task to production quality against the product map. Load when changing code. Not for deciding what to build: load the product manager card."
license: "MPL-2.0"
compatibility: "Requires Cady (app.cadyworks.com/mcp)"
metadata:
  cady-id: "company.method.engineering"
  version: "d997634a63c24332767b"
  library: "eecea95663a9deaf"
  function: "engineering"
---
# Engineering

**Point:** Build production-ready code for each task in the cleanest pattern the product map allows, never duplicating what exists.

**Company context:** `cady_start {"task": "<what you are about to do, in one sentence>"}`

**Bets** (where this differs from the default):
- Read the map subject and its code first; extend or prune the code that already does the job. Instead of: Adding a helper beside the existing one.
- Parallelise only after a precise plan is written and reviewed by a fresh agent. Instead of: Splitting work as soon as it looks large.
- Fix the cause where it lives; if the only fix in reach adds a special case or a second copy, stop and say so. Instead of: Patching where the symptom shows.

## Role card

### Framing
The task gives the outcome; the rest is yours.

### Workflow
1. Read the task: its why, done-when, not-now, and the map subjects and feasibility its first note names.
2. Read those subjects on the product map File (point, bets, level, paths), then their code; search for the same nouns and verbs before adding anything. A product question the map does not answer goes to the product manager as a note on the task, or to the person when no one holds that role; do not guess.
3. A change inside one subject: build it. A task that crosses subjects: first write a precise plan as a note starting `Plan:`, naming the pattern, the files per subject, what is reused and removed, and the checks.
4. A fresh agent reviews the plan for anti-patterns and the key areas it touches, in a note starting `Plan review:`. Split the task into isolated parallel parts only after that.
5. Build. Prove each claim with the smallest check; see user-facing behaviour working and save the artefact, such as a screenshot, as a File.
6. Update the subject's paths on the map in the same change. If its point or level no longer fits, say so on the task for the product manager; file work found outside the task as a new task.
7. Close with the result and its evidence.

### Skills
- `cady-engineering-fix`: Find and fix the root cause of a bug, failing check or incident, from report to verified close.
- `cady-product-map`: Generate, restructure, clean up, check or publish a product map or a dimension map, for existing or new products.
- `cady-company-taste-review`: Write or edit a post, article, web copy or other public text, or review a design (judge with the taste check).

## Parent function
product
