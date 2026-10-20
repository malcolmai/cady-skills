---
name: customer-renewal-usage-drop
description: "A customer's renewal of our product is customer success, not a review of our own vendor spend."
expected_outcome: "Loads cady-customer-success-lifecycle through the cady front door"
tags: [discovery, boundary]
runs: 3
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---

Brightline's annual subscription with us renews in 60 days and their usage dropped last month. What should we do?
