#!/usr/bin/env python3
"""A module for obfuscating logs.
"""


import re
from typing import List


def filter_datum(
        fields: List[str], redaction: str, message: str, separator: str,
        ) -> str:
    """fucntion that returns the log message obfuscated
    """
    for i in fields:
        pattern = rf'{i}=[^{separator}]+'
        message = re.sub(pattern, f'{i}={redaction}', message)
    return message
