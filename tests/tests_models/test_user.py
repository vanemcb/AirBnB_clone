"""Unittest for User class
"""

import unittest
import models.user
from models.user import User
from models.base_model import BaseModel
import os


class TestFile_User(unittest.TestCase):
    """Class for the test of User class
    """

    @classmethod
    def setUpClass(self):
        pass

    @classmethod
    def tearDownClass(self):
        pass

    def test_Module_documentation(self):
        """
        testing module documentation
        Args:
            None
        """
        mod_doc = (models.user.__doc__)
        self.assertTrue(len(mod_doc.strip().splitlines()) >= 3)

    def test_Class_documentation(self):
        """
        testing class documentation
        Args:
            None
        """
        class_doc = User.__doc__
        self.assertTrue(len(class_doc.splitlines()) >= 3)

    def test_shebang(self):
        """
        testing shebang
        Args:
            None
        """
        with open("models/user.py", "r") as file:
            first_line = file.readline()
            self.assertTrue(first_line.strip() == "#!/usr/bin/python3")

    def test_style(self):
        """
        testing pep8 style
        Args:
            None
        """
        with os.popen("pep8 models/user.py") as my_file:
            self.assertEqual(my_file.read(), '')

    def test_class_attributes(self):
        """
        testing class attributes
        Args:
            None
        """
        a = dir(User)
        attributes = [
            attr for attr in dir(FileStorage) if not attr.startswith('__')]
        self.assertTrue('email' in attributes)
        self.assertEqual(type(FileStorage.email), str)
        self.assertTrue('password' in attributes)
        self.assertEqual(type(FileStorage.password), str)
        self.assertTrue('first_name' in attributes)
        self.assertEqual(type(FileStorage.first_name), str)
        self.assertTrue('last_name' in attributes)
        self.assertEqual(type(FileStorage.last_name), str)

if __name__ == '__main__':
    unittest.main()
