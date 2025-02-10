from datetime import datetime
from uuid import UUID, uuid4
from typing import Optional
from sqlalchemy import Column, String, Boolean, DateTime


from config import Base

# Definição do modelo SQLAlchemy
class ClientDB(Base):
    __tablename__ = "clients"

    id = Column(String, primary_key=True, default=lambda: str(uuid4()))
    active = Column(Boolean, default=True)
    address = Column(String) 
    city = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    email = Column(String, unique=True, index=True)
    name = Column(String)
    phone = Column(String)
    postal_code = Column(String)
    state = Column(String)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)



