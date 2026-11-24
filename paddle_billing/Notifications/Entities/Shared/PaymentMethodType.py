from paddle_billing.PaddleStrEnum import (
    PaddleStrEnum as PaddleStrEnum,
    PaddleStrEnumMeta as PaddleStrEnumMeta,
    member as member,
)


class PaymentMethodType(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Alipay: "PaymentMethodType" = member("alipay")
    ApplePay: "PaymentMethodType" = member("apple_pay")
    Bancontact: "PaymentMethodType" = member("bancontact")
    Blik: "PaymentMethodType" = member("blik")
    Card: "PaymentMethodType" = member("card")
    GooglePay: "PaymentMethodType" = member("google_pay")
    Ideal: "PaymentMethodType" = member("ideal")
    KakaoPay: "PaymentMethodType" = member("kakao_pay")
    KoreaLocal: "PaymentMethodType" = member("korea_local")
    MbWay: "PaymentMethodType" = member("mb_way")
    NaverPay: "PaymentMethodType" = member("naver_pay")
    Offline: "PaymentMethodType" = member("offline")
    Payco: "PaymentMethodType" = member("payco")
    Paypal: "PaymentMethodType" = member("paypal")
    Pix: "PaymentMethodType" = member("pix")
    SamsungPay: "PaymentMethodType" = member("samsung_pay")
    SouthKoreaLocalCard: "PaymentMethodType" = member("south_korea_local_card")
    Unknown: "PaymentMethodType" = member("unknown")
    Upi: "PaymentMethodType" = member("upi")
    WechatPay: "PaymentMethodType" = member("wechat_pay")
    WireTransfer: "PaymentMethodType" = member("wire_transfer")
