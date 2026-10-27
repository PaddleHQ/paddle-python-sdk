from __future__ import annotations
from dataclasses import dataclass
from typing import Any

from paddle_billing.Entities.Settings.CheckoutPaymentMethodSetting import CheckoutPaymentMethodSetting


@dataclass
class CheckoutPaymentMethods:
    alipay: CheckoutPaymentMethodSetting
    apple_pay: CheckoutPaymentMethodSetting
    bancontact: CheckoutPaymentMethodSetting
    blik: CheckoutPaymentMethodSetting
    card: CheckoutPaymentMethodSetting
    google_pay: CheckoutPaymentMethodSetting
    ideal: CheckoutPaymentMethodSetting
    kakao_pay: CheckoutPaymentMethodSetting
    mb_way: CheckoutPaymentMethodSetting
    naver_pay: CheckoutPaymentMethodSetting
    payco: CheckoutPaymentMethodSetting
    paypal: CheckoutPaymentMethodSetting
    pix: CheckoutPaymentMethodSetting
    samsung_pay: CheckoutPaymentMethodSetting
    south_korea_local_card: CheckoutPaymentMethodSetting
    upi: CheckoutPaymentMethodSetting
    wechat_pay: CheckoutPaymentMethodSetting

    @staticmethod
    def from_dict(data: dict[str, Any]) -> CheckoutPaymentMethods:
        return CheckoutPaymentMethods(
            alipay=CheckoutPaymentMethodSetting.from_dict(data["alipay"]),
            apple_pay=CheckoutPaymentMethodSetting.from_dict(data["apple_pay"]),
            bancontact=CheckoutPaymentMethodSetting.from_dict(data["bancontact"]),
            blik=CheckoutPaymentMethodSetting.from_dict(data["blik"]),
            card=CheckoutPaymentMethodSetting.from_dict(data["card"]),
            google_pay=CheckoutPaymentMethodSetting.from_dict(data["google_pay"]),
            ideal=CheckoutPaymentMethodSetting.from_dict(data["ideal"]),
            kakao_pay=CheckoutPaymentMethodSetting.from_dict(data["kakao_pay"]),
            mb_way=CheckoutPaymentMethodSetting.from_dict(data["mb_way"]),
            naver_pay=CheckoutPaymentMethodSetting.from_dict(data["naver_pay"]),
            payco=CheckoutPaymentMethodSetting.from_dict(data["payco"]),
            paypal=CheckoutPaymentMethodSetting.from_dict(data["paypal"]),
            pix=CheckoutPaymentMethodSetting.from_dict(data["pix"]),
            samsung_pay=CheckoutPaymentMethodSetting.from_dict(data["samsung_pay"]),
            south_korea_local_card=CheckoutPaymentMethodSetting.from_dict(data["south_korea_local_card"]),
            upi=CheckoutPaymentMethodSetting.from_dict(data["upi"]),
            wechat_pay=CheckoutPaymentMethodSetting.from_dict(data["wechat_pay"]),
        )
