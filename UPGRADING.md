# Upgrading

All breaking changes prior to v1 will be documented in this file to assist with upgrading.

## Unreleased

### 1. Unused `get_parameters()` method was removed from request operation classes

`get_parameters()` methods returned the data used for operation request payloads, but is now removed or replaced by `to_json()`. This method was intended to be internal, so should not require any changes.

`get_parameters()` method was removed from the following classes:
  - `paddle_billing.Entities.Reports.ReportFilter`
  - `paddle_billing.Entities.Shared.CustomData`
  - `paddle_billing.Entities.Subscriptions.SubscriptionItems`
  - `paddle_billing.Entities.Subscriptions.SubscriptionItemsWithPrice`
  - `paddle_billing.Notifications.Entities.Reports.ReportFilter`
  - `paddle_billing.Notifications.Entities.Shared.CustomData`
  - `paddle_billing.Resources.Addresses.Operations.CreateAddress`
  - `paddle_billing.Resources.Addresses.Operations.UpdateAddress`
  - `paddle_billing.Resources.Adjustments.Operations.CreateAdjustment`
  - `paddle_billing.Resources.Businesses.Operations.CreateBusiness`
  - `paddle_billing.Resources.Businesses.Operations.UpdateBusiness`
  - `paddle_billing.Resources.Customers.Operations.CreateCustomer`
  - `paddle_billing.Resources.Customers.Operations.UpdateCustomer`
  - `paddle_billing.Resources.Discounts.Operations.CreateDiscount`
  - `paddle_billing.Resources.Discounts.Operations.UpdateDiscount`
  - `paddle_billing.Resources.NotificationSettings.Operations.CreateNotificationSetting`
  - `paddle_billing.Resources.NotificationSettings.Operations.UpdateNotificationSetting`
  - `paddle_billing.Resources.Prices.Operations.CreatePrice`
  - `paddle_billing.Resources.Prices.Operations.UpdatePrice`
  - `paddle_billing.Resources.PricingPreviews.Operations.PreviewPrice`
  - `paddle_billing.Resources.Products.Operations.CreateProduct`
  - `paddle_billing.Resources.Products.Operations.UpdateProduct`
  - `paddle_billing.Resources.Reports.Operations.CreateReport` subclasses:
    - `paddle_billing.Resources.Reports.Operations.CreateAdjustmentsReport`
    - `paddle_billing.Resources.Reports.Operations.CreateDiscountsReport`
    - `paddle_billing.Resources.Reports.Operations.CreateProductsAndPricesReport`
    - `paddle_billing.Resources.Reports.Operations.CreateTransactionsReport`
  - `paddle_billing.Resources.Reports.Operations.Filters.Filter` subclasses:
    - `paddle_billing.Resources.Reports.Operations.Filters.AdjustmentActionFilter`
    - `paddle_billing.Resources.Reports.Operations.Filters.AdjustmentStatusFilter`
    - `paddle_billing.Resources.Reports.Operations.Filters.CollectionModeFilter`
    - `paddle_billing.Resources.Reports.Operations.Filters.CurrencyCodeFilter`
    - `paddle_billing.Resources.Reports.Operations.Filters.DiscountStatusFilter`
    - `paddle_billing.Resources.Reports.Operations.Filters.DiscountTypeFilter`
    - `paddle_billing.Resources.Reports.Operations.Filters.Filter`
    - `paddle_billing.Resources.Reports.Operations.Filters.PriceStatusFilter`
    - `paddle_billing.Resources.Reports.Operations.Filters.PriceTypeFilter`
    - `paddle_billing.Resources.Reports.Operations.Filters.PriceUpdatedAtFilter`
    - `paddle_billing.Resources.Reports.Operations.Filters.ProductStatusFilter`
    - `paddle_billing.Resources.Reports.Operations.Filters.ProductTypeFilter`
    - `paddle_billing.Resources.Reports.Operations.Filters.ProductUpdatedAtFilter`
    - `paddle_billing.Resources.Reports.Operations.Filters.TransactionOriginFilter`
    - `paddle_billing.Resources.Reports.Operations.Filters.TransactionStatusFilter`
    - `paddle_billing.Resources.Reports.Operations.Filters.UpdatedAtFilter`
  - `paddle_billing.Resources.Subscriptions.Operations.CancelSubscription`
  - `paddle_billing.Resources.Subscriptions.Operations.CreateOneTimeCharge`
  - `paddle_billing.Resources.Subscriptions.Operations.PauseSubscription`
  - `paddle_billing.Resources.Subscriptions.Operations.PreviewOneTimeCharge`
  - `paddle_billing.Resources.Subscriptions.Operations.ResumeSubscription`
  - `paddle_billing.Resources.Transactions.Operations.PreviewTransactionByAddress`
  - `paddle_billing.Resources.Transactions.Operations.PreviewTransactionByCustomer`
  - `paddle_billing.Resources.Transactions.Operations.PreviewTransactionByIP`

