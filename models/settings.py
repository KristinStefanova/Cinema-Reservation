from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy import CheckConstraint, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine


Base = declarative_base()
engine = create_engine("sqlite:///cinema.db")
Session = sessionmaker(engine)
session = Session()


def create():
    Base.metadata.drop_all(engine)


def drop():
    Base.metadata.create_all(engine)
