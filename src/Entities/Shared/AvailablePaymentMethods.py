from enum import StrEnum


class AvailablePaymentMethods(StrEnum):
    Alipay     = 'alipay'
    ApplePay   = 'apple_pay'
    Bancontact = 'bancontact'
    Card       = 'card'
    GooglePay  = 'google_pay'
    Ideal      = 'ideal'
    Paypal     = 'paypal'
