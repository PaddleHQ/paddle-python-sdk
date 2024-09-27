from paddle_billing.Entities.Transactions import (
    TransactionItemPreviewWithNonCatalogPrice,
    TransactionNonCatalogProduct,
    TransactionNonCatalogPrice,
    TransactionNonCatalogPriceWithProduct,
)

from paddle_billing.Entities.Shared import (
    CountryCode,
    CurrencyCode,
    Interval,
    Money,
    TaxCategory,
)


class TestTransactionItemPreviewWithNonCatalogPrice:
    def test_from_dict_non_catalog_price(self):
        item_preview = TransactionItemPreviewWithNonCatalogPrice.from_dict(
            {
                'quantity': 20,
                'price': {
                    'name': 'Some Name',
                    'description': 'Some Description',
                    'product': {
                        'name': 'Some Product Name',
                        'description': 'Some Product Description',
                        'tax_category': 'standard',
                        'image_url': 'https://www.example.com/image.png',
                        'custom_data': {'key': 'value'},
                    },
                    'billing_cycle': {'interval': 'year', 'frequency': 1},
                    'trial_period': {'interval': 'month', 'frequency': 3},
                    'tax_mode': 'account_setting',
                    'unit_price': {'amount': '30000', 'currency_code': 'USD'},
                    'unit_price_overrides': [
                        {
                            'unit_price': {
                                'amount': '20',
                                'currency_code': 'USD',
                            },
                            'country_codes': ['US'],
                        },
                    ],
                    'quantity': {'minimum': 10, 'maximum': 999},
                    'custom_data': {'key': 'value'},
                },
                'include_in_totals': True,
            }
        )

        assert isinstance(item_preview, TransactionItemPreviewWithNonCatalogPrice)

        assert item_preview.quantity == 20
        assert item_preview.include_in_totals == True

        price = item_preview.price

        assert isinstance(price, TransactionNonCatalogPriceWithProduct)
        assert price.name == 'Some Name'
        assert price.description == 'Some Description'
        assert price.billing_cycle.interval == Interval.Year
        assert price.billing_cycle.frequency == 1
        assert price.trial_period.interval == Interval.Month
        assert price.trial_period.frequency == 3
        assert price.unit_price.amount == '30000'
        assert price.unit_price.currency_code == CurrencyCode.USD
        assert price.unit_price_overrides[0].unit_price.amount == '20'
        assert price.unit_price_overrides[0].unit_price.currency_code == CurrencyCode.USD
        assert price.unit_price_overrides[0].country_codes == [CountryCode.US]
        assert price.quantity.minimum == 10
        assert price.quantity.maximum == 999
        assert price.custom_data.data['key'] == 'value'

        product = price.product

        assert isinstance(product, TransactionNonCatalogProduct)
        assert product.name == 'Some Product Name'
        assert product.description == 'Some Product Description'
        assert product.image_url == 'https://www.example.com/image.png'
        assert product.tax_category == TaxCategory.Standard
        assert product.custom_data.data['key'] == 'value'


    def test_from_dict_catalog_price(self):
        item_preview = TransactionItemPreviewWithNonCatalogPrice.from_dict(
            {
                'quantity': 20,
                'price': {
                    'name': 'Some Name',
                    'description': 'Some Description',
                    'product_id': "pro_01gsz4t5hdjse780zja8vvr7jg",
                    'billing_cycle': {'interval': 'year', 'frequency': 1},
                    'trial_period': {'interval': 'month', 'frequency': 3},
                    'tax_mode': 'account_setting',
                    'unit_price': {'amount': '30000', 'currency_code': 'USD'},
                    'unit_price_overrides': [
                        {
                            'unit_price': {
                                'amount': '20',
                                'currency_code': 'USD',
                            },
                            'country_codes': ['US'],
                        },
                    ],
                    'quantity': {'minimum': 10, 'maximum': 999},
                    'custom_data': {'key': 'value'},
                },
                'include_in_totals': False,
            }
        )

        assert isinstance(item_preview, TransactionItemPreviewWithNonCatalogPrice)

        assert item_preview.quantity == 20
        assert item_preview.include_in_totals == False

        price = item_preview.price

        assert isinstance(price, TransactionNonCatalogPrice)
        assert price.name == 'Some Name'
        assert price.description == 'Some Description'
        assert price.billing_cycle.interval == Interval.Year
        assert price.billing_cycle.frequency == 1
        assert price.trial_period.interval == Interval.Month
        assert price.trial_period.frequency == 3
        assert price.unit_price.amount == '30000'
        assert price.unit_price.currency_code == CurrencyCode.USD
        assert price.unit_price_overrides[0].unit_price.amount == '20'
        assert price.unit_price_overrides[0].unit_price.currency_code == CurrencyCode.USD
        assert price.unit_price_overrides[0].country_codes == [CountryCode.US]
        assert price.quantity.minimum == 10
        assert price.quantity.maximum == 999
        assert price.custom_data.data['key'] == 'value'
        assert price.product_id == 'pro_01gsz4t5hdjse780zja8vvr7jg'
