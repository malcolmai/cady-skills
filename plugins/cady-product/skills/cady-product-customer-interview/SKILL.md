---
name: "cady-product-customer-interview"
description: "Customer discovery interviews. Use when: Plan, run and synthesise customer discovery interviews about past behaviour, without leading questions. Not for: Choosing which question needs evidence or its research route (use `cady-company-decision-questions`), competitor research (use `cady-product-research`) or a sales call (use `cady-gtm-calls`)."
license: "MPL-2.0"
compatibility: "Requires Cady (app.cadyworks.com/mcp)"
metadata:
  cady-id: "skill.product.customer_interview"
  version: "1cece4fd89594e1e874d"
  library: "921dfb8c2c658fd5"
  function: "product"
---
# Customer discovery interviews

**Point:** Learn what customers actually did and paid, not what they say they would, so product decisions rest on behaviour.

**Company context:** `cady_read {"search": {"query": "<what you are about to do, in one sentence>"}}`

**Bets** (where this differs from the default):
- Ask only about specific past instances: the last time it happened, what they did next and what it cost. Instead of: Ask whether they would use or pay for the idea and what they think of the concept.
- Keep the idea out of the interview; describe the product only afterwards, if at all. Instead of: Describe the product early to get reactions and feedback.
- Close by asking for a commitment that costs them something, and treat acceptance as the strongest signal of the interview. Instead of: Treat enthusiasm or 'I would buy that' as validation.
- Recruit people who had the problem recently and acted on it; stop when new interviews stop changing the pattern. Instead of: Interview whoever is reachable, friends and fans included, up to a fixed count.
- Count each pattern as n of m and keep the disconfirming cases in the synthesis. Instead of: Lead with the most vivid story as the finding.

Plan, run and synthesise customer discovery interviews about past behaviour, without leading questions.

**Not for:** Choosing which question needs evidence or its research route (use `cady-company-decision-questions`), competitor research (use `cady-product-research`) or a sales call (use `cady-gtm-calls`).

**Unit of work:** one interview round for one question or assumption. **Kind:** strategy. **Parallel:** no. 

## Inputs

### Evidence refs

- the question task or hypothesis bet it serves
- crm:party:<partyId> for each interviewee
- file:<fileId> discussion guide

## Procedure

1. Start from the decision. Name the question or assumption item it serves (`cady-company-decision-questions`) and write the two or three things you must learn and which answers would change the decision. Without that, do not schedule interviews.
2. Recruit people who had the problem recently and acted on it, not friends, fans or people who only fit a profile. Five to eight per segment usually show the pattern; stop when new interviews stop changing it. Requests to talk are outreach: an engaged contact through `cady-gtm-warm-email`, a LinkedIn connection through `cady-gtm-linkedin-message`, an introduction as `../../references/intro-request.md` says, and a cold person only in a cold cycle whose template is a plain research ask (the topic, about 20 minutes, no pitch). Once the requests are held for review, record one ask of kind call for whoever will take the interviews (question: hold N x 20 minutes; readyRefs: the guide File and the review id); in chat too, because the times arrive after this session. Booking a call with a person is an ask of kind call; messaging them is an outreach review. Do not hold an Executive work item for booking.
3. Ask about specific past behaviour. 'Tell me about the last time you...', 'What did you do next?', 'What did you try before that?', 'What did it cost you in time or money?', 'Who else was involved?', 'Why then?'. Ask to be shown the spreadsheet, workaround or tool they use. Let silences run.
4. Do not ask hypotheticals ('would you use', 'would you pay'), leading questions ('isn't X frustrating?'), yes or no questions, or for their solution. Do not pitch: describing your idea turns the rest of the interview into politeness. Spend the interview mostly listening.
5. Steer away from bad data. A compliment carries no information; move on. A generalisation ('I always', 'usually') gets 'when was the last time?'. A feature request gets 'what would that let you do?' and 'how do you handle it today?'. An opinion on price is tested by behaviour, never taken as demand.
6. End with a real commitment that costs them something: a follow-up session, an introduction to the person who owns the budget, sample data, a pilot or a pre-payment. Record whether they accepted, declined or deflected; that is the strongest signal in the interview.
7. Conduct: a person runs the live interview; the agent prepares the guide, recruits through approved channels and synthesises, and runs an interview itself only in an async or written format the participant agreed to. Say who is asking, ask consent before recording and keep notes within the hour. Mark verbatim quotes as quotes and keep observed behaviour separate from your interpretation.
8. One File per interview (files_set): date, role and context, the last real instance, current workaround and what it costs, quotes, and the commitment outcome; cite crm:party:<partyId>.
9. Synthesise across interviews: count each pattern as n of m rather than citing the most vivid story, keep the disconfirming cases and state your confidence. Update the question or assumption item with the File refs, and add their verbatim phrases to the persona's profile (`cady-gtm-persona-profile`). For a phrase to be citable in copy, the person marks the exact words on the call note in Cady (crm:words). Interest, enthusiasm or 'I would buy that' is not validation; a repeated costly workaround or an accepted commitment is evidence.

## Acceptance

- [ ] each interview records a real recent instance and a commitment outcome
- [ ] the synthesis counts patterns and names disconfirming evidence
- [ ] the question or assumption item is updated with evidence refs

## Owner checks

- every interview traces to a recorded question or assumption
- questions are about past behaviour, with no pitch or hypotheticals
- notes are Files cited from the item, quotes marked

## Result

### Artifact refs

- company:work:<workId>
- file:<fileId>
- **Transition:** the decision owner reads the synthesis against the question it serves

## References
- Read [Introduction request](../../references/intro-request.md) when you recruit through an introduction.
