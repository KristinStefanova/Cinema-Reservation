from utils.settings import (Base, Column, Integer,
                            CheckConstraint, ForeignKey, relationship)
from .user import User
from .projection import Projection


class Reservation(Base):
    __tablename__ = "reservations"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey(User.id), nullable=False)
    user = relationship("User", backref="reservations")
    projection_id = Column(Integer, ForeignKey(Projection.id), nullable=False)
    projection = relationship("Projection", backref="reservations")
    row = Column(Integer,
                 CheckConstraint('row>=1 and row<=10'),
                 nullable=False
                 )
    col = Column(Integer,
                 CheckConstraint('col>=1 and col<=10'),
                 nullable=False
                 )

    def __str__(self):
        return f"{self.projection.date} {self.projection.time} \
        {self.projection.movie.name} Seat: {self.row} {self.col} "

    def __repr__(self):
        return f"{self.id} {self.projection.date} {self.projection.time} \
        {self.projection.movie.name} Seat: {self.row} {self.col} "
