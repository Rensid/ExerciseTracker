import pytest
from httpx import AsyncClient, ASGITransport
from app.main import app


# @pytest.mark.asyncio
# async def test_login():
#     async with AsyncClient(app=app, base_url='http://test') as ac:
#         response = await ac.post("/users/", json={"username": "123", "password": "123"})
#     await response

@pytest.mark.anyio
async def test_root():
    async with AsyncClient(transport=ASGITransport(app=app), base_url='http://test')
