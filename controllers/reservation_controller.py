from models.reservation import Reservation
from models.hall import Hall
from utils.database_settings import session
from utils.exceptions import (TakenSeatError,
                              ReservationDoesNotExist,
                              SeatOutOfRangeError)
from utils.settings import HALL_SEATS, HALL_MAX_SIZE


class ReservationController:
    @classmethod
    def create(cls, user_id, projection_id, row, column):
        if cls.is_seat_valid(row, column):
            if cls.is_seat_avaliable(projection_id, row, column):
                reservation = Reservation(
                    user_id=user_id,
                    projection_id=projection_id,
                    row=row,
                    column=column)
                session.add(reservation)
                session.commit()
            else:
                raise TakenSeatError()
        else:
            raise SeatOutOfRangeError()

    @staticmethod
    def remove(reservation_id):
        reservation = session.query(Reservation).filter(
            Reservation.id == reservation_id).one_or_none()
        session.delete(reservation)

    @staticmethod
    def get(user_id, projection_id, row, column):
        reservation = session.query(Reservation).filter(
            Reservation.user_id == user_id,
            Reservation.projection_id == projection_id,
            Reservation.row == row,
            Reservation.column == column).one_or_none()

        if reservation is None:
            raise ReservationDoesNotExist()
        else:
            return reservation

    @staticmethod
    def get_all_reservations_for_projection(projection_id):
        reservations = session.query(
            Reservation.row,
            Reservation.column).filter(
            Reservation.projection_id == projection_id).all()

        return reservations

    @classmethod
    def is_seat_avaliable(cls, projection_id, row, column):
        reserved = cls.get_all_reservations_for_projection(projection_id)

        return True if (row, column) not in reserved else False

    @staticmethod
    def is_seat_valid(row, column):
        valid_row = row > 0 and row < HALL_MAX_SIZE + 1
        valid_column = column > 0 and column < HALL_MAX_SIZE + 1

        if valid_row and valid_column:
            return True
        else:
            return False

    @staticmethod
    def check_tickets_for_projection(projection_id, tickets):
        avaliable = HALL_SEATS - session.query(
            Reservation).filter(
            Reservation.projection_id == projection_id).count()

        return True if tickets <= avaliable else False

    @classmethod
    def get_projection_hall(cls, projection_id):
        reserved = cls.get_all_reservations_for_projection(projection_id)
        projection_hall = Hall()
        for row, column in reserved:
            projection_hall.take_seat(row, column)

        return projection_hall
