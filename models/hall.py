from utils.exceptions import TakenSeatError
from utils.settings import HALL_SIZE


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

    def __str__(self):
        return self.__current

    def __repr__(self):
        return self.__str__


class Hall:
    def __init__(self):
        self.__map = self.create()

    def create(self):
        self.__map = []
        for i in range(HALL_SIZE):
            sub_row = []
            for j in range(HALL_SIZE):
                sub_row.append(Seat(i, j))
            self.__map.append(sub_row)
        return self.__map

    def take_seat(self, row, column):
        if self.__map[row - 1][column - 1].is_free():
            self.__map[row - 1][column - 1].take()
        else:
            raise TakenSeatError()

    def free_seat(self, row, column):
        self.__map[row - 1][column - 1].free()

    def show(self):
        print(' ', end=' ')
        for i in range(1, 11):
            print(i, end=' ')
        print()
        for i, value in enumerate(self.__map):
            print(i + 1, end=' ')
            for sub_item in value:
                print(sub_item, end=' ')
            print()
