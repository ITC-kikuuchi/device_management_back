from sqlalchemy import Column
from sqlalchemy import Integer, String, Text, Date, Boolean
from sqlalchemy.dialects.mysql import TIMESTAMP as Timestamp

from database import Base

class T_ios(Base):
    __tablename__ = "t_ios"

    id = Column(Integer, primary_key=True, nullable=False)
    label_name = Column(String(255), nullable=False)
    ios_name = Column(String(255))
    manufacturer = Column(String(255))
    type = Column(String(255))
    os = Column(String(255))
    carrier = Column(String(255))
    condition = Column(String(255))
    delivery_date = Column(Date)
    disposal_date = Column(Date)
    remarks = Column(Text)
    delete_flag = Column(Boolean, default=0, nullable=False)
    last_updated_flag = Column(Boolean, default=0, nullable=False)
    create_id = Column(Integer)
    update_id = Column(Integer)
    created_at = Column(Timestamp)
    updated_at = Column(Timestamp)