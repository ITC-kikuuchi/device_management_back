from sqlalchemy.orm import Session

import schemas.t_android as android_schema
import models.t_android as android_model

# Android一覧取得
def getAndroid(db: Session):
    return db.query(android_model.T_android).all()

# Android登録処理
def createAndroid(db: Session, android: android_schema.createAndroid, current_user):
    db_android = android_model.T_android(**android.dict(), create_id=current_user.id, update_id=current_user.id)
    db.add(db_android)
    db.commit()
    db.refresh(db_android)

# Android詳細取得
def getDetailAndroid(db: Session, android_id: int):
    return db.query(android_model.T_android).filter(android_model.T_android.id == android_id).first()

# Android更新
def updateAndroid(db: Session, android: android_schema.updateAndroid, current_user, original: android_model.T_android):
    for field, value in android.dict().items():
        setattr(original, field, value)

    original.update_id = current_user.id
    db.commit()

# 最終更新フラグが true の情報を取得
def getLastUpdatedData(db: Session):
    return db.query(android_model.T_android).filter(android_model.T_android.last_updated_flag == True).first()

# 最終更新フラグを false に更新
def updateLastUpdateFlag(db: Session, android_data):
    android_data.last_updated_flag = False
    db.commit()