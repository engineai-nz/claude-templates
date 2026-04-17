# Claude Templates

Publish-ready industry bundles for the [Engine AI Claude Installer](https://github.com/engineai-nz/claude-installer).

Each tagged release produces pre-merged `.tar.gz` bundles per `(industry, stack)` combination. The installer downloads the right bundle and unpacks it on the client machine. Zero merging happens on the client.

---

## Source layout

```
claude-templates/
├── core/
│   └── primitives/             # Tier 1 (always installed)
│       └── mcp.json
├── stacks/
│   ├── google/                 # Tier 2a — Drive, Gmail, Calendar, Meet
│   ├── microsoft/              # Tier 2b — OneDrive, Outlook, Teams
│   └── neutral/                # Tier 2 extras, stack-agnostic (Slack, Notion, HubSpot, Xero)
├── industries/
│   ├── property/               # V1 target
│   │   ├── manifest.json
│   │   ├── mcp.json
│   │   └── skills/
│   ├── finance/                # scaffold
│   ├── investment/             # scaffold
│   ├── property-development/   # scaffold
│   └── small-business/         # scaffold
├── claude-code-settings/       # Baseline ~/.claude/ settings + permissions
├── scripts/
│   └── build-bundles.py        # Factory-side merge and tarball
└── .github/workflows/release.yml
```

---

## Build flow

```bash
python3 scripts/build-bundles.py --version v0.1.0
```

Produces:

```
dist/bundles/
├── property-google/                # Unpacked bundle (for inspection)
├── property-google.tar.gz
├── property-microsoft/
├── property-microsoft.tar.gz
└── checksums.txt
```

Each bundle contains:

```
property-microsoft/
├── claude_desktop_config.json      # Pre-merged primitives + stack + neutral + industry
├── developer_settings.json         # {"allowDevTools": true}
├── skills/                         # Industry skills, ready to drop into ~/.claude/skills/
├── claude-code/
│   ├── settings.json
│   └── permissions.json
└── manifest.json                   # version, contents, build timestamp
```

---

## Release flow

1. Update content under `core/`, `stacks/`, `industries/`, `claude-code-settings/`
2. Tag: `git tag v0.1.0 && git push --tags`
3. GitHub Action (`.github/workflows/release.yml`) builds bundles and attaches tarballs to the release
4. The [claude-installer](https://github.com/engineai-nz/claude-installer) fetches the latest release asset matching the chosen `(industry, stack)`

---

## Placeholders

Configs ship with `{{PLACEHOLDER}}` tokens for secrets:

- `{{HOME}}` — substituted at install time with the user's home directory
- `{{GOOGLE_CLIENT_ID}}`, `{{GOOGLE_CLIENT_SECRET}}` — Google OAuth
- `{{AZURE_CLIENT_ID}}`, `{{AZURE_CLIENT_SECRET}}`, `{{AZURE_TENANT_ID}}` — Microsoft OAuth
- `{{SLACK_BOT_TOKEN}}`, `{{NOTION_API_KEY}}`, etc. — per-tool credentials

The installer substitutes `{{HOME}}`. All other placeholders stay as-is and are filled in during the post-install auth step.

---

## Relationship to other repos

| Repo | Role |
|---|---|
| [engineai-nz/claude-installer](https://github.com/engineai-nz/claude-installer) | Installer scripts that fetch from this repo's releases |
| [engineai-nz/claude-business-templates](https://github.com/engineai-nz/claude-business-templates) | Private factory where content is built and tested |
| **This repo** | Public, publish-ready templates |

Content flow: private factory → publish script → this repo → tag → release → installer.

---

## Licence

TBA.
