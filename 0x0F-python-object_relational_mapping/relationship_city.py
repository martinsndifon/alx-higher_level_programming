#!/usr/bin/python3

"""
City model - will be the base model for all cities
"""

from sqlalchemy import Integer, String, Column
from sqlalchemy.sql.schema import ForeignKey
from relationship_state import State, Base


class City(Base):
    """Maps this table to the corresponding sql table"""
    __tablename__ = 'cities'
    id = Column(Integer, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'))
