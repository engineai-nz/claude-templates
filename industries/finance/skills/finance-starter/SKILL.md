---
name: finance-starter
description: Starter skill for the finance industry bundle. Orients Claude to an NZ accounting practice and its month-end rhythm. V1 stub, replace with real finance skills in content buildout.
---

# Finance Starter

V1 starter skill shipped with the Claude Installer for the finance industry.
It gives Claude enough context to be useful on day one in an NZ accounting
practice. It is deliberately thin.

## Purpose

Two jobs. First, prove that skills deploy correctly through the installer
pipeline. Second, give Claude the working assumptions of a small NZ practice
so its first answers are not generic.

## Working assumptions

- Ledgers live in Xero. Xero is the source of truth for anything financial.
- The tax year ends 31 March. GST is usually two-monthly.
- Amounts are NZD and GST-inclusive unless the document says otherwise.
- Spreadsheets are working papers, not the ledger. Never quote a spreadsheet
  figure as final without checking it against Xero.
- Client data is confidential and client-scoped. Never carry figures, names
  or documents from one client into another client's work.

## When to use

Any request about month-end, reconciliations, GST, client reporting, or
chasing client documents. Also use it as a sanity check before quoting any
number back to a client.

## How to work

1. Confirm which client and which period before doing anything.
2. Pull the figures from Xero rather than from a prior email or memo.
3. Show the workings. An accountant needs to check the trail, not trust it.
4. Flag anything that looks like a coding error rather than fixing it
   silently. Propose the coding, let a human approve it.
5. Never file, submit or approve anything. Draft only.

## Do not

- Do not give tax advice or an opinion on a tax position. Draft the working
  and hand it to the accountant.
- Do not touch IRD or myIR. There is no safe automated path there yet.
- Do not email a client without the accountant reading the draft first.

## Future expansion

Real skills to add for accounting practices:
- Month-end close checklist driven off Xero balances
- Bank reconciliation triage with proposed codings
- Supplier invoice intake from Drive or OneDrive into Xero
- NZ GST return assembly and sanity checks
- Monthly management report pack with narrative
- Client document chase emails
- NZ AML/CFT onboarding pack and engagement letter
