---
name: property-development-starter
description: Starter skill for the property development industry bundle. Orients Claude to NZ development projects, consents, feasibilities and cost control. V1 stub, replace with real development skills in content buildout.
---

# Property Development Starter

V1 starter skill shipped with the Claude Installer for the property
development industry. It gives Claude the working assumptions of an NZ
development team. It is deliberately thin.

## Purpose

Two jobs. First, prove that skills deploy correctly through the installer
pipeline. Second, keep early answers grounded in how a development project
is actually run, rather than generic construction commentary.

## Working assumptions

- Consenting runs under the Resource Management Act and the Building Act.
  Resource consent and building consent are separate processes with separate
  conditions. Never merge them in a summary.
- Every council is different. Auckland Council, Waipa, Selwyn and the rest
  all publish their own district plan and portal. Check the specific council
  rather than generalising.
- The feasibility model in Excel is the commercial source of truth. The
  Airtable register is the operational tracker. They drift. Say which one a
  number came from.
- Amounts are NZD. State whether a figure is GST-inclusive or exclusive.
  Development budgets are usually GST-exclusive and land is usually not.
- Programme dates move. Every status report is as at a date.

## When to use

Feasibility reviews, consent condition tracking, council RFIs, variation
logs, programme status, site reports, and title or LIM summaries.

## How to work

1. Name the project, the stage and the as-at date before anything else.
2. When summarising a consent, quote the condition number and the exact
   wording, then the plain-English reading. Keep them separate.
3. For cost questions, pull the committed cost from Xero and the forecast
   from the feasibility model. Show both. Never report one as the other.
4. Flag anything that looks like a scope change or a variation. Do not
   absorb it silently into a total.
5. Give risks with an owner and a next action, not just a description.

## Do not

- Do not give legal or planning advice. Summarise the document and point at
  the clause. A planner or lawyer makes the call.
- Do not submit anything to a council. Draft only.
- Do not approve a variation or a payment claim.

## Future expansion

Real skills to add for developers and project managers:
- Feasibility summary with sensitivities from an Excel model
- Resource consent condition extraction into a tracked checklist
- Council RFI response drafting from project documents
- Subcontractor variation capture and cost impact
- Weekly programme and critical-path status report
- Structured site visit report from photos and notes
- LIM, PIM and certificate of title summary into risks and actions
