# Reporting a run

- **Evaluation:** offline_evaluation and spotcheck require non-null requestId, scenarioId and repetition, the Projects-derived runId for that configuration, and no slotStartAt or effect receiptIds. Preserve actual assessable output or outputRef, not only a summary. Independent assessment remains separate from producer claims.

## Example

```json
{
  "expectedRevision": null,
  "run": {
    "finishedAt": 2,
    "outcome": "completed",
    "provenance": {
      "configurationRef": "agent-history:<current-history-id>",
      "output": "Actions: Checked the assigned records; corrected two discrepancies. Output: Saved the corrected owner artifact. Evidence: file:<id>. Next: Recheck after the next source update.",
      "outputRef": null,
      "purpose": "ordinary",
      "repetition": null,
      "requestId": null,
      "scenarioId": null,
      "traceRefs": [],
      "usage": {
        "costUsd": null,
        "denominator": "attempt",
        "durationMs": null,
        "source": null,
        "toolCalls": null
      }
    },
    "slotStartAt": 1,
    "startedAt": 1
  },
  "targetAgentId": "aaaaaaaa-aaaa-4aaa-8aaa-aaaaaaaaaaaa"
}
```
- **Metrics:** Use measured values with usage.source; otherwise all unavailable measurements and source are null. Zero means observed zero. denominator is attempt. Compare total cost including helpers and rework per independently accepted useful result, alongside quality, missed defects and needless escalations; run completion alone is not success.
- **Output:** Lead with actions and the useful output or result, cite owner evidence, then state the next step or exact blocker. Keep ordinary reports short; outputRef can point to the full owner artifact. File only what someone will open again to use or check: a deliverable, or source evidence no owner record holds; cut process notes, logs of your own steps and restatements instead of filing them. Make a review packet only when the owner must approve a set of exact materials together (for example the copy for a send); otherwise a memo does it. A memo goes only when the reader must do, decide or know something now, and its first line says which; it links the deliverables where they live and never repeats the run result, which the work record already stores. Do not upload local transcript bodies or repeat company context. Local transcript review diagnoses retries, waste, missed instructions, tool misuse and behavior; persist only the material finding, evidence reference and correction in the existing owner.
- **Shape:** An ordinary run is recorded by the run part of the step 6 close_company_work call (it forwards to manage_company_agent mode='record_run'); do not also record it there. Close derives slotStartAt and decisionsMade and stamps each skill's served version; name skills as skill.<name>. Call manage_company_agent (through call_cady_tool if not listed) with mode='record_run' directly only for offline_evaluation or spotcheck, with the example's arguments. The example uses synthetic identifiers and times: replace them with this agent, the current run identity and observed facts. Keep run facts nested. provenance is optional; if supplied, every shown provenance field is required, including nullable fields and usage.
