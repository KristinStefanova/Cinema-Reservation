from utils.database_settings import session
from models.movie import Movie
from models.projection import Projection
from models.reservation import Reservation
from models.user import User


def add_movies():
    session.add_all([
                    Movie(name="The Hunger Games: Catching Fire", rating=7.5),
                    Movie(name="Wreck-It Ralph", rating=7.8),
                    Movie(name="Her", rating=8.3),
                    Movie(name="Avengers: Infinity War", rating=8.8)])
    session.commit()


def add_projections():
    session.add_all([Projection(movie_id=1,
                                type="3D",
                                date="2018-05-25",
                                time="21:55:00"),
                     Projection(movie_id=1,
                                type="4DX",
                                date="2018-05-27",
                                time="21:55:00"),
                     Projection(movie_id=1,
                                type="2D",
                                date="2018-05-26",
                                time="15:30:00"),
                     Projection(movie_id=1,
                                type="3D",
                                date="2018-05-25",
                                time="21:30:00")])
    session.commit()


def add_users():
    session.add_all([User(username="Krisi", password="123456K!", is_active=0),
                     User(username="Krisi2", password="5678910K!", is_active=0)
                     ])
    session.commit()


def add_reservations():
    session.add_all([Reservation(user_id=1, projection_id=2, row=2, column=3),
                     Reservation(user_id=1, projection_id=2, row=2, column=4)])
    session.commit()
