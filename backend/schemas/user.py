from pydantic import BaseModel
from pydantic import EmailStr
from pydantic import Field


class UserCreate(BaseModel):
    """Expected format fo user creation request"""

    email: EmailStr
    password: str = Field(..., min_length=4)


class ShowUser(BaseModel):
    """Format of the user creation response"""

    id: int
    email: EmailStr
    is_active: bool

    class Config:
        """Convert non-dictionary objects to json"""

        orm_mode = True
