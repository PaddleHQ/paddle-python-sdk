from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta


class SavedPaymentMethodType(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Alipay: "SavedPaymentMethodType" = "alipay"
    ApplePay: "SavedPaymentMethodType" = "apple_pay"
    Blik: "SavedPaymentMethodType" = "blik"
    Card: "SavedPaymentMethodType" = "card"
    GooglePay: "SavedPaymentMethodType" = "google_pay"
    KakaoPay: "SavedPaymentMethodType" = "kakao_pay"
    KoreaLocal: "SavedPaymentMethodType" = "korea_local"
    MbWay: "SavedPaymentMethodType" = "mb_way"
    NaverPay: "SavedPaymentMethodType" = "naver_pay"
    Payco: "SavedPaymentMethodType" = "payco"
    Paypal: "SavedPaymentMethodType" = "paypal"
    Pix: "SavedPaymentMethodType" = "pix"
    SamsungPay: "SavedPaymentMethodType" = "samsung_pay"
    SouthKoreaLocalCard: "SavedPaymentMethodType" = "south_korea_local_card"
    Upi: "SavedPaymentMethodType" = "upi"
    WechatPay: "SavedPaymentMethodType" = "wechat_pay"
