from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from app.base.base import Base
from app.models.associations import users_exercises


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    password_hash = Column(String(128), nullable=False)
    exercises = relationship(
        'Exercise', secondary=users_exercises, back_populates='users', cascade='all, delete')
