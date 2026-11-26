---
name: "cady-product-map"
description: "Product map. Use when: Generate, restructure, clean up, check or publish a product map or a dimension map, for existing or new products. Not for: Deciding what to build and in what order (the product manager card), or building a task against the map (the engineering card)."
license: "MPL-2.0"
compatibility: "Requires Cady (app.cadyworks.com/mcp)"
metadata:
  cady-id: "skill.product.map"
  version: "c157723a026a122b7708"
  library: "4b5392d43606292b"
  function: "product"
---
# Product map

**Point:** Give people and agents one short, top-down map of a product: its point, its decisions and where a change goes.

**Company context:** `cady_start {"task": "<what you are about to do, in one sentence>"}`

Generate, restructure, clean up, check or publish a product map or a dimension map, for existing or new products.

**Not for:** Deciding what to build and in what order (the product manager card), or building a task against the map (the engineering card).

**Unit of work:** one product's map, or one dimension map, and the change that lands it. **Kind:** execution. **Parallel:** no. 

## Inputs

### Evidence refs

- the product's node path and its current map, if any
- the repository, or for a new product the brief and its research

## Procedure

1. Read the product map method (`references/product-map.md`) in full: it holds the format, the steps, the tool and the checks.
2. Read the map with `cady_read {view: "product.map"}`; to change it, find its File (`files_read` mode find: `<product node path>/product-map.json`). Update it where it is edited; never start a second.
3. Follow the method's build steps. Every bet keeps its origin (owner, inferred or proposed); a missing decision is a question to the owner (`todos_set`), never a written decision.
4. Run the map's check until it passes, then publish the packet as the method's Drafting part says.
5. In the change, list what clean-up removed, what now points at the map and what was kept.

## Acceptance

- [ ] (check) `render_map.py --check` passes on the map's source
- [ ] (fresh) on first generation or a format change, blind use ran, or the change says it was not run

## Result

### Artifact refs

- file:<fileId>
- **Transition:** the map's change is reviewed, then the map is published

## References
- Read [Dimension register and research](references/engineering-cycle-dimensions.md) when you name or label a product's Interface, Infrastructure or QA subjects.
- Read [Product map and dimension maps](references/product-map.md) when you generate, restructure, clean up, check or publish a product map or a dimension map.
