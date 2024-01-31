from datetime import datetime, timedelta, timezone


class DateTime:
    PADDLE_RFC3339_UTC    = '%Y-%m-%dT%H:%M:%S.%fZ'   # trailing Z for UTC
    PADDLE_RFC3339_OFFSET = '%Y-%m-%dT%H:%M:%S.%f%z'  # actual timezone offset when not UTC
    PADDLE_RFC3339        = PADDLE_RFC3339_UTC        # default to UTC


    def __init__(self, datetime_str: str = 'now'):
        if datetime_str == 'now':
            self._datetime = datetime.now(timezone.utc)
        else:
            self._datetime = datetime.fromisoformat(datetime_str).replace(tzinfo=timezone.utc)


    @property
    def as_datetime(self):
        return self._datetime


    def format(self, fmt: str | None = None) -> str:
        """Returns a RFC3339 formatted datetime string, and handles trailing Z"""
        if self._datetime.tzinfo == timezone.utc or self._datetime.utcoffset() == timedelta(0):
            return f"{self._datetime.strftime(fmt if fmt is not None else self.PADDLE_RFC3339)}"
        else:
            return f"{self._datetime.strftime(fmt if fmt is not None else self.PADDLE_RFC3339_OFFSET)}"


    @classmethod
    def from_datetime(cls, date: datetime | str):
        if isinstance(date, str) and date == '0001-01-01T00:00:00Z':
            return None

        date_str = date if isinstance(date, str) else date.strftime(cls.PADDLE_RFC3339)
        try:
            return cls(date_str)
        except Exception:
            return None


    def __str__(self):
        return self.format()
