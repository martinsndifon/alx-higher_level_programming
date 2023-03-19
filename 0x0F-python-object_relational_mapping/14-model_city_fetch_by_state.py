#!/usr/bin/python3

"""Prints all City objects from the database hbtn_0e_14_usa"""

from sys import argv
from model_state import State, Base
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm.session import Session


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                            argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(bind=engine)
    result = session.query(State.name, City.id, City.name).join(
                           City, State.id == City.state_id).order_by(
                           City.id).all()

    for state_name, city_id, city_name in result:
        print(f'{state_name}: ({city_id}) {city_name}')
