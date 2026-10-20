---
name: pipeline-pass-not-deal
description: "A pass over many due tracks is the pipeline pass, not one deal worked in depth."
expected_outcome: "Loads cady-gtm-pipeline-pass through the cady front door"
tags: [discovery, boundary]
runs: 3
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---

Go through every customer track that is due this week and set the next action on each.
