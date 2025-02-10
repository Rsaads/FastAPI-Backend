from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from datetime import datetime
from uuid import UUID, uuid4
from typing import Optional


from config import Base

# Definição do modelo SQLAlchemy
class ClientPlansDB(Base):
    __tablename__ = "clients"

    id = Column(String, primary_key=True, default=lambda: str(uuid4()))

    active = Column(Boolean, default=True)

    created_at = Column(DateTime, default=datetime.utcnow)

    client_id = Column(Integer, ForeignKey("clients.id"), nullable=False)
    
    plan_id = Column(Integer, ForeignKey("plans.id"), nullable=False)


