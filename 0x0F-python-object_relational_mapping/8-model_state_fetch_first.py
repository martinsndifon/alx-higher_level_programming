#!/usr/bin/python3

"""List all State objects from the database hbtn_0e_6_usa"""

from sys import argv
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm.session import Session


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                            argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(bind=engine)
    state = session.query(State).order_by(State.id).first()

    if not state:
        print("Nothing")
    else:
        print(f'{state.id}: {state.name}')
