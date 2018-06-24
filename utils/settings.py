from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (Column, Integer, String, Float, Boolean,
                        CheckConstraint, ForeignKey, create_engine)
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.sql import func
from hashlib import pbkdf2_hmac
from datetime import datetime
from tabulate import tabulate


DB_NAME = "cinama.db"
HALL_MIN_SIZE = 1
HALL_MAX_SIZE = 10

LOW_MOVIE_RATING = 1
HIGH_MOVIE_RATING = 10

HALL_SEATS = HALL_MAX_SIZE * HALL_MAX_SIZE

SALT = 10000
