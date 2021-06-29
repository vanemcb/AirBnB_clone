"""Unittest for State class
"""

import unittest
import models.state
from models.state import State
from models.base_model import BaseModel
import os


class TestState(unittest.TestCase):
    """Class for the test of State class
    """

    @classmethod
    def setUpClass(self):
        """
        setUp method to create two instances
        Args:
            None
        """
        self.state_obj = State()

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
        mod_doc = (models.state.__doc__)
        self.assertTrue(len(mod_doc.strip().splitlines()) >= 3)

    def test_Class_documentation(self):
        """
        testing class documentation
        Args:
            None
        """
        class_doc = State.__doc__
        self.assertTrue(len(class_doc.splitlines()) >= 3)

    def test_shebang(self):
        """
        testing shebang
        Args:
            None
        """
        with open("models/state.py", "r") as file:
            first_line = file.readline()
            self.assertTrue(first_line.strip() == "#!/usr/bin/python3")

    def test_style(self):
        """
        testing pep8 style
        Args:
            None
        """
        with os.popen("pep8 models/state.py") as my_file:
            self.assertEqual(my_file.read(), '')

    def test_class_attributes(self):
        """
        testing class attributes
        Args:
            None
        """
        self.assertTrue(hasattr(self.state_obj, 'name'))
        self.assertEqual(type(State.name), str)
        self.assertEqual(self.state_obj.name, "")


if __name__ == '__main__':
    unittest.main()
