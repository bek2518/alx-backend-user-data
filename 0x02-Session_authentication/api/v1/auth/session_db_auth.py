#!/usr/bin/env python3
'''
Holds the SessionDBAuth class that inherits from SessionExpAuth
'''
from api.v1.auth.session_exp_auth import SessionExpAuth


class SessionDBAuth(SessionExpAuth):
	'''
	Class that inherits from SessionExpAuth
	'''
	def create_session(self, user_id=None):
		'''
		Method that creates and stores new instance of UserSession and
		returns session id
		'''
		session_id = super().create_session(user_id)
        if not session_id:
            return None
        self.user_id_by_session_id[session_id] = {
            'user_id': user_id, 'created_at': datetime.now()}
        return session_id
	
	def user_id_for_session_id(self, session_id=None):
		'''
		Method that returns the user id by requesting UserSeeion in the db
		on session_id
		'''

	def destroy_session(self, request=None):
		'''
		Method that destroys the UserSession based on session_id
		'''
