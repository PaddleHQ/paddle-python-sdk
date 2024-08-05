# Upgrading

All breaking changes prior to v1 will be documented in this file to assist with upgrading.

## v0.2.0

This release includes a few breaking changes. These changes should be limited impact on most integrations but may cause problems in some circumstances. 

1. `PaddleStrEnum` has been re-implement to gracefully handle non-existent values, it is no longer using native enums

This should not require any implementation changes in your code. The new `PaddleStrEnum` is implemented in a way that minimises this impact.

However, as we have dropped native Enums there maybe native Enum specific behaviour that does not work exactly as before which would require more caution.

2. The `paddle_billing.Entities.Subscriptions.SubscriptionItem` price entity is now using the main `paddle_billing.Entities.Price` entity

The change here has again limited impact on runtime behaviour except for having more properties available, however, any instance or type checking at runtime or statically will fail.

As the `paddle_billing.Entities.Subscriptions.SubscriptionPrice` entity has been removed any references of this in the code will fail.

If you're making any of these checks or have the `SubscriptionPrice` imported you will need to update accordingly.

3. Entity factory methods are consistently static now where previously there were implementations as class methods

This should not require any real change with integrations as these factory methods never made use of being class methods but something to be aware of.
