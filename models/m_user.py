from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.mysql import TIMESTAMP as Timestamp
from sqlalchemy.orm import relationship

from database import Base


class M_user(Base):
    __tablename__ = "m_user"

    id = Column(Integer, primary_key=True, nullable=False)
    mail_address = Column(String(255), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    user_name = Column(String(255), nullable=False)
    create_id = Column(Integer)
    update_id = Column(Integer)
    created_at = Column(Timestamp)
    updated_at = Column(Timestamp)
