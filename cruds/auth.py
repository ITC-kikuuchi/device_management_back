from sqlalchemy.orm import Session

import models.m_user as user_model


# ユーザ取得
def getUser(db: Session, mail: str, password: str):
    return (
        db.query(user_model.M_user)
        .filter(
            user_model.M_user.mail_address == mail,
            user_model.M_user.password == password,
        )
        .first()
    )


# トークンに紐づくユーザ取得
def getUserById(db: Session, id: int):
    return db.query(user_model.M_user).filter(user_model.M_user.id == id).first()
