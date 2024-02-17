from __future__  import annotations
from dataclasses import dataclass

from paddle_billing.Notifications.Entities.Shared.ChargebackFee       import ChargebackFee
from paddle_billing.Notifications.Entities.Shared.CurrencyCodePayouts import CurrencyCodePayouts


@dataclass
class TransactionPayoutTotalsAdjusted:
    subtotal:       str
    tax:            str
    total:          str
    fee:            str
    chargeback_fee: ChargebackFee
    earnings:       str
    currency_code:  CurrencyCodePayouts


    @staticmethod
    def from_dict(data: dict) -> TransactionPayoutTotalsAdjusted:
        return TransactionPayoutTotalsAdjusted(
            subtotal       = data['subtotal'],
            tax            = data['tax'],
            total          = data['total'],
            fee            = data['fee'],
            chargeback_fee = ChargebackFee.from_dict(data['chargeback_fee']),
            earnings       = data['earnings'],
            currency_code  = CurrencyCodePayouts(data['currency_code']),
        )
