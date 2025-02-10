from sqlalchemy import Column, String, Text, Float, Boolean, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from datetime import datetime
import uuid
from config import Base

class PlanDB(Base):
    __tablename__ = "plans"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    name = Column(String, nullable=False)

    description = Column(Text)

    price = Column(Float, nullable=False)

    active = Column(Boolean, default=True)
    
    created_at = Column(DateTime, default=datetime.timezone.utc)