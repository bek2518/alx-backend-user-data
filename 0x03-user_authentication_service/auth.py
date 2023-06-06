#!/usr/bin/env python3
'''
Auth module that handles the authorization process
'''
import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
from uuid import uuid4
from typing import Union


def _hash_password(password: str) -> bytes:
    '''
    Method that takes in password and returns hashed, salted password
    '''
    password = password.encode('utf-8')
    hashed_password = bcrypt.hashpw(password, bcrypt.gensalt())
    return hashed_password


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        '''
        Method that hashes a password and save user to the database
        '''
        try:
            self._db.find_user_by(email=email)
        except NoResultFound:
            hashed_password = _hash_password(password)
            user = self._db.add_user(email, hashed_password)
            return user

        raise ValueError('User {} already exists'.format(email))

    def valid_login(self, email: str, password: str) -> bool:
        '''
        Method that locates user by email and if exists check the
        password matches
        '''
        try:
            user = self._db.find_user_by(email=email)
        except Exception:
            return False
        if bcrypt.checkpw(password.encode('utf-8'), user.hashed_password):
            return True
        return False

    def create_session(self, email: str) -> str:
        '''
        Method that finds user corresponding to the email and generate
        a new UUID and store it in the db as session_id
        '''
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return
        session_id = _generate_uuid()
        self._db.update_user(user_id=user.id, session_id=session_id)
        return session_id

    def get_user_from_session_id(self, session_id: str) -> Union[User, None]:
        '''
        Method that returns corresponding user or None from session_id
        '''
        if session_id is None:
            return None
        try:
            user = self._db.find_user_by(session_id=session_id)
        except NoResultFound:
            return None
        return user

    def destroy_session(self, user_id: int) -> None:
        '''
        Method that updates corresponding user's session_id to None
        '''
        self._db.update_user(user_id=user_id, session_id=None)
        return None

    def get_reset_password_token(self, email: str) -> str:
        '''
        Method that update the user's reset_token database field
        '''
        reset_token = _generate_uuid()
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            raise ValueError
        self._db.update_user(user_id=user.id, reset_token=reset_token)
        return reset_token


def _generate_uuid() -> str:
    '''
    Function that generated uuid
    '''
    return str(uuid4())
