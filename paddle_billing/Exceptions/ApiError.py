from paddle_billing.Exceptions.FieldError import FieldError

from requests import HTTPError, Response


class ApiError(HTTPError):
    def __init__(self, response: Response, error_type: str, error_code: str, detail: str, docs_url: str, *field_errors):
        super().__init__(detail, response=response)
        self.error_type = error_type
        self.error_code = error_code
        self.detail = detail
        self.docs_url = docs_url
        self.field_errors = field_errors
        retry_after = response.headers.get("Retry-After")
        self.retry_after = int(retry_after) if retry_after else None

    def __repr__(self):
        return (
            f"ApiError(error_type='{self.error_type}', error_code='{self.error_code}', detail='{self.detail}', "
            f"docs_url='{self.docs_url}', field_errors={self.field_errors})"
        )

    @classmethod
    def from_error_data(cls, response: Response, error):
        field_errors = [FieldError(fe["field"], fe["message"]) for fe in error.get("errors", [])]
        return cls(response, error["type"], error["code"], error["detail"], error["documentation_url"], *field_errors)
