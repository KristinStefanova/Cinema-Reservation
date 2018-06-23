from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (Column, Integer, String, Float, Boolean,
                        CheckConstraint, ForeignKey, create_engine)
from sqlalchemy.orm import relationship, sessionmaker


DB_NAME = "cinama.db"
