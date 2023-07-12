import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):

    def test_base_model_attributes(self):
        """
            test to  Check if the attributes are present
            and have the correct types
        """
        base_model = BaseModel()
        self.assertIsInstance(base_model.id, str)
        self.assertIsInstance(base_model.created_at, datetime)
        self.assertIsInstance(base_model.updated_at, datetime)

    def test_str_method(self):
        """
            Check if __str__ method returns the expected
            string representation
        """
        base_model = BaseModel()
        expected_str = "[BaseModel] ({}) {}".format(
                base_model.id,
                base_model.__dict__)
        self.assertEqual(str(base_model), expected_str)

    def test_save_method(self):
        """
            Call the save method and check if updated_at has been updated
        """
        base_model = BaseModel()
        old_updated_at = base_model.updated_at
        base_model.save()
        self.assertNotEqual(base_model.updated_at, old_updated_at)

    def test_to_dict_method(self):
        """
            Check if the returned value is a dictionary
        """
        base_model = BaseModel()
        obj_dict = base_model.to_dict()
        self.assertIsInstance(obj_dict, dict)

    def test_to_dict_keys(self):
        """
            Check if the dictionary contains the expected keys
        """
        base_model = BaseModel()
        obj_dict = base_model.to_dict()
        self.assertIn('__class__', obj_dict)
        self.assertIn('id', obj_dict)
        self.assertIn('created_at', obj_dict)
        self.assertIn('updated_at', obj_dict)

    def test_value_types(self):
        """
            Check if the values of the dictionary are
            of the expected types
        """
        base_model = BaseModel()
        obj_dict = base_model.to_dict()
        self.assertIsInstance(obj_dict['__class__'], str)
        self.assertIsInstance(obj_dict['id'], str)
        self.assertIsInstance(obj_dict['created_at'], str)
        self.assertIsInstance(obj_dict['updated_at'], str)


if __name__ == '__main__':
    unittest.main()
