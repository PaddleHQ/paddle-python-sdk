from paddle_billing.PaddleStrEnum import PaddleStrEnum


class AvailablePaymentMethods(PaddleStrEnum):
    Alipay     = 'alipay'
    ApplePay   = 'apple_pay'
    Bancontact = 'bancontact'
    Card       = 'card'
    GooglePay  = 'google_pay'
    Ideal      = 'ideal'
    Paypal     = 'paypal'
