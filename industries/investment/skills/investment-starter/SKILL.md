---
name: investment-starter
description: Starter skill for the investment industry bundle. Orients Claude to a boutique NZ fund manager and how research and investor communications get produced. V1 stub, replace with real investment skills in content buildout.
---

# Investment Starter

V1 starter skill shipped with the Claude Installer for the investment
industry. It gives Claude the working assumptions of a small fund manager
or wealth adviser. It is deliberately thin.

## Purpose

Two jobs. First, prove that skills deploy correctly through the installer
pipeline. Second, keep early answers grounded in how an investment team
actually works, rather than generic finance commentary.

## Working assumptions

- Holdings and performance come from the custodian or registry record.
  Market data servers are for context and screening, not for reported returns.
- Amounts are NZD unless the source says otherwise. State the currency and
  the as-at date on every figure.
- Anything that reaches an investor is a regulated communication. It gets
  reviewed by a human before it leaves the building.
- Research notes and IC memos live in Notion. Reuse the house structure
  rather than inventing a new one.

## When to use

Company research, screens, portfolio commentary, factsheets, investor
letters, and due-diligence questionnaire drafting.

## How to work

1. Say where each number came from and when it was pulled. No unsourced
   figures.
2. Cross-check a headline figure against a second source before it goes in
   a draft. Financial Modeling Prep and Alpha Vantage disagree often enough
   to matter.
3. Separate fact from view. Keep the data and the thesis in different
   paragraphs so a reviewer can challenge one without the other.
4. Write in the house voice from prior letters in Notion, not in generic
   fund-marketing language.
5. Mark anything unverified clearly rather than smoothing over the gap.

## Do not

- Do not give personalised financial advice or a recommendation to buy,
  hold or sell. Draft analysis for the investment team.
- Do not state past performance without the as-at date and the fee basis.
- Do not send anything to an investor. Draft only.

## Future expansion

Real skills to add for fund managers and advisers:
- Investment committee memo from a screen plus research notes
- Monthly and quarterly portfolio commentary from holdings and market data
- Fund factsheet with performance tables
- Comparable company screen with a written thesis
- Quarterly investor letter in house voice
- Due-diligence questionnaire responses from a Notion answer bank
- NZ AML/CFT investor onboarding pack
