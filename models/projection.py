from utils.settings import (Base, Column, Integer, String,
                            ForeignKey, relationship)
from .movie import Movie


class Projection(Base):
    __tablename__ = "projections"
    id = Column(Integer, primary_key=True)
    movie_id = Column(Integer, ForeignKey(Movie.id), nullable=False)
    type = Column(String)
    date = Column(String)
    time = Column(String)
    movie = relationship("Movie", backref="projections")

    def __str__(self):
        return f"[{self.id}] - {self.date} {self.time} ({self.type})"

    def __repr__(self):
        return f"[{self.id}] - {self.date} {self.time} ({self.type})"
