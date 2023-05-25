#!/usr/bin/env python3
'''
Project on re library, and logger
'''
import re
import logging


def filter_datum(fields, redaction, message, separator):
    '''
    Function that takes arguments returns log message obfuscated
    '''
    for field in fields:
        mess = re.sub('{}=.+?{}'.format(field, separator),
                      '{}={}{}'.format(field, redaction, separator), mess)
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
        message = super().format(record)
        obfuscated = filter_datum(self.fields, self.REDACTION,
                                  message, self.SEPARATOR)
        return (obfuscated)
