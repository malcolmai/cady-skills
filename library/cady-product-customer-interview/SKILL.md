---
name: "cady-product-customer-interview"
description: "Customer discovery interviews. Use when: Plan, run and synthesise customer discovery interviews about past behaviour, without leading questions. Not for: Choosing which question needs evidence or its research route (use `cady-company-decision-questions`), competitor research (use `cady-product-research-competition`) or a sales call (use `cady-gtm-calls`)."
license: "MPL-2.0"
compatibility: "Requires Cady (app.cadyworks.com/mcp)"
metadata:
  cady-id: "skill.product.customer_interview"
  version: "ff407633c3e3c84dc4246cf1116f52915163326074ec7481dd5cfacbaedabeea"
  library: "f1d2ef4c2e226957"
  function: "product"
---
# Customer discovery interviews

**Company context:** `get_cady_context({"area": "product/<productId>/scope", "task": "<what you are about to do, in one sentence>", "knownMethods": {"skill.product.customer_interview": "ff407633c3e3c84dc4246cf1116f52915163326074ec7481dd5cfacbaedabeea"}})`

Plan, run and synthesise customer discovery interviews about past behaviour, without leading questions.

**Not for:** Choosing which question needs evidence or its research route (use `cady-company-decision-questions`), competitor research (use `cady-product-research-competition`) or a sales call (use `cady-gtm-calls`).

**Unit of work:** one interview round for one question or hypothesis. **Kind:** strategy. **Parallel:** no. **Can release:** no. 

## Inputs

### Evidence refs

- the question:<slug> or hypothesis:<slug> decision item it serves
- crm:party:<partyId> for each interviewee

## Procedure

1. Start from the decision. Name the question or hypothesis item it serves (`cady-company-decision-questions`) and write the two or three things you must learn and which answers would change the decision. Without that, do not schedule interviews.
2. Recruit people who had the problem recently and acted on it, not friends, fans or people who only fit a profile. Five to eight per segment usually show the pattern; stop when new interviews stop changing it. Requests to talk are outreach: an engaged contact through `cady-gtm-warm-email`, a LinkedIn connection through `cady-gtm-linkedin-message`, an introduction as `../../references/intro-request.md` says, and a cold person only in a cold cycle whose template is a plain research ask (the topic, about 20 minutes, no pitch).
3. Ask about specific past behaviour. 'Tell me about the last time you...', 'What did you do next?', 'What did you try before that?', 'What did it cost you in time or money?', 'Who else was involved?', 'Why then?'. Ask to be shown the spreadsheet, workaround or tool they use. Let silences run.
4. Do not ask hypotheticals ('would you use', 'would you pay'), leading questions ('isn't X frustrating?'), yes or no questions, or for their solution. Do not pitch: describing your idea turns the rest of the interview into politeness. Spend the interview mostly listening.
5. Steer away from bad data. A compliment carries no information; move on. A generalisation ('I always', 'usually') gets 'when was the last time?'. A feature request gets 'what would that let you do?' and 'how do you handle it today?'. An opinion on price is tested by behaviour, never taken as demand.
6. End with a real commitment that costs them something: a follow-up session, an introduction to the person who owns the budget, sample data, a pilot or a pre-payment. Record whether they accepted, declined or deflected; that is the strongest signal in the interview.
7. Conduct: a person runs the live interview; the agent prepares the guide, recruits through approved channels and synthesises, and runs an interview itself only in an async or written format the participant agreed to. Say who is asking, ask consent before recording and keep notes within the hour. Mark verbatim quotes as quotes and keep observed behaviour separate from your interpretation.
8. One File per interview (files.upload): date, role and context, the last real instance, current workaround and what it costs, quotes, and the commitment outcome; cite crm:party:<partyId>.
9. Synthesise across interviews: count each pattern as n of m rather than citing the most vivid story, keep the disconfirming cases and state your confidence. Update the question or hypothesis item with the File refs. Interest, enthusiasm or 'I would buy that' is not validation; a repeated costly workaround or an accepted commitment is evidence.

## Acceptance

- [ ] each interview records a real recent instance and a commitment outcome
- [ ] the synthesis counts patterns and names disconfirming evidence
- [ ] the question or hypothesis item is updated with evidence refs

## Owner checks

- every interview traces to a recorded question or hypothesis
- questions are about past behaviour, with no pitch or hypotheticals
- notes are Files cited from the item, quotes marked

## Result

### Artifact refs

- company:work:<workId>
- file:<fileId>
- **Transition:** the decision owner reads the synthesis against the question it serves

## References
- [Introduction request](../../references/intro-request.md)
