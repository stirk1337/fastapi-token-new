from datetime import date

from fastapi import APIRouter, Depends
from fastapi_users import FastAPIUsers
from pydantic import BaseModel

from src.auth.auth import auth_backend
from src.auth.manager import get_user_manager
from src.auth.models import User

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)
current_user = fastapi_users.current_user()

router = APIRouter(
    prefix='/user',
    tags=['User']
)


class SalaryInfo(BaseModel):
    salary: float
    date_on_next_increase: date


@router.get('/salary', responses={
    401: {
            'detail': 'Unauthorized',
            }
})
async def get_salary_info(user: User = Depends(current_user)) -> SalaryInfo:
    return {'salary': user.salary,
            'date_on_next_increase': user.date_on_next_increase}
