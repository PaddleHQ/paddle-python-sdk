from __future__                            import annotations
from dataclasses                           import dataclass
from src.Entities.Entity                   import Entity
from src.Entities.Shared.CatalogType       import CatalogType
from src.Entities.Shared.TimePeriod        import TimePeriod
from src.Entities.Shared.TaxMode           import TaxMode
from src.Entities.Shared.Money             import Money
from src.Entities.Shared.UnitPriceOverride import UnitPriceOverride
from src.Entities.Shared.PriceQuantity     import PriceQuantity
from src.Entities.Shared.Status            import Status
from src.Entities.Shared.CustomData        import CustomData
from typing                                import Optional, List


@dataclass
class Price(Entity):
    id:                 str
    productId:          str
    name:               Optional[str]
    description:        str
    type:               Optional[CatalogType]
    billingCycle:       Optional[TimePeriod]
    trialPeriod:        Optional[TimePeriod]
    taxMode:            TaxMode
    unitPrice:          Money
    unitPriceOverrides: List[UnitPriceOverride]
    quantity:           PriceQuantity
    status:             Status
    customData:         Optional[CustomData]


    @classmethod
    def from_dict(cls, data: dict) -> Price:
        return cls(
            id                 = data['id'],
            productId          = data['product_id'],
            name               = data.get('name'),
            description        = data['description'],
            type               = CatalogType(data.get('type', CatalogType.Standard.value)) if data.get('type') else None,
            billingCycle       = TimePeriod.from_dict(data['billing_cycle']) if 'billing_cycle' in data else None,
            trialPeriod        = TimePeriod.from_dict(data['trial_period']) if 'trial_period' in data else None,
            taxMode            = TaxMode(data.get('tax_mode')) if 'tax_mode' in data else None,
            unitPrice          = Money.from_dict(data['unit_price']),
            unitPriceOverrides = [UnitPriceOverride.from_dict(override) for override in data.get('unit_price_overrides', [])],
            quantity           = PriceQuantity.from_dict(data['quantity']),
            status             = Status(data['status']),
            customData         = CustomData(data['custom_data']) if 'custom_data' in data else None,
        )
