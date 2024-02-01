from paddle_billing.Notifications import PaddleSignature, Verifier, Secret

from tests.Utils import FakeResponse


def test_validate_paddle_signature_header_integrity():
    test_headers = {
        PaddleSignature().HEADER:
            'ts=1696195954;h1=dummy;h1=d96299976a6eb066f484d7fde011ac56fc32b38fc9940bc419d6e537fdc6ef02',
    }
    test_data = 'hello-world'

    request = FakeResponse(test_headers, test_data)
    secrets = [
        Secret('pdl_ntf_01hbpjmytsa32fhr36nqgc3kgb_TjIG2BXbm83HPXqNfziwe506sBEdqL/4'),  # should fail
        Secret('pdl_ntf_01hbpjmytsa32fhr36nqgc3kgb_vB/yIOnTOCWIvpBadM5jzBZPHc7OmdSo'),  # should fail
        Secret('pdl_ntf_01hbpjmytsa32fhr36nqgc3kgb_WvRO0eL4Bj9rgYYIBZY6wZhG4EHy9jzh'),  # should sass
    ]

    verifier = Verifier(0)
    assert verifier.verify(request, secrets)
