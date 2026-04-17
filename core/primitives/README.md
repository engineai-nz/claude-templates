# Primitives

Tier 1 MCPs. Always installed. Stack and industry agnostic.

These are the hands Cowork uses to act on the local machine and the open web.

| Server | Purpose |
|---|---|
| `desktop-commander` | File ops, running scripts, process management |
| `filesystem` | Scoped read/write to the user's home |
| `fetch` | HTTP requests |
| `playwright` | Programmatic browser automation |
| `chrome-devtools` | Chrome debugging protocol access |

## Placeholders

`{{HOME}}` is substituted at install time with the user's home directory path.

## Runtime dependency

All primitives run via `npx` and require Node.js on the client machine. The installer handles the Node install before dropping this config.
