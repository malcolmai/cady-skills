---
name: cold-deliverability-bounces
description: "Bounce and spam thresholds and the pause they trigger belong to the cold email cycle."
expected_outcome: "Loads cady-gtm-cold-email-cycle through the cady front door"
tags: [discovery, competing]
runs: 3
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---

Our cold emails started bouncing at 6% and Gmail is putting the rest in spam. What do we do before the next batch?
