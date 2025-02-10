from uuid import UUID
from sqlalchemy.orm import Session
from models.clients import PlansDB
from schemas import PlansCreate

class planService:
    
    def __init__(self, db: Session):
        self.db = db
    