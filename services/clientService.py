from uuid import UUID
from sqlalchemy.orm import Session
from models.clients import ClientDB
from schemas import ClientCreate

class ClientService:
    def __init__(self, db: Session):
        self.db = db

    async def create_client(self, client: ClientCreate):
        # Lógica de negócio: Verifica se o e-mail já está cadastrado
        existing_client = self.db.query(ClientDB).filter(ClientDB.email == client.email).first()
        if existing_client:
            raise ValueError("Email already registered")

        # Cria o cliente
        db_client = ClientDB(**client.model_dump())
        await self.db.add(db_client)
        await self.db.commit()
        await self.db.refresh(db_client)
        
        return db_client

    def get_client(self, client_id: UUID):
        return self.db.query(ClientDB).filter(ClientDB.id == str(client_id)).first()

    def update_client(self, client_id: UUID, client: ClientCreate):
        db_client = self.get_client(client_id)
        if db_client is None:
            return None
        for key, value in client.model_dump().items():
            setattr(db_client, key, value)
        self.db.commit()
        self.db.refresh(db_client)
        return db_client

    def delete_client(self, client_id: UUID):
        db_client = self.get_client(client_id)
        if db_client is None:
            return None
        self.db.delete(db_client)
        self.db.commit()
        return db_client