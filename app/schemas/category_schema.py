from pydantic import BaseModel
from app.schemas.exercise_schema import ExerciseBase


class Category(BaseModel):
    id: int
    title: str
    exercises: list[ExerciseBase]
