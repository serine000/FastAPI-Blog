from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database.session import get_database
from database.repository.user import create_new_user
from schemas.user import UserCreate

router = APIRouter()


@router.post("/")
def create_user(user: UserCreate, db: Session = Depends(get_database)):
    """
    Create a user only after verifying that the request follows the UserCreate schema
    and fetching the database session.
    """
    user = create_new_user(user, db)
    return user 
