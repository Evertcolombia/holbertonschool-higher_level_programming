#!/usr/bin/python3

import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import exists
from sqlalchemy import update

if __name__ == '__main__':

    s_name = 'New Mexico'
    st = 'mysql+mysqldb://{}:{}@localhost/{}'
    engine = create_engine(st.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    Session = Session()

    result = exists().where(State.id==2)
    if result is not None:
        smtm = update(State).where(State.id==2).values(name=s_name)
