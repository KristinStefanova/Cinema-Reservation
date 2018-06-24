from models.projection import Projection
from models.reservation import Reservation
from models.movie import Movie
from utils.database_settings import session
from utils.settings import func
from utils.exceptions import ProjectionIdError


class ProjectionController:
    @staticmethod
    def create(movie_id, movie_type, date, time):
        projection = Projection(movie_id=movie_id,
                                type=movie_type,
                                date=date,
                                time=time)
        session.add(projection)
        session.commit()

    @staticmethod
    def remove(projection_id):
        projection = session.query(Projection).filter(
            Projection.id == projection_id).one_or_none()
        session.delete(projection)

    @staticmethod
    def get_all_by_movie_id(movie_id):
        projections = session.query(
            Projection.id,
            Projection.date,
            Projection.time,
            Projection.type).filter(
            Projection.movie_id == movie_id).order_by(
            Projection.date, Projection.time).all()

        return projections

    @staticmethod
    def get_all_by_movie_id_and_date(movie_id, date):
        projections = session.query(
            Projection.id,
            Projection.time,
            Projection.type).filter(
            Projection.movie_id == movie_id,
            Projection.date == date).order_by(
            Projection.date, Projection.time).all()

        return projections

    @staticmethod
    def get_all_with_avaliable_seats(movie_id):
        subquery = session.query(
            Reservation.projection_id, func.count(
                Reservation.projection_id).label('seats')).group_by(
            Reservation.projection_id).subquery()
        projections = session.query(
            Projection.id,
            Projection.date,
            Projection.time,
            Projection.type,
            (100 - func.coalesce(subquery.c.seats, 0))).outerjoin(
            subquery, Projection.id == subquery.c.projection_id).filter(
                Projection.movie_id == movie_id).order_by(
                Projection.date, Projection.time).all()

        return projections

    @staticmethod
    def get_by_id(projection_id):
        projection = session.query(
            Movie.name,
            Movie.rating,
            Projection.date,
            Projection.time,
            Projection.type).filter(
            Projection.movie_id == Movie.id,
            Projection.id == projection_id).one_or_none()

        if projection is None:
            raise ProjectionIdError()
        else:
            return projection
