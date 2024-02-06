from sqlalchemy.orm import Session

import models.t_windows as windows_model
import schemas.t_windows as windows_schema

# Windows(スマホ)一覧取得
def getWindows(db: Session):
    return db.query(windows_model.T_windows).all()

# Windows(スマホ)登録
def createWindows(db: Session, windows: windows_schema.createWindows, current_user):
    db_windows = windows_model.T_windows(**windows.dict(), create_id=current_user.id, update_id=current_user.id)
    db.add(db_windows)
    db.commit()
    db.refresh(db_windows)

# 最終更新フラグが true の情報を取得
def getLastUpdatedData(db: Session):
    return db.query(windows_model.T_windows).filter(windows_model.T_windows.last_updated_flag == True).first()

# 最終更新フラグを false に更新
def updateLastUpdateFlag(db: Session, windows_data):
    windows_data.last_updated_flag = False
    db.commit()