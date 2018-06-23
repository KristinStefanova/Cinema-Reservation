from .help_functions import has_capital, has_special_symbol
from .exceptions import (LessThanEightSymbolsError,
                         MissingCapitalLetterError,
                         MissingSpecialSymbolError)
from .settings import pbkdf2_hmac
from .settings import datetime


def validate_password(func):
    def decorated(username, password):
        if len(password) < 8:
            raise LessThanEightSymbolsError()
        if not has_capital(password):
            raise MissingCapitalLetterError()
        if not has_special_symbol(password):
            raise MissingSpecialSymbolError()
        return func(username, password)
    return decorated


def hashpassword(func):
    def decorated(username, password):
        hashpass = pbkdf2_hmac('sha256', password.encode(),
                               username.encode(), 10000).hex()
        return func(username, hashpass)
    return decorated


def log_info(func):
    def decorated(user_id, reservations):
        reservations = ", ".join([f'{res}' for res in reservations])
        info = f"{str(datetime.now())}, {user_id}, "
        with open("log.txt", "a") as file:
            file.write(info + reservations + '\n')
        return func(user_id, reservations)
    return decorated
