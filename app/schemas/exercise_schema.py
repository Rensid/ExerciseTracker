from pydantic import BaseModel


class ExerciseBase(BaseModel):
    name: str
    description: str | None = None
    category_title: str

    class Config:
        from_attributes = True


class ExerciseSchema(ExerciseBase):
    weight: float | None = None
    reps: int | None = None
    user_id: int | None = None
