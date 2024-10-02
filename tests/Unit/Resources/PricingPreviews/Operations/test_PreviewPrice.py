from pytest import mark, raises

from paddle_billing.Resources.PricingPreviews.Operations import PreviewPrice

from paddle_billing.Exceptions.SdkExceptions.InvalidArgumentException import InvalidArgumentException


class TestPreviewPrice:
    @mark.parametrize(
        "invalid_items, expected_message",
        [
            (
                [],
                "'items' cannot be empty",
            ),
            (
                ["some invalid type"],
                "Expected 'items' to only contain type 'PricePreviewItem' ('str' given)",
            ),
        ],
        ids=[
            "Empty items",
            "Invalid item type",
        ],
    )
    def test_raises_invalid_argument_exception_for_invalid_items(self, invalid_items, expected_message):
        with raises(InvalidArgumentException) as exception_info:
            PreviewPrice(invalid_items)

        assert str(exception_info.value) == expected_message
