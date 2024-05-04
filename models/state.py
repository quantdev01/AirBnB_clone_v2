#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import os


class State(BaseModel): # add Base
    """ State class """
    name = ""
    # __tablename__ = 'states'
    """
    name = Column(String(128))

    if os.environ.get('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship('City', backref='state', cascade='all, delete') 
    else:
        @property
        def cities(self):
            "" get the citi as attribute ""
            from models import storage, City
            cities = []
            for city in storage.all(City).values():
                if city.state_id == self.id:
                    cities.append(city)
            return cities
            """
