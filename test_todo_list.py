import unittest
from app import app

class TestApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_homepage(self):
        result = self.app.get('/')
        self.assertEqual(result.status_code, 200)
        self.assertIn(b'Welcome to my Todo List Web App!', result.data)

    def test_login(self):
        result = self.app.post('/login', data=dict(email='test@test.com', password='password'), follow_redirects=True)
        self.assertEqual(result.status_code, 200)
        self.assertIn(b'Please check your login details and try again.', result.data)

    def test_logout(self):
        result = self.app.get('/logout', follow_redirects=True)
        self.assertEqual(result.status_code, 200)
        self.assertIn(b'Please log in to access this page.', result.data)

if __name__ == '__main__':
    unittest.main()
