#!/usr/bin/python3
"""
This script initializes a FileStorage instance and reloads data,
making it available for managing and persisting data.
"""


import io
import sys
import unittest
import os
import datetime
from models.amenity import Amenity
from models import storage


class TestUser(unittest.TestCase):
    """
    This script initializes a FileStorage instance and reloads data,
    making it available for managing and persisting data.
    """

    def test_attributes(self):
        """
        This script initializes a FileStorage instance and reloads data,
        making it available for managing and persisting data.
        """

        base1 = Amenity()
        base2 = Amenity()
        self.assertNotEqual(base1.id, base2.id)
        self.assertNotEqual(base1.created_at, base2.created_at)
        self.assertNotEqual(base1.updated_at, base2.updated_at)

    def test_attribute_type(self):
        """
        This script initializes a FileStorage instance and reloads data,
        making it available for managing and persisting data.
        """

        base1 = Amenity()
        self.assertEqual(type(base1.id), str)
        self.assertEqual(type(base1.created_at), datetime.datetime)
        self.assertEqual(type(base1.updated_at), datetime.datetime)

    def test_all_attributes(self):
        """
        This script initializes a FileStorage instance and reloads data,
        making it available for managing and persisting data.
        """

        base = Amenity()
        self.assertEqual(base.name, "")
