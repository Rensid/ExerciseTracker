from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.models.category_model import Category
from app.schemas.category_schema import CategoryBase


async def create_category(session: AsyncSession, category: CategoryBase):
    if await get_category(session, category.title):
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail="Category already exists")
    else:
        new_category = Category(title=category.title)
        session.add(new_category)
        await session.commit()
        return new_category


async def get_category(session: AsyncSession, title: str):
    category = await session.execute(select(Category).where(Category.title == title))
    return category.scalar()


async def update_category(session: AsyncSession, category: Category):
    category = await get_category(session, category.title)
    if category:
        category.title = category.title
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Category not found")
    await session.commit()
    return category
