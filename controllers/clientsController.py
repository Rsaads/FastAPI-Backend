from fastapi import APIRouter, Depends, HTTPException
from uuid import UUID
from sqlalchemy.orm import Session
from services.clientService import ClientService
from schemas import Client, ClientCreate
from config import get_db

router = APIRouter()

@router.post("/", response_model=Client)
def create_client(client: ClientCreate, db: Session = Depends(get_db)):
    service = ClientService(db)
    try:
        db_client = service.create_client(client)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    return db_client

@router.get("/{client_id}", response_model=Client)
def read_client(client_id: UUID, db: Session = Depends(get_db)):
    service = ClientService(db)
    db_client = service.get_client(client_id)
    if db_client is None:
        raise HTTPException(status_code=404, detail="Client not found")
    return db_client

@router.put("/{client_id}", response_model=Client)
def update_client(client_id: UUID, client: ClientCreate, db: Session = Depends(get_db)):
    service = ClientService(db)
    db_client = service.update_client(client_id, client)
    if db_client is None:
        raise HTTPException(status_code=404, detail="Client not found")
    return db_client

@router.delete("/{client_id}", response_model=Client)
def delete_client(client_id: UUID, db: Session = Depends(get_db)):
    service = ClientService(db)
    db_client = service.delete_client(client_id)
    if db_client is None:
        raise HTTPException(status_code=404, detail="Client not found")
    return db_client