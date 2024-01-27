from fastapi import APIRouter, Depends,  HTTPException
from sqlalchemy.orm import Session
from database import get_db
from routers.auth import get_current_user

import schemas.t_ios as ios_schema
import cruds.t_ios as ios_crud

router=APIRouter()

# iOS一覧取得API
@router.get("/ios", response_model=list[ios_schema.ios])
def getIos(login_user: dict = Depends(get_current_user), db: Session = Depends(get_db)):
    try:
        return ios_crud.getIos(db)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))