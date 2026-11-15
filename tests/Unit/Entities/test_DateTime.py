from datetime import datetime, timedelta, timezone

from paddle_billing.Entities.DateTime import DateTime


def test_utc_z_string_round_trip():
    assert DateTime("2024-01-01T12:00:00+00:00").format() == "2024-01-01T12:00:00.000000Z"


def test_string_with_positive_offset_is_converted_to_utc():
    value = DateTime.from_datetime("2024-01-01T12:00:00+02:00")
    assert value.as_datetime == datetime(2024, 1, 1, 10, 0, tzinfo=timezone.utc)
    assert value.format() == "2024-01-01T10:00:00.000000Z"


def test_string_with_negative_offset_is_converted_to_utc():
    value = DateTime("2024-01-01T12:00:00-05:00")
    assert value.as_datetime == datetime(2024, 1, 1, 17, 0, tzinfo=timezone.utc)
    assert value.format() == "2024-01-01T17:00:00.000000Z"


def test_aware_datetime_with_offset_is_converted_to_utc():
    local = datetime(2024, 1, 1, 12, 0, tzinfo=timezone(timedelta(hours=2)))
    value = DateTime.from_datetime(local)
    assert value.as_datetime == datetime(2024, 1, 1, 10, 0, tzinfo=timezone.utc)
    assert str(value) == "2024-01-01T10:00:00.000000Z"


def test_aware_datetime_with_negative_offset_is_converted_to_utc():
    local = datetime(2024, 1, 1, 12, 0, tzinfo=timezone(timedelta(hours=-5, minutes=-30)))
    assert DateTime.from_datetime(local).to_json() == "2024-01-01T17:30:00.000000Z"


def test_naive_datetime_is_treated_as_utc():
    assert DateTime.from_datetime(datetime(2024, 1, 1, 12, 0)).to_json() == "2024-01-01T12:00:00.000000Z"
