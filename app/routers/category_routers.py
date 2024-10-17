from fastapi import APIRouter

category_router = APIRouter()


@category_router.get('/category/all')
async def get_all_categories():
    pass


@category_router.post('/category/{category_id}')
async def create_category(category_id):
    pass
