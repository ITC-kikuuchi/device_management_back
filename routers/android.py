from fastapi import APIRouter, Depends,  HTTPException
from sqlalchemy.orm import Session
from database import get_db
from routers.auth import get_current_user

import schemas.t_android as android_schema
import cruds.t_android as android_crud

router=APIRouter()

# 最終更新フラグを false に変更
def updateLastUpdateFlag(db: Session):
    # 最終更新データの取得
    android_data = android_crud.getLastUpdatedData(db)
    if android_data:
        # 最終更新データが存在した場合
        # 最終更新データの最終更新フラグの更新
        android_crud.updateLastUpdateFlag(db, android_data)

# Android一覧取得API
@router.get("/android", response_model=list[android_schema.android])
def getAndroid(login_user: dict = Depends(get_current_user), db: Session = Depends(get_db)):
    try:
        return android_crud.getAndroid(db)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Android登録API
@router.post("/android")
def createAndroid(android: android_schema.createAndroid, login_user: dict = Depends(get_current_user), db: Session = Depends(get_db)):
    try:
        # 最終更新フラグを false に変更
        updateLastUpdateFlag(db)
        # Android情報の登録
        android_crud.createAndroid(db, android, login_user)
        return HTTPException(status_code=200)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Android詳細取得API
@router.get("/android/{android_id}", response_model=android_schema.detailAndroid)
def getAndroidDetail(android_id: int, login_user: dict = Depends(get_current_user), db: Session = Depends(get_db)):
    android = android_crud.getDetailAndroid(db, android_id=android_id)
    if not android:
        # id に紐づくデータが存在しなかった場合
        raise HTTPException(status_code=404, detail=f"Android_ID: {android_id} not found")
    return android

# Android更新API
@router.put("/android/{android_id}")
def updateAndroid(android_id: int, android: android_schema.updateAndroid, login_user: dict = Depends(get_current_user), db: Session = Depends(get_db)):
    androidById = android_crud.getDetailAndroid(db, android_id=android_id)
    if not androidById:
        # id に紐づくデータが存在しなかった場合
        raise HTTPException(status_code=404, detail=f"Android_ID: {android_id} not found")
    try:
        # 最終更新フラグを false に変更
        updateLastUpdateFlag(db)
        # Android情報の登録
        android_crud.updateAndroid(db, android, login_user, original=androidById)
        return HTTPException(status_code=200)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Android削除API
@router.delete("/android/{android_id}")
def deleteAndroid(android_id: int, login_user: dict = Depends(get_current_user), db: Session = Depends(get_db)):
    androidById = android_crud.getDetailAndroid(db, android_id=android_id)
    if not androidById:
        # id に紐づくデータが存在しなかった場合
        raise HTTPException(status_code=404, detail=f"Android_ID: {android_id} not found")
    try:
        android_crud.deleteAndroid(db, original=androidById)
        return HTTPException(status_code=200)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))