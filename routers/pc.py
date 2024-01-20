from fastapi import APIRouter, Depends,  HTTPException, status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session, joinedload
from database import get_db

import cruds.t_pc as pc_crud
import schemas.t_pc as pc_schema
import models.t_pc as pc_model

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
    pc = pc_crud.get_detail_pc(db, pc_id=pc_id)
    if not pc:
        # id に紐づくデータが存在しなかった場合
        raise HTTPException(status_code=404, detail=f"PC_ID: {pc_id} not found")
    return pc

@router.put("/pc/{pc_id}")
def updatePc():
    pass


@router.delete("/pc/{pc_id}")
def deletePc():
    pass