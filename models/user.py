from utils.settings import Base, Column, Integer, String, Boolean


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)
    is_active = Column(Boolean, default=0)
