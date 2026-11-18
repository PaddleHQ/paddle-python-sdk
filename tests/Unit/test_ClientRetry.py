from http.server import BaseHTTPRequestHandler, HTTPServer
from threading import Thread

from pytest import fixture, mark

from paddle_billing import Client, Environment, Options


def retries_for(client: Client):
    return client.client.get_adapter("https://api.paddle.com").max_retries


class TestClientRetry:
    @mark.parametrize("status", [429, 500, 502, 503, 504, 520, 521, 522, 523, 524])
    def test_idempotent_methods_are_retried_for_transient_statuses(self, status):
        retries = retries_for(Client("test"))

        for method in ["GET", "PUT", "DELETE"]:
            assert retries.is_retry(method, status)

    @mark.parametrize("status", [429, 500, 502, 503, 504, 520, 521, 522, 523, 524])
    def test_non_idempotent_methods_are_not_retried(self, status):
        retries = retries_for(Client("test"))

        for method in ["POST", "PATCH"]:
            assert not retries.is_retry(method, status)

    @mark.parametrize("status", [400, 404, 525, 526])
    def test_other_statuses_are_not_retried(self, status):
        assert not retries_for(Client("test")).is_retry("GET", status)


@fixture
def flaky_server():
    state = {"statuses": [], "requests": []}

    class Handler(BaseHTTPRequestHandler):
        def _respond(self):
            length = int(self.headers.get("Content-Length", 0))
            self.rfile.read(length)
            state["requests"].append(self.command)
            status = state["statuses"].pop(0) if state["statuses"] else 200
            self.send_response(status)
            self.send_header("Content-Length", "2")
            self.end_headers()
            self.wfile.write(b"{}")

        do_GET = do_POST = _respond

        def log_message(self, *args):
            pass

    server = HTTPServer(("127.0.0.1", 0), Handler)
    thread = Thread(target=server.serve_forever, daemon=True)
    thread.start()
    state["url"] = f"http://127.0.0.1:{server.server_port}/customers"
    yield state
    server.shutdown()
    server.server_close()


def client_for_local_server():
    client = Client("test", options=Options(Environment.SANDBOX))
    # Reuse the SDK's own retry configuration over plain http, without the backoff delay
    retries = retries_for(client).new(backoff_factor=0)
    adapter = client.client.get_adapter("https://api.paddle.com")
    adapter.max_retries = retries
    client.client.mount("http://", adapter)
    return client


class TestClientRetryOverHttp:
    def test_get_is_retried_after_522(self, flaky_server):
        flaky_server["statuses"] = [522, 522]

        response = client_for_local_server().client.get(flaky_server["url"])

        assert response.status_code == 200
        assert flaky_server["requests"] == ["GET", "GET", "GET"]

    @mark.parametrize("status", [522, 524])
    def test_post_is_not_retried_after_cloudflare_error(self, flaky_server, status):
        flaky_server["statuses"] = [status]

        response = client_for_local_server().client.post(flaky_server["url"], data="{}")

        assert response.status_code == status
        assert flaky_server["requests"] == ["POST"]
