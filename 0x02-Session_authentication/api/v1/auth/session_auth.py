#!/usr/bin/env python3
'''
Holds the SessionAuth class that inherits from Auth
'''
from api.v1.auth.auth import Auth
from uuid import uuid4
from models.user import User

User = User()


class SessionAuth(Auth):
    '''
    First step to creating a new authentication mechanism that validates
    if everything inherits correctly without any overloading and validate
    the "switch" by using environment variables
    '''
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        '''
        Method that creates a session ID for a user_id
        '''
        if (user_id is None) or (type(user_id) != str):
            return None

        session_id = str(uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        '''
        Mehod that returns a User ID based on a Session ID
        '''
        if (session_id is None) or (type(session_id) != str):
            return None

        user_id = self.user_id_by_session_id.get(session_id)
        return user_id

    def current_user(self, request=None):
        '''
        Method that return a user instance based on a cookie value
        '''
        cookie = self.session_cookie(request)
        user_id = self.user_id_for_session_id(cookie)
        user = User.get(user_id)
        return user
