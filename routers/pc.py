from fastapi import APIRouter, Depends,  HTTPException
from sqlalchemy.orm import Session
from database import get_db
from routers.auth import get_current_user

import cruds.t_pc as pc_crud
import schemas.t_pc as pc_schema

router = APIRouter()

# 最終更新フラグを false に変更
def updateLastUpdateFlag(db: Session):
    # 最終更新データの取得
    pc_data = pc_crud.getLastUpdatedData(db)
    if pc_data:
        # 最終更新データが存在した場合
        # 最終更新データの 最終更新フラグの更新
        pc_crud.updateLastUpdateFlag(db, pc_data)

# PC一覧取得API
@router.get("/pc", response_model=list[pc_schema.pc])
def getPc(login_user: dict = Depends(get_current_user), db: Session = Depends(get_db)):
    try:
        return pc_crud.getPc(db)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# PC登録API
@router.post("/pc")
def createPc(pc: pc_schema.createPc, login_user: dict = Depends(get_current_user), db: Session = Depends(get_db)):
    try:
        # 最終更新フラグを false に変更
        updateLastUpdateFlag(db)
        # PC情報の登録
        pc_crud.createPc(db, pc, login_user)
        return HTTPException(status_code=200)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# PC詳細取得API
@router.get("/pc/{pc_id}", response_model=pc_schema.detailPc)
def getPcDetail(pc_id: int, login_user: dict = Depends(get_current_user), db: Session = Depends(get_db)):
    pc = pc_crud.getDetailPc(db, pc_id=pc_id)
    if not pc:
        # id に紐づくデータが存在しなかった場合
        raise HTTPException(status_code=404, detail=f"PC_ID: {pc_id} not found")
    return pc

# PC更新API
@router.put("/pc/{pc_id}")
def updatePc(pc_id: int, pc: pc_schema.updatePc, login_user: dict = Depends(get_current_user), db: Session = Depends(get_db)):
    pcById = pc_crud.getDetailPc(db, pc_id=pc_id)
    if not pcById:
        # id に紐づくデータが存在しなかった場合
        raise HTTPException(status_code=404, detail=f"PC_ID: {pc_id} not found")
    try:
        # 最終更新フラグを false に変更
        updateLastUpdateFlag(db)
        pc_crud.updatePc(db, pc, login_user, original=pcById)
        return HTTPException(status_code=200)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# PC削除API
@router.delete("/pc/{pc_id}")
def deletePc(pc_id: int, login_user: dict = Depends(get_current_user), db: Session = Depends(get_db)):
    pcById = pc_crud.getDetailPc(db, pc_id=pc_id)
    if not pcById:
        # id に紐づくデータが存在しなかった場合
        raise HTTPException(status_code=404, detail=f"PC_ID: {pc_id} not found")
    try:
        pc_crud.deletePc(db, original=pcById)
        return HTTPException(status_code=200)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))