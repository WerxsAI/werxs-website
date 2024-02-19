import unittest
from flask_testing import TestCase
from app import create_app, TestConfig


class AuthTestCase(unittest.TestCase):
    def setUp(self):
        """Set up a test client for your Flask application."""
        self.app = create_app(TestConfig)
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        """Tear down the test client and context after each test."""
        self.app_context.pop()

    def test_login_redirects(self):
        """Test if the login route redirects to Auth0."""
        response = self.client.get("/login", follow_redirects=False)
        self.assertEqual(response.status_code, 302)
        self.assertTrue("auth.werxs.ai" in response.headers["Location"])


if __name__ == "__main__":
    unittest.main()
