from __future__  import annotations
from dataclasses import dataclass
from typing      import Optional

from src.Entities.Shared.ChargebackFee       import ChargebackFee
from src.Entities.Shared.CurrencyCodePayouts import CurrencyCodePayouts


@dataclass
class PayoutTotalsAdjustment:
    subtotal:      str
    tax:           str
    total:         str
    fee:           str
    chargebackFee: Optional[ChargebackFee]
    earnings:      str
    currencyCode:  CurrencyCodePayouts


    @staticmethod
    def from_dict(data: dict) -> PayoutTotalsAdjustment:
        chargeback_fee = ChargebackFee.from_dict(data['chargeback_fee']) \
            if 'chargeback_fee' in data and data['chargeback_fee'] != '' \
            else None

        return PayoutTotalsAdjustment(
            subtotal      = data['subtotal'],
            tax           = data['tax'],
            total         = data['total'],
            fee           = data['fee'],
            chargebackFee = chargeback_fee,
            earnings      = data['earnings'],
            currencyCode  = CurrencyCodePayouts(data['currency_code']),
        )
