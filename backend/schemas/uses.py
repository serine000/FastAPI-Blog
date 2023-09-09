from pydantic import BaseModel, Emailstr, Field

class UserCreate(BaseModel):
    email: Emailstr
    password: str = Field(..., min_length=4)