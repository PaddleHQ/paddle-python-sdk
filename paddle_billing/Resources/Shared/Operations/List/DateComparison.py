from datetime import datetime

from paddle_billing.Entities.DateTime import DateTime

from paddle_billing.Resources.Shared.Operations.List.Comparator import Comparator


class DateComparison:
    def __init__(
        self,
        date:       datetime,
        comparator: Comparator | None = None,
    ):
        self.date       = date
        self._comparator = comparator


    @property
    def comparator(self) -> str:
        return f"[{self._comparator.value}]" if self._comparator else ''


    def formatted(self) -> str:
        if isinstance(self.date, datetime):
            date_obj = DateTime.from_datetime(self.date)
        elif isinstance(self.date, DateTime):
            date_obj = self.date
        else:
            raise TypeError(f"Invalid '{type(self.date)}' type for date")

        return date_obj.format() if date_obj else ''
