from pydantic import BaseModel
from app.schemas.exercise_schema import ExerciseBase


class CategoryBase(BaseModel):
    title: str


class CategorySchema(CategoryBase):
    id: int
