# Changelog

## Unreleased

The SDK dependency is `faxforagents>=0.2.3,<0.5`. The range ended below 0.3 and shut out the current SDK.
The tests pass against SDK 0.2.3, 0.3.2 and the 0.4.0 branch. No tool changed.

## 0.1.0

Prepared on 2026-11-04. Unpublished.

- Add 15 canonical Fax for Agents tools and `FaxForAgentsToolset`.
- Require sandbox credentials by default and approval IDs for live sends.
- Require caller idempotency keys and return structured failures.
- Mark remote results as untrusted data.
- Add offline Agent and ToolInvoker tests.
- Prepare the Haystack integration listing.
