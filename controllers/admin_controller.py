from .movie_controller import MovieController
from .user_controller import UserController
from .projection_controller import ProjectionController


def add_movie(cls, name, rating):
    MovieController.create(name, float(rating))


def remove_movie(cls, movie_id):
    MovieController.remove(movie_id)


def add_user(cls, username, password):
    UserController.create(username, password)


def remove_user(cls, user_id):
    UserController.remove(user_id)


def add_projection(cls, movie_id, movie_type, date, time):
    ProjectionController.add_projection(movie_id, movie_type, date, time)


def remove_projection(cls, projection_id):
    ProjectionController.remove(projection_id)
