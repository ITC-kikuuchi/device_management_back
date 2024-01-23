from fastapi import APIRouter, Depends,  HTTPException, status
from typing import Annotated
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from database import get_db

import cruds.auth as auth_crud
import models.m_user as M_user

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)], db: Session = Depends(get_db)):
    user = auth_crud.getUserByName(db, user_name=token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user

# ログインAPI
@router.post("/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = auth_crud.getUser(db, user=form_data.username, password=form_data.password)
    if not user:
        raise HTTPException(status_code=401, detail=f'メールアドレスまたはパスワードが違います。')
    return {"access_token": user.user_name, "token_type": "bearer"}

# 　ログイン情報取得API
@router.get("/me")
async def me(current_user: M_user = Depends(get_current_user)):
    return current_user

@router.post("/logout")
async def logout():
    pass