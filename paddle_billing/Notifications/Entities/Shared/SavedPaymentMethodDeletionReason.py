from paddle_billing.PaddleStrEnum import (
    PaddleStrEnum as PaddleStrEnum,
    PaddleStrEnumMeta as PaddleStrEnumMeta,
    member as member,
)


class SavedPaymentMethodDeletionReason(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    ReplacedByNewerVersion: "SavedPaymentMethodDeletionReason" = member("replaced_by_newer_version")
    Api: "SavedPaymentMethodDeletionReason" = member("api")
