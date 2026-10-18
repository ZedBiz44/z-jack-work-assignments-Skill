# Z Jack Work Assignments

This repository contains ZedBiz's Operational skill for selected Jack-Work assignments and related AI-Agent-Convo records. `SKILL.md` is the authoritative runtime source.

## When to use

Use when Jack explicitly asks an agent to record work in Jack-Work. Continue at meaningful milestones for that assignment. Continuous Grokbot/Muse discussions receive separate records per assignment, even without chat links.

## Do not use

Do not use for casual chats, recipes, quoted triggers, or read-only questions about Jack-Work. Logging grants no authority to dispatch work, change schemas, publish chats or alter permissions. Never include secrets or raw transcripts.

## Source and SOP

Publisher: ZedBiz. Adapted from Z3's user-supplied `skill.zip` containing `jack-work-conversation-logger`, supplied by Jack for this build. No third-party code or license grant is introduced; distribution is for the authorized ZedBiz agents.

The maintained human SOP is [in Notion](https://app.notion.com/p/3fda3e33d58180429d8eff45699578fd). Implementation and pilot evidence: [issue 1](https://github.com/ZedBiz44/z-jack-work-assignments-Skill/issues/1).

## Validate and package

Run the Z AI Skill Developer repository validator and the target platform's native skill validator. Build with `python scripts/build_package.py`; it includes only SKILL.md and the folders in package-resources.txt. The generated release receipt records source commit, per-file hashes and ZIP SHA-256 outside the runtime package.

Install the generated `dist/z-jack-work-assignments/` folder or ZIP through the target platform's supported skill installation method. The skill needs the agent's own approved Notion read/write connection; it does not configure one. Platforms without a skill loader may use the instructions as a reference, but automatic discovery is not claimed.

Test one agent with a real assignment and read back both records before broader installation. Jack has authorized Cody first, then Marsha and Harry; further fleet deployment requires approval. Recovery is removal of only this new skill directory, or restoration of a backed-up prior version if upgrading. Saved Notion work is retained.
