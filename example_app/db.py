from sqlalchemy import Column, Integer, String, Table, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
import os

engine = create_engine(os.environ['DATABASE_URL'])

Base = declarative_base(bind=engine)

Session = sessionmaker(expire_on_commit=False, bind=engine)

session = Session()


class User(Base):

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name =  Column(String)