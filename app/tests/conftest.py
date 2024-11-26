import random
from app.auth.auth import get_current_user
from app.dependences.test_dependences import get_username
from app.main import app
from app.base.base import get_async_session
from app.base.test_base import get_test_async_session

import pytest


@pytest.fixture
def app_with_user():
    app.dependency_overrides[get_current_user] = get_username
    app.dependency_overrides[get_async_session] = get_test_async_session
    yield app
    app.dependency_overrides.clear()


@pytest.fixture
def app_with_test_db():
    app.dependency_overrides[get_async_session] = get_test_async_session
    yield app
    app.dependency_overrides.clear()


async def data_generator(number):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    result = ''
    for number in range(number):
        letter = random.choice(alphabet)
        result += letter
    return result
