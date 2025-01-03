#!/usr/bin/env python3
"""A module for obfuscating logs.
"""


import re
from typing import List
import logging
import mysql.connector
import os


PII_FIELDS = ('name', 'email', 'phone', 'ssn', 'password')


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

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.feilds = fields

    def format(self, record: logging.LogRecord) -> str:
        """fucntion that returns the log message obfuscated
        """
        return filter_datum(self.feilds, self.REDACTION,
                            super(RedactingFormatter, self).format(record),
                            self.SEPARATOR)


def get_logger() -> logging.Logger:
    """fucntion that gets the logger
    """
    StreamHandler = logging.StreamHandler()
    StreamHandler.setFormatter(RedactingFormatter)
    user_data = logging.getLogger('name')
    user_data.propagate = False
    logger.setLevel(logging.INFO)


def get_db() -> mysql.connector.connection.MySQLConnection:
    """connect to MySQL database"""
    connection = mysql.connector.connect(
        host=os.getenv("PERSONAL_DATA_DB_HOST", "localhost"),
        database=os.getenv("PERSONAL_DATA_DB_NAME"),
        user=os.getenv("PERSONAL_DATA_DB_USERNAME", "root"),
        password=os.getenv("PERSONAL_DATA_DB_PASSWORD", "")
    )
    return connection


def main():
    con = get_db()
    cursor = con.cursor()
    cursor.execute('SELECT * FROM users')
    for row in cursor:
        print(filter_datum(
            list(PII_FIELDS), 
            RedactingFormatter.REDACTION, 
            row, RedactingFormatter.SEPARATOR))
        
if __name__ == "__main__":
    main()