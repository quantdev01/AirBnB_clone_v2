#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel


class State(BaseModel, Base):
    """ State class """
    # name = ""
    __tablename__ = 'states'
    name = Column(String(128))
