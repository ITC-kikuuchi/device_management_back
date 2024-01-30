from fastapi import APIRouter, Depends,  HTTPException
from sqlalchemy.orm import Session
from database import get_db
from routers.auth import get_current_user

import schemas.t_ios as ios_schema
import cruds.t_ios as ios_crud

router=APIRouter()

# 最終更新フラグを false に変更
def updateLastUpdateFlag(db: Session):
    # 最終更新データの取得
    ios_data = ios_crud.getLastUpdatedData(db)
    if ios_data:
        # 最終更新データが存在した場合
        # 最終更新データの最終更新フラグの更新
        ios_crud.updateLastUpdateFlag(db, ios_data)

# iOS一覧取得API
@router.get("/ios", response_model=list[ios_schema.ios])
def getIos(login_user: dict = Depends(get_current_user), db: Session = Depends(get_db)):
    try:
        return ios_crud.getIos(db)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# iOS登録API
@router.post("/ios")
def createIos(ios: ios_schema.createIos, login_user: dict = Depends(get_current_user), db: Session = Depends(get_db)):
    try:
        ios_crud.createIos(db, ios)
        # 最終更新フラグを false に変更
        updateLastUpdateFlag(db)
        return HTTPException(status_code=200)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# iOS詳細取得API
@router.get("/ios/{ios_id}", response_model=ios_schema.detailIos)
def createIos(ios_id: int, login_user: dict = Depends(get_current_user), db: Session = Depends(get_db)):
    ios = ios_crud.getDetailIos(db, ios_id=ios_id)
    if not ios:
        # id に紐づくデータが存在しなかった場合
        raise HTTPException(status_code=404, detail=f"IOS_ID: {ios_id} not found")
    return ios

# iOS更新API
@router.put("/ios/{ios_id}")
def updateIos(ios_id: int, ios: ios_schema.updateIos, login_user: dict = Depends(get_current_user), db: Session = Depends(get_db)):
    iosById = ios_crud.getDetailIos(db, ios_id=ios_id)
    if not iosById:
        # id に紐づくデータが存在しなかった場合
        raise HTTPException(status_code=404, detail=f"IOS_ID: {ios_id} not found")
    try:
        ios_crud.updateIos(db, ios, original=iosById)
        return HTTPException(status_code=200)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# iOS削除API
@router.delete("/ios/{ios_id}")
def deleteIos(ios_id: int, login_user: dict = Depends(get_current_user), db: Session = Depends(get_db)):
    iosById = ios_crud.getDetailIos(db, ios_id=ios_id)
    if not iosById:
        # id に紐づくデータが存在しなかった場合
        raise HTTPException(status_code=404, detail=f"IOS_ID: {ios_id} not found")
    try:
        ios_crud.deleteIos(db, original=iosById)
        return HTTPException(status_code=200)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))