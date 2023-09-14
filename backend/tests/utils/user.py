from database.repository.user import create_new_user
from schemas.user import UserCreate
from sqlalchemy.orm import Session


def create_random_user(db: Session):
    create_user = UserCreate(email="ping@fastapitutorial.com", password="Hello!")
    user = create_new_user(user=create_user, db_session=db)
    return user
