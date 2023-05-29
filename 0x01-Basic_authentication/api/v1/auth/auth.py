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
        Public method that returns true if the path is not in the list of
        strings excluded_paths
        '''
        if (path is None) or (excluded_paths is None):
            return True

        if path[-1] != '/':
            path += '/'

        if path not in excluded_paths:
            return True

        return False

    def authorization_header(self, request=None) -> str:
        '''
        Public method that returns None for now
        '''
        if (request is None) or ('Authorization' not in request.headers):
            return None

        return request.headers['Authorization']

    def current_user(self, request=None) -> TypeVar('User'):
        '''
        Public method that returns None for now
        '''
        return None
