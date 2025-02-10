from sqlalchemy import Column, String, Text, Float, Boolean, DateTime, ForeignKey, Integer
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from datetime import datetime
import uuid
from config import Base

class TelegramTopicsDB(Base):
    __tablename__ = "telegram_topics"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    id_telegram_group = Column(UUID(as_uuid=True), ForeignKey("telegram_group.id"), nullable=False)

    client_plan_id = Column(UUID(as_uuid=True), ForeignKey("client_plan.id"), nullable=False)

    id_thread = Column(Integer)

    active = Column(Boolean, default=True)

    created_at = Column(DateTime, default=datetime.timezone.utc)

    topic_name = Column(String)
    
