"""Unittest for City class
"""

import unittest
import models.city
from models.city import City
from models.base_model import BaseModel
import os


class TestState(unittest.TestCase):
    """Class for the test of City class
    """

    @classmethod
    def setUpClass(self):
        """
        setUp method to create two instances
        Args:
            None
        """
        self.city_obj = City()

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
        mod_doc = (models.city.__doc__)
        self.assertTrue(len(mod_doc.strip().splitlines()) >= 3)

    def test_Class_documentation(self):
        """
        testing class documentation
        Args:
            None
        """
        class_doc = City.__doc__
        self.assertTrue(len(class_doc.splitlines()) >= 3)

    def test_shebang(self):
        """
        testing shebang
        Args:
            None
        """
        with open("models/city.py", "r") as file:
            first_line = file.readline()
            self.assertTrue(first_line.strip() == "#!/usr/bin/python3")

    def test_style(self):
        """
        testing pep8 style
        Args:
            None
        """
        with os.popen("pep8 models/city.py") as my_file:
            self.assertEqual(my_file.read(), '')

    def test_class_attributes(self):
        """
        testing class attributes
        Args:
            None
        """
        self.assertTrue(hasattr(self.city_obj, 'name'))
        self.assertEqual(type(City.name), str)
        self.assertEqual(self.city_obj.name, "")
        self.assertTrue(hasattr(self.city_obj, 'state_id'))
        self.assertEqual(type(City.state_id), str)
        self.assertEqual(self.city_obj.state_id, "")


if __name__ == '__main__':
    unittest.main()
