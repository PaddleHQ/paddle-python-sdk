from logging import Logger

from paddle_billing.Logger import get_logger, CustomLogger


def test_validate_paddle_signature_header_integrity():
    log = get_logger()
    assert isinstance(log, Logger), "Our logger instance did not initialize correctly"
    assert isinstance(log.filters[0], CustomLogger), "Our CustomLogger logger filter is not removing sensitive secrets"
    assert log.name == 'paddle_billing'
