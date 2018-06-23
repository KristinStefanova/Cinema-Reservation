from models.projection import Projection
from models.reservation import Reservation
from models.movie import Movie
from utils.database_settings import session
from utils.settings import func


class ProjectionController:
    @classmethod
    def create(cls, movie_id, movie_type, date, time):
        projection = Projection(movie_id=movie_id,
                                type=movie_type,
                                date=date,
                                time=time)
        session.add(projection)
        session.commit()

    @classmethod
    def remove(cls, projection_id):
        projection = session.query(Projection).filter(
            Projection.id == projection_id).one()
        session.delete(projection)

    @classmethod
    def get_all_by_movie_id(cls, movie_id):
        projections = session.query(
            Projection.id,
            Projection.date,
            Projection.time,
            Projection.type).filter(
            Projection.movie_id == movie_id).order_by(
            Projection.date).all(),
        return projections

    @classmethod
    def get_all_by_movie_id_and_date(cls, movie_id, date):
        projections = session.query(
            Projection.id,
            Projection.time,
            Projection.type).filter(
            Projection.movie_id == movie_id,
            Projection.date == date).order_by(
            Projection.time).all(),
        return projections

    @classmethod
    def get_all_with_avaliable_seats(cls, movie_id):
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
                Projection.movie_id == movie_id).all()
        return projections

    @classmethod
    def get(cls, projection_id):
        projection = session.query(
            Movie.name,
            Movie.rating,
            Projection.date,
            Projection.time,
            Projection.type).filter(
            Projection.movie_id == Movie.id,
            Projection.id == projection_id).one()
        return projection
