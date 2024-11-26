from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.crud.category_crud import create_category, get_category
from app.schemas.category_schema import CategoryBase
from app.base.base import get_async_session

category_router = APIRouter()


@category_router.post('/category/')
async def category_creation(category_data: CategoryBase,
                            session: Session = Depends(get_async_session)) -> CategoryBase:
    category = await create_category(session, category_data)
    return category
