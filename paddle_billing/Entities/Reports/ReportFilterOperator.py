from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta


class ReportFilterOperator(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Lt  = 'lt'
    Gte = 'gte'
