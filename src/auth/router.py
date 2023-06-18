from fastapi import APIRouter, Depends
from fastapi_users import FastAPIUsers

from auth.models import User
from auth.auth import auth_backend
from auth.manager import get_user_manager

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)
current_user = fastapi_users.current_user()

router = APIRouter(
    prefix="/user",
    tags=["User"]
)


@router.get("/salary")
async def get_salary_info(user: User = Depends(current_user)) -> dict:
    return {'salary': user.salary,
            'date_on_next_increase': user.date_on_next_increase}
