import unittest
import sys
sys.path.append('/home/kristin/Cinema-Reservation')
from utils.exceptions import *
from utils.database_settings import Database
from controllers.movie_controller import MovieController
from populate import add_movies


class MovieControllerTest(unittest.TestCase):
    db = Database

    @classmethod
    def setUpClass(cls):
        cls.db.create()
        add_movies()

    @classmethod
    def tearDownClass(cls):
        cls.db.drop()

    def test_create_with_incorrect_rating(self):
        with self.assertRaises(MovieRatingOutOfRangeError):
            MovieController.create("Movie with wrong rating", -5)

    def test_get_all_movies(self):
        expected = [(1, "The Hunger Games: Catching Fire", 7.5),
                    (2, "Wreck-It Ralph", 7.8),
                    (3, "Her", 8.3),
                    (4, "Avengers: Infinity War", 8.8)]
        actual = MovieController.get_all()
        self.assertEqual(expected, actual)

    def test_get_movie_with_correct_id(self):
        movie_id = 1
        expected = (1, "The Hunger Games: Catching Fire", 7.5)
        actual = MovieController.get_by_id(movie_id)
        self.assertEqual(expected, actual)

    def test_get_movie_with_incorrect_id(self):
        movie_id = 42
        with self.assertRaises(MovieIdError):
            MovieController.get_by_id(movie_id)


if __name__ == "__main__":
    unittest.main()
