from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta, member


class SavedPaymentMethodDeletionReason(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    ReplacedByNewerVersion: "SavedPaymentMethodDeletionReason" = member("replaced_by_newer_version")
    Api: "SavedPaymentMethodDeletionReason" = member("api")
