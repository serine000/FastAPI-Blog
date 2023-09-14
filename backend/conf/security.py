"""
We make use of a secret key and algorithms to encode
the data dictionary we recieve from the user to get a dedicated access token.
"""
import os
import logging
from datetime import datetime
from datetime import timedelta
from typing import Optional

from conf.config import settings
from jose import jwt


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    """
    Generate a JSON Web Token (JWT) access token.

    Args:
        data (dict): A dictionary of data to be encoded.
        expires_delta (Optional[timedelta]): An optional
            expiration time for the token.
            If not provided, it defaults to the value
            specified in the settings.

    Returns:
        str: The encoded JWT access token.

    Example Usage:
        data = {"user_id": 123}
        expires_delta = timedelta(hours=1)
        access_token = create_access_token                         (data, expires_delta)
        print(access_token)
    """
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(
            minutes=settings.JWT_ACCESS_TOKEN_EXPIRE_MINUTES
        )
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(
        to_encode, settings.JWT_SECRET_KEY, algorithm=settings.JWT_ALGORITHM
    )
    return encoded_jwt
