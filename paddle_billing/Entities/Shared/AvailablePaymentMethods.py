from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta


class AvailablePaymentMethods(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Alipay     = 'alipay'
    ApplePay   = 'apple_pay'
    Bancontact = 'bancontact'
    Card       = 'card'
    GooglePay  = 'google_pay'
    Ideal      = 'ideal'
    Paypal     = 'paypal'
