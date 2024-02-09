import logging
import re


class CustomLogger(logging.Filter):
    def filter(self, record):
        # Define multiple regex patterns for different sensitive data types
        search_patterns = {
            r"'X-Transaction-ID': '\s*([^']+)'": "'X-Transaction-ID': '<redacted>'",
            r"Bearer \s*([^']+)":                "Bearer <API_SECRET_KEY>",
        }

        # If the log record's message is a string, apply each regex substitution
        if isinstance(record.msg, str):
            for pattern, replacement in search_patterns.items():
                record.msg = re.sub(pattern, replacement, record.msg)

        return True  # Return True to indicate the record should be processed
