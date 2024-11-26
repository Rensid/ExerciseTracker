import asyncio
from app.main import app
import json
import pytest
from httpx import AsyncClient, ASGITransport

from app.tests.conftest import data_generator


@pytest.mark.asyncio
async def test_login():
    async with AsyncClient(transport=ASGITransport(app=app), base_url='http://test') as ac:
        response = await ac.post("/login", data={"username": "123", "password": "123"})
    assert response.status_code == 200
    assert response.json().get('access') is not None
    assert response.json().get('refresh') is not None


@pytest.mark.asyncio
async def test_registration(app_with_test_db):
    username = await data_generator(8)
    password = await data_generator(8)
    async with AsyncClient(app=app_with_test_db, base_url='http://test') as ac:
        response = await ac.post("/registration",
                                 json={"username": username, "hashed_password": password})
    assert response.status_code == 200
    assert response.json()['refresh'] is not None
    assert response.json()['access'] is not None


# @pytest.mark.asyncio
# async def test_multiple_requests():
#     async with AsyncClient(transport=ASGITransport(app=app), base_url='http://test') as ac:
#         tasks = [ac.post(
#             "/login", data={"username": "123", "password": "123"}) for _ in range(10)]
#         responses = await asyncio.gather(*tasks)
#         for i, response in enumerate(responses):

#             assert response.status_code == 200
