from typing import TYPE_CHECKING

from paddle_billing_python_sdk.ResponseParser import ResponseParser

from paddle_billing_python_sdk.Entities.PricePreview import PricePreview

from paddle_billing_python_sdk.Resources.PricingPreviews.Operations.PreviewPrice import PreviewPrice


if TYPE_CHECKING:
    from paddle_billing_python_sdk.Client import Client


class PricingPreviewsClient:
    def __init__(self, client: 'Client'):
        self.client = client


    def preview_prices(self, operation: PreviewPrice) -> PricePreview:
        response = self.client.post_raw('/pricing-preview', operation.get_parameters())
        parser   = ResponseParser(response)

        return PricePreview.from_dict(parser.get_data())
