#!/usr/bin/env python3
'''
Holds class that will be used to implement authentication system
'''
from flask import request
from typing import List, TypeVar


class Auth:
    '''
    Template for all authentication system to be implemented
    '''
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        '''
        Public method that returns False for now
        '''
        return False

    def authorization_header(self, request=None) -> str:
        '''
        Public method that returns None for now
        '''
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        '''
        Public method that returns None for now
        '''
        return None
