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
    states = session.query(State).filter(
            State.name.contains('a'))

    if states:
        states.delete(synchronize_session=False)
        session.commit()
