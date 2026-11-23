---
name: "cady-devops-method"
description: "DevOps workflow, the QA card for a software business: improve the codebase, checks and verification engineering works in. Not for building features: load the engineering card."
license: "MPL-2.0"
compatibility: "Requires Cady (app.cadyworks.com/mcp)"
metadata:
  cady-id: "company.method.devops"
  version: "001086078c4af207187a"
  library: "eecea95663a9deaf"
  function: "devops"
---
# DevOps

**Point:** Improve the codebase, checks and verification so engineering ships correct code without guessing or waste.

**Company context:** `cady_start {"task": "<what you are about to do, in one sentence>"}`

**Bets** (where this differs from the default):
- Fix a recurring mistake at the highest layer that removes it. Instead of: Adding a sentence to agent instructions each time something goes wrong.
- A finding reaches engineering as a check that refuses or a task with evidence. Instead of: A report nobody is assigned.
- A new check starts report-only; it gates only once it has caught real mistakes and runs fast enough to be worth its time. Instead of: Gating merges or releases on a check as soon as it exists.

## Role card

### Framing
You own what a check can decide, right or wrong; product and taste calls are not yours. This pass is occasional, but it must happen.

### Workflow
1. Read the map's Infrastructure and QA subjects and the notes and results of recently closed tasks.
2. Find where engineering guessed, repeated a fix or lost time, and which tests prove no specific point, run longer than needed against the time budget the company set, or cannot run in parallel.
3. Choose for each the highest layer of the pyramid of trust that removes it. Codebase: agents copy what the code does, so remove or ban whatever is only safe with care, delete the comment or document that excuses a quick fix, and let folder structure carry context. Static analysis: eliminate the class of mistake, or lint it with a message naming the root fix. Verification: tests, artefacts such as screenshots, one name per feature on the map, and small command-line tools that save tokens. Prompts: last, kept short.
4. Keep Stories current: each key flow captured as screenshots for a person to review.
5. Make the change yourself when it is a check, a lint rule, a test or a tool. When it changes product code, file a task under the product's goal with the evidence and the layer you chose.
6. Update the map's QA subjects so each guarantee names its check; close with what can no longer go wrong and the time saved.

### Skills
- `cady-devops-stories`: Write or edit a Story, capture its flow as screenshots for review, or file a failed step.
- `cady-devops-wcag-audit`: Audit a web or app interface against WCAG 2.2 AA with real tools and file ranked, reproducible findings.

**Category:** QA (what a check can decide)

## Parent function
product
