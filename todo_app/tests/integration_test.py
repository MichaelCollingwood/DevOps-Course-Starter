import json
import os
from dotenv import load_dotenv, find_dotenv
import pytest
import requests
from todo_app import app

@pytest.fixture
def client():
    # Use our test integration config instead of the 'real' version
    file_path = find_dotenv('.env.test')
    load_dotenv(file_path, override=True)

    # Create the new app.
    test_app = app.create_app()

    # Use the app to create a test_client that can be used in our tests.
    with test_app.test_client() as client:
        yield client

class StubResponse():
    def __init__(self, fake_response_data):
        self.fake_response_data = json.dumps(fake_response_data)
    
    @property
    def text(self):
        return self.fake_response_data

# Stub replacement for requests.get(url)
def stub(method, url, headers, params={}):
    test_board_id = os.environ.get('TRELLO_BOARD_ID')
    fake_response_data = None
    if url == f'https://api.trello.com/1/boards/{test_board_id}/lists':
        fake_response_data = [{
            'id': '123abc',
            'name': 'To Do'
        }]
        return StubResponse(fake_response_data)
    
    if url == f'https://api.trello.com/1/boards/{test_board_id}/cards':
        fake_response_data = [{
            'id': '345xyz',
            'name': 'Some todo item',
            'idList': '123abc'
        }]
        return StubResponse(fake_response_data)

    raise Exception(f'Integration test did not expect URL "{url}"')

def test_index_page(monkeypatch, client):
    # Arrange
    monkeypatch.setattr(requests, 'request', stub)

    # Act
    response = client.get('/')

    # Assert
    assert response.status_code == 200
    assert 'Some todo item' in response.data.decode()
