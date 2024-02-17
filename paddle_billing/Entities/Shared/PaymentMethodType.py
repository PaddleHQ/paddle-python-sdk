from paddle_billing.PaddleStrEnum import PaddleStrEnum


class PaymentMethodType(PaddleStrEnum):
    Alipay       = 'alipay'
    ApplePay     = 'apple_pay'
    Bancontact   = 'bancontact'
    Card         = 'card'
    GooglePay    = 'google_pay'
    Ideal        = 'ideal'
    Offline      = 'offline'
    Paypal       = 'paypal'
    Unknown      = 'unknown'
    WireTransfer = 'wire_transfer'
    Visa         = 'visa'
