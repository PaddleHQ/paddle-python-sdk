import logging
from paddle_billing.Logger.Formatter import CustomLogger


def get_logger(
    log_level:     int        = logging.INFO,
    log_file_path: str | None = None,
) -> logging.Logger:
    """
    Configures a logger instance that our Client() uses

    @param log_level:     Defaults to logging.INFO
    @param log_file_path: Defaults to None, which streams logs to the console. If a file path is provided logs are written to the file.
    @return:              Returns a logger instance
    """
    logger = logging.getLogger('paddle_billing')

    if not logger.handlers:
        logger.setLevel(log_level)

        formatter = logging.Formatter("{asctime} {levelname:<8} {message}", style='{')
        handler   = logging.StreamHandler() if not log_file_path else logging.FileHandler(log_file_path)

        handler.setFormatter(formatter)
        logger.addHandler(handler)

        # Filter out secrets from outputting to logs
        logger.addFilter(CustomLogger())

    return logger
