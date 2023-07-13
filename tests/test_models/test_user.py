import unittest
from models.user import User

class UserTestCase(unittest.TestCase):
    """Test case for the User class."""

    def test_email_initialization(self):
        """Test the initialization of the email attribute."""
        user = User()
        self.assertEqual(user.email, "")
        
    def test_password_initialization(self):
        """Test the initialization of the password attribute."""
        user = User()
        self.assertEqual(user.password, "")
        
    def test_first_name_initialization(self):
        """Test the initialization of the first_name attribute."""
        user = User()
        self.assertEqual(user.first_name, "")
        
    def test_first_name_initialization(self):
        """Test the initialization of the first_name attribute."""
        user = User()
        self.assertEqual(user.first_name, "")    

