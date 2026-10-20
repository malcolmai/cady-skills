---
name: checkout-down-postmortem
description: "A live outage and its blameless review are the incident part of debugging, phrased without the word debug."
expected_outcome: "Loads cady-engineering-debugging through the cady front door"
tags: [discovery, positive]
runs: 3
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---

Checkout is down for customers. Run the incident and write the postmortem.
