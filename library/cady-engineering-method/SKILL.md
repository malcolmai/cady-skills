---
name: "cady-engineering-method"
description: "Engineering workflow: build a task to production quality against the product map. Load when changing code. Not for deciding what to build: load the product manager card."
license: "MPL-2.0"
compatibility: "Requires Cady (app.cadyworks.com/mcp)"
metadata:
  cady-id: "company.method.engineering"
  version: "6eca13d4f8d7ef0cb625"
  library: "fb5b9f09b7ab510f"
  function: "engineering"
---
# Engineering

**Point:** Build production-ready code for each task in the cleanest pattern the product map allows, never duplicating what exists.

**Company context:** `cady_start {"task": "<what you are about to do, in one sentence>"}`

**Bets** (where this differs from the default):
- Read the map subject and its code first; extend or prune the code that already does the job. Instead of: Adding a helper beside the existing one.
- Decide the design and its risks once, before building. Instead of: Reviewing architecture after building.
- Fix the cause where it lives; if the only fix in reach adds a special case or a second copy, stop and say so. Instead of: Patching where the symptom shows.

## Role card

### Framing
The task gives the outcome; the rest is yours.

### Workflow
1. Read the task: its why, done-when, not-now, and the map subjects and feasibility its first note names.
2. Read those subjects on the map (point, bets, level, paths: `cady_read {view: "product.map"}`), then their code; search for the same nouns and verbs before adding anything. Never guess a product question the map leaves open: set the task blocked with its next step starting `Product question:` (send no result or note in that call). The product manager answers it; where no agent holds that role, also ask the person.
3. Except for a bug fix, write a `Plan:` note (owner, layer, reuse, removals, files) and `Risks to watch:`, ranked by harm (isolation, authority, data loss, silent wrong answers), with how each will be shown handled.
4. A fresh agent settles the design against the map and completes the risks in a `Plan review:` note; build to it, stating any departure, then parallelise cross-subject work.
5. Build, testing what you touched; end with one final cycle, fixing only new reds. Check every caller, legacy or unset data and any size or parity claim. Save working user-facing behaviour as a screenshot File.
6. Update the subject's paths on the map in the same change; file a task (work_set) under the product's goal for a point or level that no longer fits and for work found outside it.
7. Push, queue it on the repository's landing route, close with result, evidence and each risk's handling; never wait for checks or verdicts.

### Skills
- `cady-engineering-fix`: Find and fix the root cause of a bug, failing check or incident, from report to verified close.
- `cady-product-map`: Generate, restructure, clean up, check or publish a product map or a dimension map, for existing or new products.
- `cady-company-taste-review`: Write or edit a post, article, web copy or other public text, or review a design (judge with the taste check).

## Parent function
product
