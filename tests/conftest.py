import os
import uuid

import pytest
import requests
from dotenv import load_dotenv


class TestConfig:
    def __init__(self):
        load_dotenv()
        self.base_url = os.getenv("BASE_URL")


@pytest.fixture(scope="session")
def config() -> TestConfig:
    return TestConfig()


@pytest.fixture(scope="session")
def http_client():
    session = requests.Session()
    yield session
    session.close()


@pytest.fixture
def request_id():
    return str(uuid.uuid4())
