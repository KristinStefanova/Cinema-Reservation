from models.reservation import Reservation
from models.hall import Hall
from utils.database_settings import session
from utils.exceptions import TakenSeatError
from utils.settings import HALL_SEATS


class ReservationController:
    @classmethod
    def create(cls, user_id, projection_id, row, column):
        if cls.is_seat_avaliable_for_projection(projection_id, row, column):
            reservation = Reservation(
                user_id=user_id,
                projection_id=projection_id,
                row=row,
                column=column)
            session.add(reservation)
            session.commit()
        else:
            raise TakenSeatError()

    @staticmethod
    def remove(reservation_id):
        reservation = session.query(Reservation).filter(
            Reservation.id == reservation_id).one()
        session.delete(reservation)

    @staticmethod
    def get(user_id, projection_id, row, column):
        reservation = session.query(Reservation).filter(
            Reservation.user_id == user_id,
            Reservation.projection_id == projection_id,
            Reservation.row == row,
            Reservation.column == column).one_or_none()

        return reservation

    @staticmethod
    def get_all_reservations_for_projection(projection_id):
        reservations = session.query(
            Reservation.row,
            Reservation.column).filter(
            Reservation.projection_id == projection_id).all()

        return reservations

    @classmethod
    def is_seat_avaliable_for_projection(cls, projection_id, row, column):
        reserved = cls.get_all_reservations_for_projection(projection_id)

        return True if (row, column) not in reserved else False

    @staticmethod
    def check_tickets_for_projection(projection_id, tickets):
        avaliable = HALL_SEATS - session.query(
            Reservation).filter(
            Reservation.projection_id == projection_id).count()

        return True if tickets < avaliable else False

    @classmethod
    def get_projection_hall(cls, projection_id):
        reserved = cls.get_all_reservations_for_projection(projection_id)
        projection_hall = Hall()
        for row, column in reserved:
            projection_hall.take_seat()

        return projection_hall
