from paddle_billing.PaddleStrEnum import (
    PaddleStrEnum as PaddleStrEnum,
    PaddleStrEnumMeta as PaddleStrEnumMeta,
    member as member,
)


class SouthKoreaLocalCardType(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    BC: "SouthKoreaLocalCardType" = member("bc")
    Citi: "SouthKoreaLocalCardType" = member("citi")
    Hana: "SouthKoreaLocalCardType" = member("hana")
    Hyundai: "SouthKoreaLocalCardType" = member("hyundai")
    Jeju: "SouthKoreaLocalCardType" = member("jeju")
    Jeonbuk: "SouthKoreaLocalCardType" = member("jeonbuk")
    KakaoBank: "SouthKoreaLocalCardType" = member("kakaobank")
    KBank: "SouthKoreaLocalCardType" = member("kbank")
    KDBBank: "SouthKoreaLocalCardType" = member("kdbbank")
    Kookmin: "SouthKoreaLocalCardType" = member("kookmin")
    Kwangju: "SouthKoreaLocalCardType" = member("kwangju")
    Lotte: "SouthKoreaLocalCardType" = member("lotte")
    MG: "SouthKoreaLocalCardType" = member("mg")
    NH: "SouthKoreaLocalCardType" = member("nh")
    Post: "SouthKoreaLocalCardType" = member("post")
    Samsung: "SouthKoreaLocalCardType" = member("samsung")
    SavingsBank: "SouthKoreaLocalCardType" = member("savingsbank")
    Shinhan: "SouthKoreaLocalCardType" = member("shinhan")
    Shinhyup: "SouthKoreaLocalCardType" = member("shinhyup")
    Suhyup: "SouthKoreaLocalCardType" = member("suhyup")
    TossBank: "SouthKoreaLocalCardType" = member("tossbank")
    Unknown: "SouthKoreaLocalCardType" = member("unknown")
    Woori: "SouthKoreaLocalCardType" = member("woori")
