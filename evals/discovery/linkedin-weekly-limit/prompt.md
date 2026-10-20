---
name: linkedin-weekly-limit
description: "A LinkedIn limit notice is the stop rule in the LinkedIn message skill."
expected_outcome: "Loads cady-gtm-linkedin-message through the cady front door"
tags: [discovery, positive]
runs: 3
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---

LinkedIn just showed me a weekly invitation limit warning halfway through the connection requests. Carry on with the rest of the list.
