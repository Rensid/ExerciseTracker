from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from app.base.base import Base


class Category(Base):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True)
    title = Column(String, unique=True, nullable=False)
    exercises = relationship(
        'Exercise', back_populates='category', cascade='all, delete-orphan')
