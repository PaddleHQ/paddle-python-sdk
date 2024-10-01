from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta


class PaymentMethodType(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Alipay: "PaymentMethodType" = "alipay"
    ApplePay: "PaymentMethodType" = "apple_pay"
    Bancontact: "PaymentMethodType" = "bancontact"
    Card: "PaymentMethodType" = "card"
    GooglePay: "PaymentMethodType" = "google_pay"
    Ideal: "PaymentMethodType" = "ideal"
    Offline: "PaymentMethodType" = "offline"
    Paypal: "PaymentMethodType" = "paypal"
    Unknown: "PaymentMethodType" = "unknown"
    WireTransfer: "PaymentMethodType" = "wire_transfer"
