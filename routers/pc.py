from fastapi import APIRouter, Depends,  HTTPException, status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from database import get_db

import cruds.t_pc as pc_crud

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
def createPc():
    pass


@router.get("/pc/{pc_id}")
def getPcDetail():
    pass


@router.put("/pc/{pc_id}")
def updatePc():
    pass


@router.delete("/pc/{pc_id}")
def deletePc():
    pass