#!/usr/bin/python3


import sys
from sqlalchemy import (create_engine)
from model_state import Base, State
from model_city import City
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":

    st = 'mysql+mysqldb://{}:{}@localhost/{}'
    engine = create_engine(st.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    Session = Session()

    query = Session.query(State, City).filter(City.state_id == State.id).order_by(City.id)

    for el in query:
        print('{}: ({}) {}'.format(el[0].name, el[1].id, el[1].name))
