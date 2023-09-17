#!/usr/bin/python3
"""
Script that creates the State “California” with the City “San Francisco”
from the database hbtn_0e_100_usa
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State, Base
from relationship_city import City


if __name__ == "__main__":
    """
    Function that creates the State “California” with the City “San Francisco”
    from the database hbtn_0e_100_usa
    """

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3],
                                   pool_pre_ping=True))
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    new_state = State(name='California')
    new_city = City(name='San Francisco')
    new_state.cities.append(new_city)
    session.add(new_city)
    session.commit()
    session.close()
