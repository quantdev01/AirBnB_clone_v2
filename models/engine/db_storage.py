#!/usr/bin/python3
""" DBStorage """
from sqlalchemy import create_engine 
from models.base_model import Base

class DBStorage:
    """ Storage db """
    __engine = None
    __session = None

    def __init__(self):
        """ Init the instance """
        import os
        user = os.environ.get('HBNB_MYSQL_USER')
        password = os.environ.get('HBNB_MYSQL_PWD')
        host = os.environ.get('HBNB_MYSQL_HOST')
        database = os.environ.get('HBNB_MYSQL_DB')
        my_env = os.environ.get('HBNB_ENV')

        self.__engine = create_engine(f'mysql://{user}:{password}@{host}/{database}', pool_pre_ping=True)

        # self.__engine = create_engine('mysql://hbnb_dev:Hbnb_dev_pwd@24@localhost/hbnb_dev_db', pool_pre_ping=True)

        if my_env == 'test':
            """Have to drop all the table"""
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ Query from session all objects """
        if cls:
            results = self.__session.query(eval(cls)).all()
        else:
            # results = self.__session.query(User, State, City, Amenyity, Place, Review).all()
            results= self.__session.query(State).all()
            results.extend(self.__session.query(User).all())
        return {f"{type(obj).__name__}.{obj.id}": obj for obj in results}

    def new(self, obj):
        """ Adding the object to our session """
        self.__session.query.add(obj);

    def save(self):
        """ Commit changes """
        self.__session.commit();

    def delete(self, obj=None):
        """ Deleting the object from our session """
        if obj != None:
            self.__session.delete(obj)

    def reload(self):
        """ Creating actually our session """
        from models.base_model import BaseModel, Base
        from models.city import City
        from models.state import State
        from sqlalchemy.orm import sessionmaker, scoped_session

        Session = sessionmaker(bind=self.__engine)

        # Create a scoped session
        ScopedSession = scoped_session(Session)

        # Bind the scoped session to the engine
        ScopedSession.configure(bind=self.__engine)

        self.__session = ScopedSession()

