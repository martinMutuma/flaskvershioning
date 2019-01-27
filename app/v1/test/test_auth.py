import unittest
from app.v1 import test
class TestAuth(unittest.TestCase):
    def test_signup(self):
        response = test.signup()

        self.assertEqual(response.status_code, 201)


    