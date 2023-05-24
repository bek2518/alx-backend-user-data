#!/usr/bin/env python3
'''
Project on re library, and logger
'''
import re


def filter_datum(fields, redaction, message, separator):
    '''
    Function that takes arguments returns log message obfuscated
    '''
    for field in fields:
        regex = '{}=.+?{}'.format(field, separator)
        redaction = '{}={}{}'.format(field, redaction, separator)
        message = re.sub(regex, redaction, message)
    return message
