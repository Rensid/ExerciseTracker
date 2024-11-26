import pytest
import json
from app.main import app
import asyncio
from httpx import AsyncClient, ASGITransport


@pytest.mark.asyncio
async def test_add_exercises(app_with_user):
    async with AsyncClient(app=app_with_user, base_url='http://test') as ac:
        response = await ac.post("/users/add_exercise?username=123", json={
            "exercise": {
                "name": "jumprope",
                "category_title": "cardio",
                "reps": 6
            }})

        assert response.json() == 200
        assert json.loads(response.text)["name"] == "jumprope"


# @pytest.mark.asyncio
# async def test_multiple_adds():
#     async with AsyncClient(app=app, base_url='https://test') as ac:
#         test_requests = [ac.post(
#             '/users/add_exercise',
#             data={"exercise": {
#                 "name": f"test exercise {i}",
#                 "category": "Test category 1"
#             }})
#             for i in range(10)]
#         responses = await asyncio.gather(*test_requests)
#         for response in responses:
#             assert response.status_code == 200
