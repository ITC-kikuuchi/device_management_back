from sqlalchemy.orm import Session

import models.t_android as android_model

# Android一覧取得
def getAndroid(db: Session):
    return db.query(android_model.T_android).all()