from sqlalchemy.orm import selectinload
from sqlalchemy.future import select
from fastapi import HTTPException, status
from app.auth.jwt import get_password_hash
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.crud.exercise_crud import get_exercise_by_title
from app.models.associations import UserExercise
from app.models.exercise_model import Exercise
from app.models.user_model import User
from app.schemas.user_schema import UserPasswordSchema, UserWithExercises


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


async def add_exercise_to_user(session: AsyncSession, user: User, exercise):
    exercise_by_title = await get_exercise_by_title(session, exercise.exercise.name)
    user_exercise = UserExercise(user_id=user.id, exercise_id=exercise_by_title.id,
                                 exercise=exercise_by_title, user=user)

    for key, value in exercise.exercise.dict().items():
        setattr(user_exercise, key, value)

    session.add(user_exercise)
    await session.commit()

    # Перезагружаем пользователя с подгруженными user_exercises
    user = (await session.execute(
        select(User).options(selectinload(
            User.user_exercises)).where(User.id == user.id)
    )).scalars().first()
    print(UserWithExercises.from_orm(user))
    return user
