import uvicorn
from fastapi import FastAPI
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from fastapi_users import FastAPIUsers
from redis import asyncio as aioredis

from src.auth.auth import auth_backend
from src.auth.manager import get_user_manager
from src.auth.models import User
from src.auth.router import router as user_router
from src.auth.schemas import UserCreate, UserRead
from src.operations.router import operation_router

app = FastAPI()

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix='/auth/jwt',
    tags=['auth'],
)


app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix='/auth',
    tags=['auth'],
)

app.include_router(user_router)

app.include_router(operation_router)


@app.on_event('startup')
async def startup():
    redis = aioredis.from_url('redis://localhost')
    FastAPICache.init(RedisBackend(redis), prefix='fastapi-cache')

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
