---
name: "cady-product-map"
description: "Product map. Use when: Generate, restructure, clean up, check or publish a product map or a dimension map, for existing or new products. Not for: Deciding what to build and for whom (`cady-product-manage`) or running the engineering cycle on a map (`cady-engineering-system-cycle`)."
license: "MPL-2.0"
compatibility: "Requires Cady (app.cadyworks.com/mcp)"
metadata:
  cady-id: "skill.product.map"
  version: "f5121183cc4d83b9955e"
  library: "60dff102dc062caf"
  function: "product"
---
# Product map

**Point:** Give people and agents one short, top-down map of a product: its point, its decisions and where a change goes.

**Company context:** `cady_start {"task": "<what you are about to do, in one sentence>"}`

Generate, restructure, clean up, check or publish a product map or a dimension map, for existing or new products.

**Not for:** Deciding what to build and for whom (`cady-product-manage`) or running the engineering cycle on a map (`cady-engineering-system-cycle`).

**Unit of work:** one product's map, or one dimension map, and the change that lands it. **Kind:** execution. **Parallel:** no. 

## Inputs

### Evidence refs

- the product's node path and its current map, if any
- the repository, or for a new product the brief and its research
- the tracker or roadmap, if any

## Procedure

1. Read the product map method (`references/product-map.md`) in full before you start: it holds the format, the steps, the tool and the checks.
2. Find the map as its Drafting part says (files_read mode find), then follow its Build steps in order. A dimension map follows its Dimension maps part and is saved with files_set.

## Acceptance

- [ ] (check) `render_map.py --check` passes on the map's source
- [ ] the map's change lists what clean-up removed, what now points at the map and what was kept, and the reorganisation change lists what it moved and what it left as items, or each says there was nothing to do
- [ ] on first generation or a format change, blind use ran, or the change says it was not run

## Owner checks

- each bet keeps its origin; a missing decision is an owner question, never a written decision

## Result

### Artifact refs

- file:<fileId>
- **Transition:** the map's change lands through the project's review, then the map is published

## References
- Read [Product map and dimension maps](references/product-map.md) when you generate, restructure, clean up, check or publish a product map or a dimension map.
