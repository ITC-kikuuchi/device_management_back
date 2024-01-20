from sqlalchemy import select
from sqlalchemy.orm import Session

import models.t_pc as pc_model

# PC一覧取得
def get_pc(db: Session):
    return db.query(pc_model.T_pc).all()

# PC詳細取得
def get_detail_pc(db: Session, pc_id: int):
    return db.query(pc_model.T_pc).filter(pc_model.T_pc.id == pc_id).first()