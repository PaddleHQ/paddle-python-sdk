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
