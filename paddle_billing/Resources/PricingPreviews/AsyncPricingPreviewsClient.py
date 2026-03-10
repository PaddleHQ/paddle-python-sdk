# AUTO-GENERATED FILE — DO NOT EDIT DIRECTLY.
# Source: paddle_billing/Resources/PricingPreviews/PricingPreviewsClient.py
# Regenerate with: python scripts/generate_async_clients.py
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
        def parse(response):
            self.response = response
            return PricePreview.from_dict(ResponseParser(response).get_dict())
        return await self.client._post("/pricing-preview", operation, parse)
