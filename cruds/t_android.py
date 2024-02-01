from sqlalchemy.orm import Session

import models.t_android as android_model

# Android一覧取得
def getAndroid(db: Session):
    return db.query(android_model.T_android).all()

# 最終更新フラグが true の情報を取得
def getLastUpdatedData(db: Session):
    return db.query(android_model.T_android).filter(android_model.T_android.last_updated_flag == True).first()

# 最終更新フラグを false に更新
def updateLastUpdateFlag(db: Session, android_data):
    android_data.last_updated_flag = False
    db.commit()