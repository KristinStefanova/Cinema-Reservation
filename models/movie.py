from utils.settings import (Base, Column, Integer, String, Float,
                            CheckConstraint)


class Movie(Base):
    __tablename__ = "movies"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    rating = Column(Float,
                    CheckConstraint('rating>=1 and rating<=10'),
                    default=1,
                    nullable=False
                    )

    def __str__(self):
        return f"[{self.id}] - {self.name} ({self.rating})"

    def __repr__(self):
        return self.__str__
