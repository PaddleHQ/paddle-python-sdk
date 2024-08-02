from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta


class Status(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Active   = 'active'
    Archived = 'archived'
