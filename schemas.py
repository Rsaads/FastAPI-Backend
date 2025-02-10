from typing import Optional
from pydantic import BaseModel, ConfigDict
from datetime import datetime
from uuid import UUID




# =========================================================
# Schemas para a tabela "clients"
# =========================================================

class ClientBase(BaseModel):
    active: bool = True
    address: Optional[str] = None 
    city: str
    email: str
    name: str
    phone: str
    postal_code: str
    state: str

class ClientCreate(ClientBase):
    pass

class Client(ClientBase):
    id: UUID
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

# =========================================================
# Schemas para a tabela "plans"
# =========================================================

class PlanBase(BaseModel):
    name: str
    description: str
    price: float
    active: bool = True

class PlanCreate(PlanBase):
    pass

class Plan(PlanBase):
    id: UUID
    created_at: datetime

    class Config:
        orm_mode = True

# =========================================================
# Schemas para a tabela "client_discounts"
# =========================================================

class ClientDiscountBase(BaseModel):
    client_id: UUID
    discount_percentage: float
    active: bool = True

class ClientDiscountCreate(ClientDiscountBase):
    pass

class ClientDiscount(ClientDiscountBase):
    id: UUID
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

# =========================================================
# Schemas para a tabela "client_plans"
# =========================================================

class ClientPlansBase(BaseModel):
    client_id: UUID
    active: bool = True
    plan_id: UUID

class CliensPlansCreate():
    pass

class ClientDiscount(ClientDiscountBase):
    id: UUID
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

# =========================================================
# Schemas para a tabela "telegramGroups"
# =========================================================

class TelegramGroupsBase(BaseModel):
    client_id: UUID
    active: bool = True
    chat_id: UUID
    group_name: str
    bot_token: str

class TelegramGroupsCreate():
    pass

class TelegramGroups(ClientDiscountBase):
    id: UUID
    created_at: datetime

# =========================================================
# Schemas para a tabela "telegramTopics"
# =========================================================

class TelegramTopicsBase(BaseModel):

    id_telegram_group: UUID

    client_plan_id: UUID

    active: bool = True

    topic_name: str

    id_thread: UUID

class TelegramTopics:

    id: UUID
    created_at: datetime
    

