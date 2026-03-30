from datetime import date

from paddle_billing.HasParameters import HasParameters


class GetMetrics(HasParameters):
    def __init__(
        self,
        date_from: str,
        date_to: str,
    ):
        self.date_from = date_from
        self.date_to = date_to

        for field_name, field_value in [
            ("date_from", self.date_from),
            ("date_to", self.date_to),
        ]:
            try:
                date.fromisoformat(field_value)
            except (ValueError, TypeError):
                raise ValueError(f"'{field_name}' must be a date string in YYYY-MM-DD format, got '{field_value}'")

            if "T" in field_value:
                raise ValueError(
                    f"'{field_name}' must be a date string in YYYY-MM-DD format without time, got '{field_value}'"
                )

    def get_parameters(self) -> dict[str, str]:
        return {
            "from": self.date_from,
            "to": self.date_to,
        }
