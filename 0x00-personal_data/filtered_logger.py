#!/usr/bin/env python3
'''
Project on re library, and logger
'''
import re
from typing import List
import logging


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

    def __init__(self, fields):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        '''
        Filters values in incoming log records using filter_datum
        '''
        obfuscated = filter_datum(self.fields, self.REDACTION,
                                  super().format(record), self.SEPARATOR)
        return (obfuscated)
