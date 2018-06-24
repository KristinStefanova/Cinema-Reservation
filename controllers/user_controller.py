from models.user import User
from utils.database_settings import session
from utils.decorators import validate_password, hashpassword
from utils.exceptions import UserDoesNotExist


class UserController:
    @staticmethod
    @validate_password
    @hashpassword
    def create(username, password):
        user = User(username=username, password=password)
        session.add(user)
        session.commit()

    @staticmethod
    def remove(user_id):
        user = session.query(User).filter(User.id == user_id).one_or_none()
        session.delete(user)

    @staticmethod
    def get_by_username(username):
        user = session.query(User).filter(
            User.username == username).one_or_none()
        if user is None:
            raise UserDoesNotExist()
        else:
            return user

    @staticmethod
    def is_logged(username):
        user = UserController.get_by_username(username)
        return True if user.is_active == 1 else False

    @staticmethod
    def log_in(username):
        user = UserController.get_by_username(username)
        user.is_active = 1
        session.commit()

    @staticmethod
    def log_out(user_id):
        user = session.query(User).filter(User.id == user_id).one_or_none()
        user.is_active = 0
        session.commit()
