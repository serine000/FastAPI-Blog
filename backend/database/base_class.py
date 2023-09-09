"""
This model class is a representation of our databse table.
This is the Base parent class for all future database tables.
Later, we inherit from this Base class when creating SQLAlchemy model classes.
In SQLAlchemy, models refer to the classes that represent 
the structure and behavior of database tables. 
"""

from typing import Any
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.orm import as_declarative

@as_declarative()
class Base:
    """
    Declarative base class for all SQLAlchemy model classes.
    """

    id: Any
    __name__: str

    @declared_attr
    def __tablename__(cls) -> str:
        """
        Generates the name of the database table associated with the SQLAlchemy model class.
        Derives the table name from the class name.
        """
        return cls.__name__.lower()