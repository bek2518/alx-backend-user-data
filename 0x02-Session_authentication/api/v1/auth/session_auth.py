#!/usr/bin/env python3
'''
Holds the SessionAuth class that inherits from Auth
'''
from api.v1.auth.auth import Auth
from uuid import uuid4


class SessionAuth(Auth):
    '''
    First step to creating a new authentication mechanism that validates
    if everything inherits correctly without any overloading and validate
    the "switch" by using environment variables
    '''
    def __init__(self):
        '''
        Initialize class
        '''
        self.user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        '''
        Method that creates a session ID for a user_id
        '''
        if user_id is None:
            return None

        if type(user_id) != str:
            return None

        session_id = uuid4()
        self.user_id_by_session_id[session_id] = user_id
        return session_id
