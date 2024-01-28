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