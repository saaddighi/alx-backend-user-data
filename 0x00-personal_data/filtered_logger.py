#!/usr/bin/env python3
"""A module for obfuscating logs.
"""


import re
from typing import List
import logging


def filter_datum(
        fields: List[str], redaction: str, message: str, separator: str,
        ) -> str:
    """fucntion that returns the log message obfuscated
    """
    for i in fields:
        pattern = rf'{i}=[^{separator}]+'
        message = re.sub(pattern, f'{i}={redaction}', message)
    return message


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.feilds = fields

    def format(self, record: logging.LogRecord) -> str:
        """fucntion that returns the log message obfuscated
        """
        return filter_datum(self.feilds,self.REDACTION,str(record),self.SEPARATOR)
        



