from fastapi_users import schemas
from datetime import date


class UserRead(schemas.BaseUser[int]):
    pass


class UserCreate(schemas.BaseUserCreate):
    salary: float
    date_on_next_increase: date


class UserUpdate(schemas.BaseUserUpdate):
    pass
