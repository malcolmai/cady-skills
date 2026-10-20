## Inputs

### Authority

- verified member credential
- host identity from the current Cady connection
- omit decisionId and nonce (the server fills them) unless retrying an exact call
- expectedRevision null for a new agent or run, or the current revision for a change
- current targetAgentId for changes

### Design

- agent name and function
- one goal
- risk class (critical or standard)
- measure and its data
- cadence or trigger, with why
- approval limits
- tool pack
- owner member
- first task, its checks and evaluation criteria
- end or escalation condition
