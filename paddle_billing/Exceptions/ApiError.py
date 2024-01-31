from paddle_billing.Exceptions.FieldError import FieldError


class ApiError(Exception):
    def __init__(self, error_type, error_code, detail, docs_url, *field_errors):
        self.error_type   = error_type
        self.error_code   = error_code
        self.detail       = detail
        self.docs_url     = docs_url
        self.field_errors = field_errors
        super().__init__(self.detail)


    def __repr__(self):
        return (f"ApiError(type='{self.error_type}', error_code='{self.error_code}', detail='{self.detail}', "
                f"docs_url='{self.docs_url}', field_errors={self.field_errors})")


    @classmethod
    def from_error_data(cls, error):
        field_errors = [FieldError(fe['field'], fe['message']) for fe in error.get('errors', [])]
        return cls(
            error['type'],
            error['code'],
            error['detail'],
            error['documentation_url'],
            *field_errors
        )
