from utils.settings import tabulate
from .movie_controller import MovieController
from .projection_controller import ProjectionController
from .reservation_controller import ReservationController
from .user_controller import UserController


class Controller:

    @staticmethod
    def log_user(username, password):
        user = UserController.get(username)
        UserController.log_in(username)
        return user.id

    @staticmethod
    def register_user(username, password):
        UserController.create(username, password)
        UserController.log_in(username)
        user = UserController.get(username)
        return user.id

    @staticmethod
    def show_all_movies():
        movies = MovieController.get_all()
        return tabulate(movies,
                        headers=['id', 'title', 'rating'],
                        tablefmt="plain")

    @staticmethod
    def show_all_projections(movie_id):
        projections = ProjectionController.get_all_by_movie_id(int(movie_id))
        return tabulate(projections,
                        headers=['id', 'date', 'time', 'type'],
                        tablefmt="plain")

    @staticmethod
    def show_all_projections_by_date(movie_id, date):
        projections = ProjectionController.get_all_by_movie_id_and_date(
            int(movie_id), date)
        return tabulate(projections,
                        headers=['id', 'time', 'type'],
                        tablefmt="plain")

    @staticmethod
    def check_movie_projection_tickets(projection_id, tickets):
        return ReservationController.check_tickets_for_projection(
            projection_id, tickets)

    @staticmethod
    def show_all_projections_with_avaliable_seats(movie_id):
        projections = ProjectionController.get_all_with_avaliable_seats(
            int(movie_id))
        return tabulate(projections,
                        headers=['id', 'date', 'time', 'type', 'spots'],
                        tablefmt="plain")

    @staticmethod
    def show_projection_hall(projection_id):
        hall = ReservationController.get_projection_hall(int(projection_id))
        return hall

    @staticmethod
    def add_reservation(user_id, projection_id, row, column):
        ReservationController.create(
            int(user_id), int(projection_id), int(row), int(column))

    @staticmethod
    def get_reservation_id(user_id, projection_id, row, column):
        reservation = ReservationController.get(
            int(user_id), int(projection_id), int(row), int(column))
        return reservation.id

    @staticmethod
    def delete_reservation(reservation_id):
        ReservationController.remove(int(reservation_id))

    @staticmethod
    def exit(username):
        UserController.log_out(username)


class AdminPanel():

    @staticmethod
    def add_movie(name, rating):
        MovieController.create(name, float(rating))

    @staticmethod
    def delete_movie(movie_id):
        MovieController.remove(int(movie_id))

    @staticmethod
    def add_user(username, password):
        UserController.create(username, password)

    @staticmethod
    def delete_user(user_id):
        UserController.remove(int(user_id))

    @staticmethod
    def add_projection(movie_id, movie_type, date, time):
        ProjectionController.create(int(movie_id), movie_type, date, time)

    @staticmethod
    def delete_projection(projection_id):
        ProjectionController.remove(int(projection_id))
