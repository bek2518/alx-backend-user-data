#!/usr/bin/env python3
'''
Project on re library, and logger
'''
import re
from typing import List


def filter_datum(fields: List[str],
                 redaction: str, message: str, separator: str) -> str:
    '''
    Function that takes arguments returns log message obfuscated
    '''
    for fld in fields:
        message = re.sub('{}=.+?{}'.format(fld, separator),
                         '{}={}{}'.format(fld, redaction, separator), message)
    return message
