# Small Business Industry Bundle

**Status:** V1 stub. Real content in content buildout phase.

## What's in here

- `manifest.json` - industry metadata, stack-neutral add-ons, skill list
- `mcp.json` - general SMB MCPs (payments, ops database, research, tasks)
- `skills/` - industry skills (currently one stub)

## Who this is for

The default bundle. NZ owner-operator businesses that do not fit one of the
named industries: trades, services, small agencies, retail. Usually one to
twenty staff, one person doing sales, admin and delivery.

## Design principle

Keep this bundle thin. Most of the value for a general SMB comes from the
stack-neutral four plus the skills, not from a long tail of MCP servers.
Every extra server is another credential the owner has to set up and another
thing that can break on their machine.

## Intended coverage (post-V1)

**Inherited from the stack-neutral bundle:**
- Xero (accounting, invoicing, debtors)
- HubSpot (customer pipeline)
- Slack (team comms)
- Notion (documents and process)

**Shipped in this bundle:**
- Stripe (payments, invoices, subscriptions)
- Airtable (the default SMB operations database)
- Exa (competitor and market research)
- Todoist (lightweight task capture for owner-operators)

**Planned skills:**
- Quote and proposal generation from a rate card
- Overdue debtor identification and chase emails
- Inbound enquiry triage and first response
- Monday morning numbers pack
- Review response drafting in brand voice
- Supplier price comparison
- Job scheduling against calendar and crew availability

## MCP servers deliberately not shipped

These were researched and left out. Do not add them without checking again.

- **Shopify store data** - `@shopify/dev-mcp` exists on npm but it is a
  **developer documentation** server. It cannot read orders, products or
  customers. Do not ship it as if it can. Shopify's storefront MCP is
  per-store and unverified, so a retail client needs a manual setup.
- **Google Maps and local listings** - `@modelcontextprotocol/server-google-maps`
  exists on npm and works, but it comes from the archived reference-server
  repo and was last published in December 2024. Useful for local SEO and
  review monitoring. Add it per client with eyes open.
- **Todoist** is shipped but optional. Drop it if the client already runs
  tasks somewhere else, rather than giving them two task systems.
