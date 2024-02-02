from datetime import date, datetime, timezone, timedelta
from typing import Optional

from pydantic import BaseModel, Field

"""
BaseModel は FastApi のスキーマモデルであることを示す。
Pc クラスは BaseModel を継承しているクラス
"""

# 日本時間のタイムゾーンの設定
jst = timezone(timedelta(hours=9))

class pc(BaseModel):
    id: int
    label_name: Optional[str] = None
    pc_name: Optional[str] = None
    pc_user: Optional[str] = None
    manufacturer: Optional[str] = None
    type: Optional[str] = None
    delete_flag: bool
    last_updated_flag: bool

    class Config:
        orm_mode = True

class createPc(BaseModel):
    label_name: Optional[str] = None
    pc_name: Optional[str] = None
    user_name: Optional[str] = None
    pc_user: Optional[str] = None
    condition: Optional[str] = None
    manufacturer: Optional[str] = None
    type: Optional[str] = None
    service_tag: Optional[str] = None
    os: Optional[str] = None
    bit: int = None
    ie_version: Optional[str] = None
    ip_address: Optional[str] = None
    gx_wwp_license: Optional[str] = None
    delivery_date: Optional[date] = None
    disposal_date: Optional[date] = None
    remarks: Optional[str] = None
    last_updated_flag: bool = Field(default=True)
    created_at: Optional[datetime] = Field(default_factory=lambda: datetime.now(jst))
    updated_at: Optional[datetime] = Field(default_factory=lambda: datetime.now(jst))

    class Config:
        orm_mode = True

class detailPc(BaseModel):
    id: int
    label_name: Optional[str] = None
    pc_name: Optional[str] = None
    user_name: Optional[str] = None
    pc_user: Optional[str] = None
    condition: Optional[str] = None
    manufacturer: Optional[str] = None
    type: Optional[str] = None
    service_tag: Optional[str] = None
    os: Optional[str] = None
    bit: int = None
    ie_version: Optional[str] = None
    ip_address: Optional[str] = None
    gx_wwp_license: Optional[str] = None
    delivery_date: Optional[date] = None
    disposal_date: Optional[date] = None
    remarks: Optional[str] = None

    class Config:
        orm_mode = True

class updatePc(BaseModel):
    label_name: Optional[str] = None
    pc_name: Optional[str] = None
    user_name: Optional[str] = None
    pc_user: Optional[str] = None
    condition: Optional[str] = None
    manufacturer: Optional[str] = None
    type: Optional[str] = None
    service_tag: Optional[str] = None
    os: Optional[str] = None
    bit: int = None
    ie_version: Optional[str] = None
    ip_address: Optional[str] = None
    gx_wwp_license: Optional[str] = None
    delivery_date: Optional[date] = None
    disposal_date: Optional[date] = None
    remarks: Optional[str] = None
    last_updated_flag: bool = Field(default=True)
    updated_at: Optional[datetime] = Field(default_factory=lambda: datetime.now(jst))

    class Config:
        orm_mode = True