import unittest
import sys
sys.path.append('/home/kristin/Cinema-Reservation')
from utils.exceptions import *
from utils.database_settings import Database
from controllers.projection_controller import ProjectionController
from populate import add_movies, add_projections, add_reservations, add_users


class ProjectionControllerTest(unittest.TestCase):
    db = Database

    @classmethod
    def setUpClass(cls):
        cls.db.create()
        add_movies()
        add_projections()
        add_users()
        add_reservations()

    @classmethod
    def tearDownClass(cls):
        cls.db.drop()

    def test_get_all_by_movie_id_for_movie_with_projections(self):
        expected = [(4, "2018-05-25", "21:30:00", "3D"),
                    (1, "2018-05-25", "21:55:00", "3D"),
                    (3, "2018-05-26", "15:30:00", "2D"),
                    (2, "2018-05-27", "21:55:00", "4DX")
                    ]
        actual = ProjectionController.get_all_by_movie_id(1)
        self.assertEqual(expected, actual)

    def test_get_all_by_movie_id_for_movie_without_projections(self):
        expected = []
        actual = ProjectionController.get_all_by_movie_id(2)
        self.assertEqual(expected, actual)

    def test_get_all_by_movie_id_date_for_movie_with_projections(self):
        expected = [(4, "21:30:00", "3D"),
                    (1, "21:55:00", "3D")
                    ]
        actual = ProjectionController.get_all_by_movie_id_and_date(
            1, "2018-05-25")
        self.assertEqual(expected, actual)

    def test_get_all_by_movie_id_date_for_movie_without_projections(self):
        expected = []
        actual = ProjectionController.get_all_by_movie_id_and_date(
            2, "2018-05-25")
        self.assertEqual(expected, actual)

    def test_get_all_with_avaliable_seats_for_movie_with_projections(self):
        expected = [(4, "2018-05-25", "21:30:00", "3D", 100),
                    (1, "2018-05-25", "21:55:00", "3D", 100),
                    (3, "2018-05-26", "15:30:00", "2D", 100),
                    (2, "2018-05-27", "21:55:00", "4DX", 98)]
        actual = ProjectionController.get_all_with_avaliable_seats(1)
        self.assertEqual(expected, actual)

    def test_get_all_with_avaliable_seats_for_movie_without_projections(self):
        expected = []
        actual = ProjectionController.get_all_with_avaliable_seats(2)
        self.assertEqual(expected, actual)

    def test_get_by_id(self):
        projection_id = 1
        expected = (
            "The Hunger Games: Catching Fire",
            7.5, "2018-05-25",
            "21:55:00", "3D")
        actual = ProjectionController.get_by_id(projection_id)
        self.assertEqual(expected, actual)

    def test_get_by_id_with_incorrect_id(self):
        projection_id = 42
        with self.assertRaises(ProjectionIdError):
            ProjectionController.get_by_id(projection_id)


if __name__ == "__main__":
    unittest.main()
