from typing import Optional
from datetime import date, timezone, timedelta, datetime

from pydantic import BaseModel, Field

"""
BaseModel は FastApi のスキーマモデルであることを示す。
android クラスは BaseModel を継承しているクラス
"""

class android(BaseModel):
    id: int
    label_name: Optional[str] = None
    android_name: Optional[str] = None
    manufacturer: Optional[str] = None
    type: Optional[str] = None
    os: Optional[str] = None
    delete_flag: bool

    class Config:
        orm_mode = True