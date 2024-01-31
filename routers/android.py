from fastapi import APIRouter, Depends,  HTTPException
from sqlalchemy.orm import Session
from database import get_db
from routers.auth import get_current_user

import schemas.t_android as android_schema
import cruds.t_android as android_crud

router=APIRouter()

# Android一覧取得API
@router.get("/android", response_model=list[android_schema.android])
def getAndroid(login_user: dict = Depends(get_current_user), db: Session = Depends(get_db)):
    try:
        return android_crud.getAndroid(db)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Android登録API
@router.post("/android")
def createAndroid():
    pass

# Android詳細取得API
@router.get("/android/{android_id}")
def createAndroid():
    pass

# Android更新API
@router.put("/android/{android_id}")
def updateAndroid():
    pass

# Android削除API
@router.delete("/android/{android_id}")
def deleteAndroid():
    pass