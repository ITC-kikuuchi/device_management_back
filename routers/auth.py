from fastapi import APIRouter, Depends,  HTTPException, status
from typing import Annotated
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from database import get_db
from datetime import datetime, timedelta
from jose import jwt


import cruds.auth as auth_crud
import models.m_user as M_user

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# パスワード認証を行い、トークンを生成
def create_tokens(user_id: int):
    # ペイロード作成
    access_payload = {
        'token_type': 'access_token',
        'exp': datetime.utcnow() + timedelta(minutes=60),
        'user_id': user_id,
    }
    access_token = jwt.encode(access_payload, 'SECRET_KEY123', algorithm='HS256')
    return {'access_token': access_token, 'token_type': 'bearer'}

# トークンからユーザーを取得
def get_current_user_from_token(token: str, db: Session):
    # トークンをデコードしてペイロードを取得。
    payload = jwt.decode(token, 'SECRET_KEY123', algorithms=['HS256'])

    # トークンに紐づくユーザ情報の取得
    user = auth_crud.getUserById(db, payload['user_id'])
    if not user:
        # トークンに紐づくユーザ情報が存在しない場合に Not authenticated を返却
        raise HTTPException(status_code=401, detail=f'Not authenticated')
    return user

# トークンからログイン中のユーザーを取得
def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    return get_current_user_from_token(token, db)

# ログインAPI
@router.post("/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = auth_crud.getUser(db, mail=form_data.username, password=form_data.password)
    if not user:
        raise HTTPException(status_code=401, detail=f'メールアドレスまたはパスワードが違います。')
    return create_tokens(user.id)

# 　ログイン情報取得API
@router.get("/me")
async def me(current_user: M_user = Depends(get_current_user)):
    return current_user

@router.post("/logout")
async def logout():
    pass