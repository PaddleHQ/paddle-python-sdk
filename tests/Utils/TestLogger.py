from pytest import fixture
from logging import getLogger, Logger, Handler, LogRecord


class LogHandler(Handler):
    def __init__(self):
        super().__init__()
        self._logs = []

    def emit(self, record):
        self._logs.append(record)

    def get_logs(self) -> list[LogRecord]:
        return self._logs


@fixture
def test_log_handler() -> LogHandler:
    return LogHandler()


@fixture
def test_logger(test_log_handler) -> Logger:
    logger = getLogger("paddle_test_logger")
    logger.addHandler(test_log_handler)
    return logger
