from controllers.main_controller import Controller
from utils.exceptions import *
from utils.settings import COMMANDS


class Menu:
    controller = Controller()

    @classmethod
    def show_movies(cls):
        print(cls.controller.show_movies())

    @classmethod
    def show_movie_projections(cls, movie_id, date=None):
        if date is None:
            print(cls.controller.show_movie_projections(movie_id))
        else:
            print(cls.controller.show_movie_projections(movie_id, date))

    @classmethod
    def log_user(cls):
        print("You need to a account in the system to make reservations!")
        username = input("Username: ")
        password = input("Password: ")
        try:
            user_id = cls.controller.log_user(username, password)
        except UserDoesNotExist:
            print("You are not register user! Please register!")
        else:
            print(f"Hello, {username}")
            return user_id

    @classmethod
    def register_user(cls):
        username = input("Username: ")
        password = input("Password: ")
        try:
            user_id = cls.controller.register_user(username, password)
        except LessThanEightSymbolsError:
            print("Password must contain at least 8 symbols! Try again!")
        except MissingCapitalLetterError:
            print("Password must have at least 1 capital letter! Try again!")
        except MissingSpecialSymbolError:
            print("Password must have at least 1 special symbol! Try again!")
        else:
            print(f"Hello, {username}")
            return user_id

    @classmethod
    def get_tickets(cls):
        tickets = input("Step 1 (User): Choose number of tickets> ")

        print("Current movies: \n")
        print(cls.controller.show_movies())
        return tickets

    @classmethod
    def get_movie_id(cls):
        movie_id = input("Step 2 (Movie): Choose a movie> ")

        print("Projections for movie: \n")
        print(cls.controller.show_movie_projections_with_avaliable_seats(
            movie_id))

    @classmethod
    def get_projection(cls, tickets):
        projection_id = input("Step 3 (Projection): Choose a projection> ")
        while (not cls.controller.check_movie_projection(
            projection_id, tickets)
        ):
            projection_id = input(
                "Step 3 (Projection): Choose a projection> ")

        print("Available seats (marked with a dot): \n")
        cls.controller.show_projection_hall(projection_id)
        return projection_id

    @classmethod
    def make_reservations(cls, user_id, projection_id, tickets):
        count = 0
        while count < int(tickets):
            seat = custom_input(f"Step 4 (Seats): Choose seat {count + 1}> ")
            row = int(seat.split(', ')[0]),
            column = int(seat.split(', ')[1])
            try:
                cls.controller.add_reservation(
                    user_id, projection_id, row, column)
            except SeatOutOfRangeError:
                print("Row and Column must be in range [1, 10]!")
            except TakenSeatError:
                print("Seat is alredy taken!")
            else:
                count += 1
            print(f"Your reservation is \
             for {projection_id}, seat: {row} {column}")

    @classmethod
    def cancel_reservation(cls, user_id, projection_id, row, column):
        try:
            cls.controller.get_reservation_id(
                user_id, projection_id, row, column)
        except ReservationDoesNotExist:
            print("Reservation does not exist!")

    @classmethod
    def help(cls):
        print(COMMANDS)

    @classmethod
    def exit(cls):
        cls.controller.exit()
        exit()

    @classmethod
    def start(cls):
        print("Welcome to Krisky Cinema!")
        print(cls.help())
        user_id = None
        tickets = None
        projection_id = None

        while True:
            command = input("> ")

            if command == 'show movies':
                cls.show_movies()

            elif command.startswith('show movie projections'):
                try:
                    movie_id = command.split(' ')[3]
                    date = command.split(' ')[4]
                except IndexError:
                    cls.show_movie_projections(movie_id)
                else:
                    cls.show_movie_projections(movie_id, date)

            elif command == 'make reservation':
                user_id = cls.log_user()
                while user_id is None:
                    user_id = cls.register_user()
                tickets = cls.get_tickets()
                cls.get_movie_id()
                projection_id = cls.get_projection(tickets)
                cls.make_reservations(user_id, projection_id, tickets)

            elif command.startswith('cancel reservation'):
                if user_id is None:
                    user_id = cls.log_user()
                cls.cancel_reservation(user_id, projection_id, row, column)

            elif command == 'help':
                cls.help()

            elif command == 'exit':
                cls.exit()
            else:
                print("Not a valid command")
