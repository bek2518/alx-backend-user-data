#!/usr/bin/env python3
'''
Working with bcrypt
'''
import bcrypt


def hash_password(password: str) -> bytes:
    '''
    Function that takes argument password and returns salted,
    hashed password
    '''
    password = password.encode('utf-8')
    hashed_password = bcrypt.hashpw(password, bcrypt.gensalt())
    return (hashed_password)
