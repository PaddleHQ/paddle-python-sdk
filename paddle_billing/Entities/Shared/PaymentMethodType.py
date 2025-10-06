from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta


class PaymentMethodType(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Alipay: "PaymentMethodType" = "alipay"
    ApplePay: "PaymentMethodType" = "apple_pay"
    Bancontact: "PaymentMethodType" = "bancontact"
    Blik: "PaymentMethodType" = "blik"
    Card: "PaymentMethodType" = "card"
    GooglePay: "PaymentMethodType" = "google_pay"
    Ideal: "PaymentMethodType" = "ideal"
    KoreaLocal: "PaymentMethodType" = "korea_local"
    MbWay: "PaymentMethodType" = "mb_way"
    Offline: "PaymentMethodType" = "offline"
    Paypal: "PaymentMethodType" = "paypal"
    Pix: "PaymentMethodType" = "pix"
    Unknown: "PaymentMethodType" = "unknown"
    Upi: "PaymentMethodType" = "upi"
    WireTransfer: "PaymentMethodType" = "wire_transfer"
