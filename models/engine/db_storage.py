from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        import os
        user = os.environ.get('HBNB_MYSQL_USER')
        password = os.environ.get('HBNB_MYSQL_PWD')
        host = os.environ.get('HBNB_MYSQL_HOST')
        database = os.environ.get('HBNB_MYSQL_DB')
        env = os.environ.get('HBNB_ENV')

        self.__engine = create_engine(f'mysql://{user}:{password}@{host}/{database}', pool_pre_ping=True)

        # self.__engine = create_engine('mysql://hbnb_dev:Hbnb_dev_pwd@24@localhost/hbnb_dev_db', pool_pre_ping=True)

        if env == 'test':
            """Have to drop all the table"""

    def all(self, cls=None):

