"""Unittest for Review class
"""

import unittest
import models.review
from models.review import Review
from models.base_model import BaseModel
import os


class TestState(unittest.TestCase):
    """Class for the test of Review class
    """

    @classmethod
    def setUpClass(self):
        """
        setUp method to create two instances
        Args:
            None
        """
        self.review_obj = Review()

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
        mod_doc = (models.review.__doc__)
        self.assertTrue(len(mod_doc.strip().splitlines()) >= 3)

    def test_Class_documentation(self):
        """
        testing class documentation
        Args:
            None
        """
        class_doc = Review.__doc__
        self.assertTrue(len(class_doc.splitlines()) >= 3)

    def test_shebang(self):
        """
        testing shebang
        Args:
            None
        """
        with open("models/review.py", "r") as file:
            first_line = file.readline()
            self.assertTrue(first_line.strip() == "#!/usr/bin/python3")

    def test_style(self):
        """
        testing pep8 style
        Args:
            None
        """
        with os.popen("pep8 models/review.py") as my_file:
            self.assertEqual(my_file.read(), '')

    def test_class_attributes(self):
        """
        testing class attributes
        Args:
            None
        """
        self.assertTrue(hasattr(self.review_obj, 'text'))
        self.assertEqual(type(Review.text), str)
        self.assertEqual(self.review_obj.text, "")
        self.assertTrue(hasattr(self.review_obj, 'place_id'))
        self.assertEqual(type(Review.place_id), str)
        self.assertEqual(self.review_obj.place_id, "")
        self.assertTrue(hasattr(self.review_obj, 'user_id'))
        self.assertEqual(type(Review.user_id), str)
        self.assertEqual(self.review_obj.user_id, "")


if __name__ == '__main__':
    unittest.main()
