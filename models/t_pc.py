from sqlalchemy import Column
from sqlalchemy import Integer, String, Text, Date, Boolean
from sqlalchemy.dialects.mysql import TIMESTAMP as Timestamp
from sqlalchemy.orm import relationship

from database import Base


class T_pc(Base):
    __tablename__ = "t_pc"

    id = Column(Integer, primary_key=True, nullable=False)
    label_name = Column(String(255), nullable=False)
    pc_name = Column(String(255))
    user_name = Column(String(255))
    pc_user = Column(String(255))
    condition = Column(String(255))
    manufacturer = Column(String(255))
    type = Column(String(255))
    service_tag = Column(String(255))
    os = Column(String(255))
    bit = Column(Integer)
    ie_version = Column(String(255))
    ip_address = Column(String(255))
    gx_wwp_license = Column(String(255))
    delivery_date = Column(Date)
    disposal_date = Column(Date)
    remarks = Column(Text)
    delete_flag = Column(Boolean, default=0, nullable=False)
    create_id = Column(Integer)
    update_id = Column(Integer)
    created_at = Column(Timestamp)
    updated_at = Column(Timestamp)