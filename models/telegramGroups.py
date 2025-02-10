from sqlalchemy import Column,String ,Integer, Text, Float, Boolean, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from datetime import datetime
import uuid
from config import Base

class TelegramGroupsDB(Base):
    __tablename__ = "telegram_topics"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    
    client_id = Column(Integer, ForeignKey("clients.id"), nullable=False)

    group_name = Column(String, nullable=False)

    chat_id = Column(Integer, nullable=False)

    thread_id = Column(UUID)

    bot_token = Column(String, default=True)

    active = Column(Boolean, default=True)

    created_at = Column(DateTime, default=datetime.utcnow)