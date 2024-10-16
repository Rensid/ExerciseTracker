from sqlalchemy import Table, Column, Integer, ForeignKey
from app.base.base import Base

users_exercises = Table('users_exercise', Base.metadata,
                        Column('user_id', Integer, ForeignKey(
                            'user.id', ondelete='CASCADE'), primary_key=True),
                        Column('exercise_id', Integer, ForeignKey(
                            'exercise.id', ondelete='CASCADE'), primary_key=True)
                        )
