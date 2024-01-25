import logging
from paddle_billing_python_sdk.Logger.Formatter import CustomLogger


__pkg__ = 'paddle-billing-python-sdk'


# Initialize our logger
# TODO this is temporary
logger = logging
logger.basicConfig(
    level=logging.DEBUG,
    format="{asctime} {levelname:<8} {message}",
    style='{',
    # filename=f"{environ['TITLE']}-{environ['ENVIRONMENT']}.log",
    filemode='a',  # Append existing log instead
)
log = logger.getLogger(__pkg__)
log.addFilter(CustomLogger())

