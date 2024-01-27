from fastapi import APIRouter, Depends,  HTTPException
from sqlalchemy.orm import Session
from database import get_db
from routers.auth import get_current_user

import schemas.t_ios as ios_schema
import cruds.t_ios as ios_crud

router=APIRouter()
