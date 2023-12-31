# FastAPI Project

This is a simple blog application developed using python, sqlalchemy, alembic, docker and FastAPI.

## Steps
1. Setup a virtual environement using `python3 -m venv venv`
2. Activate that environement using `cd backend` then running `make install`
3. Launch the app using `uvicorn main:app --reload` and view your web app on http://127.0.0.1:8000/

## Concepts

- A **request-response cycle** explains the journey of the browser making a request and our framework (e.g. FastAPI, Django, etc) sending back a response. It describs how a web application handles incoming HTTP requests and produces corresponding HTTP responses.

- In SQLAlchemy, **models** refer to the classes that represent the structure and behavior of database tables. These classes are used to interact with the database using Python code.

- A **schema** is used to validate the data we receive as well as to reformat the data that we want to send to the client/browser. We create pydantic classes that verify the types, called Schemas.

- We use the **repository pattern** in this code to encapsulate all database operations and make sure the application only interacts with the repository while keeping the database code isolated in one place.

- In a typical blog list, we are more concerned about **rendering a list of blogs** instead of just fetching one single blog. This is generally called a list view.

- For deleting a blog, since blog object has no delete() method defined we instead call in the **reference of the blog object** with the `first()` function and delete it.

- In our unit tests, we will be overriding the `get_database()` dependency and providing our brand new test database instead. This concept is known as **dependency injection**.

- In order to skip any pre-commit hooks, run `--no-verify` after your commit message in your git commit command.

- To run the pre-commit on all your codebase run `pre-commit run --all-files`

- In most API-based approaches, a commong way to ensure user authentication is by using **JSON Web Tokens**, aka jwt-based authentication.

- **Authentication** is related to login and **authorization** is related to permission.