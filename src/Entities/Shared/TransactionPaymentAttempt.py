from __future__            import annotations
from .ErrorCode            import ErrorCode
from .MethodDetails        import MethodDetails
from .StatusPaymentAttempt import StatusPaymentAttempt
from dataclasses           import dataclass
from datetime              import datetime
from typing                import Optional


@dataclass
class TransactionPaymentAttempt:
    paymentAttemptId:      str
    storedPaymentMethodId: str
    amount:                str
    status:                StatusPaymentAttempt
    errorCode:             Optional[ErrorCode]
    methodDetails:         MethodDetails
    createdAt:             datetime
    capturedAt:            Optional[datetime]


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
