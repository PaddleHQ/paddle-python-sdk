from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta


class SavedPaymentMethodType(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Alipay: "SavedPaymentMethodType" = "alipay"
    ApplePay: "SavedPaymentMethodType" = "apple_pay"
    Card: "SavedPaymentMethodType" = "card"
    GooglePay: "SavedPaymentMethodType" = "google_pay"
    Paypal: "SavedPaymentMethodType" = "paypal"
