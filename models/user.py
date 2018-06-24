from utils.database_settings import Base
from utils.settings import Column, Integer, String


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)
    is_active = Column(Integer, nullable=False, default=0)
