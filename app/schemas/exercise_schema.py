from pydantic import BaseModel


class ExerciseBase(BaseModel):
    id: int
    name: str
    description: str
    category_title: str
    weight: float
