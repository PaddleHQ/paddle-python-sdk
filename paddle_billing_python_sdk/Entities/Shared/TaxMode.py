from enum import StrEnum


class TaxMode(StrEnum):
    AccountSetting = 'account_setting'
    External       = 'external'
    Internal       = 'internal'
