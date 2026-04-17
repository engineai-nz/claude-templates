# Claude Code Settings

Baseline `~/.claude/settings.json` and `~/.claude/permissions.json` for client machines.

## Why pre-approved permissions

Claude Code prompts for permission on every new tool use. For a non-power-user first-run experience, this is friction that kills confidence. The `permissions.json` here pre-approves a tight allowlist of safe read-only shell commands and blocks obvious footguns (`sudo`, `rm -rf`, piped-to-shell downloads).

Clients can widen this over time once they're comfortable.

## Future additions

- Per-industry permissions (e.g. property-specific bash tools)
- MCP-level permissions once the MCP ecosystem supports them
- A "dangerously open" profile for trusted internal users
