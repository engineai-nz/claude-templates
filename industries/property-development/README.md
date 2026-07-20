# Property Development Industry Bundle

**Status:** V1 stub. Real content in content buildout phase.

## What's in here

- `manifest.json` - industry metadata, stack-neutral add-ons, skill list
- `mcp.json` - development-specific MCPs (project registers, cost models, research)
- `skills/` - industry skills (currently one stub)

## Who this is for

NZ property developers, development project managers and quantity surveyors.
Small teams running multi-year projects through councils, consultants and
subcontractors.

## Intended coverage (post-V1)

**Inherited from the stack-neutral bundle:**
- Xero (project cost tracking, subcontractor invoices)
- Slack (site and office comms)
- Notion (project knowledge base)

**Shipped in this bundle:**
- Airtable (lot schedules, feasibility registers, consent trackers)
- Excel (feasibility models and cost plans, no credentials needed)
- Firecrawl (council district plans, consent portals, LIM and PIM documents)
- Asana (official hosted MCP, programme and task tracking)

**Planned skills:**
- Feasibility summary in plain English with sensitivities
- Resource consent condition tracker
- Council RFI response drafting
- Subcontractor variation log
- Weekly programme and critical-path status
- Site visit reports from photos and notes
- LIM, PIM and title summaries

## Project management: pick one

Asana is shipped because it has an official hosted MCP server. If the client
runs Trello or ClickUp instead, swap the `asana` entry for one of these and
delete the other. Do not ship two project tools to the same machine.

- Trello: `mcp-server-trello` (community)
- ClickUp: `clickup-mcp-server` (community)

## MCP servers deliberately not shipped

These were researched and left out. Do not add them without checking again.

- **LINZ titles, council GIS and consent portals** - no MCP servers exist.
  This is the genuine build opportunity for this industry. Cover with
  Firecrawl and the Playwright primitive in the interim.
- **DocuSign** - could not be confirmed. The npm package `docusign-mcp` does
  not exist and the hosted endpoint returned an ambiguous response. Do not
  ship until someone verifies it end to end.
- **Procore and Buildertrend** - no public MCP servers found.
- **Google Maps** - `@modelcontextprotocol/server-google-maps` exists on npm
  and works, but it comes from the archived reference-server repo and was
  last published in December 2024. Add it per client with eyes open, do not
  ship it by default.
