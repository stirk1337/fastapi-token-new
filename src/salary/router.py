from fastapi import APIRouter, Depends
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

from db import get_async_session
from salary.models import Salary
from salary.schemas import SalaryCreate

router = APIRouter(
    prefix="/salary",
    tags=["Salary"]
)


@router.get("/")
async def get_specific_operations(operation_type: str, session: AsyncSession = Depends(get_async_session)):
    query = select(Salary).where(Salary.c.type == operation_type)
    result = await session.execute(query)
    return result.all()


@router.post("/")
async def add_specific_operations(new_operation: SalaryCreate, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(Salary).values(**new_operation.dict())
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}