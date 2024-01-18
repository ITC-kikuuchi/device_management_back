from typing import Optional

from pydantic import BaseModel

"""
BaseModel は FastApi のスキーマモデルであることを示す。
Pc クラスは BaseModel を継承しているクラス
"""
class pc(BaseModel):
    id: int
    label_name: Optional[str] = None
    pc_name: Optional[str] = None
    pc_user: Optional[str] = None
    manufacturer: Optional[str] = None
    type: Optional[str] = None

    class Config:
        orm_mode = True