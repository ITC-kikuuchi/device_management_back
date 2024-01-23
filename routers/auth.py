from fastapi import APIRouter, Depends,  HTTPException, status
from typing import Annotated
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from database import get_db

import cruds.auth as auth_crud
import models.m_user as M_user

router = APIRouter()


# ログインAPI
@router.post("/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = auth_crud.getUser(db, user=form_data.username, password=form_data.password)
    if not user:
        raise HTTPException(status_code=401, detail=f'メールアドレスまたはパスワードが違います。')
    return {"access_token": user.user_name, "token_type": "bearer"}


@router.post("/logout")
async def logout():
    pass
