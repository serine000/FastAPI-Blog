from conf.hashing import Hasher
from database.models.user import User
from schemas.user import UserCreate
from sqlalchemy.orm import Session


def create_new_user(user: UserCreate, db_session: Session):
    user = User(
        email=user.email,
        password=Hasher.generate_password_hash(password=user.password),
        is_active=True,
        is_superuser=False,
    )
    db_session.add(user)
    db_session.commit()
    db_session.refresh(user)
    return user
