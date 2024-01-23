import logging
import re


class CustomLogger(logging.Filter):
    def filter(self, record):
        # Define multiple regex patterns for different sensitive data types
        search_patterns = {
            r"'password': '\s*([^']+)'":      "'password': '<redacted>'",
            r"'id_token': '\s*([^']+)'":      "'id_token': '<redacted>'",
            r"'access_token': '\s*([^']+)'":  "'access_token': '<redacted>'",
            r"'refresh_token': '\s*([^']+)'": "'refresh_token': '<redacted>'",
            r"'Authorization': '\s*([^']+)'": "'Authorization': '<redacted>'",
            r"'password_hash': '\s*([^']+)'": "'password_hash': '<redacted>'",
        }

        # If the log record's message is a string, apply each regex substitution
        if isinstance(record.msg, str):
            for pattern, replacement in search_patterns.items():
                record.msg = re.sub(pattern, replacement, record.msg)

        return True  # Return True to indicate the record should be processed
