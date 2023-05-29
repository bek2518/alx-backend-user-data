#!/usr/bin/env python3
'''
Holds the BasicAuth class that inherits from Auth
'''
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    '''
    Inherits from Auth and does nothing for now
    '''
    def extract_base64_authorization_header(self, authorization_header: str) -> str:
        '''
        Method that returns the Base64 patr of the authorization header
        '''
        if (authorization_header is None) or (type(authorization_header) != str) or\
            (authorization_header[0:6] != 'Basic '):
            return None
        return authorization_header[6:]
