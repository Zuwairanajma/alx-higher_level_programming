#!/usr/bin/python3
"""
deletes all State objects with a name containing the letter 'a'
from the database
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys
from model_state import Base, State


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3],
                                   pool_pre_ping=True))

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    for each in session.query(State).filter(State.name.like('%a%')):
        session.delete(each)
    session.commit()
    session.close()
