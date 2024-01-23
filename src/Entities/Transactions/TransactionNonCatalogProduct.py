from __future__  import annotations
from dataclasses import dataclass

from src.Entities.Shared.TaxCategory import TaxCategory
from src.Entities.Shared.CustomData import CustomData


@dataclass
class TransactionNonCatalogProduct:
    name:        str
    description: str | None
    taxCategory: TaxCategory
    imageUrl:    str | None
    customData:  CustomData | None
