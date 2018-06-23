class TakenSeatError(Exception):
    def __init__(self):
        Exception.__init__(self, "This seat is taken!")


class LessThanEightSymbolsError(Exception):
    def __init__(self):
        Exception.__init__(self, "The password is less than 8 symbols!")


class MissingCapitalLetterError(Exception):
    def __init__(self):
        Exception.__init__(
            self, "The password must contain at least one capital letter!")


class MissingSpecialSymbolError(Exception):
    def __init(self):
        Exception.__init__(
            self, "The password must contain at least one special symbol!")


class MovieRatingOutOfRangeError(Exception):
    def __init__(self):
        Exception.__init__(self, "Movie rating must be in range 1.0 - 10.0!")


class MovieIdError(Exception):
    def __init__(self):
        Exception.__init__(self, "Movie ID not expected!")
