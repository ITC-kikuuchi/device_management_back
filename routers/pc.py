from fastapi import APIRouter, Depends,  HTTPException
from sqlalchemy.orm import Session
from database import get_db

import cruds.t_pc as pc_crud
import schemas.t_pc as pc_schema

router = APIRouter()

# PC一覧取得API
@router.get("/pc", response_model=list[pc_schema.pc])
def getPc(db: Session = Depends(get_db)):
    try:
        return pc_crud.getPc(db)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# PC登録API
@router.post("/pc")
def createPc(pc: pc_schema.createPc, db: Session = Depends(get_db)):
    try:
        pc_crud.createPc(db, pc)
        return HTTPException(status_code=200)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# PC詳細取得API
@router.get("/pc/{pc_id}", response_model=pc_schema.detailPc)
def getPcDetail(pc_id: int, db: Session = Depends(get_db)):
    pc = pc_crud.getDetailPc(db, pc_id=pc_id)
    if not pc:
        # id に紐づくデータが存在しなかった場合
        raise HTTPException(status_code=404, detail=f"PC_ID: {pc_id} not found")
    return pc

# PC更新API
@router.put("/pc/{pc_id}")
def updatePc(pc_id: int, pc: pc_schema.updatePc, db: Session = Depends(get_db)):
    pcById = pc_crud.getDetailPc(db, pc_id=pc_id)
    if not pcById:
        # id に紐づくデータが存在しなかった場合
        raise HTTPException(status_code=404, detail=f"PC_ID: {pc_id} not found")
    try:
        pc_crud.updatePc(db, pc, original=pcById)
        return HTTPException(status_code=200)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# PC削除API
@router.delete("/pc/{pc_id}")
def deletePc(pc_id: int, db: Session = Depends(get_db)):
    pcById = pc_crud.getDetailPc(db, pc_id=pc_id)
    if not pcById:
        # id に紐づくデータが存在しなかった場合
        raise HTTPException(status_code=404, detail=f"PC_ID: {pc_id} not found")
    try:
        pc_crud.deletePc(db, original=pcById)
        return HTTPException(status_code=200)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))