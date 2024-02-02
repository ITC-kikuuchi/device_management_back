from typing import Optional
from datetime import date, timezone, timedelta, datetime

from pydantic import BaseModel, Field

"""
BaseModel は FastApi のスキーマモデルであることを示す。
android クラスは BaseModel を継承しているクラス
"""

# 日本時間のタイムゾーンの設定
jst = timezone(timedelta(hours=9))

class android(BaseModel):
    id: int
    label_name: Optional[str] = None
    android_name: Optional[str] = None
    manufacturer: Optional[str] = None
    type: Optional[str] = None
    os: Optional[str] = None
    delete_flag: bool
    last_updated_flag: bool

    class Config:
        orm_mode = True

class createAndroid(BaseModel):
    label_name: Optional[str] = None
    android_name: Optional[str] = None
    manufacturer: Optional[str] = None
    type: Optional[str] = None
    os: Optional[str] = None
    carrier: Optional[str] = None
    condition: Optional[str] = None
    delivery_date: Optional[date] = None
    disposal_date: Optional[date] = None
    remarks: Optional[str] = None
    location: Optional[str] = None
    last_updated_flag: bool = Field(default=True)
    created_at: Optional[datetime] = Field(default_factory=lambda: datetime.now(jst))
    updated_at: Optional[datetime] = Field(default_factory=lambda: datetime.now(jst))

    class Config:
        orm_mode = True

class detailAndroid(BaseModel):
    label_name: Optional[str] = None
    android_name: Optional[str] = None
    manufacturer: Optional[str] = None
    type: Optional[str] = None
    os: Optional[str] = None
    carrier: Optional[str] = None
    condition: Optional[str] = None
    delivery_date: Optional[date] = None
    disposal_date: Optional[date] = None
    remarks: Optional[str] = None
    location: Optional[str] = None
    delete_flag: bool

    class Config:
        orm_mode = True

class updateAndroid(BaseModel):
    label_name: Optional[str] = None
    android_name: Optional[str] = None
    manufacturer: Optional[str] = None
    type: Optional[str] = None
    os: Optional[str] = None
    carrier: Optional[str] = None
    condition: Optional[str] = None
    delivery_date: Optional[date] = None
    disposal_date: Optional[date] = None
    remarks: Optional[str] = None
    location: Optional[str] = None
    last_updated_flag: bool = Field(default=True)
    updated_at: Optional[datetime] = Field(default_factory=lambda: datetime.now(jst))

    class Config:
        orm_mode = True