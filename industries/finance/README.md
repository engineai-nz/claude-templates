# Finance Industry Bundle

**Status:** V1 stub. Real content in content buildout phase.

## What's in here

- `manifest.json` - industry metadata, stack-neutral add-ons, skill list
- `mcp.json` - finance-specific MCPs (Stripe, Excel)
- `skills/` - industry skills (currently one stub)

## Who this is for

NZ accounting practices, bookkeepers and financial advisers. Small teams,
Xero-first, spreadsheet-heavy, working across a book of SMB clients.

## Intended coverage (post-V1)

**Inherited from the stack-neutral bundle:**
- Xero (practice and client ledgers)
- HubSpot (client pipeline)
- Slack (internal comms)
- Notion (practice knowledge base)

**Shipped in this bundle:**
- Stripe (payment and merchant reconciliation)
- Excel (reads and writes .xlsx, no credentials needed)

**Planned skills:**
- Month-end close checklist
- Bank reconciliation triage
- Accounts payable invoice intake
- NZ GST return preparation
- Monthly management report pack
- Client document chase emails
- NZ AML/CFT client onboarding

## MCP servers deliberately not shipped

These were researched and left out. Do not add them without checking again.

- **IRD / myIR** - no MCP server exists. Cover with the Playwright and
  Desktop Commander primitives until one is built.
- **MYOB** - no MCP server exists. Second-place ANZ accounting package,
  so this is a real gap for some practices.
- **QuickBooks** - the `quickbooks-mcp` npm package exists but is a
  single-maintainer community build. Only relevant to US-facing clients.
  Pilot it on one machine before adding it here.
- **SQL practice-management databases** - `@bytebase/dbhub` exists and works,
  but only a minority of practices have a SQL-backed system. Add per client
  rather than shipping it to everyone.
