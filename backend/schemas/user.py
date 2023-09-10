from pydantic import BaseModel, EmailStr, Field

class UserCreate(BaseModel):
    """Expected format fo user creation request"""
    email: EmailStr
    password: str = Field(..., min_length=4)


class ShowUser(BaseModel):
    """Format of the user creation response"""
    id: int
    email : EmailStr
    is_active : bool

    class Config():
        """Convert non-dictionary objects to json"""
        orm_mode = True