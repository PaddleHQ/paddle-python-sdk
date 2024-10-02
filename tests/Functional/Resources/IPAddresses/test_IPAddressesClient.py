from urllib.parse import unquote

from paddle_billing.Entities.IPAddresses import IPAddresses

from tests.Utils.ReadsFixture import ReadsFixtures


class TestIPAddressesClient:
    def test_get_ip_addresses(self, test_client, mock_requests):
        expected_url = f"{test_client.base_url}/ips"
        mock_requests.get(expected_url, status_code=200, text=ReadsFixtures.read_raw_json_fixture("response/ips"))

        response = test_client.client.ip_addresses.get_ip_addresses()
        last_request = mock_requests.last_request

        assert isinstance(response, IPAddresses)

        ipv4_cidrs = response.ipv4_cidrs

        assert len(ipv4_cidrs) == 3

        assert ipv4_cidrs[0] == "34.194.127.46/32"
        assert ipv4_cidrs[1] == "54.234.237.108/32"
        assert ipv4_cidrs[2] == "3.208.120.145/32"

        assert last_request is not None
        assert last_request.method == "GET"
        assert test_client.client.status_code == 200
        assert (
            unquote(last_request.url) == expected_url
        ), "The URL does not match the expected URL, verify the query string is correct"
