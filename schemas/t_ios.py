from typing import Optional
from datetime import date, timezone, timedelta, datetime

from pydantic import BaseModel, Field

"""
BaseModel は FastApi のスキーマモデルであることを示す。
ios クラスは BaseModel を継承しているクラス
"""

# 日本時間のタイムゾーンの設定
jst = timezone(timedelta(hours=9))

class ios(BaseModel):
    id: int
    label_name: Optional[str] = None
    ios_name: Optional[str] = None
    manufacturer: Optional[str] = None
    type: Optional[str] = None
    os: Optional[str] = None
    delete_flag: bool
    last_updated_flag: bool

    class Config:
        orm_mode = True

class createIos(BaseModel):
    label_name: Optional[str] = None
    ios_name: Optional[str] = None
    manufacturer: Optional[str] = None
    type: Optional[str] = None
    os: Optional[str] = None
    carrier: Optional[str] = None
    condition: Optional[str] = None
    delivery_date: Optional[date] = None
    disposal_date: Optional[date] = None
    remarks: Optional[str] = None
    last_updated_flag: bool = Field(default=True)
    created_at: Optional[datetime] = Field(default_factory=lambda: datetime.now(jst))
    updated_at: Optional[datetime] = Field(default_factory=lambda: datetime.now(jst))

    class Config:
        orm_mode = True

class detailIos(BaseModel):
    id: int
    label_name: Optional[str] = None
    ios_name: Optional[str] = None
    manufacturer: Optional[str] = None
    type: Optional[str] = None
    os: Optional[str] = None
    carrier: Optional[str] = None
    condition: Optional[str] = None
    delivery_date: Optional[date] = None
    disposal_date: Optional[date] = None
    remarks: Optional[str] = None
    delete_flag: bool

    class Config:
        orm_mode = True

class updateIos(BaseModel):
    label_name: Optional[str] = None
    ios_name: Optional[str] = None
    manufacturer: Optional[str] = None
    type: Optional[str] = None
    os: Optional[str] = None
    carrier: Optional[str] = None
    condition: Optional[str] = None
    delivery_date: Optional[date] = None
    disposal_date: Optional[date] = None
    remarks: Optional[str] = None
    delete_flag: bool
    last_updated_flag: bool = Field(default=True)
    updated_at: Optional[datetime] = Field(default_factory=lambda: datetime.now(jst))

    class Config:
        orm_mode = True