from paddle_billing_python_sdk.ResponseParser import ResponseParser


class Paginator:
    def __init__(self, client, pagination, mapper):
        self._client     = client
        self._pagination = pagination
        self._mapper     = mapper


    def has_more(self):
        return self._pagination.hasMore


    def next_page(self):
        response        = self._client.get_raw(self._pagination.next)
        response_parser = ResponseParser(response)

        return self._mapper.from_array(
            response_parser.get_data(),
            Paginator(self._client, response_parser.get_pagination(), self._mapper)
        )
