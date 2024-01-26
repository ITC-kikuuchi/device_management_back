from typing import Optional

from pydantic import BaseModel

class user(BaseModel):
    mail_address: Optional[str] = None
    password: Optional[str] = None

class loginUser(BaseModel):
    id: int
    user_name: Optional[str]

    class Config:
        orm_mode = True
