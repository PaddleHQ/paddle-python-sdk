from pytest import mark

from paddle_billing.Entities.Metrics import MetricsExplorePagination


class TestMetricsExplorePagination:
    @mark.parametrize(
        "next_url, has_more, expected_after",
        [
            ("https://api.paddle.com/metrics/explore?after=eyJjIjoxfQ", True, "eyJjIjoxfQ"),
            ("https://api.paddle.com/metrics/explore?per_page=5&after=eyJjIjoxfQ", True, "eyJjIjoxfQ"),
            ("", False, None),
            ("https://api.paddle.com/metrics/explore?after=eyJjIjoxfQ", False, None),
            ("", True, None),
            ("https://api.paddle.com/metrics/explore", True, None),
        ],
        ids=[
            "Next page",
            "Cursor among other query parameters",
            "Last page",
            "Last page with a next URL",
            "Empty next with more pages",
            "Next without a cursor",
        ],
    )
    def test_after_is_parsed_from_next(self, next_url, has_more, expected_after):
        pagination = MetricsExplorePagination.from_dict(
            {"per_page": 5, "next": next_url, "has_more": has_more, "estimated_total": 42}
        )

        assert pagination.per_page == 5
        assert pagination.next == next_url
        assert pagination.has_more is has_more
        assert pagination.estimated_total == 42
        assert pagination.after == expected_after
