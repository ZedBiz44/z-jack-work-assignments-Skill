# Notion destinations and field mapping

Verified 2026-10-18. Fetch live schemas before writes; these identifiers locate records but do not grant access.

## Jack-Work

- Database: https://app.notion.com/p/3bea3e33d58180989d15ec73375f412e
- Data source: `3bea3e33-d581-8014-af33-000bd1c27569`
- Title: `Name`; progress: `Update Notes`; state: `Status` (Not started, In progress, Done).
- Reciprocal relation: `AI Conversations` to AI-Agent-Convo.
- Preserve `Priority`, `Revenue Rating`, `GrowthRating`, `Overall Rating`, parent/sub-item relations, existing links and other unrelated properties.
- Known owner, objective, next action and finish condition belong in page content when no matching property exists. Do not create extra fields just for this skill.

## AI-Agent-Convo

- Database: https://app.notion.com/p/2c585f2f9e3542ec812c91a0f375320d
- Data source: `af9d6b1f-e527-4d6f-b519-351ba657292f`
- `Conversation / Topic`: title.
- `Jack-Work Assignment`: multi-page relation to Jack-Work; preserve existing members.
- `AI Agents`: multi-select. Use actual agent names supported by the current schema; otherwise Other plus exact name in title/body.
- `Platform`: select. Use the actual platform supported by the current schema; otherwise Other plus exact platform in body.
- `Chat / Thread Link`: URL. A missing link does not prevent creating the rest of the record.
- `Date Last Active`: date, using America/Edmonton for date-only entries.
- `Status`: Active, Waiting, Completed, Archived.
- `Role`: Primary or Supporting, according to the discussion's actual role; leave unset if unknown.
- `Key Findings / Decisions`: short current summary, supported by preserved milestone notes where needed.
- `Next Action`: clear action and owner when known.
- `Created` is system-managed; do not write it.

## Related workflow sources

- Starting page: https://app.notion.com/p/5d7a3e33d58183b5a58401a78eff8d70
- Assignment Process Planning: https://app.notion.com/p/3e5a3e33d58180ba9cd5d9523798f83d
- System design and acceptance assignment: https://app.notion.com/p/3fda3e33d581819781e7ca356014f76f
- Maintained SOP: https://app.notion.com/p/3fda3e33d58180429d8eff45699578fd

Read relevant live sources; do not automatically rewrite the morning summary, launch a review, or change Asana records. Conversation logging supports those workflows without taking over their owners' responsibilities.

## Connector mechanics

Use the current tool's schema. Native Notion connectors may accept relation URL arrays and expanded date keys such as `date:Date Last Active:start`; REST clients use their own typed property objects. Never copy one connector's payload into another without checking.

Search by assignment and identity as well as URL. Continuous-chat records are assignment-specific. Preserve page IDs for later updates and check returned content after every milestone save.
