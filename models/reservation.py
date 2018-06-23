from .settings import *


class Reservation(Base):
    __tablename__ = "reservations"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey(User.id), nullable=False)
    projection_id = Column(Integer, ForeignKey(Projection.id), nullable=False)
    row = Column(Integer, CheckConstraint('row>=1 and row<=10'))
    col = Column(Integer, CheckConstraint('col>=1 and col<=10'))
    user = relationship("User", backref="reservations")
    projection = relationship("Projection", backref="reservations")
