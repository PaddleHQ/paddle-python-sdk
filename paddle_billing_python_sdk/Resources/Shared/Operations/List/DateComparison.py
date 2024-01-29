from datetime import datetime

from paddle_billing_python_sdk.Entities.DateTime import DateTime

from paddle_billing_python_sdk.Resources.Shared.Operations.List.Comparator import Comparator


class DateComparison:
    def __init__(
        self,
        date:       datetime | str,
        comparator: Comparator = None,
    ):
        self.date       = DateTime.from_datetime(date)
        self.comparator = comparator


    def comparator(self) -> str:
        return f"[{self.comparator.value}]" if self.comparator else ''


    def formatted(self) -> str:
        return self.date.format() if self.date else ''
