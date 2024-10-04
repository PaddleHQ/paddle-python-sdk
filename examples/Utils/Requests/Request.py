from pathlib import Path

from paddle_billing.Notifications.Requests import Headers


class Request:
    def __init__(self, headers: Headers, body: bytes | str):
        self.headers = headers if headers is not None else {}
        self.body = body.encode() if isinstance(body, str) else body

    @staticmethod
    def create_from_fixture(filename: str, headers: Headers) -> "Request":
        fixture_path = Path(__file__).parent.parent.parent / "_fixtures" / filename

        fixture_data = None
        with fixture_path.open("r") as file:
            fixture_data = file.read().strip()

        return Request(headers=headers, body=fixture_data)
