from models.user import User
from utils.database_settings import session
from utils.decorators import validate_password, hashpassword


class UserController:
    @classmethod
    @validate_password
    @hashpassword
    def create(cls, username, password):
        user = User(username=username, password=password)
        session.add(user)
        session.commit()

    @classmethod
    def remove(cls, user_id):
        user = session.query(User).filter(User.id == user_id).one()
        session.delete(user)

    @classmethod
    @hashpassword
    def get(cls, username, password):
        user = session.query(User).filter(User.username == username,
                                          User.password == password).one()
        return user

    @classmethod
    @hashpassword
    def is_user(cls, username, password):
        user = session.query(User).filter(User.username == username,
                                          User.password == password).one()
        return False if user is None else True

    @classmethod
    @hashpassword
    def is_logged(cls, username, password):
        user = session.query(User).filter(User.username == username,
                                          User.password == password).one()
        return True if user.is_active == 1 else False

    @classmethod
    @hashpassword
    def logged(cls, username, password):
        user = session.query(User).filter(User.username == username,
                                          User.password == password).one()
        user.is_active = 1
        session.commit()

    @classmethod
    def log_out(cls, user_id):
        user = session.query(User).filter(User.id == user_id).one()
        user.is_active = 0
        session.commit()
