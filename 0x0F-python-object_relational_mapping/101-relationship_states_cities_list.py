#!/usr/bin/python3
"""
prints the State object with the name passed as argument from the database
"""
import sys
from sqlalchemy.orm import sessionmaker, relationship
from relationship_city import City
from relationship_state import State, Base
from sqlalchemy import create_engine

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    for state in session.query(State).order_by(State.id):
        print(state.id, state.name, sep=": ")
        for cities in state.cities:
            print("    {}: {}".format(cities.id, cities.name))
    session.close()
