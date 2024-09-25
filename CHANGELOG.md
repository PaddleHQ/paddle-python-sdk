# Paddle Python SDK Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

Check our main [developer changelog](https://developer.paddle.com/?utm_source=dx&utm_medium=paddle-python-sdk) for information about changes to the Paddle Billing platform, the Paddle API, and other developer tools.

## [Unreleased]

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

### Changed

- `paddle_billing.Entities.Shared.CustomData` is no longer a `dataclass`
- `NotificationSettingsClient.delete` now returns `None` for `204 No Content` response

### Fixed

- `PreviewPrice` operation no longer allows empty `items`
- `CustomersClient.credit_balances` can now be filtered by `currency_code`

### Removed

- `AvailablePaymentMethods` - replaced by `PaymentMethodType`
- Removed `receipt_data` from `CreateOneTimeCharge` and `PreviewOneTimeCharge` subscription operations
- Removed `receipt_data` from `Transaction`

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
