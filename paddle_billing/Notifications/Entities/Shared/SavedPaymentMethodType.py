from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta


class SavedPaymentMethodType(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Alipay: "SavedPaymentMethodType" = "alipay"
    ApplePay: "SavedPaymentMethodType" = "apple_pay"
    Blik: "SavedPaymentMethodType" = "blik"
    Card: "SavedPaymentMethodType" = "card"
    GooglePay: "SavedPaymentMethodType" = "google_pay"
    KoreaLocal: "SavedPaymentMethodType" = "korea_local"
    MbWay: "SavedPaymentMethodType" = "mb_way"
    Paypal: "SavedPaymentMethodType" = "paypal"
    Pix: "SavedPaymentMethodType" = "pix"
    Upi: "SavedPaymentMethodType" = "upi"
