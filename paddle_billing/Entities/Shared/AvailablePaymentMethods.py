from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta


class AvailablePaymentMethods(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Alipay: "AvailablePaymentMethods"     = 'alipay'
    ApplePay: "AvailablePaymentMethods"   = 'apple_pay'
    Bancontact: "AvailablePaymentMethods" = 'bancontact'
    Card: "AvailablePaymentMethods"       = 'card'
    GooglePay: "AvailablePaymentMethods"  = 'google_pay'
    Ideal: "AvailablePaymentMethods"      = 'ideal'
    Paypal: "AvailablePaymentMethods"     = 'paypal'
