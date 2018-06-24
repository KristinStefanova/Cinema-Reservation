from utils.database_settings import Database
from controllers.main_controller import add_movie

Database.create()
add_movie("aaaa", 5)

Database.drop()