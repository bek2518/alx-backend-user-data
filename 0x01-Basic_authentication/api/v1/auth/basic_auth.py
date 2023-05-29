#!/usr/bin/env python3
'''
Holds the BasicAuth class that inherits from Auth
'''
from api.v1.auth.auth import Auth
import base64


class BasicAuth(Auth):
    '''
    Inherits from Auth and does nothing for now
    '''
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        '''
        Method that returns the Base64 patr of the authorization header
        '''
        if (authorization_header is None) or\
            (type(authorization_header) != str) or\
                (authorization_header[0:6] != 'Basic '):
            return None
        return authorization_header[6:]

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        '''
        Method that returns the decoded value of the base64 string argument
        '''
        if (base64_authorization_header is None) or\
           (type(base64_authorization_header) != str):
            return None

        try:
            decoded = base64.b64decode(base64_authorization_header)
        except Exception:
            return None

        return decoded.decode('utf-8')

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        '''
        Method that returns the user email and password from
        Base64 decoded value
        '''
        if (decoded_base64_authorization_header is None) or\
           (type(decoded_base64_authorization_header) != str) or\
           (':' not in decoded_base64_authorization_header):
            return (None, None)

        credentials = decoded_base64_authorization_header.split(':')
        return (credentials[0], credentials[1])
