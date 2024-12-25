#!/usr/bin/env python3


import re
from typing import List


def filter_datum(fields: str,redaction: str,message: str,seperator: str) -> str:
    """fucntion that returns the log message obfuscated
    """
    for i in fields:
        pattern = rf'{i}=[^{seperator}]+'
        message = re.sub(pattern, f'{i}={redaction}', message)
    return message
