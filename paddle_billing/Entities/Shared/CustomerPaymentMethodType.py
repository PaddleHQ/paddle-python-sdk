from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta


class CustomerPaymentMethodType(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Alipay: "CustomerPaymentMethodType" = "alipay"
    ApplePay: "CustomerPaymentMethodType" = "apple_pay"
    Card: "CustomerPaymentMethodType" = "card"
    GooglePay: "CustomerPaymentMethodType" = "google_pay"
    Paypal: "CustomerPaymentMethodType" = "paypal"
