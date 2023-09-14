import logging

from apis.base import api_router
from conf.config import settings
from database.base import Base
from database.session import engine
from fastapi import FastAPI


def create_tables():
    Base.metadata.create_all(bind=engine)


def include_router(app: FastAPI):
    app.include_router(api_router)


def start_application(settings):
    logging.info("Starting application...")
    try:
        app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)
        create_tables()
        include_router(app)
        logging.info("Application started successfully.")
        return app
    except Exception as e:
        logging.info("Could not start the application.")
        # Handle the exception here, for example:
        raise Exception("An error occurred")


app = start_application(settings)


@app.get("/")
async def hello_api():
    """
    Returns a JSON response with the message "Hello FastAPI".
    """
    return {"msg": "Hello FastAPI"}
