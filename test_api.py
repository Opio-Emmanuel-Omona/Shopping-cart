import pytest
from app import APP


@pytest.fixture
def client():
    APP.config['TESTING'] = True
    test_client = APP.test_client()
    return test_client

def test_home_route(client):
    response = client.get('/')
    assert b'Hello World' in response.data
