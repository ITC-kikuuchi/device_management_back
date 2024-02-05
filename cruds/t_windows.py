from sqlalchemy.orm import Session

import models.t_windows as windows_model

# Windows(スマホ)一覧取得
def getWindows(db: Session):
    return db.query(windows_model.T_windows).all()