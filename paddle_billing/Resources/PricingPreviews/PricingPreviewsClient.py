from paddle_billing.ResponseParser                       import ResponseParser
from paddle_billing.Entities.PricePreview                import PricePreview
from paddle_billing.Resources.PricingPreviews.Operations import PreviewPrice

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from paddle_billing.Client import Client


class PricingPreviewsClient:
    def __init__(self, client: 'Client'):
        self.client   = client
        self.response = None


    def preview_prices(self, operation: PreviewPrice) -> PricePreview:
        self.response = self.client.post_raw('/pricing-preview', operation.get_parameters())
        parser        = ResponseParser(self.response)

        return PricePreview.from_dict(parser.get_data())
