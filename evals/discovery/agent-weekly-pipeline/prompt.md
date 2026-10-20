---
name: agent-weekly-pipeline
description: "Creating and scheduling a company agent is agent management; loading the pipeline pass it will run is also a defensible route."
expected_outcome: "Loads cady-company-manage-agents or cady-gtm-pipeline-pass through the cady front door"
tags: [discovery, positive]
runs: 3
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---

Set up an agent that reviews our sales pipeline every Monday morning.
