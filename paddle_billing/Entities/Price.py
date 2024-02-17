from __future__  import annotations
from dataclasses import dataclass

from paddle_billing.Entities.Entity  import Entity

from paddle_billing.Entities.Shared import (
    CatalogType,
    CustomData,
    ImportMeta,
    Money,
    PriceQuantity,
    Status,
    TaxMode,
    TimePeriod,
    UnitPriceOverride,
)

from paddle_billing.Logger import get_logger
log = get_logger()


@dataclass
class Price(Entity):
    id:                   str
    product_id:           str
    name:                 str | None
    description:          str
    type:                 CatalogType | None
    billing_cycle:        TimePeriod  | None
    trial_period:         TimePeriod  | None
    tax_mode:             TaxMode
    unit_price:           Money
    unit_price_overrides: list[UnitPriceOverride]
    quantity:             PriceQuantity
    status:               Status
    custom_data:          CustomData | None
    import_meta:          ImportMeta | None
    product:              Product    | None


    @classmethod
    def from_dict(cls, data: dict) -> Price:
        return Price(
            id                   = data['id'],
            product_id           = data['product_id'],
            name                 = data.get('name'),
            description          = data['description'],
            unit_price           = Money.from_dict(data['unit_price']),
            quantity             = PriceQuantity.from_dict(data['quantity']),
            status               = Status(data['status']),
            tax_mode             = TaxMode(data.get('tax_mode')),
            unit_price_overrides = [UnitPriceOverride.from_dict(override) for override in data.get('unit_price_overrides', [])],
            type                 = CatalogType(data.get('type'))               if data.get('type')          else None,
            billing_cycle        = TimePeriod.from_dict(data['billing_cycle']) if data.get('billing_cycle') else None,
            trial_period         = TimePeriod.from_dict(data['trial_period'])  if data.get('trial_period')  else None,
            custom_data          = CustomData(data['custom_data'])             if data.get('custom_data')   else None,
            import_meta          = ImportMeta.from_dict(data['import_meta'])   if data.get('import_meta')   else None,
            product              = Product.from_dict(data['product'])          if data.get('product')       else None,
        )



# Prevents circular import
from paddle_billing.Entities.Product import Product  # noqa E402
