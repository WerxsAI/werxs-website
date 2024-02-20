import unittest
from flask_testing import TestCase
from app import create_app, TestConfig


class TestRoutes(TestCase):

    def create_app(self):
        # Pass TestConfig to use testing configurations
        return create_app(TestConfig)

    def setUp(self):
        # Setup logic before each test. For example, initializing a test database.
        pass  # Implement if needed

    def tearDown(self):
        # Cleanup logic after each test. For example, closing database connections.
        pass  # Implement if needed

    def test_home_page(self):
        # Test the home page route
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        # Add more assertions based on expected content

    def test_realtor_page(self):
        # Test the realtor page route
        response = self.client.get("/realtor")
        self.assertEqual(response.status_code, 200)
        # Add more assertions based on expected content

    def test_news_page(self):
        # Test the realtor page route
        response = self.client.get("/news")
        self.assertEqual(response.status_code, 200)
        # Add more assertions based on expected content
        
    def test_contact_page(self):
        # Test the realtor page route
        response = self.client.get("/contact")
        self.assertEqual(response.status_code, 200)
        # Add more assertions based on expected content

    def test_login_redirect(self):
        """
        Test if accessing the login route redirects to the Auth0 login page.
        This assumes that the actual redirection URL contains 'auth.werxs.ai'.
        """
        response = self.client.get("/login", follow_redirects=False)
        self.assertEqual(response.status_code, 302)
        self.assertIn("auth.werxs.ai", response.headers["Location"])


    def test_logout_redirect(self):
        """
        Test if the logout route clears the session and redirects to the home page.
        This test simulates logging in by setting a user in the session before testing logout.
        """
        with self.client.session_transaction() as session:
            session["user"] = "testuser"  # Simulate a user session

        response = self.client.get("/logout", follow_redirects=False)
        self.assertEqual(response.status_code, 302)
        # Check if the redirection is towards the home page or Auth0 logout URL
        self.assertTrue(
            "/" in response.headers["Location"]
            or "auth.werxs.ai" in response.headers["Location"]
        )

        # Re-check the session to see if the user key has been cleared
        with self.client.session_transaction() as session:
            self.assertNotIn("user", session)


if __name__ == "__main__":
    unittest.main()
