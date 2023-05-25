#!/usr/bin/env python3
'''
Project on re library, and logger
'''
import re
from typing import List
import logging
import mysql.connector.connection
import os


def filter_datum(fields: List[str],
                 redaction: str, message: str, separator: str) -> str:
    '''
    Function that takes arguments returns log message obfuscated
    '''
    for fld in fields:
        message = re.sub('{}=.+?{}'.format(fld, separator),
                         '{}={}{}'.format(fld, redaction, separator), message)
    return message


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        '''
        Filters values in incoming log records using filter_datum
        '''
        message = super().format(record)
        obfuscated = filter_datum(self.fields, self.REDACTION,
                                  message, self.SEPARATOR)
        return (obfuscated)


PII_FIELDS = ('name', 'email', 'phone', 'ssn', 'password')


def get_logger() -> logging.Logger:
    '''
    Function that takes no argument and returns logging.Logger object
    '''
    user_data = logging.getLogger('user_data')
    user_data.setLevel(logging.INFO)
    user_data.propagate = False
    ch = logging.StreamHandler()
    ch.setFormatter(RedactingFormatter(PII_FIELDS))
    user_data.addHandler(ch)
    return user_data


def get_db() -> mysql.connector.connection.MySQLConnection:
    '''
    Function that returns connector to a database
    '''
    USERNAME = os.getenv('PERSONAL_DATA_DB_USERNAME', 'root')
    PASSWORD = os.getenv('PERSONAL_DATA_DB_PASSWORD', '')
    HOST = os.getenv('PERSONAL_DATA_DB_HOST', 'localhost')
    DB_NAME = os.getenv('PERSONAL_DATA_DB_NAME')
    cxn = mysql.connector.connect(
        username=USERNAME,
        password=PASSWORD,
        host=HOST,
        database=DB_NAME
    )
    return (cxn)
