#!/usr/bin/python3
"""
Script that lists all State objects, and corresponding City objects,
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State, Base
from relationship_city import City


if __name__ == "__main__":
    """
    Function that lists all State objects, and corresponding City objects,
    """

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3],
                                   pool_pre_ping=True))
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    for state in session.query(State).order_by(State.id).all():
        print("{}: {}".format(state.id, state.name))
        for city in sorted(state.cities, key=lambda city: city.id):
            print("    {}: {}".format(city.id, city.name))
    session.close()