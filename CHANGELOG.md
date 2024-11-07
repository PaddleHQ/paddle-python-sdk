# Paddle Python SDK Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

Check our main [developer changelog](https://developer.paddle.com/?utm_source=dx&utm_medium=paddle-python-sdk) for information about changes to the Paddle Billing platform, the Paddle API, and other developer tools.

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
