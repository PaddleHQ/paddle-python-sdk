import logging
from time import time

from pytest import mark

from paddle_billing.Notifications import PaddleSignature, Verifier, Secret

from tests.Utils import FakeRequest
from tests.Utils.ReadsFixture import ReadsFixtures


class TestVerifier:
    def test_validate_paddle_signature_header_integrity(self):
        test_headers = {
            PaddleSignature().HEADER: "ts=1696195954;h1=dummy;h1=d96299976a6eb066f484d7fde011ac56fc32b38fc9940bc419d6e537fdc6ef02",
        }
        test_data = "hello-world"

        request = FakeRequest(test_headers, test_data)
        secrets = [
            Secret("pdl_ntf_01hbpjmytsa32fhr36nqgc3kgb_TjIG2BXbm83HPXqNfziwe506sBEdqL/4"),  # should fail
            Secret("pdl_ntf_01hbpjmytsa32fhr36nqgc3kgb_vB/yIOnTOCWIvpBadM5jzBZPHc7OmdSo"),  # should fail
            Secret("pdl_ntf_01hbpjmytsa32fhr36nqgc3kgb_WvRO0eL4Bj9rgYYIBZY6wZhG4EHy9jzh"),  # should pass
        ]

        verifier = Verifier(0)
        assert verifier.verify(request, secrets)

    @mark.parametrize(
        "signature, payload",
        [
            (
                "ts=1710498758;h1=558bf93944dbeb4790c7a8af6cb2ea435c8ca9c8396aafc1a4e37424ac132744",
                ReadsFixtures.read_raw_json_fixture("standard_payload").strip(),
            ),
            (
                "ts=1710498288;h1=38219b3ba1578184e625c29d201a27cd25bd69e2ec9c3ab87dcb90d87ff73a41",
                ReadsFixtures.read_raw_json_fixture("special_chars_payload").strip(),
            ),
        ],
        ids=[
            "Standard payload",
            "Special characters payload",
        ],
    )
    def test_validate_payload_body_integrity(
        self,
        monkeypatch,
        test_client,
        mock_requests,
        signature,
        payload,
    ):
        monkeypatch.setenv("TEST_MODE", "1")  # Required to disable time drift verification in Verifier.verify()

        headers = {PaddleSignature().HEADER: signature}
        secret = "pdl_ntfset_01hs0t3tw21j988db1pam5xg8m_GrOWLNef+vmtjJYq4mSnHNzvc8uWoJ1I"
        request = FakeRequest(headers, payload)
        assert request is not None

        integrity_check = Verifier().verify(request, Secret(secret))
        assert integrity_check is True

    @staticmethod
    def _signed_request(secret: str, body: str, timestamp: int) -> FakeRequest:
        signature = PaddleSignature.calculate_hmac(secret, f"{timestamp}:{body}".encode("utf-8")).hexdigest()

        return FakeRequest({PaddleSignature().HEADER: f"ts={timestamp};h1={signature}"}, body)

    @mark.parametrize(
        "offset, expected",
        [(0, True), (-60, False), (60, False), (315360000, False)],
        ids=["Current timestamp", "Old timestamp", "Future timestamp", "Far future timestamp"],
    )
    def test_verify_rejects_timestamps_outside_maximum_variance(self, monkeypatch, offset, expected):
        monkeypatch.delenv("TEST_MODE", raising=False)
        secret = "pdl_ntfset_01hs0t3tw21j988db1pam5xg8m_GrOWLNef+vmtjJYq4mSnHNzvc8uWoJ1I"
        request = self._signed_request(secret, '{"event_type":"transaction.completed"}', int(time()) + offset)

        assert Verifier().verify(request, Secret(secret)) is expected

    @mark.parametrize("maximum_variance", [None, 0], ids=["None", "Zero"])
    def test_verify_skips_time_drift_check_without_maximum_variance(self, monkeypatch, maximum_variance):
        monkeypatch.delenv("TEST_MODE", raising=False)
        secret = "pdl_ntfset_01hs0t3tw21j988db1pam5xg8m_GrOWLNef+vmtjJYq4mSnHNzvc8uWoJ1I"
        request = self._signed_request(secret, '{"event_type":"transaction.completed"}', int(time()) - 3600)

        assert Verifier(maximum_variance).verify(request, Secret(secret)) is True

    def test_verify_does_not_log_signatures(self, monkeypatch, caplog):
        monkeypatch.setenv("TEST_MODE", "1")
        caplog.set_level(logging.DEBUG, logger="paddle_billing")
        secret = "pdl_ntfset_01hs0t3tw21j988db1pam5xg8m_GrOWLNef+vmtjJYq4mSnHNzvc8uWoJ1I"
        body = '{"event_type":"transaction.completed"}'
        timestamp = int(time())
        received_signature = "f" * 64
        calculated_signature = PaddleSignature.calculate_hmac(secret, f"{timestamp}:{body}".encode("utf-8")).hexdigest()
        request = FakeRequest({PaddleSignature().HEADER: f"ts={timestamp};h1={received_signature}"}, body)

        assert Verifier().verify(request, Secret(secret)) is False
        assert calculated_signature not in caplog.text
        assert received_signature not in caplog.text

    @mark.parametrize(
        "headers, offset, message",
        [
            ({}, None, "Unable to extract the 'Paddle-Signature' header from the request"),
            (None, -60, "Too much time has elapsed between the request and this process"),
            (None, 60, "The request timestamp is too far in the future"),
        ],
        ids=["Missing header", "Expired timestamp", "Future timestamp"],
    )
    def test_verify_logs_expected_rejections_as_warning(self, monkeypatch, caplog, headers, offset, message):
        monkeypatch.delenv("TEST_MODE", raising=False)
        caplog.set_level(logging.DEBUG, logger="paddle_billing")
        secret = "pdl_ntfset_01hs0t3tw21j988db1pam5xg8m_GrOWLNef+vmtjJYq4mSnHNzvc8uWoJ1I"
        if headers is None:
            request = self._signed_request(secret, "{}", int(time()) + offset)
        else:
            request = FakeRequest(headers, "{}")

        assert Verifier().verify(request, Secret(secret)) is False

        rejections = [record for record in caplog.records if record.getMessage() == message]
        assert len(rejections) == 1
        assert rejections[0].levelno == logging.WARNING
        assert not [record for record in caplog.records if record.levelno >= logging.ERROR]

    def test_verify_skips_none_body_attributes(self):
        headers = {
            PaddleSignature().HEADER: "ts=1696195954;h1=d96299976a6eb066f484d7fde011ac56fc32b38fc9940bc419d6e537fdc6ef02",
        }
        request = FakeRequest(headers, "hello-world")
        request.body = None
        secret = Secret("pdl_ntf_01hbpjmytsa32fhr36nqgc3kgb_WvRO0eL4Bj9rgYYIBZY6wZhG4EHy9jzh")

        assert Verifier(0).verify(request, secret)
