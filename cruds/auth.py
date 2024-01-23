from sqlalchemy.orm import Session

import models.m_user as user_model

# ユーザ取得
def getUser(db: Session, user: str, password: str):
    return db.query(user_model.M_user).filter(
        user_model.M_user.user_name == user,
        user_model.M_user.password == password
        ).first()

# トークンに紐づくユーザ取得
def getUserByName(db: Session, user_name: str):
    return db.query(user_model.M_user).filter(
        user_model.M_user.user_name == user_name
        ).first()

