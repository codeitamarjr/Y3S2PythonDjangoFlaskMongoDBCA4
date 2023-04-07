import pytest
from app import create_app
from bson.objectid import ObjectId


@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True

    with app.test_client() as client:
        yield client


def test_index_route(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Todo List' in response.data


def test_add_todo_route(client):
    response = client.post('/', data={'content': 'New todo', 'degree': 'High'})
    assert response.status_code == 302
    assert response.headers['Location'] == 'http://localhost/'


def test_delete_todo_route(client):
    # Insert a new todo
    todos = client.application.db.todos
    todo_id = todos.insert_one({'content': 'New todo', 'degree': 'High'}).inserted_id

    # Delete the new todo
    response = client.post(f'/{todo_id}/delete/')
    assert response.status_code == 302
    assert response.headers['Location'] == 'http://localhost/'
    assert todos.find_one({'_id': ObjectId(todo_id)}) is None
