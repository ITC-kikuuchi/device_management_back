from sqlalchemy.orm import Session

import models.t_pc as pc_model
import schemas.t_pc as pc_schema

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

# PC更新
def updatePc(db: Session, pc: pc_schema.updatePc, original: pc_model.T_pc):
    original.label_name = pc.label_name
    original.pc_name = pc.pc_name
    original.user_name = pc.user_name
    original.pc_user = pc.pc_user
    original.condition = pc.condition
    original.manufacturer = pc.manufacturer
    original.type = pc.type
    original.service_tag = pc.service_tag
    original.os = pc.os
    original.bit = pc.bit
    original.ie_version = pc.ie_version
    original.ip_address = pc.ip_address
    original.gx_wwp_license = pc.gx_wwp_license
    original.delivery_date = pc.delivery_date
    original.disposal_date = pc.disposal_date
    original.remarks = pc.remarks
    db.commit()