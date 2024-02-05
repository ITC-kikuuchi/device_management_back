from datetime import date, datetime, timezone, timedelta
from typing import Optional

from pydantic import BaseModel, Field

"""
BaseModel は FastApi のスキーマモデルであることを示す。
windows クラスは BaseModel を継承しているクラス
"""

class windows(BaseModel):
    id: int
    label_name: Optional[str] = None
    windows_name: Optional[str] = None
    manufacturer: Optional[str] = None
    type: Optional[str] = None
    os: Optional[str] = None
    delete_flag: bool
    last_updated_flag: bool

    class Config:
        orm_mode = True