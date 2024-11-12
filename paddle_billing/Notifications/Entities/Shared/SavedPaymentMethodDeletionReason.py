from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta


class SavedPaymentMethodDeletionReason(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    ReplacedByNewerVersion: "SavedPaymentMethodDeletionReason" = "replaced_by_newer_version"
    Api: "SavedPaymentMethodDeletionReason" = "api"
