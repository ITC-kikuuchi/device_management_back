from sqlalchemy.orm import Session

import schemas.t_ios as ios_schema
import models.t_ios as ios_model

# iOS一覧取得
def getIos(db: Session):
    return db.query(ios_model.T_ios).all()

# iOS登録
def createIos(db:Session, ios: ios_schema.createIos):
    db_ios = ios_model.T_ios(**ios.dict())
    db.add(db_ios)
    db.commit()
    db.refresh(db_ios)

# iOS詳細取得
def getDetailIos(db:Session, ios_id:int):
    return db.query(ios_model.T_ios).filter(ios_model.T_ios.id == ios_id).first()

# iOS更新
def updateIos(db: Session, ios: ios_schema.updateIos, original: ios_model.T_ios):
    for field, value in ios.dict().items():
        setattr(original, field, value)
    db.commit()

# PC削除
def deleteIos(db: Session, original: ios_model.T_ios):
    db.delete(original)
    db.commit()