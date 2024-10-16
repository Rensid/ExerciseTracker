from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.base.base import Base
from app.models.associations import users_exercises


class Exercise(Base):
    __tablename__ = 'exercise'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    category_title = Column(String, ForeignKey(
        'category.title'), ondelete='CASCADE')
    weight = Column(Integer, nullable=False)
    reps = Column(Integer, nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    users = relationship('User', secondary=users_exercises,
                         back_populates='exercises')
    category = relationship('Category', back_populates='exercises')
