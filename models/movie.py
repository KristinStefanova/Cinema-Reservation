from .settings import *


class Movie(Base):
    __tablename__ = "movies"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    rating = Column(
        Float, CheckConstraint('rating>=1 and rating<=10'), default=0)