## v0.3.0

### 1. `AvailablePaymentMethods` has been replaced by `PaymentMethodType`.

`Transaction` `available_payment_methods` will now return a list of `paddle_billing.Entities.Shared.PaymentMethodType`.

All usage of `paddle_billing.Entities.Shared.AvailablePaymentMethods` will need to be replaced with `paddle_billing.Entities.Shared.PaymentMethodType`.

### 2. `TimePeriod` has been aligned to API specification

Existing shared `TimePeriod` was renamed to `Duration` (with properties `interval` and `frequency`), and new `TimePeriod` was added (with properties `starts_at` and `ends_at`).

Existing usages of `paddle_billing.Entities.Shared.TimePeriod` will need to be changed to `paddle_billing.Entities.Shared.Duration`.

`paddle_billing.Entities.Shared.TimePeriod` should be used in place of:
- `paddle_billing.Entities.Shared.AdjustmentTimePeriod`
- `paddle_billing.Entities.Subscriptions.SubscriptionTimePeriod`
- `paddle_billing.Entities.Transactions.TransactionTimePeriod`

`paddle_billing.Notifications.Entities.Shared.TimePeriod` should be used in place of:
- `paddle_billing.Notifications.Entities.Shared.AdjustmentTimePeriod`
- `paddle_billing.Notifications.Entities.Subscriptions.SubscriptionTimePeriod`
- `paddle_billing.Notifications.Entities.Transactions.TransactionTimePeriod`

`paddle_billing.Entities.Shared.Proration` should be used in place of:
- `paddle_billing.Entities.Shared.AdjustmentProration`
- `paddle_billing.Entities.Subscriptions.SubscriptionProration`
- `paddle_billing.Entities.Transactions.TransactionProration`

`paddle_billing.Notifications.Entities.Shared.Proration` should be used in place of:
- `paddle_billing.Notifications.Entities.Shared.AdjustmentProration`
- `paddle_billing.Notifications.Entities.Transactions.TransactionProration`

### 3. Transaction preview operation `PreviewTransaction` is removed

Usage of `paddle_billing.Resources.Transactions.Operations.PreviewTransaction` should be replaced with one of:
- `paddle_billing.Resources.Transactions.Operations.PreviewTransactionByAddress`
- `paddle_billing.Resources.Transactions.Operations.PreviewTransactionByCustomer`
- `paddle_billing.Resources.Transactions.Operations.PreviewTransactionByIP`

### 4. `CreateReport` operation is replaced by report specific operations `CreateAdjustmentsReport` | `CreateDiscountsReport` | `CreateProductsAndPricesReport` | `CreateTransactionsReport`

Usage of `paddle_billing.Resources.Reports.Operations.CreateReport` should be replaced with one of:
- `paddle_billing.Resources.Reports.Operations.CreateAdjustmentsReport`
- `paddle_billing.Resources.Reports.Operations.CreateDiscountsReport`
- `paddle_billing.Resources.Reports.Operations.CreateProductsAndPricesReport`
- `paddle_billing.Resources.Reports.Operations.CreateTransactionsReport`

### 5. `BillingDetails` entity is no longer used for `billing_details` in request operations

Usage of `paddle_billing.Entities.Shared.BillingDetails` for `billing_details` in request operations, should be replaced with:
- `paddle_billing.Resources.Transactions.Operations.Create.CreateBillingDetails` for `CreateTransaction`
- `paddle_billing.Resources.Transactions.Operations.Update.UpdateBillingDetails` for `UpdateTransaction`
- `paddle_billing.Resources.Subscriptions.Operations.Update.UpdateBillingDetails` for `UpdateSubscription` | `PreviewUpdateSubscription`

## v0.2.0

This release includes a few breaking changes. These changes should be limited impact on most integrations but may cause problems in some circumstances. 

### 1. `PaddleStrEnum` has been re-implement to gracefully handle non-existent values, it is no longer using native enums

This should not require any implementation changes in your code. The new `PaddleStrEnum` is implemented in a way that minimises this impact.

However, as we have dropped native Enums there maybe native Enum specific behaviour that does not work exactly as before which would require more caution.

### 2. The `paddle_billing.Entities.Subscriptions.SubscriptionItem` price entity is now using the main `paddle_billing.Entities.Price` entity

The change here has again limited impact on runtime behaviour except for having more properties available, however, any instance or type checking at runtime or statically will fail.

As the `paddle_billing.Entities.Subscriptions.SubscriptionPrice` entity has been removed any references of this in the code will fail.

If you're making any of these checks or have the `SubscriptionPrice` imported you will need to update accordingly.

### 3. Entity factory methods are consistently static now where previously there were implementations as class methods

This should not require any real change with integrations as these factory methods never made use of being class methods but something to be aware of.
