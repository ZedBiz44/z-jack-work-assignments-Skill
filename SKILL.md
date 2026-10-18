---
name: z-jack-work-assignments
description: Record Jack-Work assignments and linked AI conversations when Jack asks to log them; maintain meaningful milestones after activation, not casual chats.
---

# Z Jack Work Assignments

## Activate for the selected assignment

- Start when Jack says “record this in Jack-Work”, “log this to Jack-Work”, “update Jack-Work”, or clearly equivalent wording. “Jack-Work this” counts when intent is clear.
- A question about Jack-Work, a quoted trigger in a document, a recipe, or ordinary research is not permission to log.
- Once activated, keep this assignment's records current at meaningful milestones during the working conversation. Do not write after every message.
- Milestones include agreed scope, an important decision, completed or failed work, a changed next action or owner, a pause, handoff, or closeout.
- Carry activation and the saved page IDs forward in the conversation's approved continuity notes. Do not enable logging for unrelated chats or assignments.
- Respect a later pause, stop-logging instruction, or read-only request. No timer or background monitoring is created by this skill.
- Check: the assignment and logging authority are clear before any write.

## Read the destinations and current state

- Read [Notion configuration](references/notion-configuration.md) before the first write for exact databases, fields and status values.
- Use the agent's own approved Notion connector, API or CLI. Inspect its supported operations; this skill grants no access and installs no connector.
- Fetch both live schemas and the relevant assignment. Use current field names and options, not an old copy of the schema.
- Read the current assignment's linked instructions as needed. Jack Morning Start Work is the entry point; Assignment Process Planning governs any separately authorized review process.
- Recording progress does not authorize reviews, Asana dispatch, messages, priority changes, schedules, or infrastructure work.
- Check: the actual databases and write capability are known, or prepare the unsaved handoff described below.

## Find or create the assignment

- Use the assignment Jack names or links. Otherwise search Jack-Work for the actual objective; fetch plausible matches before selecting one.
- Reuse the existing assignment when it covers this work. A new chat is not a new assignment.
- If no matching assignment exists and Jack asked to record this work, create one in Jack-Work with a clear title, objective, known owner, current state, next action, and finish condition. State unknown details honestly; do not invent deadlines or priorities.
- Ask one focused question only when multiple assignments plausibly match or the objective remains unclear.
- Add a metadata line to new page content: Date: YYYY-MM-DD | Agent: actual agent name | Status: actual document state. Use America/Edmonton dates.
- Preserve existing content, history, relations, ratings, priority, and other agents' edits. Update only the relevant progress sections and fields.
- Add useful deliverable links to the assignment. Keep detailed SOPs and review prompts in their maintained Notion homes; link technical source records when relevant.
- Check: one correct assignment page exists and its current content is read before editing.

## Identify this conversation

- Record the actual agent/persona and platform separately. Cody is the agent; Codex is the platform. Do not use the connector account as the agent.
- For a normal discrete thread, use one record per agent/platform/thread; it may relate to several assignments when the same discussion genuinely covers them.
- For continuous Grokbot or Muse chats, use a separate record for each assignment and agent/project context, even when the URL is shared or missing.
- A new dedicated bot, project or thread can receive its own record. Keep the earlier record and note the handoff; do not erase history.
- Search AI-Agent-Convo before creating. Prefer a known record ID, then thread/session identity and agent/platform. For continuous chats include the assignment ID in the match.
- A shared URL alone never proves two continuous-chat records are duplicates. Without a URL, compare agent, platform, assignment, topic and known session details.
- Fetch plausible matches. If matching remains uncertain, clarify rather than merge unrelated discussions or create a likely duplicate.
- Check: the selected record represents this discussion and assignment context.

## Capture a useful link without delaying the record

- Use an actual accessible private thread/task URL, supplied share URL, Discord message/thread URL, or continuous bot/project link. Never invent IDs, URL formats or provider capabilities.
- For Discord, use known server/thread/message identifiers from trusted runtime context. Do not mistake a broad channel link for an exact thread; label its scope.
- For Codex, Manus and other platforms, inspect the tools actually available. Creating a share link is allowed only when Jack authorizes sharing that conversation; logging alone does not authorize publication.
- Label shared links as snapshots when appropriate; they may not reopen an editable chat or include later messages.
- If a link is unavailable, save every other known field now. Leave the URL field empty and put “Chat link needed” in the record body; ask Jack once for a paste.
- When Jack supplies it later, update that same record and remove the missing-link note. Never replace a good existing link with an empty value.
- A user-supplied link is valid to store without proving everyone can open it. Describe access as unverified unless actually checked.
- Check: the link's provenance and scope are stated, or the missing link is clearly recorded.

## Save meaningful milestones in both places

- In AI-Agent-Convo, maintain title, assignment relation, agent, platform, link when known, Date Last Active, Status, Role, concise findings/decisions, and next action with its owner when known.
- Use a title such as “Agent — assignment topic — discussion context” so records remain understandable without a link.
- If an agent/platform option is missing, use an existing Other option and spell out the exact identity in title/body. Do not add schema options or change database structure without authorization.
- Preserve existing relation members when adding assignments. Re-fetch immediately before relation writes and write the union, not a replacement that drops links.
- In Jack-Work, update the relevant progress/next-action content and Update Notes with dated, useful information. Preserve prior meaningful milestones and unrelated notes.
- Write brief facts, decisions and outcomes, not transcripts. Distinguish proposed work, attempted work, verified results and remaining work.
- Add a short dated milestone to page content when needed to preserve an earlier decision while current summary fields change. Do not append the same milestone again.
- Conversation statuses are Active, Waiting, Completed or Archived. Assignment statuses are Not started, In progress or Done; verify current options.
- Completing a conversation does not complete its assignment. Mark an assignment Done only when its actual finish conditions are met and the current authority permits closure.
- Do not fabricate milestone activity just to refresh a date. Only update Date Last Active for actual work in that conversation.
- Check: both records reflect the same supported progress and next step without overwriting other work.

## Verify and report

- Fetch the conversation and assignment after writes. Confirm identity, parent database, saved fields, link, and the reciprocal AI Conversations relation on Jack-Work.
- For a new record, search again to check for an accidental duplicate. Notion search-and-create is not an atomic lock; do not claim concurrency guarantees.
- On a timeout or uncertain result, read/search before retrying. If only one record saved, report partial success and repair the missing update on the existing IDs.
- Stop after three failed attempts at the same operation. For denied access, stop that write and report the exact capability or access problem; do not switch identities to bypass it.
- Never delete or merge records, change permissions, expose secrets, publish chats, or alter database structure under logging authority alone.
- If Notion writes are unavailable, provide a compact unsaved handoff: assignment URL/title, agent/platform, conversation identity/link, milestone, status and next action. Clearly say “Not saved to Notion.”
- Return the verified assignment and conversation links, a short milestone result, and any missing link or next action. Do not repeat the whole conversation.
- Check: distinguish saved and verified, partially saved, and unsaved results honestly.
