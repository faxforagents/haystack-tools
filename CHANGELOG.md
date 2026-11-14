# Changelog

## 0.2.0

Prepared on 2026-11-14. Unpublished.

The package has the 17 tools of the hosted MCP server at API 1.20.3. It had 15.

- Add `request_card_payment`: a person pays for one quoted fax by card, with no wallet balance.
- It returns a payment link in `status_url`. It takes no card details and cannot pay.
- Add `get_card_payment_status`: the order, its next step, and the fax once it was released.
- Both results leave out the order's status token, the payer's email address and the order's card field.
- A live card order requires `approval_id`, the same rule this package applies to live sends.
- `quote_fax` takes `quality`, `sender_name`, `from_number` and `delete_after_send`.
- `list_faxes` takes `idempotency_key` as a filter.
- The local guide has the sections `one_time` and `going_live`.
- Tool descriptions and annotations follow the hosted server. `cancel_fax` is now marked idempotent.

The SDK dependency is `faxforagents>=0.2.3,<0.7`. It ended below 0.5 and shut out SDK 0.6.0.
The card tools need SDK 0.4.1. The quote options and the list filter need 0.4.0.
With an older SDK those calls answer `sdk_upgrade_required` and send no request.
The tests pass against SDK 0.2.3, 0.4.0, 0.5.0 and 0.6.0. The lock file uses 0.6.0.

## 0.1.0

Prepared on 2026-11-04. Unpublished.

- Add 15 canonical Fax for Agents tools and `FaxForAgentsToolset`.
- Require sandbox credentials by default and approval IDs for live sends.
- Require caller idempotency keys and return structured failures.
- Mark remote results as untrusted data.
- Add offline Agent and ToolInvoker tests.
- Prepare the Haystack integration listing.
