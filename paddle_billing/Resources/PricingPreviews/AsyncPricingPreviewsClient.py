from paddle_billing.ResponseParser import ResponseParser

from paddle_billing.Entities.PricePreview import PricePreview
from paddle_billing.Resources.PricingPreviews.Operations import PreviewPrice

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from paddle_billing.AsyncClient import AsyncClient


class AsyncPricingPreviewsClient:
    def __init__(self, client: "AsyncClient"):
        self.client = client
        self.response = None

    async def preview_prices(self, operation: PreviewPrice) -> PricePreview:
        self.response = await self.client.post_raw("/pricing-preview", operation)
        parser = ResponseParser(self.response)

        return PricePreview.from_dict(parser.get_dict())
