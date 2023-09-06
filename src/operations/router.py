import time

from fastapi import APIRouter
from fastapi_cache.decorator import cache

operation_router = APIRouter(
    prefix='/operations',
    tags=['Operation']
)


@operation_router.get('/long_operation')
@cache(expire=30)
def get_long_op():
    time.sleep(2)
    return 'Много много данных, которые вычислялись сто лет'
