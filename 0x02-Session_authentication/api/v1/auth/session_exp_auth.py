#!/usr/bin/env python3
'''
Holds the SessionExpAuth class that inherits from SessionAuth
'''
from api.v1.auth.session_auth import SessionAuth
import os
from datetime import datetime, timedelta


class SessionExpAuth(SessionAuth):
    '''
    Adds expiry date to session id
    '''
    def __init__(self):
        '''
        Initialized the class
        '''
        try:
            self.session_duration = int(os.getenv('SESSION_DURATION'))
        except Exception:
            self.session_duration = 0

    def create_session(self, user_id=None):
        '''
        method that create a session ID
        '''
        session_id = super().create_session(user_id)
        if not session_id:
            return None
        self.user_id_by_session_id[session_id] = {
            'user_id': user_id, 'created_at': datetime.now()}
        return session_id

    def user_id_for_session_id(self, session_id=None):
        '''
        Returns the user_id from session deictionary
        '''
        if session_id is None:
            return None

        if session_id not in self.user_id_by_session_id.keys():
            return None

        user_id = self.user_id_by_session_id[session_id]['user_id']
        if self.session_duration <= 0:
            return user_id

        created_at = self.user_id_by_session_id[session_id]['created_at']
        if created_at is None:
            return None

        if (created_at + timedelta(seconds=self.session_duration) <
                datetime.now()):
            return None

        return user_id
