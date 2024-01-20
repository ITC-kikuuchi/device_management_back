from sqlalchemy import select
from sqlalchemy.orm import Session

import models.t_pc as pc_model

# PC一覧取得
def getPc(db: Session):
    return db.query(pc_model.T_pc).all()

# PC登録
def createPc(db: Session, pc: pc_schema.createPc):
    db_pc = pc_model.T_pc(**pc.dict())
    db.add(db_pc)
    db.commit()
    db.refresh(db_pc)

# PC詳細取得
def getDetailPc(db: Session, pc_id: int):
    return db.query(pc_model.T_pc).filter(pc_model.T_pc.id == pc_id).first()