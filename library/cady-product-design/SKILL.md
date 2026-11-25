---
name: "cady-product-design"
description: "Design production. Use when: Produce design work (an interface, page, asset, motion piece or deck) and hand it on buildable. Not for: Judging taste (`cady-company-taste-review`), building it (engineering builds it) or an accessibility audit (`cady-devops-wcag-audit`)."
license: "MPL-2.0"
compatibility: "Requires Cady (app.cadyworks.com/mcp)"
metadata:
  cady-id: "skill.product.design"
  version: "50940a2e44df8a7f53bf"
  library: "bff495952413386a"
  function: "product"
---
# Design production

**Point:** Make the surface carry its job from trigger to result, so the work moves the decision it exists for.

**Company context:** `cady_start {"task": "<what you are about to do, in one sentence>"}`

**Bets** (where this differs from the default):
- For a material redesign, render about three meaningfully different directions in the real medium and compare them on the same flow. Instead of: Iterate on one direction, or offer palette swaps as the options.
- Judge concept and execution separately: is the idea surprising and right for this audience, then does the rendered result carry it. Instead of: Judge by legibility, restraint and a clean checklist.
- Start from the hardest user decision and the whole trigger-to-result journey, including empty, denied, failed and recovery states. Instead of: Start from the requested screen in its happy state.
- Show the real product where it exists: capture real screens from realistic state and compose around them, never redrawing or generating UI pixels; a new surface follows the standard pattern. Instead of: Mock up or generate a polished product image.
- Where the surface is not a buying reason, follow the standard pattern and the design system; spend bespoke craft where it wins customers. Instead of: Design every page bespoke so it looks distinctive everywhere.
- Work from the accepted design source in context; a draft is not a default, and accepted work updates that source. Instead of: Treat the latest draft as the company's design choices.

Produce design work (an interface, page, asset, motion piece or deck) and hand it on buildable.

**Not for:** Judging taste (`cady-company-taste-review`), building it (engineering builds it) or an accessibility audit (`cady-devops-wcag-audit`).

**Unit of work:** one surface and the journey it serves. **Kind:** execution. **Parallel:** no. 

## Inputs

### Evidence refs

- the decision and journey the work serves
- the node's bets and the accepted design source

## Procedure

1. Name the hardest customer decision and the journey from trigger to result, states included: empty, denied, failed and recovery.
2. Read the company's design choices first: the bets on the node and its parents, and the accepted design source in Files.
3. For a material redesign, render and compare the directions on one flow, then build the chosen one; a routine refinement needs none.
4. Capture real screens from realistic state and compose around them; keep the capture and its recipe in Files (`files_set`), cited as file:<fileId>.
5. Judge it with the taste check before handoff (`cady-company-taste-review`), then hand engineering the journey, states and design reference.
6. After accepted work, update the accepted design source in Files with what changed (`files_set`), then close the run as `references/run-reporting.md` says.

## Acceptance

- [ ] (check) the journey and its empty, denied, failed and recovery states are named
- [ ] (check) a material redesign compares about three rendered directions, or the direction was already set
- [ ] (fresh) judged with the taste check before handoff, concept and execution apart

## Result

### Artifact refs

- file:<fileId>
- company:work:<workId>
- **Transition:** engineering has the journey, states and design reference; the run closes with what was judged
