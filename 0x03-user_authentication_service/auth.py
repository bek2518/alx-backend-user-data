#!/usr/bin/env python3
'''
Auth module that handles the authorization process
'''
import bcrypt


def _hash_password(password: str) -> bytes:
    '''
    Method that takes in password and returns hashed, salted password
    '''
    password = password.encode('utf-8')
    hashed_password = bcrypt.hashpw(password, bcrypt.gensalt())
    return hashed_password
