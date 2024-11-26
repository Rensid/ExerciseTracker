import pytest
import json
from app.main import app
import asyncio
from httpx import AsyncClient, ASGITransport
from app.base.test_base import get_test_async_session


@pytest.mark.asyncio
async def test_category_create():
    async with AsyncClient(app=app, base_url='http://test') as ac:
        response = await ac.post('/category/', json={'title': 'Test Category 2'})
        assert response.status_code == 200
        data = response.json()
        assert data['title'] == 'Test Category 2'
