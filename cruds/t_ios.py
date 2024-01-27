from sqlalchemy.orm import Session

import models.t_ios as ios_model

# iOS一覧取得
def getIos(db: Session):
    return db.query(ios_model.T_ios).all()