#!/usr/bin/env python3
'''
Create a new authentication system based on session if stored in database
'''
from models.base import Base


class UserSession(Base):
	'''
	Class that inherits from Base
	'''
	def __init__(self, *args: list, **kwargs: dict):
		super().__init__(*args, **kwargs)
		self.user_id = kwargs.get('user_id')
		self.session_id = kwargs.get('session_id')
