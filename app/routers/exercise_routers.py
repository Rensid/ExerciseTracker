from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.auth.auth import get_current_user
from app.crud.exercise_crud import get_exercise_by_title, add_exercise, get_exercise_for_user, upgrade_exercise, delete_exercise
from app.models.user_model import User
from app.schemas.exercise_schema import ExerciseBase, ExerciseSchema
from app.base.base import get_async_session

exercise_router = APIRouter()


@exercise_router.post('/exercise/')
async def create_exercise_endpoint(exercise_data: ExerciseBase, session: Session = Depends(get_async_session)):
    exercise = await add_exercise(session, exercise_data)
    return exercise


@exercise_router.put('/exercise/{title}')
async def upgrade_exercise_endpoint(exercise_data: ExerciseSchema, title: str,  session: Session = Depends(get_async_session)):
    exercise = await upgrade_exercise(session, exercise_data, title)
    return exercise


@exercise_router.delete('/exercise/{title}')
async def delete_exercise_endpoint(title: str, session: Session = Depends(get_async_session)):
    exercise_router.delete(session, title)
    if exercise_router:
        return True
    else:
        return False


@exercise_router.get('/exercise/')
async def get_all_exercise_of_user(session: Session = Depends(get_async_session), user: User = Depends(get_current_user)):
    return get_exercise_for_user(session, user)
