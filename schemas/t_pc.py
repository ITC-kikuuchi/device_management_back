from datetime import date
from typing import Optional

from pydantic import BaseModel

"""
BaseModel は FastApi のスキーマモデルであることを示す。
Pc クラスは BaseModel を継承しているクラス
"""

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
    delete_flag: bool

    class Config:
        orm_mode = True

class pc(BaseModel):
    id: int
    label_name: Optional[str] = None
    pc_name: Optional[str] = None
    pc_user: Optional[str] = None
    manufacturer: Optional[str] = None
    type: Optional[str] = None

    class Config:
        orm_mode = True