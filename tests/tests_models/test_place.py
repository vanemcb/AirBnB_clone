"""Unittest for Place class
"""

import unittest
import models.place
from models.place import Place
from models.base_model import BaseModel
import os


class TestState(unittest.TestCase):
    """Class for the test of Place class
    """

    @classmethod
    def setUpClass(self):
        """
        setUp method to create two instances
        Args:
            None
        """
        self.place_obj = Place()

    @classmethod
    def tearDownClass(self):
        """
        tearDown method
        Args:
            None
        """
        pass

    def test_Module_documentation(self):
        """
        testing module documentation
        Args:
            None
        """
        mod_doc = (models.place.__doc__)
        self.assertTrue(len(mod_doc.strip().splitlines()) >= 3)

    def test_Class_documentation(self):
        """
        testing class documentation
        Args:
            None
        """
        class_doc = Place.__doc__
        self.assertTrue(len(class_doc.splitlines()) >= 3)

    def test_shebang(self):
        """
        testing shebang
        Args:
            None
        """
        with open("models/place.py", "r") as file:
            first_line = file.readline()
            self.assertTrue(first_line.strip() == "#!/usr/bin/python3")

    def test_style(self):
        """
        testing pep8 style
        Args:
            None
        """
        with os.popen("pep8 models/place.py") as my_file:
            self.assertEqual(my_file.read(), '')

    def test_class_attributes(self):
        """
        testing class attributes
        Args:
            None
        """
        self.assertTrue(hasattr(self.place_obj, 'name'))
        self.assertEqual(type(Place.name), str)
        self.assertEqual(self.place_obj.name, "")
        self.assertTrue(hasattr(self.place_obj, 'city_id'))
        self.assertEqual(type(Place.city_id), str)
        self.assertEqual(self.place_obj.city_id, "")
        self.assertTrue(hasattr(self.place_obj, 'user_id'))
        self.assertEqual(type(Place.user_id), str)
        self.assertEqual(self.place_obj.user_id, "")
        self.assertTrue(hasattr(self.place_obj, 'description'))
        self.assertEqual(type(Place.description), str)
        self.assertEqual(self.place_obj.description, "")
        self.assertTrue(hasattr(self.place_obj, 'number_rooms'))
        self.assertEqual(type(Place.number_rooms), int)
        self.assertEqual(self.place_obj.number_rooms, 0)
        self.assertTrue(hasattr(self.place_obj, 'number_bathrooms'))
        self.assertEqual(type(Place.number_bathrooms), int)
        self.assertEqual(self.place_obj.number_bathrooms, 0)
        self.assertTrue(hasattr(self.place_obj, 'max_guest'))
        self.assertEqual(type(Place.max_guest), int)
        self.assertEqual(self.place_obj.max_guest, 0)
        self.assertTrue(hasattr(self.place_obj, 'price_by_night'))
        self.assertEqual(type(Place.price_by_night), int)
        self.assertEqual(self.place_obj.price_by_night, 0)
        self.assertTrue(hasattr(self.place_obj, 'latitude'))
        self.assertEqual(type(Place.latitude), float)
        self.assertEqual(self.place_obj.latitude, 0.0)
        self.assertTrue(hasattr(self.place_obj, 'longitude'))
        self.assertEqual(type(Place.longitude), float)
        self.assertEqual(self.place_obj.longitude, 0.0)
        self.assertTrue(hasattr(self.place_obj, 'amenity_ids'))
        self.assertEqual(type(Place.amenity_ids), list)
        self.assertEqual(self.place_obj.amenity_ids, [])


if __name__ == '__main__':
    unittest.main()
