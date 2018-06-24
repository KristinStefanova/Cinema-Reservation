from models import Movie
from utils.database_settings import session
from utils.settings import LOW_MOVIE_RATING, HIGH_MOVIE_RATING
from utils.exceptions import MovieRatingOutOfRangeError, MovieIdError


class MovieController:

    @classmethod
    def create(cls, name, rating):
        if rating < LOW_MOVIE_RATING or rating > HIGH_MOVIE_RATING:
            raise MovieRatingOutOfRangeError()
        else:
            movie = Movie(name=name, rating=rating)
            session.add(movie)
            session.commit()

    @classmethod
    def remove(cls, movie_id):
        movie = session.query(Movie).filter(Movie.id == movie_id).one()
        session.delete(movie)

    @classmethod
    def get_all(cls):
        movies = session.query(Movie.id, Movie.name, Movie.rating).all()
        return movies

    @classmethod
    def get_by_id(cls, movie_id):
        movie = session.query(Movie).filter(Movie.id == movie_id).one()
        if movie is None:
            raise MovieIdError()
        else:
            return movie
