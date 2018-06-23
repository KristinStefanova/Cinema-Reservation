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
