from fastapi import APIRouter, Depends,  HTTPException
from sqlalchemy.orm import Session
from database import get_db
from routers.auth import get_current_user

router=APIRouter()

# Windows(スマホ)一覧取得API
@router.get("/windows")
def getWindows():
    pass

# Windows(スマホ)登録API
@router.post("/windows")
def createWindows():
    pass

# Windows(スマホ)詳細取得API
@router.get("/windows/{windows_id}")
def getWindowsDetail():
    pass

# Windows(スマホ)更新API
@router.put("/windows/{windows_id}")
def updateWindows():
    pass

# Windows(スマホ)削除API
@router.delete("/windows/{windows_id}")
def deleteWindows():
    pass