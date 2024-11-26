

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.crud.user_crud import check_user_by_username
from app.schemas.user_schema import UserBase
from app.base.test_base import get_test_async_session


async def get_username(session: AsyncSession = Depends(get_test_async_session),
                       request: UserBase = Depends()):
    user = await check_user_by_username(session, request.username)
    return user
