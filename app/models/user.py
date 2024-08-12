from pydantic import BaseModel, EmailStr
from typing import Optional

class UserModel(BaseModel):
    username: str
    email: EmailStr
    full_name: Optional[str] = None
    disabled: Optional[bool] = None

    class Config:
        orm_mode  = True