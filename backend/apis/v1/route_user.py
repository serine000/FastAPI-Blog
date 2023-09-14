from database.repository.user import create_new_user
from database.session import get_database
from fastapi import APIRouter
from fastapi import Depends
from fastapi import status
from schemas.user import ShowUser
from schemas.user import UserCreate
from sqlalchemy.orm import Session

router = APIRouter()


@router.post("/users", response_model=ShowUser, status_code=status.HTTP_201_CREATED)
def create_user(user: UserCreate, db: Session = Depends(get_database)):
    """
    Create a user only after verifying that the request follows the UserCreate schema
    and fetching the database session.
    """
    user = create_new_user(user, db)
    return user
