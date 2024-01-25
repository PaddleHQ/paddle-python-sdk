from datetime import datetime, timezone


class DateTime:
    PADDLE_RFC3339 = '%Y-%m-%dT%H:%M:%S.%f'

    def __init__(self, datetime_str='now'):
        self._datetime = datetime.now(timezone.utc) \
            if datetime_str == 'now' \
            else datetime.fromisoformat(datetime_str).replace(tzinfo=timezone.utc)


    def format(self, fmt=None):
        if fmt is None:
            fmt = self.PADDLE_RFC3339
        return self._datetime.strftime(fmt)


    @classmethod
    def from_datetime(cls, date):
        if isinstance(date, str) and date == '0001-01-01T00:00:00Z':
            return None

        date_str = date if isinstance(date, str) else date.strftime(cls.PADDLE_RFC3339)
        try:
            return cls(date_str)
        except Exception:
            return None
