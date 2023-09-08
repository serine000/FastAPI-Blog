import os
from dataclasses import dataclass
from pathlib import Path

from dotenv import load_dotenv

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)


@dataclass
class Settings:
    PROJECT_NAME:str = "FastAPI project starting !"
    PROJECT_VERSION: str = "1.0.0"

    DATABASE_URL = "sqlite:///./sql_app.db"




settings = Settings()