from __future__  import annotations
from dataclasses import dataclass
from datetime    import datetime

from src.Entities.Shared.ErrorCode            import ErrorCode
from src.Entities.Shared.MethodDetails        import MethodDetails
from src.Entities.Shared.StatusPaymentAttempt import StatusPaymentAttempt


@dataclass
class TransactionPaymentAttempt:
    paymentAttemptId:      str
    storedPaymentMethodId: str
    amount:                str
    status:                StatusPaymentAttempt
    errorCode:             ErrorCode | None
    methodDetails:         MethodDetails
    createdAt:             datetime
    capturedAt:            datetime | None


    @staticmethod
    def from_dict(data: dict) -> TransactionPaymentAttempt:
        return TransactionPaymentAttempt(
            paymentAttemptId      = data['payment_attempt_id'],
            storedPaymentMethodId = data['stored_payment_method_id'],
            amount                = data['amount'],
            status                = StatusPaymentAttempt(data['status']),
            errorCode             = ErrorCode(data['error_code']) if data.get('error_code') else None,
            methodDetails         = MethodDetails.from_dict(data['method_details']),
            createdAt             = datetime.fromisoformat(data['created_at']),
            capturedAt            = datetime.fromisoformat(data['captured_at']) if data.get('captured_at') else None,
        )
