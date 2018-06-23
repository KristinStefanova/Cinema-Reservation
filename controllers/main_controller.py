from utils.settings import tabulate
from .movie_controller import MovieController
from .projection_controller import ProjectionController


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
