"""
This file defines an sqlalchemy engine with a sqlite database.
sqlite is a ifle system based database.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from conf.config import settings


SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, 
    connect_args = {"check_same_thread": False}
)

# Our actual database session
# We will create a database session for each request later
SessionLocal = sessionmaker(
    autocommit = False,
    autoflush = False,
    bind = engine)