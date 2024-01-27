import pytest
import requests

from paddle_billing_python_sdk.Notification import PaddleSignature, Verifier, Secret


def test_it_verifies_a_signature():
    # Prepare headers and data for the simulated POST request
    test_headers = {
        PaddleSignature().HEADER:
            'ts=1696195954;h1=dummy;h1=d96299976a6eb066f484d7fde011ac56fc32b38fc9940bc419d6e537fdc6ef02',
    }
    test_data = 'hello-world'

    # Create a fake response object to mimic 'requests' behavior
    class FakeResponse:
        def __init__(self, content, headers):
            self.content = content.encode() if isinstance(content, str) else content
            self.headers = headers

    request = FakeResponse(test_data, test_headers)
    secrets = [
        Secret('pdl_ntf_01hbpjmytsa32fhr36nqgc3kgb_TjIG2BXbm83HPXqNfziwe506sBEdqL/4'),  # should fail
        Secret('pdl_ntf_01hbpjmytsa32fhr36nqgc3kgb_vB/yIOnTOCWIvpBadM5jzBZPHc7OmdSo'),  # should fail
        Secret('pdl_ntf_01hbpjmytsa32fhr36nqgc3kgb_WvRO0eL4Bj9rgYYIBZY6wZhG4EHy9jzh'),  # should sass
    ]

    verifier = Verifier(0)
    assert verifier.verify(request, secrets)


# def test_test():
#     assert True is True
