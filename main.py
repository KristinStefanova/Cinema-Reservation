from utils.database_settings import Database
from .populate import *
from view.menu import Menu


def main():
    Database.create
    add_movies()
    add_projections()
    add_reservations()
    add_users()
    Menu.start()


if __name__ == '__main__':
    main()
