from typing import Optional

from pydantic import BaseModel

class user(BaseModel):
    mail_address: Optional[str] = None
    password: Optional[str] = None
