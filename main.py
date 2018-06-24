from utils.database_settings import Database
from view.menu import Menu


def main():
    Database.create()
    Menu.start()


if __name__ == '__main__':
    main()
