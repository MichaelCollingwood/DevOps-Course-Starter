from dotenv import load_dotenv, find_dotenv
import pytest
from todo_app import app
import mongomock

@pytest.fixture
def client():
    file_path = find_dotenv('.env.test')
    load_dotenv(file_path, override=True)
    
    with mongomock.patch(servers=(('fakemongo.com', 27017),)):
        test_app = app.create_app()
        with test_app.test_client() as client:
            db = test_app.db
            db["items"].insert_one({"title": "Some todo item", "status": "To Do"})
            yield client

def test_index_page(client):
    # Act
    response = client.get('/')

    # Assert
    assert response.status_code == 200
    assert 'Some todo item' in response.data.decode()
