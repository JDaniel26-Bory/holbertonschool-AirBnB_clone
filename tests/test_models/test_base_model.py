import unittest
from datetime import datetime
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):

    def setUp(self):
        self.base_model = BaseModel()
    
    def tearDown(self):
        self.base_model = None
    
    def test_to_dict(self):
        expected_keys = ['id', 'created_at', 'updated_at', '__class__']
        obj = self.base_model.to_dict()
        self.assertEqual(obj['__class__'], 'BaseModel')
        self.assertIsInstance(obj['created_at'], str)
        self.assertIsInstance(obj['updated_at'], str)

    def test_id(self):
        base_model = BaseModel()
        self.assertIsInstance(base_model.id, str)

    def test_created_at(self):
        base_model = BaseModel()
        self.assertIsInstance(base_model.created_at, datetime)

    def test_str(self):
        base_model = BaseModel()
        expected_str = f"[BaseModel] ({base_model.id}) {base_model.__dict__}"
        self.assertEqual(str(base_model), expected_str)

    def test_save(self):
        self.updated_at = datetime.now()
        self.base_model.save()
        self.assertNotEqual(datetime.now, self.base_model.updated_at)
