import logging

from sqlalchemy.orm import selectinload
from sqlalchemy.future import select
from fastapi import HTTPException, status
from app.auth.jwt import get_password_hash
from sqlalchemy.ext.asyncio import AsyncSession
from app.crud.exercise_crud import get_exercise_by_title
from app.logs.logs import log_decorator, configure_logging
from app.models.associations import UserExercise
from app.models.exercise_model import Exercise
from app.models.user_model import User
from app.schemas.user_schema import UserPasswordSchema

configure_logging()


@log_decorator
async def check_user_by_username(session: AsyncSession, username: str) -> User:
    user = await session.execute(select(User).where(User.username == username))
    user = user.scalar()
    if user:
        logging.info("Пользователь %s найден", username)
    else:
        logging.info("Пользователь %s не найден", username)
    return user


@log_decorator
async def check_user_by_id(session: AsyncSession, id: int) -> User:
    user = await session.execute(select(User).where(User.id == id))
    user = user.scalar()
    if user:
        logging.info("Пользователь с id %d найден", id)
    else:
        logging.info("Пользователь с id %d не найден", id)
    return user


@log_decorator
async def create_new_user(session: AsyncSession, user: UserPasswordSchema) -> User:
    is_user_exist = await check_user_by_username(session, user.username)
    if is_user_exist is None:
        new_user = User(
            username=user.username,
            hashed_password=get_password_hash(user.hashed_password),
        )
        session.add(new_user)
        await session.commit()
        logging.info("Создан новый пользователь с именем %s", user.username)
        return new_user
    else:
        logging.warning(
            "Попытка создания пользователя с уже существующим именем %s",
            user.username,
        )
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="username already registered",
        )


@log_decorator
async def add_exercise_to_user(session: AsyncSession, user: User, exercise):
    try:
        exercise_by_title = await get_exercise_by_title(session, exercise.exercise.name)
        user_exercise = UserExercise(
            user_id=user.id,
            exercise_id=exercise_by_title.id,
            exercise=exercise_by_title,
            user=user,
        )
        for key, value in exercise.exercise.dict().items():
            setattr(user_exercise, key, value)

        session.add(user_exercise)
        await session.commit()

        logging.info(
            "Упражнение %s добавлено пользователю %s",
            exercise.exercise.name,
            user.username,
        )

        user = (
            (
                await session.execute(
                    select(User)
                    .options(selectinload(User.user_exercises))
                    .where(User.id == user.id)
                )
            )
            .scalars()
            .first()
        )
        return user
    except Exception as e:
        logging.exception(
            "Ошибка при добавлении упражнения %s пользователю %s: %s",
            exercise.exercise.name,
            user.username,
            e,
        )
        raise


@log_decorator
async def remove_exercise_from_user(session: AsyncSession, user: User, exercise):
    try:
        user_exercise = await session.execute(
            select(UserExercise)
            .where(UserExercise.user_id == user.id)
            .where(UserExercise.exercise_id == exercise.id)
        )
        user_exercise = user_exercise.scalar_one_or_none()

        if user_exercise:
            await session.delete(user_exercise)
            await session.commit()
            logging.info(
                "Упражнение %s удалено у пользователя %s", exercise.name, user.username
            )
        else:
            logging.warning(
                "Упражнение %s не найдено для пользователя %s",
                exercise.name,
                user.username,
            )
        return user
    except Exception as e:
        logging.exception(
            "Ошибка при удалении упражнения %s у пользователя %s: %s",
            exercise.name,
            user.username,
            e,
        )
        raise
