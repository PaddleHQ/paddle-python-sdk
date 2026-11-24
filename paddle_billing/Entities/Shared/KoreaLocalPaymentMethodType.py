from paddle_billing.PaddleStrEnum import (
    PaddleStrEnum as PaddleStrEnum,
    PaddleStrEnumMeta as PaddleStrEnumMeta,
    member as member,
)


class KoreaLocalPaymentMethodType(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    BC: "KoreaLocalPaymentMethodType" = member("bc")
    Citi: "KoreaLocalPaymentMethodType" = member("citi")
    Hana: "KoreaLocalPaymentMethodType" = member("hana")
    Hyundai: "KoreaLocalPaymentMethodType" = member("hyundai")
    Jeju: "KoreaLocalPaymentMethodType" = member("jeju")
    Jeonbuk: "KoreaLocalPaymentMethodType" = member("jeonbuk")
    KakaoBank: "KoreaLocalPaymentMethodType" = member("kakaobank")
    KakaoPay: "KoreaLocalPaymentMethodType" = member("kakaopay")
    KBank: "KoreaLocalPaymentMethodType" = member("kbank")
    KDBBank: "KoreaLocalPaymentMethodType" = member("kdbbank")
    Kookmin: "KoreaLocalPaymentMethodType" = member("kookmin")
    Kwangju: "KoreaLocalPaymentMethodType" = member("kwangju")
    Lotte: "KoreaLocalPaymentMethodType" = member("lotte")
    MG: "KoreaLocalPaymentMethodType" = member("mg")
    NaverPayCard: "KoreaLocalPaymentMethodType" = member("naverpaycard")
    NaverPayPoint: "KoreaLocalPaymentMethodType" = member("naverpaypoint")
    NH: "KoreaLocalPaymentMethodType" = member("nh")
    PayCo: "KoreaLocalPaymentMethodType" = member("payco")
    Post: "KoreaLocalPaymentMethodType" = member("post")
    Samsung: "KoreaLocalPaymentMethodType" = member("samsung")
    SamsungPay: "KoreaLocalPaymentMethodType" = member("samsungpay")
    SavingsBank: "KoreaLocalPaymentMethodType" = member("savingsbank")
    Shinhan: "KoreaLocalPaymentMethodType" = member("shinhan")
    Shinhyup: "KoreaLocalPaymentMethodType" = member("shinhyup")
    Suhyup: "KoreaLocalPaymentMethodType" = member("suhyup")
    TossBank: "KoreaLocalPaymentMethodType" = member("tossbank")
    Unknown: "KoreaLocalPaymentMethodType" = member("unknown")
    Woori: "KoreaLocalPaymentMethodType" = member("woori")
