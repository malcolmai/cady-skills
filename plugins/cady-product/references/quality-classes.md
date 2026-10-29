# Software quality classes

- **Guide:** | Family | Class | The question | Boundary |
|---|---|---|---|
| Trust | QC1 Identity and session lifecycle | Does "who is calling" stay true across renewal, revocation, devices, versions and client types? | Establishing and keeping who; what they may do is QC2. |
| | QC2 Authority and isolation | May this caller do or see this, including getting too little access? | Includes a policy the system fails to enforce. Benign misuse of a permitted action is QC5. |
| | QC3 Privacy, data governance and compliance | What reaches an allowed recipient through outputs, logs or derived data? Which retention, deletion and residency duties apply? | Content exposure; access itself is QC2. |
| | QC4 Hostile input and abuse | What does a hostile caller do with volume, spoofing or injected text? | Hostile intent; a well-meaning agent getting it wrong is QC5. |
| | QC5 Agent safety and judgment | Does a well-meaning agent do the right thing within its authority, and keep doing so across models and hosts? | The system permitted it; if the system should have refused, it is QC2. |
| Operation | QC6 Performance and cost | What does it cost in time, resources and money under current and credibly expected load? | Cost; the agent needing more turns to finish is QC16. |
| | QC7 Concurrency, retry and partial failure | What happens if one operation runs twice, races or dies halfway? | One operation; losing a whole component is QC8. |
| | QC8 Availability and recovery | What happens when a region, database or provider is lost, and can we restore it? | Whole-component loss. |
| | QC9 Observability and incident response | Will we see it break, and who acts? | Seeing and acting; the failure itself has its own class. |
| | QC10 Parity across routes, environments and versions | Does it hold on every route, client, region and runtime version? | Behaviour differs by variant. A generated file left stale is QC15. |
| | QC11 Dependencies and supply chain | What do we inherit from vendors, libraries and licences, and what happens if one changes? | External code and services. |
| Coherence | QC12 Data semantics | Do numbers, units, windows and history mean what they claim? | Meaning of values. |
| | QC13 Loop closure and state lifecycle | Does every record have a reader and a closer, can every valid transition happen, and do linked records stay consistent? | Lifecycle; two writers of one fact is QC14. |
| | QC14 Ownership, duplication and layer | Is this the one writer and home, at the lowest layer that can carry it? | Design of homes. |
| | QC15 Change propagation | Did every consumer update: generated files, migrations, renames, tests, docs? | Process of updating consumers. |
| Understanding | QC16 Agent usability | Can an agent find the right call first, call it, recover and continue? | Agent audience. |
| | QC17 Human usability and truthfulness | Can a person read the true state and consequence, and act, at every width and with assistive tools? | Human audience. |

Place a whole-outcome failure under the journey. Other findings go to the class of their root cause, using the boundary sentences. If two classes still apply, use the lower-numbered class. A finding that moves cost between resources is judged under QC6 as a whole.

For owner boundaries and active or folded owners, use `cady-engineering-system-cycle` step 3.

| Change touches | Default classes |
|---|---|
| sign-in, sessions, keys, OAuth | QC1, QC2, QC7, QC10 |
| a permission, approval or effect | QC2, QC5, QC7, QC13 |
| a page or read path | QC6, QC17, QC2 |
| a tool, refusal or method text | QC16, QC14, QC5 |
| a new record or state | QC13, QC14, QC12 |
| schema, migration or export | QC12, QC15, QC8 |
| an external provider or route | QC10, QC11, QC7, QC4 |
| release, config, deploy | QC15, QC9, QC8 |

For bug-fix planning, use `cady-engineering-system-cycle` step 5.

Measures are proxies and evidence, never targets; budgets set by us stay flags, while external hard limits remain hard: choose the correct, proper solution even when it misses a number. A release threshold may cite a differentiating class measure as evidence; judge a miss against the scenario. Decision concerns map outcome_workflow to journeys, authority_security_privacy to Trust, data_performance_reliability to Operation, architecture_maintainability to Coherence and interface_accessibility to Understanding.
