from dataclasses import dataclass

from paddle_billing.Undefined import Undefined
from paddle_billing.Entities.Settings.CheckoutPaymentMethodSettingUpdate import CheckoutPaymentMethodSettingUpdate


@dataclass
class CheckoutPaymentMethodsUpdate:
    alipay: CheckoutPaymentMethodSettingUpdate | Undefined = Undefined()
    apple_pay: CheckoutPaymentMethodSettingUpdate | Undefined = Undefined()
    bancontact: CheckoutPaymentMethodSettingUpdate | Undefined = Undefined()
    blik: CheckoutPaymentMethodSettingUpdate | Undefined = Undefined()
    card: CheckoutPaymentMethodSettingUpdate | Undefined = Undefined()
    google_pay: CheckoutPaymentMethodSettingUpdate | Undefined = Undefined()
    ideal: CheckoutPaymentMethodSettingUpdate | Undefined = Undefined()
    kakao_pay: CheckoutPaymentMethodSettingUpdate | Undefined = Undefined()
    mb_way: CheckoutPaymentMethodSettingUpdate | Undefined = Undefined()
    naver_pay: CheckoutPaymentMethodSettingUpdate | Undefined = Undefined()
    payco: CheckoutPaymentMethodSettingUpdate | Undefined = Undefined()
    paypal: CheckoutPaymentMethodSettingUpdate | Undefined = Undefined()
    pix: CheckoutPaymentMethodSettingUpdate | Undefined = Undefined()
    samsung_pay: CheckoutPaymentMethodSettingUpdate | Undefined = Undefined()
    south_korea_local_card: CheckoutPaymentMethodSettingUpdate | Undefined = Undefined()
    upi: CheckoutPaymentMethodSettingUpdate | Undefined = Undefined()
    wechat_pay: CheckoutPaymentMethodSettingUpdate | Undefined = Undefined()
