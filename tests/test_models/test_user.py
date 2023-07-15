import unittest
from models.user import User


class TestUser(unittest.TestCase):
    def setUp(self):
        """Set up any necessary objects before each test case."""
        # Create an instance of User for testing
        self.user = User()

    def tearDown(self):
        """Clean up any resources after each test case."""
        # Remove the reference to the user instance
        self.user = None

    def test_user_attributes(self):
        """Test the attributes of the User class."""
        self.assertTrue(hasattr(self.user, 'email'))
        self.assertTrue(hasattr(self.user, 'password'))
        self.assertTrue(hasattr(self.user, 'first_name'))
        self.assertTrue(hasattr(self.user, 'last_name'))

    def test_user_instance(self):
        """Test the instance of the User class."""
        self.assertIsInstance(self.user, User)

    def test_user_str(self):
        """Test the __str__() method of the User class."""
        expected_str = f"[User] ({self.user.id}) {self.user.__dict__}"
        self.assertEqual(str(self.user), expected_str)

    def test_user_save(self):
        """Test the save() method of the User class."""
        old_updated_at = self.user.updated_at
        self.user.save()
        new_updated_at = self.user.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)

    def test_user_to_dict(self):
        """Test the to_dict() method of the User class."""
        user_dict = self.user.to_dict()
        self.assertEqual(user_dict['__class__'], 'User')
        self.assertEqual(
                user_dict['created_at'], self.user.created_at.isoformat())
        self.assertEqual(
                user_dict['updated_at'], self.user.updated_at.isoformat())


if __name__ == '__main__':
    unittest.main()
