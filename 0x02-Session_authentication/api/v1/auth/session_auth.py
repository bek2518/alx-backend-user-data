#!/usr/bin/env python3
'''
Holds the SessionAuth class that inherits from Auth
'''
from api.v1.auth.auth import Auth


class SessionAuth(Auth):
	'''
	First step to creating a new authentication mechanism that validates
	if everything inherits correctly without any overloading and validate
	the "switch" by using environment variables
	'''
	pass