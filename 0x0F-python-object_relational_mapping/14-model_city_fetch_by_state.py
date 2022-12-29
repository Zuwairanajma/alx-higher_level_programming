#!/usr/bin/python3
"""
prints all City objects from the database
command-line args:
    1st: username
    2nd: password
    3rd: database name to perform operation
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City
import sys


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3],
                                   pool_pre_ping=True))
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    for instance in session.query(City.name, City.id,
                                  State.name).order_by(City.id).filter(
                                  State.id == City.state_id):
        print('{}: ({}) {}'.format(instance[2], instance[1], instance[0]))
    session.close()
