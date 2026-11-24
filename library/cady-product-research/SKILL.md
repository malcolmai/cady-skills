---
name: "cady-product-research"
description: "Research. Use when: Write or update a research file on how users see the product and its alternatives, or on a technology. Not for: Deciding the roadmap or writing a plan: research supplies evidence, not policy."
license: "MPL-2.0"
compatibility: "Requires Cady (app.cadyworks.com/mcp)"
metadata:
  cady-id: "skill.product.research"
  version: "59a911b406809a7c44c1"
  library: "e8872d5e32bf66b3"
  function: "product"
---
# Research

**Point:** Lay out the options for one question, with evidence and tradeoffs, so the owner can decide without redoing the analysis.

**Company context:** `cady_start {"task": "<what you are about to do, in one sentence>"}`

Write or update a research file on how users see the product and its alternatives, or on a technology.

**Not for:** Deciding the roadmap or writing a plan: research supplies evidence, not policy.

**Unit of work:** one research question and its evolving research file. **Kind:** strategy. **Parallel:** no. 

## Inputs

### Evidence refs

- the question and the decision it serves
- the existing research file, if any
- dated source references

## Procedure

1. State the question and the decision it serves in one sentence.
2. Search Files for the same question (`cady_read`, kinds file); update that file, never start a second.
3. Users: go through the product as a new user would, from its public pages to first value, and record what they would understand, expect and get. Then list what they can really choose for the job instead, a manual workaround and doing nothing included; compare on dated evidence and say when each wins.
4. Technology, assets and value chain: say what the best version needs and who supplies each part; compare against the no-build and existing-capability baseline at the real workload. A vendor's claim stays a claim until measured.
5. Keep observation, interpretation and recommendation apart, mark guesses, and include the evidence against your leading view.
6. End with the test that would tell the options apart.
7. Save one File named `research/<title>.md`, first line `Node: <path>` (`files_set`); read it back and cite it on the task.

## Acceptance

- [ ] (fresh) a reader of the file alone can compare the options and name the test that would separate them

## Result

### Artifact refs

- file:<fileId>
- **Transition:** the research file is saved, read back and cited on its task
