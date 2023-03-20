import pytest
from rest_framework.test import APIClient


@pytest.fixture
def client() -> APIClient:
    """
    An API Client fixture for Pytest.
    """
    return APIClient()
