import unittest
import sys
sys.path.append('/home/kristin/Cinema-Reservation')

from utils.exceptions import TakenSeatError, SeatOutOfRangeError
from models.hall import Seat, Hall


class SeatTest(unittest.TestCase):

    def setUp(self):
        self.seat = Seat(1, 2)

    def test_take(self):
        self.seat.take()
        expected = 'X'
        actual = self.seat.get()
        self.assertEqual(actual, expected)

    def test_free(self):
        self.seat.take()
        self.seat.free()
        expected = '.'
        actual = self.seat.get()
        self.assertEqual(actual, expected)

    def test_is_free_for_free_seat(self):
        self.assertTrue(self.seat.is_free())

    def test_is_free_for_taken_seat(self):
        self.seat.take()
        self.assertFalse(self.seat.is_free())

    def test_get_seat(self):
        expected = '.'
        actual = self.seat.get()
        self.assertEqual(actual, expected)


class HallTest(unittest.TestCase):

    def setUp(self):
        self.hall = Hall()

    def test_get_seat(self):
        expected = '.'
        actual = self.hall.get_seat(2, 3)
        self.assertEqual(actual, expected)

    def test_take_seat(self):
        self.hall.take_seat(2, 3)
        expected = 'X'
        actual = self.hall.get_seat(2, 3)
        self.assertEqual(actual, expected)

    def test_double_take_seat(self):
        self.hall.take_seat(2, 3)
        with self.assertRaises(TakenSeatError):
            self.hall.take_seat(2, 3)

    def test_take_seat_out_of_hall_size(self):
        with self.assertRaises(SeatOutOfRangeError):
            self.hall.take_seat(22, 33)

    def test_free_seat(self):
        self.hall.take_seat(2, 3)
        self.hall.free_seat(2, 3)
        expected = '.'
        actual = self.hall.get_seat(2, 3)
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
