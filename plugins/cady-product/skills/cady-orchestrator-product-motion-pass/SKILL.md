---
name: "cady-orchestrator-product-motion-pass"
description: "Orchestrate product. Use when: A due product pass, or an event: a release due, work in progress over its limit or results arriving. Not for: Building, designing or testing the work itself, or deciding product scope (the product agents do both)."
license: "MPL-2.0"
compatibility: "Requires Cady (app.cadyworks.com/mcp)"
metadata:
  cady-id: "skill.orchestrator_product.motion_pass"
  version: "68c62653af1108aed504"
  library: "4df067661df56e5b"
  function: "orchestrator_product"
---
# Orchestrate product

**Point:** Each pass, in-flight work is few, names what it will change, and returns its results to discovery.

**Company context:** `cady_read {"search": {"query": "<what you are about to do, in one sentence>"}}`

**Bets** (where this differs from the default):
- Limit work in progress and finish before starting. Instead of: Many half-built items in flight.

A due product pass, or an event: a release due, work in progress over its limit or results arriving.

**Not for:** Building, designing or testing the work itself, or deciding product scope (the product agents do both).

**Unit of work:** one pass over the company's product loop. **Kind:** execution. **Parallel:** no. 

## Inputs

### Evidence refs

- product goals and initiatives
- work in progress and its limit
- releases due and the latest results

### Work fields

- the product in scope
- the work in progress limit

## Procedure

1. Read the product goals and initiatives, the work in progress against its limit, the releases due and the latest results.
2. Check that each in-flight item names its learning goal or acceptance; an item that cannot say what it will change waits.
3. Cut each build to the smallest version a real user can judge, and hold new starts while work in progress is over its limit.
4. Gate each release on a story walk by a fresh user, not on merged work.
5. Read each release's results back into discovery before the next scope is set.
6. Read each result one level down with `cady-company-challenge`. Decide inside the family's node by its point and bets, and record each call on the lowest node both pieces of work serve. Hand a call that crosses families to the orchestrator and one that would change a point, bet or goal to the Executive, with both options and the evidence.
7. Report work in progress against its limit, items held and why, releases passed or held, and what was learned.

## Acceptance

- [ ] (check) work in progress is within its limit
- [ ] (check) every in-flight item names its learning goal or acceptance
- [ ] (check) no release closed without a story walk

## Owner checks

- a release closes only on a fresh user's walk
- results are read before the next scope

## Result

### Artifact refs

- company:work:<workId>
- **Transition:** one pass recorded as a finished run
