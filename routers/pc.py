from fastapi import APIRouter, Depends,  HTTPException, status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session, joinedload
from database import get_db

import cruds.t_pc as pc_crud
import schemas.t_pc as pc_schema
import models.t_pc as pc_model

router = APIRouter()


@router.get("/pc")
def getPc(db: Session = Depends(get_db)):
    try:
        pc_list = pc_crud.get_pc(db)
        results = [
            {
                "id": pc.id,
                "label_name": pc.label_name,
                "pc_name": pc.pc_name,
                "pc_user": pc.pc_user,
                "manufacturer": pc.manufacturer,
                "type": pc.type,
            }
            for pc in pc_list
        ]
        return JSONResponse(content=results)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/pc")
def createPc(pc: pc_schema.createPc, db: Session = Depends(get_db)):
    try:
        db_pc = pc_model.T_pc(**pc.dict())
        db.add(db_pc)
        db.commit()
        db.refresh(db_pc)
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