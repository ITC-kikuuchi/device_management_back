from sqlalchemy.orm import Session

import models.t_windows as windows_model

# Windows(スマホ)一覧取得
def getWindows(db: Session):
    return db.query(windows_model.T_windows).all()

# 最終更新フラグが true の情報を取得
def getLastUpdatedData(db: Session):
    return db.query(windows_model.T_windows).filter(windows_model.T_windows.last_updated_flag == True).first()

# 最終更新フラグを false に更新
def updateLastUpdateFlag(db: Session, windows_data):
    windows_data.last_updated_flag = False
    db.commit()