from httpx import AsyncClient, ASGITransport

import pytest
import asyncio

from app.tests.conftest import data_generator


@pytest.mark.asyncio
async def test_create_category(app_with_test_db):
    category = data_generator(8)
    async with AsyncClient(app=app_with_test_db, base_url="http://test") as ac:
        response = await ac.post("/category/", json={"title": category})
    assert response.status_code == 200
    assert response.json() == {"title": category}
