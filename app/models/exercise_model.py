from sqlalchemy import Column, String, Integer, ForeignKey, Float
from sqlalchemy.orm import relationship
from app.base.base import Base
from app.models.associations import UserExercise


class Exercise(Base):
    __tablename__ = 'exercise'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    category_title = Column(String, ForeignKey('category.title'))

    users = relationship('UserExercise', back_populates='exercise')
    category = relationship('Category', back_populates='exercises')
