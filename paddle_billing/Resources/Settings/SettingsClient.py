from paddle_billing.ResponseParser import ResponseParser

from paddle_billing.Entities.Settings import (
    BalanceCurrency,
    CheckoutFeatures,
    CheckoutPaymentMethodSettings,
    CheckoutRecovery,
    CheckoutStylesOverlay,
    CheckoutUrl,
    CurrencyConversions,
    StatementDescriptorSettings,
    TaxSettings,
)

from paddle_billing.Resources.Settings.Operations import (
    UpdateBalanceCurrency,
    UpdateCheckoutFeatures,
    UpdateCheckoutPaymentMethodSettings,
    UpdateCheckoutRecovery,
    UpdateCheckoutStylesOverlay,
    UpdateCheckoutUrl,
    UpdateCurrencyConversions,
    UpdateStatementDescriptorSettings,
    UpdateTaxSettings,
)

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from paddle_billing.Client import Client


class SettingsClient:
    def __init__(self, client: "Client"):
        self.client = client
        self.response = None

    def get_balance_currency(self) -> BalanceCurrency:
        self.response = self.client.get_raw("/settings/balance-currency")
        parser = ResponseParser(self.response)

        return BalanceCurrency.from_dict(parser.get_dict())

    def update_balance_currency(self, operation: UpdateBalanceCurrency) -> BalanceCurrency:
        self.response = self.client.patch_raw("/settings/balance-currency", operation)
        parser = ResponseParser(self.response)

        return BalanceCurrency.from_dict(parser.get_dict())

    def get_checkout_features(self) -> CheckoutFeatures:
        self.response = self.client.get_raw("/settings/checkout-features")
        parser = ResponseParser(self.response)

        return CheckoutFeatures.from_dict(parser.get_dict())

    def update_checkout_features(self, operation: UpdateCheckoutFeatures) -> CheckoutFeatures:
        self.response = self.client.patch_raw("/settings/checkout-features", operation)
        parser = ResponseParser(self.response)

        return CheckoutFeatures.from_dict(parser.get_dict())

    def get_checkout_payment_method_settings(self) -> CheckoutPaymentMethodSettings:
        self.response = self.client.get_raw("/settings/checkout-payment-methods")
        parser = ResponseParser(self.response)

        return CheckoutPaymentMethodSettings.from_dict(parser.get_dict())

    def update_checkout_payment_method_settings(
        self, operation: UpdateCheckoutPaymentMethodSettings
    ) -> CheckoutPaymentMethodSettings:
        self.response = self.client.patch_raw("/settings/checkout-payment-methods", operation)
        parser = ResponseParser(self.response)

        return CheckoutPaymentMethodSettings.from_dict(parser.get_dict())

    def get_checkout_recovery(self) -> CheckoutRecovery:
        self.response = self.client.get_raw("/settings/checkout-recovery")
        parser = ResponseParser(self.response)

        return CheckoutRecovery.from_dict(parser.get_dict())

    def update_checkout_recovery(self, operation: UpdateCheckoutRecovery) -> CheckoutRecovery:
        self.response = self.client.patch_raw("/settings/checkout-recovery", operation)
        parser = ResponseParser(self.response)

        return CheckoutRecovery.from_dict(parser.get_dict())

    def get_checkout_styles_overlay(self) -> CheckoutStylesOverlay:
        self.response = self.client.get_raw("/settings/checkout-styles-overlay")
        parser = ResponseParser(self.response)

        return CheckoutStylesOverlay.from_dict(parser.get_dict())

    def update_checkout_styles_overlay(self, operation: UpdateCheckoutStylesOverlay) -> CheckoutStylesOverlay:
        self.response = self.client.patch_raw("/settings/checkout-styles-overlay", operation)
        parser = ResponseParser(self.response)

        return CheckoutStylesOverlay.from_dict(parser.get_dict())

    def get_checkout_url(self) -> CheckoutUrl:
        self.response = self.client.get_raw("/settings/checkout-url")
        parser = ResponseParser(self.response)

        return CheckoutUrl.from_dict(parser.get_dict())

    def update_checkout_url(self, operation: UpdateCheckoutUrl) -> CheckoutUrl:
        self.response = self.client.patch_raw("/settings/checkout-url", operation)
        parser = ResponseParser(self.response)

        return CheckoutUrl.from_dict(parser.get_dict())

    def get_currency_conversions(self) -> CurrencyConversions:
        self.response = self.client.get_raw("/settings/currency-conversions")
        parser = ResponseParser(self.response)

        return CurrencyConversions.from_dict(parser.get_dict())

    def update_currency_conversions(self, operation: UpdateCurrencyConversions) -> CurrencyConversions:
        self.response = self.client.patch_raw("/settings/currency-conversions", operation)
        parser = ResponseParser(self.response)

        return CurrencyConversions.from_dict(parser.get_dict())

    def get_statement_descriptor_settings(self) -> StatementDescriptorSettings:
        self.response = self.client.get_raw("/settings/statement-descriptor")
        parser = ResponseParser(self.response)

        return StatementDescriptorSettings.from_dict(parser.get_dict())

    def update_statement_descriptor_settings(
        self, operation: UpdateStatementDescriptorSettings
    ) -> StatementDescriptorSettings:
        self.response = self.client.patch_raw("/settings/statement-descriptor", operation)
        parser = ResponseParser(self.response)

        return StatementDescriptorSettings.from_dict(parser.get_dict())

    def get_tax_settings(self) -> TaxSettings:
        self.response = self.client.get_raw("/settings/tax")
        parser = ResponseParser(self.response)

        return TaxSettings.from_dict(parser.get_dict())

    def update_tax_settings(self, operation: UpdateTaxSettings) -> TaxSettings:
        self.response = self.client.patch_raw("/settings/tax", operation)
        parser = ResponseParser(self.response)

        return TaxSettings.from_dict(parser.get_dict())
