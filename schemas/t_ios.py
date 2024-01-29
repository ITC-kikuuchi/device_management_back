from typing import Optional
from datetime import date

from pydantic import BaseModel

"""
BaseModel は FastApi のスキーマモデルであることを示す。
ios クラスは BaseModel を継承しているクラス
"""

class ios(BaseModel):
    id: int
    label_name: Optional[str] = None
    ios_name: Optional[str] = None
    manufacturer: Optional[str] = None
    type: Optional[str] = None
    os: Optional[str] = None
    delete_flag: bool

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

    class Config:
        orm_mode = True