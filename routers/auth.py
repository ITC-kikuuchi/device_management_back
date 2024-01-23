from fastapi import APIRouter, Depends,  HTTPException, status
from typing import Annotated
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from database import get_db

import cruds.auth as auth_crud
import models.m_user as M_user

router = APIRouter()


@router.post("/login")
async def login():
    pass


@router.post("/logout")
async def logout():
    pass
