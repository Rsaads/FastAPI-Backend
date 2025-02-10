from fastapi import APIRouter

from controllers import clientsController as clients

router = APIRouter()

router.include_router(clients.router, prefix='/clients')
router.include_router(clients.router, prefix='/plans')
