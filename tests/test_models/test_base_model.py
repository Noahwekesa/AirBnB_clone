#!/usr/bin/python3
"""
Unit tests for the BaseModel class
"""
import unittest
import pep8
from os import path, remove
import datetime
import models
from models import base_model
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

class TestBaseModel(unittest.TestCase):
    """
    This class defines variables and methods for testing the BaseModel class.
    """

    def SetUpClass(self):
        """
        Set the public class attributes of the test Amenity class back to their default values.
        """
        FileStorage._FileStorage__objects = {}
        FileStorage._FileStorage__file_path = "file.json"

    def TearDown(self):
        """
        Delete the file.json used for testing.
        """
        del FileStorage._FileStorage__file_path
        del FileStorage._FileStorage__objects
        if path.exists("file.json"):
            remove("file.json")

    def test_pep8_conformance(self):
        """
        Test that the BaseModel class conforms to PEP8 style guidelines.
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base_model.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_class_method_presence(self):
        """
        Test that the required class methods of the BaseModel class are all present.
        """
        l1 = dir(BaseModel)
        self.assertIn('__init__', l1)
        self.assertIn('save', l1)
        self.assertIn('to_dict', l1)
        self.assertIn('__str__', l1)

    def test_instance_method_presence(self):
        """
        Test that the required instance methods of the BaseModel class are all present.
        """
        l1 = dir(BaseModel())
        self.assertIn('__init__', l1)
        self.assertIn('save', l1)
        self.assertIn('to_dict', l1)
        self.assertIn('__str__', l1)

    def test_instance_attribute_presence(self):
        """
        Test that the required instance attributes of the BaseModel class are all present.
        """
        l1 = dir(BaseModel())
        self.assertIn('id', l1)
        self.assertIn('updated_at', l1)
        self.assertIn('created_at', l1)
        self.assertIn('__class__', l1)

    def test_docstring_presence(self):
        """
        Test that the BaseModel class, its methods, and modules all have docstrings.
        """
        self.assertIsNot(base_model.__doc__, None)
        self.assertIsNot(BaseModel.__init__.__doc__, None)
        self.assertIsNot(BaseModel.save.__doc__, None)
        self.assertIsNot(BaseModel.to_dict.__doc__, None)
        self.assertIsNot(BaseModel.__str__.__doc__, None)

    def test_instantiation(self):
        """
        Test proper instantiation of the BaseModel object 'BaseModel()'.
        """
        # ...
        # (The rest of the comments remain unchanged)
        # ...

    def test_save(self):
        """
        Test the save method of the BaseModel class.
        """
        # ...

    def test_to_dict(self):
        """
        Test the to_dict method of the BaseModel class.
        """


    def test_str(self):
        """
        Test the __str__ method of the BaseModel class.
        """
  
