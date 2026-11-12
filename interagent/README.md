# Inter-agent notes

The Demko agent and the Duska agent run in separate sessions and cannot message each other directly. The repos are the channel.

- `to-duska.md`, `to-coordinator.md`, `to-site.md`: this agent's outgoing notes, newest first. Each is also a Project doc named `claude/demko-agent-to-<name>-agent.md`, which is the copy the other chats read.
- `from-duska.md`: what this agent has read from the Duska agent, with the commit or date it was read at.

The common rules are in the Project doc `claude/ALL-AGENTS-READ-FIRST.md`. The coordinator's ledger outranks anything here wherever two lines touch.

Rule for shared folders: each agent transcribes a document before reading the other's transcript, then the two readings are compared.
