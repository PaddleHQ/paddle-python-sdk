# Paddle Python SDK Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

Check our main [developer changelog](https://developer.paddle.com/?utm_source=dx&utm_medium=paddle-python-sdk) for information about changes to the Paddle Billing platform, the Paddle API, and other developer tools.

## [Unreleased]

### Added

- Support for payout reconciliation reports and `remittance_reference`, see [changelog](https://developer.paddle.com/changelog/2025/payout-reconciliation-report)

## 1.11.0 - 2025-10-07

### Added

- Non-catalog discounts on Transactions, see [changelog](https://developer.paddle.com/changelog/2025/custom-discounts?utm_source=dx&utm_medium=paddle-python-sdk)
- Support `retained_fee` field on totals objects to show the fees retained by Paddle for the adjustment.
- Added support for new payment methods `blik`, `mb_way`, `pix` and `upi`. See [related changelog](https://developer.paddle.com/changelog/2025/blik-mbway-payment-methods?utm_source=dx&utm_medium=paddle-python-sdk).
- `ApiError` will now have `retry_after` property set for [too_many_requests](https://developer.paddle.com/errors/shared/too_many_requests?utm_source=dx&utm_medium=paddle-python-sdk) errors

## 1.10.0 - 2025-08-15

### Added

- Added support for filtering events by `event_type` in event list operation, see [related changelog](https://developer.paddle.com/changelog/2025/filter-events-by-type?utm_source=dx&utm_medium=paddle-python-sdk).

## 1.9.0 - 2025-07-31

### Added

- Added support to fetch and update discount groups see [related changelog](https://developer.paddle.com/changelog/2025/discount-groups-new-api-operations?utm_source=dx&utm_medium=paddle-python-sdk)
- Added `exchange_rate` and `fee_rate` to `TransactionPayoutTotals`
- Added `exchange_rate` to `TransactionPayoutTotalsAdjusted`

## 1.8.0 - 2025-07-09

### Added

- Added support for client tokens see [related changelog](https://developer.paddle.com/changelog/2025/client-side-token-api?utm_source=dx&utm_medium=paddle-python-sdk)

## 1.7.0 - 2025-06-27

### Added

- Added support for Korean local payment methods, see [related changelog](https://developer.paddle.com/changelog/2024/korean-payment-methods?utm_source=dx&utm_medium=paddle-python-sdk).
- Added support for `balance` reports, see [related changelog](https://developer.paddle.com/changelog/2025/balance-reports?utm_source=dx&utm_medium=paddle-python-sdk).
- Added support for API key events, see [related changelog](https://developer.paddle.com/changelog/2025/api-key-improvements?utm_source=dx&utm_medium=paddle-python-sdk).
- Added support for discount mode
- Added support for discount group resources, see [related changelog](https://developer.paddle.com/changelog/2025/discount-groups?utm_source=dx&utm_medium=paddle-python-sdk).
- Added `tax_mode` to adjustment create operation
- Support for simulation scenario configuration, see [related changelog](https://developer.paddle.com/changelog/2025/webhook-simulator-scenario-configuration?utm_source=dx&utm_medium=paddle-python-sdk)

## 1.6.1 - 2025-06-10

### Fixed
- Fixed JSON encoding of undefined notification entities
  - `paddle_billing.Notifications.Entities.UndefinedEntity` now implements `to_json` and can be encoded using `paddle_billing.Json.PayloadEncoder`
- Improved type hints throughout SDK

## 1.6.0 - 2025-02-10

### Added

- Added `PreviewTransaction` operation to support transaction previews without location information.

### Fixed

- Transaction preview `currency_code` can now be set to `null`.

## 1.5.0 - 2025-01-28

### Added

- Added `transactions.revise` operation to revise a transaction and added `revised_at` to `Transaction` entity, see [related changelog](https://developer.paddle.com/changelog/2024/revise-transaction-customer-information?utm_source=dx&utm_medium=paddle-python-sdk).
- Added support for `transaction.revised` notification, see [related changelog](https://developer.paddle.com/changelog/2024/revise-transaction-customer-information?utm_source=dx&utm_medium=paddle-python-sdk).
- Added simulation API support [related changelog](https://developer.paddle.com/changelog/2024/webhook-simulator?utm_source=dx&utm_medium=paddle-python-sdk)
  - `Client.simulations.create`
  - `Client.simulations.update`
  - `Client.simulations.get`
  - `Client.simulations.list`
  - `Client.simulation_runs.create`
  - `Client.simulation_runs.get`
  - `Client.simulation_runs.list`
  - `Client.simulation_run_events.replay`
  - `Client.simulation_run_events.get`
  - `Client.simulation_run_events.list`
  - `Client.simulation_types.list`

## 1.4.0 - 2024-12-19

### Added

- Added `on_resume` support to subscription resume and pause operations

## 1.3.1 - 2024-12-17

### Fixed

- Adjustment type in responses is now the correct type

## 1.3.0 - 2024-12-17

### Added

- Support for adjustment type, see [related changelog](https://developer.paddle.com/changelog/2024/refund-credit-full-total?utm_source=dx&utm_medium=paddle-python-sdk)
- Added Vietnamese Dong (`VND`) as a supported currency for payments [related changelog](https://developer.paddle.com/changelog/2024/vietnamese-dong-vnd-supported-currency?utm_source=dx&utm_medium=paddle-python-sdk)

## 1.2.2 - 2024-12-17

### Fixed

- Subscription discount now supports null `starts_at`

## 1.2.1 - 2024-12-04

### Fixed

- Subscription IDs can be omitted when creating customer portal sessions
- Customer portal session customer ID will always be returned as string
- `Client.notifications.replay` now calls correct endpoint

## 1.2.0 - 2024-12-03

### Added

- Support for customer portal sessions, see [related changelog](https://developer.paddle.com/changelog/2024/customer-portal-sessions?utm_source=dx&utm_medium=paddle-python-sdk)
  - `Client.customer_portal_sessions.create`

## 1.1.2 - 2024-11-20

### Fixed
- `paddle_billing.Notifications.Entities.Subscription` and `paddle_billing.Notifications.Entities.SubscriptionCreated` `current_billing_period` would return `None` if `billing_details` was `None`. `current_billing_period` will now return `TimePeriod` when set.

### Added

- Added missing `traffic_source` property to `paddle_billing.Entities.NotificationSetting` entity

## 1.1.1 - 2024-11-14

### Fixed

- `paddle_billing.Entities.PaymentMethod` `type` property is required

## 1.1.0 - 2024-11-14

### Added

- Support for saved payment methods, see [related changelog](https://developer.paddle.com/changelog/2024/saved-payment-methods?utm_source=dx&utm_medium=paddle-python-sdk)
  - `Client.payment_methods.list`
  - `Client.payment_methods.get`
  - `Client.payment_methods.delete`
  - `Client.customers.create_auth_token`

## 1.0.0 - 2024-11-11

### Changed

- `paddle_billing.Resources.Discounts.Operations.CreateDiscount` `expires_at` is now `paddle_billing.Entities.DateTime`
- `paddle_billing.Resources.Discounts.Operations.UpdateDiscount` `expires_at` is now `paddle_billing.Entities.DateTime`
- Transaction and Subscription operation items now allow optional properties to be omitted.
  - The following property types have changed (See UPGRADING.md for further details)
    - `paddle_billing.Resources.Subscriptions.Operations`:
      - `UpdateSubscription.items`
      - `PreviewUpdateSubscription.items`
      - `CreateOneTimeCharge.items`
      - `PreviewOneTimeCharge.items`
    - `paddle_billing.Resources.Transactions.Operations`:
      - `CreateTransaction.items`
      - `UpdateTransaction.items`
      - `PreviewTransactionByAddress.items`
      - `PreviewTransactionByCustomer.items`
      - `PreviewTransactionByIP.items`
- Transaction and Subscription preview responses now support preview products and prices without IDs (see UPGRADING.md for further details)

### Removed
- `get_parameters()` method on request operation classes is now removed or replaced by `to_json()` (see UPGRADING.md for further details)

## 0.3.2 - 2024-11-07

### Fixed

- `paddle_billing.Entities.Shared.TransactionLineItemPreview` `proration` can now be None

## 0.3.1 - 2024-10-14

### Fixed

- Added missing initialization file for `paddle_billing.Resources.IPAddresses`

## 0.3.0 - 2024-10-09

### Added

- Added `product` to `subscription.items[]`, see [related changelog](https://developer.paddle.com/changelog/2024/subscription-items-product?utm_source=dx&utm_medium=paddle-python-sdk)
- Support custom prices when updating and previewing subscriptions, see [related changelog](https://developer.paddle.com/changelog/2024/add-custom-items-subscription)
- Support for `custom_data` on discounts
- Support notification settings pagination, see [related changelog](https://developer.paddle.com/changelog/2024/notification-settings-pagination)
- Support notification settings `active` filter
- `TransactionsClient.get_invoice_pdf` now supports `disposition` parameter, see [related changelog](https://developer.paddle.com/changelog/2024/invoice-pdf-open-in-browser)
- `SubscriptionClient` `preview_update` and `preview_one_time_charge` responses now have `import_meta` property
- Support for `tax_rates_used` on Adjustments
- Added `IPAddressesClient.get_ip_addresses` to support retrieval of Paddle IP addresses
- Support for `proration` on subscription `recurring_transaction_details.line_items[]` and `next_transaction.details.line_items[]`
- Added `AdjustmentsClient.get_credit_note`, see [related changelog](https://developer.paddle.com/changelog/2024/generate-adjustments-credit-notes)

### Changed

- `paddle_billing.Entities.Shared.CustomData` is no longer a `dataclass`
- `NotificationSettingsClient.delete` now returns `None` for `204 No Content` response
- `TimePeriod` is now aligned to API specification:
  - Existing shared `TimePeriod` was renamed to `Duration` (with properties `interval` and `frequency`)
  - New shared `TimePeriod` was added (with properties `starts_at` and `ends_at`)
- Replaced `AdjustmentTimePeriod`, `SubscriptionTimePeriod` and `TransactionTimePeriod` with shared `TimePeriod`
- Replaced `AdjustmentProration`, `SubscriptionProration` and `TransactionProration` with shared `Proration`
- `paddle_billing.Entities.Event` `data` will now be `paddle_billing.Notifications.Entities.SubscriptionCreated` for `subscription.created` events
- `paddle_billing.Entities.Event` `data` will now be `paddle_billing.Notifications.Entities.UndefinedEntity` for unknown event types
- `paddle_billing.Resources.Reports.Operations.CreateReport` is replaced by report specific operations `CreateAdjustmentsReport` | `CreateDiscountsReport` | `CreateProductsAndPricesReport` | `CreateTransactionsReport`
- `paddle_billing.Entities.Notification` `payload` is now `paddle_billing.Entities.Notifications.NotificationEvent`
- `paddle_billing.Entities.Shared.BillingDetails` is no longer used for `billing_details` in request operations
  - `CreateTransaction` now uses `paddle_billing.Resources.Transactions.Operations.Create.CreateBillingDetails`
  - `UpdateTransaction` now uses `paddle_billing.Resources.Transactions.Operations.Update.UpdateBillingDetails`
  - `UpdateSubscription` | `PreviewUpdateSubscription` now uses `paddle_billing.Resources.Subscriptions.Operations.Update.UpdateBillingDetails`

### Fixed

- `PreviewPrice` operation no longer allows empty `items`
- `CustomersClient.credit_balances` can now be filtered by `currency_code`
- Transaction payments `payment_method_id` can be `string` or `None`
- `paddle_billing.Notifications.Verifier` `verify()` now expects `request` to be `paddle_billing.Notifications.Requests.Request` protocol
- Client connection errors will be raised as `requests.exceptions.ConnectionError` instead of an `AttributeError`

### Removed

- `AvailablePaymentMethods` - replaced by `PaymentMethodType`
- Removed `receipt_data` from `CreateOneTimeCharge` and `PreviewOneTimeCharge` subscription operations
- Removed `receipt_data` from `Transaction`
- Removed `paddle_billing.Resources.Transactions.Operations.PreviewTransaction` - replaced by `PreviewTransactionByAddress` | `PreviewTransactionByCustomer` | `PreviewTransactionByIP`

## 0.2.2 - 2024-09-03

### Fixed

- Fixed [bug](https://github.com/PaddleHQ/paddle-python-sdk/pull/24) - set default timeout.

## 0.2.1 - 2024-08-19

### Fixed

- Fix `setup.py` version

## 0.2.0 - 2024-08-05

### Changed

- `PaddleStrEnum` has been re-implement to gracefully handle non-existent values, it is no longer using native enums
- The `paddle_billing.Entities.Subscriptions.SubscriptionItem` price entity is now using the main `paddle_billing.Entities.Price` entity
- Updated the version of `pytest` supported to accept 8.4.0

### Added

- The `paddle_billing.Notifications.Entities.Subscriptions.SubscriptionPrice` entity has been updated to include support for all `Price` properties
- Improved IDE support for Collections, IDEs will now know the variable type when iterating through the collection

### Fixed

- Entity factory methods are consistently static now where previously there were implementations as class methods 

### Removed

- The `paddle_billing.Entities.Subscriptions.SubscriptionPrice` entity which has been removed in favour of reusing `paddle_billing.Entities.Price` entity.


## 0.1.3 - 2024-06-20

### Fixed

- Fixed [bug](https://github.com/PaddleHQ/paddle-python-sdk/issues/10) - raise Paddle API errors


## 0.1.2 - 2024-06-20

### Fixed

- Fixed [bug](https://github.com/PaddleHQ/paddle-python-sdk/pull/12) - corrected import in `NotificationSettingCollection`.

---

## 0.1.1 - 2024-05-24

### Fixed

- Fixed a [bug](https://github.com/PaddleHQ/paddle-python-sdk/issues/7) with `UpdateBusiness` operation.

---

## 0.1.0 - 2024-04-05

### Added:

- Initial release.
