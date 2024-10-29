from pydantic import BaseModel, Field
from typing import Annotated, List, Union

from app.schemas.exercise_schema import ExerciseBase, ExerciseSchema


class UserBase(BaseModel):
    username: Annotated[str, Field(max_length=50)]

    class Config:
        from_attributes = True


class UserPasswordSchema(UserBase):
    hashed_password: str


class UserSchema(UserBase):
    id: Annotated[int, Field(gt=0)]


class TokenData(BaseModel):
    id: Union[int, None] = None
    username: Union[str, None] = None


class Token(BaseModel):
    access: str
    refresh: str


class UserExercise(BaseModel):
    exercise: ExerciseBase
    weight: float | None = None
    reps: int | None = None

    class Config:
        from_attributes = True


class UserWithExercises(BaseModel):
    id: int
    username: str
    user_exercises: List[UserExercise] = []

    class Config:
        from_attributes = True
