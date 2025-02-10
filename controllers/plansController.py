# controllers/plansController.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.plans import PlanDB
from schemas import Plan, PlanCreate
from config import get_db

router = APIRouter()

# Rota para criar um plano
@router.post("/plans/", response_model=Plan)
async def create_plan(plan: PlanCreate, db: AsyncSession = Depends(get_db)):
    db_plan = PlanDB(**plan.model_dump())
    db.add(db_plan)
    await db.commit()
    await db.refresh(db_plan)
    return db_plan

# Rota para listar todos os planos
@router.get("/plans/", response_model=list[Plan])
async def list_plans(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(PlanDB))
    plans = result.scalars().all()
    return plans