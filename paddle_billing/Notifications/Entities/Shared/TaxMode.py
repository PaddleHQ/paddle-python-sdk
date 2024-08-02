from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta


class TaxMode(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    AccountSetting = 'account_setting'
    External       = 'external'
    Internal       = 'internal'
