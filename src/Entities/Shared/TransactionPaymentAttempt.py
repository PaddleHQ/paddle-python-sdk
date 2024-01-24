from __future__  import annotations
from dataclasses import dataclass
from datetime    import datetime

from src.Entities.Shared.ErrorCode            import ErrorCode
from src.Entities.Shared.MethodDetails        import MethodDetails
from src.Entities.Shared.StatusPaymentAttempt import StatusPaymentAttempt


@dataclass
class TransactionPaymentAttempt:
    payment_attempt_id:       str
    stored_payment_method_id: str
    amount:                   str
    status:                   StatusPaymentAttempt
    error_code:               ErrorCode | None
    method_details:           MethodDetails
    created_at:               datetime
    captured_at:              datetime | None


    @staticmethod
    def from_dict(data: dict) -> TransactionPaymentAttempt:
        return TransactionPaymentAttempt(
            payment_attempt_id       = data['payment_attempt_id'],
            stored_payment_method_id = data['stored_payment_method_id'],
            amount                   = data['amount'],
            status                   = StatusPaymentAttempt(data['status']),
            error_code               = ErrorCode(data['error_code']) if 'error_code' in data else None,
            method_details           = MethodDetails.from_dict(data['method_details']),
            created_at               = datetime.fromisoformat(data['created_at']),
            captured_at              = datetime.fromisoformat(data['captured_at']) if 'captured_at' in data else None,
        )
