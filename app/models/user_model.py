from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from app.base.base import Base


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    hashed_password = Column(String(128), nullable=False)
    user_exercises = relationship('UserExercise', back_populates='user',
                                  cascade='all, delete')
