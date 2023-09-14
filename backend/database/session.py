"""
This file defines an SQLAlchemy engine with a SQLite database.
SQLite is a file system-based database.
"""
from typing import Generator

from conf.config import settings
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = settings.DATABASE_ENGINE

# Our actual database session
# We will create a database session for each request later
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_database() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
