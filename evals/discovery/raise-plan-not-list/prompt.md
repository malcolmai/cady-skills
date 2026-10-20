---
name: raise-plan-not-list
description: "Amount and instrument are the raise plan; who to pitch is the investor list."
expected_outcome: "Loads cady-fundraise-raise-plan through the cady front door"
tags: [discovery, competing]
runs: 3
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---

Should we raise on a SAFE or do a priced seed round, and how much should we take?
