import os
from dataclasses import dataclass
from pathlib import Path

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy import Engine

env_path = Path(".") / ".env"
load_dotenv(dotenv_path=env_path)


@dataclass
class Settings:
    PROJECT_NAME: str = "FastAPI project starting !"
    PROJECT_VERSION: str = "1.0.0"

    # Database settings
    DATABASE_URL = "sqlite:///./sql_app.db"
    DATABASE_ENGINE: Engine = create_engine(
        DATABASE_URL, connect_args={"check_same_thread": False}
    )

    JWT_SECRET_KEY: str = os.getenv("SECRET_KEY")
    JWT_ALGORITHM = "HS256"
    JWT_ACCESS_TOKEN_EXPIRE_MINUTES = 30


settings = Settings()
