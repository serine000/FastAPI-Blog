# FastAPI Project

This is a simple blog application developed using python, sqlalchemy, alembic, docker and FastAPI.

## Steps
1. Setup a virtual environement using `python3 -m venv venv`
2. Activate that environement using `cd backend` then running `make install`
3. Launch the app using ` uvicorn main:app --reload` and view your web app on http://127.0.0.1:8000/

## Concepts

- A **request-response cycle** explains the journey of the browser making a request and our framework (e.g. FastAPI, Django, etc) sending back a response. It describs how a web application handles incoming HTTP requests and produces corresponding HTTP responses.

- In SQLAlchemy, **models** refer to the classes that represent the structure and behavior of database tables. These classes are used to interact with the database using Python code.