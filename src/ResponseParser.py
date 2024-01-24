import json
from urllib.parse import urlparse, parse_qs

from src.Entities.Shared.Pagination import Pagination

from src.Exceptions.ApiError import ApiError


# TODO
class ResponseParser:
    def __init__(self, response):
        self.body = None

        try:
            self.body = json.loads(response.text)
        except json.JSONDecodeError:
            self.body = None

        self.parse_errors()


    def get_data(self):
        return self.body.get('data', [])


    def get_pagination(self):
        meta = self.body.get('meta', {})
        pagination = meta.get('pagination', {})

        next_page = pagination.get('next')
        next_page_number = None

        if next_page:
            parsed_url = urlparse(next_page)
            query_params = parse_qs(parsed_url.query)
            next_page_number = query_params.get('page', [None])[0]

        return Pagination(
            per_page=pagination.get('per_page'),
            next=next_page_number,
            has_more=pagination.get('has_more'),
            estimated_total=pagination.get('estimated_total'),
        )


    def parse_errors(self):
        if 'error' not in self.body:
            return

        error = self.body['error']
        code = error.get('code', 'shared_error')
        exception_class = self.find_exception_class_from_code(code)

        raise exception_class(error)


    @staticmethod
    def find_exception_class_from_code(code):
        parts = code.split('_')
        resource = parts[0].capitalize() if parts else ''

        if not resource:
            return ApiError

        class_name = f"api_error.{resource}ApiError"
        try:
            module = __import__(class_name, fromlist=[''])
            return getattr(module, f'{resource}ApiError')
        except (ImportError, AttributeError):
            return ApiError  # TODO
