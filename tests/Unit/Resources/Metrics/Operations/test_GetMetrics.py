from pytest import mark, raises

from paddle_billing.Resources.Metrics.Operations import GetMetrics


class TestGetMetrics:
    def test_accepts_valid_date_strings(self):
        operation = GetMetrics(date_from="2025-09-01", date_to="2025-09-05")

        assert operation.get_parameters() == {"from": "2025-09-01", "to": "2025-09-05"}

    @mark.parametrize(
        "date_from, date_to",
        [
            ("2025-09-01T00:00:00Z", "2025-09-05"),
            ("2025-09-01", "2025-09-05T23:59:59Z"),
            ("2025-09-01T00:00:00.000000Z", "2025-09-05"),
        ],
        ids=[
            "date_from with datetime",
            "date_to with datetime",
            "date_from with microseconds",
        ],
    )
    def test_rejects_datetime_strings(self, date_from, date_to):
        with raises(ValueError, match="YYYY-MM-DD format"):
            GetMetrics(date_from=date_from, date_to=date_to)

    @mark.parametrize(
        "date_from, date_to",
        [
            ("not-a-date", "2025-09-05"),
            ("2025-09-01", "invalid"),
            ("", "2025-09-05"),
            ("2025/09/01", "2025-09-05"),
            ("01-09-2025", "2025-09-05"),
        ],
        ids=[
            "date_from not a date",
            "date_to not a date",
            "date_from empty string",
            "date_from wrong separator",
            "date_from wrong order",
        ],
    )
    def test_rejects_invalid_date_strings(self, date_from, date_to):
        with raises(ValueError, match="YYYY-MM-DD format"):
            GetMetrics(date_from=date_from, date_to=date_to)
