import unittest
import sys
sys.path.append('/home/kristin/Cinema-Reservation')
from utils.exceptions import (LessThanEightSymbolsError,
                              MissingSpecialSymbolError,
                              MissingCapitalLetterError,
                              UserDoesNotExist)
from utils.database_settings import Database
from controllers.user_controller import UserController
from populate import add_users


class UserControllerTest(unittest.TestCase):
    db = Database

    @classmethod
    def setUpClass(cls):
        cls.db.create()
        add_users()

    @classmethod
    def tearDownClass(cls):
        cls.db.drop()

    def test_create_with_password_length_less_than_8(self):
        with self.assertRaises(LessThanEightSymbolsError):
            UserController.create("KrisiK", "1234K!")

    def test_create_with_password_missing_special_symbol(self):
        with self.assertRaises(MissingSpecialSymbolError):
            UserController.create("KrisiK", "1234567K")

    def test_create_with_password_missing_capital_letter(self):
        with self.assertRaises(MissingCapitalLetterError):
            UserController.create("KrisiK", "1234567!")

    def test_get_by_username(self):
        expected = "Krisi"
        actual = UserController.get_by_username("Krisi")
        self.assertEqual(actual.username, expected)

    def test_get_by_username_user_does_not_exist(self):
        with self.assertRaises(UserDoesNotExist):
            UserController.get_by_username("Sasho")

    def test_is_user_logged(self):
        self.assertFalse(UserController.is_logged("Krisi"))

    def test_log_user_in(self):
        UserController.log_in("Krisi")
        self.assertTrue(UserController.is_logged("Krisi"))

    def test_log_user_out(self):
        UserController.log_in("Krisi")
        UserController.log_out("Krisi")
        self.assertFalse(UserController.is_logged("Krisi"))


if __name__ == "__main__":
    unittest.main()
