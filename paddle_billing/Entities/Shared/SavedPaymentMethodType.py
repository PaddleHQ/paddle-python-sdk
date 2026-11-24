from paddle_billing.PaddleStrEnum import (
    PaddleStrEnum as PaddleStrEnum,
    PaddleStrEnumMeta as PaddleStrEnumMeta,
    member as member,
)


class SavedPaymentMethodType(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Alipay: "SavedPaymentMethodType" = member("alipay")
    ApplePay: "SavedPaymentMethodType" = member("apple_pay")
    Blik: "SavedPaymentMethodType" = member("blik")
    Card: "SavedPaymentMethodType" = member("card")
    GooglePay: "SavedPaymentMethodType" = member("google_pay")
    KakaoPay: "SavedPaymentMethodType" = member("kakao_pay")
    KoreaLocal: "SavedPaymentMethodType" = member("korea_local")
    MbWay: "SavedPaymentMethodType" = member("mb_way")
    NaverPay: "SavedPaymentMethodType" = member("naver_pay")
    Payco: "SavedPaymentMethodType" = member("payco")
    Paypal: "SavedPaymentMethodType" = member("paypal")
    Pix: "SavedPaymentMethodType" = member("pix")
    SamsungPay: "SavedPaymentMethodType" = member("samsung_pay")
    SouthKoreaLocalCard: "SavedPaymentMethodType" = member("south_korea_local_card")
    Upi: "SavedPaymentMethodType" = member("upi")
    WechatPay: "SavedPaymentMethodType" = member("wechat_pay")
