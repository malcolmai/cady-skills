## Selection

| Mode | When |
|---|---|
| script | Known steps and deterministic rules; no LLM needed. |
| fixed_llm_pipeline | Known stages with bounded model calls or map/batch work; choose stage boundaries by distinct judgment and handoff, not an arbitrary call count. Validate output schemas; code owns branching, tools and effects. |
| agent | The work needs adaptive planning, tool selection or investigation. Bound tool scope and escalation by the outcome and actual host/provider limits. |
