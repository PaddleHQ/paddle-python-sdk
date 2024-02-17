from paddle_billing.PaddleStrEnum import PaddleStrEnum


class TaxMode(PaddleStrEnum):
    AccountSetting = 'account_setting'
    External       = 'external'
    Internal       = 'internal'
