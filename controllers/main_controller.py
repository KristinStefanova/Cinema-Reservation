from utils.settings import tabulate
from .movie_controller import MovieController
from .projection_controller import ProjectionController
from .reservation_controller import ReservationController
from .user_controller import UserController


def add_movie(name, rating):
    MovieController.create(name, float(rating))


def remove_movie(movie_id):
    MovieController.remove(movie_id)


def add_user(username, password):
    UserController.create(username, password)


def remove_user(user_id):
    UserController.remove(user_id)


def add_projection(movie_id, movie_type, date, time):
    ProjectionController.add_projection(movie_id, movie_type, date, time)


def remove_projection(projection_id):
    ProjectionController.remove(projection_id)


def show_all_movies():
    movies = MovieController.get_all()
    return tabulate(movies,
                    headers=['id', 'title', 'rating'],
                    tablefmt="plain")


def show_all_projections(movie_id):
    projections = ProjectionController.get_all_by_movie_id(int(movie_id))
    return tabulate(projections,
                    headers=['id', 'date', 'time', 'type'],
                    tablefmt="plain")


def show_all_projections_by_date(movie_id, date):
    projections = ProjectionController.get_all_by_movie_id_and_date(
        int(movie_id), date)
    return tabulate(projections,
                    headers=['id', 'time', 'type'],
                    tablefmt="plain")


def show_all_projections_with_avaliable_seats(movie_id):
    projections = ProjectionController.get_all_with_avaliable_seats(
        int(movie_id))
    return tabulate(projections,
                    headers=['id', 'date', 'time', 'type', 'spots'],
                    tablefmt="plain")


def show_projection_hall(projection_id):
    hall = ReservationController.get_projection_hall(projection_id)
    return tabulate(hall, tablefmt='plain')


def create_reservation(user_id, projection_id, row, column):
    ReservationController.create(user_id, projection_id, row, column)


def remove_reservation(reservation_id):
    ReservationController.remove(reservation_id)
