from .settings import *


class Projection(Base):
    __tablename__ = "projections"
    id = Column(Integer, primary_key=True)
    movie_id = Column(Integer, ForeignKey(Movie.id), nullable=False)
    type = Column(String)
    date = Column(String)
    time = Column(String)
    movie = relationship("Movie", backref="projections")
