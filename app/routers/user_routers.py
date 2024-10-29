from fastapi import APIRouter, Body, Depends, Form
from sqlalchemy.ext.asyncio import AsyncSession
from app.auth.auth import get_current_user
from app.base.base import get_async_session
from app.crud.user_crud import add_exercise_to_user
from app.models.user_model import User
from app.schemas.user_schema import UserWithExercises, UserExercise

user_router = APIRouter()


@user_router.post("/users/add_exercise")
async def add_exercise(exercise: UserExercise,
                       session: AsyncSession = Depends(get_async_session),
                       user: User = Depends(get_current_user)):
    user = await add_exercise_to_user(session, user, exercise)
    return UserWithExercises.from_orm(user)
