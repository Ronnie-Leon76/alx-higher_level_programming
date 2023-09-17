#!/usr/bin/python3
"""
Script defines a City class
to work with MySQLAlchemy ORM
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from relationship_state import Base, State


class City(Base):
    """
    City class

    Attributes:
        __tablename__ (str): The table name of the class
        id (int): The City id of the class
        name (str): The City name of the class
        state_id (int): The City's state id of the class
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer,
                      ForeignKey(State.id),
                      nullable=False)
