#!/usr/bin/python3

"""
creates the State “California” with the City “San Francisco” from the
database hbtn_0e_100_usa
"""

from sys import argv
from relationship_state import State, Base
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm.session import Session


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                            argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(bind=engine)

    state = State(name="California")
    state.cities = [City(name="San Francisco")]
    session.add(state)
    session.commit()
