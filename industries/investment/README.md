# Investment Industry Bundle

**Status:** V1 stub. Real content in content buildout phase.

## What's in here

- `manifest.json` - industry metadata, stack-neutral add-ons, skill list
- `mcp.json` - investment-specific MCPs (market data and research)
- `skills/` - industry skills (currently one stub)

## Who this is for

Boutique fund managers and wealth advisers. Small investment teams running
their own research, writing their own IC memos and investor letters.

## Intended coverage (post-V1)

**Inherited from the stack-neutral bundle:**
- Notion (research library, IC memos, answer bank)
- Slack (internal comms)
- Xero (the fund's own books)

**Shipped in this bundle:**
- Financial Modeling Prep (fundamentals, statements, ratios, screeners)
- Alpha Vantage (official hosted MCP, quotes and time series)
- Exa (neural search for company diligence, news, filings)
- Firecrawl (scrape NZX/ASX announcements, factsheets, PDS documents)

**Planned skills:**
- Investment committee memo drafting
- Monthly and quarterly portfolio commentary
- Fund factsheet generation
- Comparable company screens
- Quarterly investor letters
- Due-diligence questionnaire responses
- NZ AML/CFT investor onboarding

## MCP servers deliberately not shipped

These were researched and left out. Do not add them without checking again.

- **Polygon.io market data** - the npm package `polygon-mcp` is a Polygon
  **blockchain** server, not Polygon.io market data. Do not install it.
  Polygon.io maintain a Python MCP repo that is not published to npm.
- **NZX, FMA and Sharesies** - no MCP servers exist. This is the real gap for
  NZ funds. Cover with Firecrawl and the Playwright primitive for now.
- **Bloomberg, FactSet, Morningstar** - no public MCP servers. Enterprise
  licensing puts them out of SMB scope anyway.
- **Yahoo Finance** - the `yfinance-mcp` npm package exists and works as a
  no-API-key fallback, but it is a community build. Add it per client if
  they will not pay for a data feed.

## A note on data quality

Every server in this bundle returns third-party market data. None of it is
a compliance-grade source. Anything that goes in front of an investor is
checked against the custodian or registry record first.
