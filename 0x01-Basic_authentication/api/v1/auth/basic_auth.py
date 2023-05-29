#!/usr/bin/env python3
'''
Holds the BasicAuth class that inherits from Auth
'''
from api.v1.auth.auth import Auth
import base64
from typing import TypeVar
from models.user import User

User = User()


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
            decoded = base64.b64decode(base64_authorization_header)\
                .decode('utf-8')
        except Exception:
            return None

        return decoded

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

    def user_object_from_credentials(self, user_email: str,
                                     user_pwd: str) -> TypeVar('User'):
        '''
        Method that returns the User instance based on email and password
        '''
        if (user_email is None) or (type(user_email) != str) or\
           (user_pwd is None) or (type(user_pwd) != str):
            return None

        attributes = {'email': user_email}
        user_list = User.search(attributes)
        if user_list:
            for user in user_list:
                if user.is_valid_password(user_pwd):
                    return user
            return None
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        '''
        Method that overloads Auth and retrieves the User
        instance for a request
        '''
        auth_header = self.authorization_header(request)
        extracted = self.extract_base64_authorization_header(auth_header)
        decoded = self.decode_base64_authorization_header(extracted)
        user_credentials = self.extract_user_credentials(decoded)
        user_email = user_credentials[0]
        user_pwd = user_credentials[1]
        user = self.user_object_from_credentials(user_email, user_pwd)
        return user
