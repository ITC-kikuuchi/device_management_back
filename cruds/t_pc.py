from sqlalchemy.orm import Session

import models.t_pc as pc_model
import schemas.t_pc as pc_schema

# PC一覧取得
def getPc(db: Session):
    return db.query(pc_model.T_pc).all()

# PC登録
def createPc(db: Session, pc: pc_schema.createPc, current_user):
    db_pc = pc_model.T_pc(**pc.dict(), create_id=current_user.id, update_id=current_user.id)
    db.add(db_pc)
    db.commit()
    db.refresh(db_pc)

# PC詳細取得
def getDetailPc(db: Session, pc_id: int):
    return db.query(pc_model.T_pc).filter(pc_model.T_pc.id == pc_id).first()

# PC更新
def updatePc(db: Session, pc: pc_schema.updatePc, current_user, original: pc_model.T_pc):
    for field, value in pc.dict().items():
        setattr(original, field, value)

    original.update_id = current_user.id
    db.commit()

# PC削除
def deletePc(db: Session, original: pc_model.T_pc) -> None:
    db.delete(original)
    db.commit()

# 最終更新フラグが true の情報を取得
def getLastUpdatedData(db: Session):
    return db.query(pc_model.T_pc).filter(pc_model.T_pc.last_updated_flag == True).first()

# 最終更新フラグを false に更新
def updateLastUpdateFlag(db: Session, pc_data):
    pc_data.last_updated_flag = False
    db.commit()