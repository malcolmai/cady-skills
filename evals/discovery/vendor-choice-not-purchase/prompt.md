---
name: vendor-choice-not-purchase
description: "Choosing which connector to integrate is the integration vendor choice; spend review follows only if it costs money."
expected_outcome: "Loads cady-engineering-integrations through the cady front door"
tags: [discovery, competing]
runs: 3
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---

Compare Clay and Apollo as the enrichment source we connect our CRM to, and pick one.
