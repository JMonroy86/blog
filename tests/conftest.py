import sys
import os
from fastapi.testclient import TestClient
from main import app


import pytest


sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


@pytest.fixture()
def test_client():
    return TestClient(app)
