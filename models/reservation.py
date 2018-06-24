from utils.database_settings import Base
from utils.settings import (Column, Integer,
                            CheckConstraint, ForeignKey, relationship,
                            HALL_MIN_SIZE, HALL_MAX_SIZE)
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
                 CheckConstraint(f"row>={HALL_MIN_SIZE} and \
                    row<={HALL_MAX_SIZE}"),
                 nullable=False
                 )
    column = Column(Integer,
                    CheckConstraint(f"column>={HALL_MIN_SIZE} and \
                    column<={HALL_MAX_SIZE}"),
                    nullable=False
                    )

    def __str__(self):
        return f"{self.projection.date} {self.projection.time} \
        {self.projection.movie.name} Seat: {self.row} {self.col} "

    def __repr__(self):
        return f"{self.id} {self.projection.date} {self.projection.time} \
        {self.projection.movie.name} Seat: {self.row} {self.col} "
