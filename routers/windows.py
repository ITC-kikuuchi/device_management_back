from fastapi import APIRouter, Depends,  HTTPException
from sqlalchemy.orm import Session
from database import get_db
from routers.auth import get_current_user

import schemas.t_windows as windows_schema
import cruds.t_windows as windows_crud

router=APIRouter()

# 最終更新フラグを false に変更
def updateLastUpdateFlag(db: Session):
    # 最終更新データの取得
    windows_data = windows_crud.getLastUpdatedData(db)
    if windows_data:
        # 最終更新データが存在した場合
        # 最終更新データの最終更新フラグの更新
        windows_crud.updateLastUpdateFlag(db, windows_data)

# Windows(スマホ)一覧取得API
@router.get("/windows", response_model=list[windows_schema.windows])
def getWindows(login_user: dict = Depends(get_current_user), db: Session = Depends(get_db)):
    try:
        return windows_crud.getWindows(db)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Windows(スマホ)登録API
@router.post("/windows")
def createWindows(windows: windows_schema.createWindows, login_user: dict = Depends(get_current_user), db: Session = Depends(get_db)):
    try:
        # 最終更新フラグを false に変更
        updateLastUpdateFlag(db)
        # Windows情報の登録
        windows_crud.createWindows(db, windows, login_user)
        return HTTPException(status_code=200)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Windows(スマホ)詳細取得API
@router.get("/windows/{windows_id}", response_model=windows_schema.detailWindows)
def getWindowsDetail(windows_id: int, login_user: dict = Depends(get_current_user), db: Session = Depends(get_db)):
    windows = windows_crud.getDetailWindows(db, windows_id)
    if not windows:
        # id に紐づくデータが存在しなかった場合
        raise HTTPException(status_code=404, detail=f"Windows_ID: {windows_id} not found")
    return windows

# Windows(スマホ)更新API
@router.put("/windows/{windows_id}")
def updateWindows(windows_id: int, windows: windows_schema.updateWindows, login_user: dict = Depends(get_current_user), db: Session = Depends(get_db)):
    windowsById = windows_crud.getDetailWindows(db, windows_id)
    if not windowsById:
        # id に紐づくデータが存在しなかった場合
        raise HTTPException(status_code=404, detail=f"Windows_ID: {windows_id} not found")
    try:
        # 最終更新フラグを false に変更
        updateLastUpdateFlag(db)
        # Windows 情報の更新
        windows_crud.updateWindows(db, windows, login_user, original=windowsById)
        return HTTPException(status_code=200)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Windows(スマホ)削除API
@router.delete("/windows/{windows_id}")
def deleteWindows():
    pass