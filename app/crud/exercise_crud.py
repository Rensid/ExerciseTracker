from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.models.exercise_model import Exercise
from app.models.user_model import User
from app.schemas.exercise_schema import ExerciseSchema, ExerciseBase


async def get_exercise_by_title(session: AsyncSession, name: str) -> Exercise:
    print(f"exer {name} name")
    exercise = await session.execute(select(Exercise).where(Exercise.name == name))
    return exercise.scalar()


async def add_exercise(session: AsyncSession, exercise: ExerciseBase):
    is_exercise_exist = await get_exercise_by_title(session, exercise.name)
    if is_exercise_exist:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail="Category already exists")
    else:
        new_exercise = Exercise(
            name=exercise.name, description=exercise.description, category_title=exercise.category_title)
        session.add(new_exercise)
        await session.commit()
        return new_exercise


async def upgrade_exercise(session: AsyncSession, exercise: ExerciseSchema, title: str) -> Exercise:
    updated_exercise = await get_exercise_by_title(session, title)
    if exercise:
        exercise_data = exercise.dict()
        print(type(exercise_data))
        for key, value in exercise_data.items():
            setattr(updated_exercise, key, value)
        session.add(updated_exercise)
        await session.commit()
        return updated_exercise


async def delete_exercise(session: AsyncSession, title: str):
    exercise = await get_exercise_by_title(session, title)
    if exercise:
        session.delete(exercise)
        await session.commit()
        return True
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Exercise not found")


async def get_exercise_for_user(session: AsyncSession, user: User):
    exercises = await session.execute(select(Exercise).where(Exercise.user_id == user.id))
    return exercises.scalars()
