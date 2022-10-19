import sys
import os


from unittest.mock import AsyncMock
import pytest


sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


@pytest.fixture()
def mock_create_user(mocker):
    async_mock = AsyncMock()
    mocker.patch('blog.user.application.user.create_an_user',
                 side_effect=async_mock)
    return async_mock
