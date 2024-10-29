from sqlalchemy import DateTime, Float, Table, Column, Integer, ForeignKey, func
from app.base.base import Base
from sqlalchemy.orm import relationship
# users_exercises = Table('users_exercise', Base.metadata,
#                         Column('user_id', Integer, ForeignKey(
#                             'user.id', ondelete='CASCADE'), primary_key=True),
#                         Column('exercise_id', Integer, ForeignKey(
#                             'exercise.id', ondelete='CASCADE'), primary_key=True)
#                         )


# class UserExercise(Base):
#     __tablename__ = 'users_exercise'

#     user_id = Column(Integer, ForeignKey(
#         'user.id', ondelete='CASCADE'), primary_key=True)
#     exercise_id = Column(Integer, ForeignKey(
#         'exercise.id', ondelete='CASCADE'), primary_key=True)
#     date = Column(DateTime, default=func.now())
#     weight = Column(Float, nullable=True)
#     reps = Column(Integer, nullable=True)

#     user = relationship('User', back_populates='user_exercises')
#     exercise = relationship('Exercise', back_populates='users')

class UserExercise(Base):
    __tablename__ = 'users_exercise'

    # уникальный идентификатор для каждой записи
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey(
        'user.id', ondelete='CASCADE'), nullable=False)
    exercise_id = Column(Integer, ForeignKey(
        'exercise.id', ondelete='CASCADE'), nullable=False)
    date = Column(DateTime, default=func.now())
    weight = Column(Float, nullable=True)
    reps = Column(Integer, nullable=True)

    user = relationship('User', back_populates='user_exercises')
    exercise = relationship('Exercise', back_populates='users')
