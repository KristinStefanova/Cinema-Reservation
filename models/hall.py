from utils.exceptions import TakenSeatError, SeatOutOfRangeError
from utils.settings import HALL_MAX_SIZE


class Seat:
    def __init__(self, row, column):
        self.__row = row
        self.__column = column
        self.__current = '.'

    def take(self):
        self.__current = 'X'

    def free(self):
        self.__current = '.'

    def is_free(self):
        return self.__current == '.'

    def get(self):
        return self.__current

    def __str__(self):
        return self.__current

    def __repr__(self):
        return str(self)


class Hall:
    def __init__(self):
        self.__map = self.create()

    @staticmethod
    def is_valid_seat(row, column):
        valid_row = row > 0 and row < HALL_MAX_SIZE + 1
        valid_column = column > 0 and column < HALL_MAX_SIZE + 1

        if valid_row and valid_column:
            return True
        else:
            return False

    def create(self):
        self.__map = [[Seat(i, j) for i in range(HALL_MAX_SIZE + 1)]
                      for j in range(HALL_MAX_SIZE + 1)]
        for i in range(HALL_MAX_SIZE + 1):
            for j in range(HALL_MAX_SIZE + 1):
                if i == 0 and j == 0:
                    self.__map[i][j] = ' '
                if i == 0 and j != 0:
                    self.__map[i][j] = str(j)
                if i != 0 and j == 0:
                    self.__map[i][j] = str(i)
        return self.__map

    def take_seat(self, row, column):
        if self.is_valid_seat(row, column):
            if self.__map[row][column].is_free():
                self.__map[row][column].take()
            else:
                raise TakenSeatError()
        else:
            raise SeatOutOfRangeError()

    def free_seat(self, row, column):
        self.__map[row][column].free()

    def get_seat(self, row, column):
        return self.__map[row][column].get()

    def __str__(self):
        hall = ""
        for i in range(HALL_MAX_SIZE + 1):
            row = ""
            for j in range(HALL_MAX_SIZE + 1):
                if i == HALL_MAX_SIZE and j == 1:
                    row += str(self.__map[i][j])
                else:
                    row += ' ' + str(self.__map[i][j])
            hall += row + '\n'
        return hall

    def __repr__(self):
        return str(self)
