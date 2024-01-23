from __future__  import annotations
from dataclasses import dataclass

from src.Entities.Shared.TimePeriod        import TimePeriod
from src.Entities.Shared.TaxMode           import TaxMode
from src.Entities.Shared.Money             import Money
from src.Entities.Shared.PriceQuantity     import PriceQuantity
from src.Entities.Shared.CustomData        import CustomData
from src.Entities.Shared.UnitPriceOverride import UnitPriceOverride


@dataclass
class TransactionNonCatalogPrice:
    description:        str
    name:               str | None
    billingCycle:       TimePeriod | None
    trialPeriod:        TimePeriod | None
    taxMode:            TaxMode
    unitPrice:          Money
    unitPriceOverrides: list[UnitPriceOverride]
    quantity:           PriceQuantity
    customData:         CustomData | None
    productId:          str
