"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from user import Base, User
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=True)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        '''
        Method that saves the user to the database
        '''
        user = User(email=email, hashed_password=hashed_password)
        self._session.add(user)
        self._session.commit()
        return user

    def find_user_by(self, **kwargs) -> User:
        '''
        Method that takes arbitrary keyword argument and returns the
        first row foind in the users table
        '''
        try:
            user = self._session.query(User).filter_by(**kwargs).first()
        except Exception:
            raise InvalidRequestError
        if user is None:
            raise NoResultFound
        return user
    
    def update_user(self, user_id: int, **kwargs) -> None:
        '''
        Finds user using find_use_by and updated the value passed as
        kwargs
        '''
        user = self.find_user_by(id=user_id)
        attributes = ['email', 'hashed_password', 'session_id', 'reset_token']
        for key, value in kwargs.items():
            if key not in attributes:
                raise ValueError
            setattr(user, key, value)
        self._session.commit()
        return None
