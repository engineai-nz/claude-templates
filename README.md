# Claude Templates

Publish-ready industry bundles for the [Engine AI Claude Installer](https://github.com/engineai-nz/claude-installer).

This repo holds the MCP configurations, skills, and Claude Code settings that clients actually install. Bundles are composed at install time from three tiers:

1. **Primitives** (always installed) — Chrome MCP, Desktop Commander, Filesystem, Playwright, Fetch
2. **Stack** (Google or Microsoft) — Drive+Gmail+Gcal+Meet vs OneDrive+Outlook+Ocal+Teams
3. **Industry add-ons** — stack-neutral SMB tools plus industry-specific MCPs

---

## Layout

```
claude-templates/
├── core/
│   └── primitives/             # Tier 1 (always installed)
├── stacks/
│   ├── google/                 # Tier 2a
│   ├── microsoft/              # Tier 2b
│   └── neutral/                # Stack-agnostic add-ons
├── industries/
│   ├── property/               # V1 target
│   ├── finance/
│   ├── investment/
│   ├── property-development/
│   └── small-business/
└── claude-code-settings/       # Baseline settings.json + permissions.json
```

---

## Manifest shape

Each industry folder has a `manifest.json`:

```json
{
  "industry": "property",
  "version": "1.0.0",
  "add_ons": ["slack", "hubspot", "notion"],
  "industry_mcps": {
    "trade-me": { "command": "npx", "args": ["-y", "@engineai/mcp-trade-me"] }
  },
  "skills": ["property-skill-a", "property-skill-b"]
}
```

---

## Relationship to other repos

| Repo | Role |
|---|---|
| [engineai-nz/claude-installer](https://github.com/engineai-nz/claude-installer) | Installer scripts that fetch from this repo |
| [engineai-nz/claude-business-templates](https://github.com/engineai-nz/claude-business-templates) | Private factory where templates are built and tested |
| **This repo** | Public, publish-ready templates clients install from |

Content flows: private factory → publish script → this repo → client machine.

---

## Status

**Scaffolding phase.** Directory structure is intentional; real content comes with the V1 installer ship and the per-industry content track.

---

## Licence

TBA.
