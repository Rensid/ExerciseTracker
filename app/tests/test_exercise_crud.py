
import json
from httpx import AsyncClient
import pytest
from app.tests.conftest import data_generator


@pytest.mark.asyncio
async def test_exercise_add(app_with_test_db):
    async with AsyncClient(app=app_with_test_db, base_url='http://test') as ac:
        name = await data_generator(5)
        response = await ac.post('/exercise/', content=json.dumps({
            "name": name,
            "category_title": "cardio"
        }))
    assert response.json()["name"] == name
    assert response.status_code == 200
