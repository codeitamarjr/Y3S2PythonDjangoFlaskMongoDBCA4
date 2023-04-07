import unittest
from flask_testing import TestCase
from app import app, db, todos
from bson.objectid import ObjectId

class FormTodoTestCase(TestCase):

    def create_app(self):
        app.config['TESTING'] = True
        return app

    def setUp(self):
        db.drop_collection('todos')

    def test_todo_form_submit(self):
        # Create a user session
        with self.client.session_transaction() as sess:
            sess['user_id'] = str(ObjectId())

        # Submit the todo form
        response = self.client.post('/todo', data=dict(
            content='Test todo',
            degree='low'
        ), follow_redirects=True)

        # Verify the response
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Test todo', response.data)
        self.assertIn(b'low', response.data)

if __name__ == '__main__':
    unittest.main()
