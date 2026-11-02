from functools import reduce
from json import loads
from pytest import mark
from urllib.parse import unquote

from paddle_billing.Entities.Settings import (
    AudienceOptIn,
    BalanceCurrency,
    BalanceCurrencyCode,
    CheckoutFeatures,
    CheckoutPaymentMethodSettings,
    CheckoutPaymentMethodSettingUpdate,
    CheckoutPaymentMethodsUpdate,
    CheckoutRecovery,
    CheckoutRecoveryDiscountType,
    CheckoutRecoveryDiscountUpdate,
    CheckoutStylesOverlay,
    CheckoutUrl,
    CurrencyConversion,
    CurrencyConversions,
    CurrencyConversionUpdate,
    DefaultTaxMode,
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
from paddle_billing.Undefined import Undefined

from tests.Utils.ReadsFixture import ReadsFixtures

PAYMENT_METHODS = [
    "alipay",
    "apple_pay",
    "bancontact",
    "blik",
    "card",
    "google_pay",
    "ideal",
    "kakao_pay",
    "mb_way",
    "naver_pay",
    "payco",
    "paypal",
    "pix",
    "samsung_pay",
    "south_korea_local_card",
    "upi",
    "wechat_pay",
]


def resolve(entity, path):
    return reduce(getattr, path.split("."), entity)


class TestSettingsClient:
    @mark.parametrize(
        "method, expected_url, expected_entity, response_fixture, expected_fields",
        [
            (
                "get_balance_currency",
                "/settings/balance-currency",
                BalanceCurrency,
                "response/balance_currency",
                {"primary": BalanceCurrencyCode.USD, "preferred": BalanceCurrencyCode.USD, "enabled": ["USD"]},
            ),
            (
                "get_checkout_features",
                "/settings/checkout-features",
                CheckoutFeatures,
                "response/checkout_features",
                {
                    "discounts_enabled": True,
                    "audience_opt_in": AudienceOptIn.Choice,
                    "saved_payment_methods_enabled": True,
                },
            ),
            (
                "get_checkout_payment_method_settings",
                "/settings/checkout-payment-methods",
                CheckoutPaymentMethodSettings,
                "response/checkout_payment_method_settings",
                {
                    "payment_methods.alipay.enabled": False,
                    "payment_methods.alipay.available": True,
                    "payment_methods.apple_pay.enabled": True,
                    "payment_methods.blik.available": False,
                    "payment_methods.south_korea_local_card.enabled": False,
                    "payment_methods.wechat_pay.available": False,
                },
            ),
            (
                "get_checkout_recovery",
                "/settings/checkout-recovery",
                CheckoutRecovery,
                "response/checkout_recovery",
                {
                    "enabled": True,
                    "discount.type": CheckoutRecoveryDiscountType.Percentage,
                    "discount.amount": "10",
                },
            ),
            (
                "get_checkout_recovery",
                "/settings/checkout-recovery",
                CheckoutRecovery,
                "response/checkout_recovery_no_discount",
                {"enabled": True, "discount": None},
            ),
            (
                "get_checkout_styles_overlay",
                "/settings/checkout-styles-overlay",
                CheckoutStylesOverlay,
                "response/checkout_styles_overlay",
                {"primary_checkout_color": "#4F46E5"},
            ),
            (
                "get_checkout_styles_overlay",
                "/settings/checkout-styles-overlay",
                CheckoutStylesOverlay,
                "response/checkout_styles_overlay_unset",
                {"primary_checkout_color": None},
            ),
            (
                "get_checkout_url",
                "/settings/checkout-url",
                CheckoutUrl,
                "response/checkout_url",
                {"default_url": "https://example.com/buy"},
            ),
            (
                "get_checkout_url",
                "/settings/checkout-url",
                CheckoutUrl,
                "response/checkout_url_unset",
                {"default_url": None},
            ),
            (
                "get_statement_descriptor_settings",
                "/settings/statement-descriptor",
                StatementDescriptorSettings,
                "response/statement_descriptor_settings",
                {"name": "AEROEDIT", "preview.default": "PADDLE.NET* AEROEDIT", "preview.paypal": "PAYPAL *PADDLE.NET"},
            ),
            (
                "get_tax_settings",
                "/settings/tax",
                TaxSettings,
                "response/tax_settings",
                {"default_tax_mode": DefaultTaxMode.Exclusive},
            ),
        ],
        ids=[
            "Get balance currency",
            "Get checkout features",
            "Get checkout payment method settings",
            "Get checkout recovery",
            "Get checkout recovery without discount",
            "Get checkout styles overlay",
            "Get checkout styles overlay without color",
            "Get checkout URL",
            "Get checkout URL without default",
            "Get statement descriptor settings",
            "Get tax settings",
        ],
    )
    def test_get_setting_returns_expected_response(
        self,
        test_client,
        mock_requests,
        method,
        expected_url,
        expected_entity,
        response_fixture,
        expected_fields,
    ):
        expected_url = f"{test_client.base_url}{expected_url}"
        expected_response_body = ReadsFixtures.read_raw_json_fixture(response_fixture)
        mock_requests.get(expected_url, status_code=200, text=expected_response_body)

        response = getattr(test_client.client.settings, method)()
        response_json = test_client.client.settings.response.json()
        last_request = mock_requests.last_request

        assert isinstance(response, expected_entity)
        assert last_request is not None
        assert last_request.method == "GET"
        assert test_client.client.status_code == 200
        assert unquote(last_request.url) == expected_url
        assert response_json == loads(expected_response_body)
        for path, expected in expected_fields.items():
            assert resolve(response, path) == expected, path

    @mark.parametrize(
        "method, expected_url, operation, request_fixture, response_fixture, expected_entity",
        [
            (
                "update_balance_currency",
                "/settings/balance-currency",
                UpdateBalanceCurrency(preferred=BalanceCurrencyCode.GBP),
                "request/update_balance_currency_minimal",
                "response/balance_currency_updated",
                BalanceCurrency,
            ),
            (
                "update_balance_currency",
                "/settings/balance-currency",
                UpdateBalanceCurrency(preferred=BalanceCurrencyCode.EUR),
                "request/update_balance_currency_full",
                "response/balance_currency_updated",
                BalanceCurrency,
            ),
            (
                "update_checkout_features",
                "/settings/checkout-features",
                UpdateCheckoutFeatures(discounts_enabled=True, audience_opt_in=AudienceOptIn.Choice),
                "request/update_checkout_features_minimal",
                "response/checkout_features_updated",
                CheckoutFeatures,
            ),
            (
                "update_checkout_features",
                "/settings/checkout-features",
                UpdateCheckoutFeatures(
                    discounts_enabled=False,
                    audience_opt_in=AudienceOptIn.Never,
                    saved_payment_methods_enabled=False,
                ),
                "request/update_checkout_features_full",
                "response/checkout_features_updated",
                CheckoutFeatures,
            ),
            (
                "update_checkout_payment_method_settings",
                "/settings/checkout-payment-methods",
                UpdateCheckoutPaymentMethodSettings(
                    CheckoutPaymentMethodsUpdate(
                        apple_pay=CheckoutPaymentMethodSettingUpdate(True),
                        alipay=CheckoutPaymentMethodSettingUpdate(False),
                    )
                ),
                "request/update_checkout_payment_method_settings_minimal",
                "response/checkout_payment_method_settings_updated",
                CheckoutPaymentMethodSettings,
            ),
            (
                "update_checkout_payment_method_settings",
                "/settings/checkout-payment-methods",
                UpdateCheckoutPaymentMethodSettings(
                    CheckoutPaymentMethodsUpdate(
                        **{
                            method: CheckoutPaymentMethodSettingUpdate(index % 2 == 0)
                            for index, method in enumerate(PAYMENT_METHODS)
                        }
                    )
                ),
                "request/update_checkout_payment_method_settings_full",
                "response/checkout_payment_method_settings_updated",
                CheckoutPaymentMethodSettings,
            ),
            (
                "update_checkout_recovery",
                "/settings/checkout-recovery",
                UpdateCheckoutRecovery(
                    enabled=True,
                    discount=CheckoutRecoveryDiscountUpdate(CheckoutRecoveryDiscountType.Percentage, "10"),
                ),
                "request/update_checkout_recovery_minimal",
                "response/checkout_recovery_updated",
                CheckoutRecovery,
            ),
            (
                "update_checkout_recovery",
                "/settings/checkout-recovery",
                UpdateCheckoutRecovery(
                    enabled=True,
                    discount=CheckoutRecoveryDiscountUpdate(CheckoutRecoveryDiscountType.Percentage, "15"),
                ),
                "request/update_checkout_recovery_full",
                "response/checkout_recovery_updated",
                CheckoutRecovery,
            ),
            (
                "update_checkout_recovery",
                "/settings/checkout-recovery",
                UpdateCheckoutRecovery(discount=None),
                "request/update_checkout_recovery_clear_discount",
                "response/checkout_recovery_no_discount",
                CheckoutRecovery,
            ),
            (
                "update_checkout_styles_overlay",
                "/settings/checkout-styles-overlay",
                UpdateCheckoutStylesOverlay(primary_checkout_color="#2E1065"),
                "request/update_checkout_styles_overlay_minimal",
                "response/checkout_styles_overlay_updated",
                CheckoutStylesOverlay,
            ),
            (
                "update_checkout_styles_overlay",
                "/settings/checkout-styles-overlay",
                UpdateCheckoutStylesOverlay(primary_checkout_color="#4F46E5"),
                "request/update_checkout_styles_overlay_full",
                "response/checkout_styles_overlay_updated",
                CheckoutStylesOverlay,
            ),
            (
                "update_checkout_styles_overlay",
                "/settings/checkout-styles-overlay",
                UpdateCheckoutStylesOverlay(primary_checkout_color=None),
                "request/update_checkout_styles_overlay_clear_color",
                "response/checkout_styles_overlay_unset",
                CheckoutStylesOverlay,
            ),
            (
                "update_checkout_url",
                "/settings/checkout-url",
                UpdateCheckoutUrl(default_url="https://example.com/checkout"),
                "request/update_checkout_url_minimal",
                "response/checkout_url_updated",
                CheckoutUrl,
            ),
            (
                "update_checkout_url",
                "/settings/checkout-url",
                UpdateCheckoutUrl(default_url="https://example.com/checkout"),
                "request/update_checkout_url_full",
                "response/checkout_url_updated",
                CheckoutUrl,
            ),
            (
                "update_checkout_url",
                "/settings/checkout-url",
                UpdateCheckoutUrl(default_url=None),
                "request/update_checkout_url_clear",
                "response/checkout_url_unset",
                CheckoutUrl,
            ),
            (
                "update_currency_conversions",
                "/settings/currency-conversions",
                UpdateCurrencyConversions({"GBP": CurrencyConversionUpdate(True)}),
                "request/update_currency_conversions_minimal",
                "response/currency_conversions_updated",
                CurrencyConversions,
            ),
            (
                "update_currency_conversions",
                "/settings/currency-conversions",
                UpdateCurrencyConversions(
                    {
                        "GBP": CurrencyConversionUpdate(True),
                        "USD": CurrencyConversionUpdate(False),
                        "JPY": CurrencyConversionUpdate(True),
                    }
                ),
                "request/update_currency_conversions_full",
                "response/currency_conversions_updated",
                CurrencyConversions,
            ),
            (
                "update_statement_descriptor_settings",
                "/settings/statement-descriptor",
                UpdateStatementDescriptorSettings(name="AEROEDIT"),
                "request/update_statement_descriptor_settings_minimal",
                "response/statement_descriptor_settings_updated",
                StatementDescriptorSettings,
            ),
            (
                "update_statement_descriptor_settings",
                "/settings/statement-descriptor",
                UpdateStatementDescriptorSettings(name="AERO EDIT"),
                "request/update_statement_descriptor_settings_full",
                "response/statement_descriptor_settings_updated",
                StatementDescriptorSettings,
            ),
            (
                "update_tax_settings",
                "/settings/tax",
                UpdateTaxSettings(default_tax_mode=DefaultTaxMode.Inclusive),
                "request/update_tax_settings_minimal",
                "response/tax_settings_updated",
                TaxSettings,
            ),
            (
                "update_tax_settings",
                "/settings/tax",
                UpdateTaxSettings(default_tax_mode=DefaultTaxMode.Location),
                "request/update_tax_settings_full",
                "response/tax_settings_updated",
                TaxSettings,
            ),
        ],
        ids=[
            "Update balance currency minimal",
            "Update balance currency full",
            "Update checkout features minimal",
            "Update checkout features full",
            "Update checkout payment methods minimal",
            "Update checkout payment methods full",
            "Update checkout recovery minimal",
            "Update checkout recovery full",
            "Update checkout recovery clearing discount",
            "Update checkout styles overlay minimal",
            "Update checkout styles overlay full",
            "Update checkout styles overlay clearing color",
            "Update checkout URL minimal",
            "Update checkout URL full",
            "Update checkout URL clearing default",
            "Update currency conversions minimal",
            "Update currency conversions full",
            "Update statement descriptor minimal",
            "Update statement descriptor full",
            "Update tax settings minimal",
            "Update tax settings full",
        ],
    )
    def test_update_setting_uses_expected_payload(
        self,
        test_client,
        mock_requests,
        method,
        expected_url,
        operation,
        request_fixture,
        response_fixture,
        expected_entity,
    ):
        expected_url = f"{test_client.base_url}{expected_url}"
        expected_request_body = ReadsFixtures.read_raw_json_fixture(request_fixture)
        expected_response_body = ReadsFixtures.read_raw_json_fixture(response_fixture)
        mock_requests.patch(expected_url, status_code=200, text=expected_response_body)

        response = getattr(test_client.client.settings, method)(operation)
        response_json = test_client.client.settings.response.json()
        request_json = test_client.client.payload
        last_request = mock_requests.last_request

        assert isinstance(response, expected_entity)
        assert last_request is not None
        assert last_request.method == "PATCH"
        assert test_client.client.status_code == 200
        assert unquote(last_request.url) == expected_url
        assert loads(request_json) == loads(expected_request_body)
        assert response_json == loads(expected_response_body)

    def test_update_omits_undefined_fields(self, test_client, mock_requests):
        expected_url = f"{test_client.base_url}/settings/checkout-features"
        mock_requests.patch(
            expected_url,
            status_code=200,
            text=ReadsFixtures.read_raw_json_fixture("response/checkout_features_updated"),
        )

        test_client.client.settings.update_checkout_features(UpdateCheckoutFeatures(discounts_enabled=False))

        assert loads(test_client.client.payload) == {"discounts_enabled": False}

    def test_empty_update_sends_empty_object(self, test_client, mock_requests):
        expected_url = f"{test_client.base_url}/settings/checkout-recovery"
        mock_requests.patch(
            expected_url,
            status_code=200,
            text=ReadsFixtures.read_raw_json_fixture("response/checkout_recovery_updated"),
        )

        test_client.client.settings.update_checkout_recovery(UpdateCheckoutRecovery())

        assert loads(test_client.client.payload) == {}

    def test_checkout_payment_methods_update_omits_undefined_methods(self):
        update = UpdateCheckoutPaymentMethodSettings(
            CheckoutPaymentMethodsUpdate(card=CheckoutPaymentMethodSettingUpdate(True))
        )

        assert isinstance(update.payment_methods.alipay, Undefined)

    def test_get_currency_conversions_returns_expected_response(self, test_client, mock_requests):
        expected_url = f"{test_client.base_url}/settings/currency-conversions"
        expected_response_body = ReadsFixtures.read_raw_json_fixture("response/currency_conversions")
        mock_requests.get(expected_url, status_code=200, text=expected_response_body)

        response = test_client.client.settings.get_currency_conversions()
        last_request = mock_requests.last_request

        assert isinstance(response, CurrencyConversions)
        assert last_request is not None
        assert last_request.method == "GET"
        assert unquote(last_request.url) == expected_url
        assert len(response.conversions) == 33
        assert all(isinstance(setting, CurrencyConversion) for setting in response.conversions.values())
        assert response.conversions["USD"].enabled is True
        assert response.conversions["GBP"].enabled is False
        assert response.conversions["ZAR"].enabled is False
