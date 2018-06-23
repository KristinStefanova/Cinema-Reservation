from .settings import declarative_base, create_engine, DB_NAME, sessionmaker

Base = declarative_base()


class Database:
    engine = create_engine(f"sqlite:///{DB_NAME}")

    @classmethod
    def create(cls):
        Base.metadata.create_all(cls.engine)

    @classmethod
    def drop(cls):
        Base.metadata.drop_all(cls.engine)


Session = sessionmaker(bind=Database.engine)
session = Session()
