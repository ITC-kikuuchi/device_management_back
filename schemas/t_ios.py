from typing import Optional

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