import json
from requests     import Response

from paddle_billing.Entities.Shared import Pagination

from paddle_billing.Exceptions.ApiError import ApiError


class ResponseParser:
    def __init__(self, response: Response):
        self.body = None

        if not hasattr(response, 'text'):
            return

        try:
            self.body = json.loads(response.text)
        except json.JSONDecodeError:
            self.body = None

        if self.body and 'error' in self.body:
            self.parse_errors()


    def get_data(self) -> list | dict:
        return self.body.get('data', []) if self.body else []


    def get_pagination(self) -> Pagination:
        meta       = self.body.get('meta',  {}) if self.body  else {}
        pagination = meta.get('pagination', {}) if meta       else {}

        return Pagination(
            per_page        = pagination.get('per_page'),
            next            = pagination.get('next'),
            has_more        = pagination.get('has_more'),
            estimated_total = pagination.get('estimated_total'),
        )


    def parse_errors(self):
        if not self.body or 'error' not in self.body:
            return

        error           = self.body['error']
        code            = error.get('code', 'shared_error')
        exception_class = self.find_exception_class_from_code(code)

        raise exception_class(error)


    @staticmethod
    def find_exception_class_from_code(code):
        parts    = code.split('_')
        resource = parts[0].capitalize() if parts else ''

        if not resource:
            return ApiError

        class_name = f"api_error.{resource}ApiError"
        try:
            module = __import__(class_name, fromlist=[''])
            return getattr(module, f'{resource}ApiError')
        except (ImportError, AttributeError):
            return ApiError
