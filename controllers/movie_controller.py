from models.movie import Movie
from utils.database_settings import session
from utils.settings import LOW_MOVIE_RATING, HIGH_MOVIE_RATING
from utils.exceptions import MovieRatingOutOfRangeError, MovieIdError


class MovieController:

    @staticmethod
    def create(name, rating):
        if rating < LOW_MOVIE_RATING or rating > HIGH_MOVIE_RATING:
            raise MovieRatingOutOfRangeError()
        else:
            movie = Movie(name=name, rating=rating)
            session.add(movie)
            session.commit()

    @staticmethod
    def remove(movie_id):
        movie = session.query(Movie).filter(Movie.id == movie_id).one_or_none()
        session.delete(movie)

    @staticmethod
    def get_all():
        movies = session.query(Movie.id, Movie.name, Movie.rating).all()

        return movies

    @staticmethod
    def get_by_id(movie_id):
        movie = session.query(Movie.id, Movie.name, Movie.rating).filter(
            Movie.id == movie_id).one_or_none()

        if movie is None:
            raise MovieIdError()
        else:
            return movie
