#!/usr/bin/python3
"""Unittest Module for Amenity class"""

import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """testing the correct functioning of the class"""
    def test_name(self):
        """test attributes"""
        amenity = Amenity()
        self.assertEqual(amenity.name, "")
