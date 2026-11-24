from __future__ import annotations
from dataclasses import dataclass

from paddle_billing.Undefined import Undefined as Undefined
from paddle_billing.Entities.Shared.CustomData import CustomData as CustomData
from paddle_billing.Entities.Shared.TaxCategory import TaxCategory as TaxCategory


@dataclass
class TransactionNonCatalogProduct:
    name: str
    tax_category: TaxCategory
    description: str | None | Undefined = Undefined()
    image_url: str | None | Undefined = Undefined()
    custom_data: CustomData | None | Undefined = Undefined()
