from sqlalchemy import DateTime, Float, Table, Column, Integer, ForeignKey, func
from app.base.base import Base
from sqlalchemy.orm import relationship


class UserExercise(Base):
    __tablename__ = "users_exercise"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("user.id", ondelete="CASCADE"), nullable=False)
    exercise_id = Column(
        Integer, ForeignKey("exercise.id", ondelete="CASCADE"), nullable=False
    )
    date = Column(DateTime, default=func.now())
    weight = Column(Float, nullable=True)
    reps = Column(Integer, nullable=True)

    user = relationship("User", back_populates="user_exercises")
    exercise = relationship("Exercise", back_populates="users")
