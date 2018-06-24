import unittest
import sys
sys.path.append('/home/kristin/Cinema-Reservation')
from utils.exceptions import *
from utils.database_settings import Database
from controllers.reservation_controller import ReservationController
from populate import add_movies, add_users, add_projections, add_reservations


class ReservationControllerTest(unittest.TestCase):
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

    def test_create_with_incorrect_seat_raises_error(self):
        user_id = 1
        projection_id = 1
        row = 22
        column = 33
        with self.assertRaises(SeatOutOfRangeError):
            ReservationController.create(user_id, projection_id, row, column)

    def test_create_with_taken_seat_raises_error(self):
        user_id = 1
        projection_id = 2
        row = 2
        column = 3
        with self.assertRaises(TakenSeatError):
            ReservationController.create(user_id, projection_id, row, column)

    def test_get_reservation(self):
        data = (1, 2, 2, 3)
        actual = ReservationController.get(*data)
        self.assertEqual(
            (actual.user_id, actual.projection_id, actual.row, actual.column),
            data)

    def test_get_reservation_raises_error(self):
        data = (2, 2, 2, 3)
        with self.assertRaises(ReservationDoesNotExist):
            ReservationController.get(*data)

    def test_get_all_reservations_for_projection(self):
        projection_id = 2
        expected = [(2, 3), (2, 4)]
        actual = ReservationController.get_all_reservations_for_projection(
            projection_id)
        self.assertEqual(actual, expected)

    def test_get_all_reservations_for_projection_without_reservations(self):
        projection_id = 1
        expected = []
        actual = ReservationController.get_all_reservations_for_projection(
            projection_id)
        self.assertEqual(actual, expected)

    def test_check_tickets_for_projection_less_than_avaliable(self):
        projection_id = 2
        tickets = 2
        self.assertTrue(ReservationController.check_tickets_for_projection(
            projection_id, tickets))

    def test_check_tickets_for_projection_great_than_avaliable(self):
        projection_id = 2
        tickets = 99
        self.assertFalse(ReservationController.check_tickets_for_projection(
            projection_id, tickets))


if __name__ == "__main__":
    unittest.main()
