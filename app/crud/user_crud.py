from fastapi import HTTPException, status
from app.auth.jwt import get_password_hash
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.models.user_model import User
from app.schemas.user_schema import UserPasswordSchema


async def check_user_by_username(session: AsyncSession, username: str) -> User:
    user = await session.execute(select(User).where(User.username == username))

    return user.scalar()


async def check_user_by_id(session: AsyncSession, id: int) -> User:
    user = await session.execute(select(User).where(User.id == id))
    return user.scalar()


async def create_new_user(session: AsyncSession, user: UserPasswordSchema) -> User:
    is_user_exist = await check_user_by_username(session, user.username)
    if is_user_exist is None:
        new_user = User(username=user.username,
                        hashed_password=get_password_hash(user.hashed_password))
        session.add(new_user)
        await session.commit()
        return new_user
    else:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="username already registered"
        )
