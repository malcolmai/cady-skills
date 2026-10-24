---
name: "cady-company-voice-pack"
description: "Build or refresh the sender's voice pack. Use when: A member has no voice pack, drafts read like the AI, or the pack is 90 days old or the sender rewrote 5 or more drafts since its last revision. Not for: Drafting a message (the channel skill reads the pack). Company brand voice for public posts (`cady-company-taste-review`)."
license: "MPL-2.0"
compatibility: "Requires Cady (app.cadyworks.com/mcp)"
metadata:
  cady-id: "skill.company.voice_pack"
  version: "75b3358abacf29c38858bfc278cf8194eac09f6292be9a4366dff234481217a2"
  library: "c4b98ee2d7bd8432"
  function: "company"
---
# Build or refresh the sender's voice pack

**Company context:** `get_cady_context({"area": "ops/records", "task": "<what you are about to do, in one sentence>", "knownMethods": {"skill.company.voice_pack": "75b3358abacf29c38858bfc278cf8194eac09f6292be9a4366dff234481217a2"}})`

A member has no voice pack, drafts read like the AI, or the pack is 90 days old or the sender rewrote 5 or more drafts since its last revision.

**Not for:** Drafting a message (the channel skill reads the pack). Company brand voice for public posts (`cady-company-taste-review`).

**Unit of work:** one member's pack. **Kind:** execution. **Parallel:** no. **Can release:** no. 

## Inputs

### Evidence refs

- voice:me
- the connectors the owner authorised for reading his own sent messages

## Procedure

1. Read voice:me and keep its revision; an existing pack is a candidate to improve, not truth. Read the owner's sent messages read-only and bounded through the connectors he authorised (wacli, LinkedIn conversations, Slack, email Sent). Prefer, in order: replies in threads with people he already knows, short logistics and decision messages, warm messages he started. Messages before 30 Nov 2022 count as organic. His own rewrites of agent drafts are for contrasts (step 5), not examples.
2. Exclude, and keep each reason for the audit: anything prepared through crm.prepare_outreach_review or released under a grant (an interaction with an approvalId, or text matching a review's or grant's copy); sequence, campaign or bulk sends; cold first touches since 2023 unless he says he typed them; the same text to several people; materials such as decks and posts; quoted or forwarded text.
3. Flag as possible AI, with the signals listed, any candidate with an em dash in a chat message, a stock opener or closer ("I hope this finds you well", "I'd love to", "quick chat", "happy to", "feel free to", "looking forward to hearing"), "I'm building X" before the ask, a group of three or "not X but Y", or two of: uniform sentence length with perfect punctuation in a chat, curly quotes in a channel where he types straight ones, trend words (delve, leverage, foster, crucial, seamless). The owner can reinstate any flagged message, and his verified pre-2023 habits win: if he used dashes then, a dash is his.
4. From a pool of 20 to 40 pick 5 to 8 for spread, not polish: at least 2 channels, at least 2 replies and 1 message he started, one very short and one longer, an ask and a no if any, at most 2 per thread, and each relationship stage he writes in (stranger, warm, ongoing) where his messages have it. Put the most typical email and the most typical chat message first, because the drafting summary shows only the first two for the channel. Paste each exactly as sent; never add or keep a typo to look human. Record origin organic and the stage (stranger: met once or never; warm: knows him, not in regular contact; ongoing: live thread), and a sourceRef he can reopen.
5. Describe how he writes by layer, in this order, each from what he actually does at that stage: (1) relationship: how he addresses a stranger, a warm contact and an ongoing thread; (2) reason: how he says why this person and why now (a first message must carry one specific true reason); (3) substance: how he states what is happening, plain, no positioning lines; (4) ask: how he sizes it (stranger: light and easy to decline; warm: direct, with a time); (5) texture last and conditional on stage and channel: length, greeting, sign-off, punctuation, casing. Lowercase starts belong only to a very short, very casual reply; typos and quirks are situational, never the voice, and drafts need not copy them. Use counts and verbatim fragments, plain words, the 300 most decisive characters first (the drafting summary clips there). Then write 2 or 3 contrasts that each show one subtle layer difference between too-AI, natural and too-casual or spammy, not caricatures: draft the message for a chosen example's situation without the pack, set it beside what he sent (draft, sent, one line naming the layer that differs); an owner rewrite of an agent draft goes in the same way. Turn the clearest differences and anything he rejected into up to 8 avoid lines as quoted phrases or named marks, covering AI tells ("I'd love to", em dash) and spam tells ("no ask without a reason in a first message", "no direct call ask to a stranger"). Add personalisation rules only for signals he states or shows in the organic set; invent none.
6. Audit with him before saving, in the chat or a Cady file: each chosen example verbatim with channel, date, relationship, sourceRef and why chosen; the excluded candidates grouped by reason (reviewed or approved copy, template, possible AI with signals, off-voice) so he can reinstate any; the counts and description; the contrasts and avoid lines; and two unlabelled drafts of one real upcoming message, with and without the pack, for him to pick and edit. Save with crm.manage_voice_pack only after he approves (expectedRevision from step 1; origin owner_rewrite for any example he mostly rewrote, stage on every example). Act on the warnings the save returns: replace a flagged example with a message he typed. Read voice:me back and report the revision and digest.

## Acceptance

- [ ] no example is prepared, reviewed, sequenced or templated copy, and the save returned no review-match warning (or the owner knowingly kept the example)
- [ ] every example has a sourceRef he can reopen
- [ ] the description is written by layer (relationship, reason, substance, ask, texture last) with counts and verbatim habits, not adjectives or typo mimicry
- [ ] the audit listed chosen and excluded messages with reasons and stats
- [ ] voice:me readback matches the saved revision
- [ ] every example carries its relationship stage

## Owner checks

- the owner approved the exact pack before the write
- voice:me readback matches the saved revision and digest

## Result

### Artifact refs

- voice:me
- **Transition:** the claim holder reports the result
