#!/usr/bin/python3
# """Unittest for Base class
# """

# import unittest
# import models.base_model
# #from models.base_model import BaseModel
# from datetime import datetime
# import json
# import os


# class TestBase_ModelClass(unittest.TestCase):
#     """Class for the test of BaseModel class
#     """
#     @classmethod
#     def setUpClass(self):
#         """
#         setUp method to create two instances
#         Args:
#             None
#         """
#         self.my_model1 = models.base_model.BaseModel()
#         self.my_model2 = models.base_model.BaseModel()

#     @classmethod
#     def tearDownClass(self):
#         """
#         tearDown method
#         Args:
#             None
#         """
#         pass

#     def test_Module_documentation(self):
#         """
#         testing module documentation
#         Args:
#             None
#         """
#         mod_doc = (models.base_model.__doc__)
#         self.assertTrue(len(mod_doc.strip().splitlines()) >= 3)

#     def test_Class_documentation(self):
#         """
#         testing class documentation
#         Args:
#             None
#         """
#         class_doc = models.base_model.BaseModel.__doc__
#         self.assertTrue(len(class_doc.splitlines()) >= 3)

#     def test_shebang(self):
#         """
#         testing shebang
#         Args:
#             None
#         """
#         with open("models/base_model.py", "r") as file:
#             first_line = file.readline()
#             self.assertTrue(first_line.strip() == "#!/usr/bin/python3")

#     def test_style(self):
#         """
#         testing pep8 style
#         Args:
#             None
#         """
#         with os.popen("pep8 models/base_model.py") as my_file:
#             self.assertEqual(my_file.read(), '')

#     def test_constructor(self):
#         """
#         testing __init__ method
#         Args:
#             None
#         """
#         self.assertIsInstance(self.my_model1, models.base_model.BaseModel)
#         self.assertIsInstance(self.my_model2, models.base_model.BaseModel)
#         self.assertTrue(hasattr(self.my_model1, "created_at"))
#         self.assertTrue(hasattr(self.my_model1, "updated_at"))
#         self.assertTrue(hasattr(self.my_model2, "created_at"))
#         self.assertTrue(hasattr(self.my_model2, "updated_at"))
#         self.assertIsInstance(self.my_model1.created_at, datetime)
#         self.assertIsInstance(self.my_model1.updated_at, datetime)
#         self.assertIsInstance(self.my_model2.created_at, datetime)
#         self.assertIsInstance(self.my_model2.updated_at, datetime)
#         self.assertNotEqual(self.my_model1.created_at,
#                             self.my_model2.created_at)
#         self.assertNotEqual(self.my_model1.updated_at,
#                             self.my_model2.updated_at)

#     def test_id(self):
#         """
#         testing id attribute
#         Args:
#             None
#         """
#         self.assertTrue(hasattr(self.my_model1, "id"))
#         self.assertTrue(hasattr(self.my_model2, "id"))
#         self.assertNotEqual(self.my_model1.id, self.my_model2.id)
#         self.assertEqual(type(self.my_model1.id), str)

#     def test_str(self):
#         """
#         testing __str__ method
#         Args:
#             None
#         """
#         self.assertEqual(
#             print(
#                 self.my_model1), print(
#                     "[{}] ({}) {}".format(
#                         type(self.my_model1).__name__,
#                         self.my_model1.id,
#                         self.my_model1.__dict__)))
#         self.assertEqual(
#             print(
#                 self.my_model2), print(
#                     "[{}] ({}) {}".format(
#                         type(self.my_model2).__name__,
#                         self.my_model2.id,
#                         self.my_model2.__dict__)))

#     def test_save(self):
#         """
#         testing save method
#         Args:
#             None
#         """
#         date1 = self.my_model1.updated_at
#         self.my_model1.save()
#         self.assertNotEqual(self.my_model1.updated_at, date1)
#         date2 = self.my_model2.updated_at
#         self.my_model2.save()
#         self.assertNotEqual(self.my_model2.updated_at, date2)

#     def test_kwargs(self):
#         """
#         testing __init__ with kwargs
#         Args:
#             None
#         """
#         new_dict = self.my_model1.to_dict()
#         my_model3 = models.base_model.BaseModel(**new_dict)

#         self.assertEqual(self.my_model1.__dict__, my_model3.__dict__)
#         self.assertEqual(self.my_model1.to_dict(), my_model3.to_dict())
#         self.assertIsInstance(my_model3, models.base_model.BaseModel)
#         self.assertNotEqual(self.my_model1, my_model3)
#         self.assertIsInstance(my_model3.created_at, datetime)
#         self.assertIsInstance(my_model3.updated_at, datetime)
#         self.assertFalse(type(my_model3.created_at) is str)


# if __name__ == '__main__':
#     unittest.main()

"""
Unitest Class BaseModel
"""
import unittest
from models.base_model import BaseModel, __doc__ as mrdoc
import inspect
import pep8
import models
from datetime import datetime as datetime


class TestBaseModel(unittest.TestCase):
    """
    Unitest for testing
    """

    def test_module_docstring(self):
        """
        Tests docstring for module
        """
        self.assertTrue(len(mrdoc) > 0)

    def test_class_docstring(self):
        """
        Tests docstring for class
        """
        self.assertTrue(len(BaseModel.__doc__) > 0)

    def test_methods_docstring(self):
        """
        Tests docstring for methods
        """
        methods = inspect.getmembers(BaseModel, predicate=inspect.ismethod)
        for name, func in methods:
            self.assertTrue(len(func.__doc__) > 0)
        methods = inspect.getmembers(BaseModel, predicate=inspect.isfunction)
        for name, func in methods:
            self.assertTrue(len(func.__doc__) > 0)

    def test_docstring_for_test(self):
        """
        Tests docstring for this test
        """
        self.assertTrue(len(__doc__) > 0)

    def test_docstring_class_test(self):
        """
        Tests dosctring for class TestBaseModel
        """
        self.assertTrue(len(TestBaseModel.__doc__) > 0)

    def test_docstring_methods(self):
        """
        Tests docstring for all methods in TestBaseModel class
        """
        methods = inspect.getmembers(TestBaseModel, predicate=inspect.ismethod)
        for name, func in methods:
            self.assertTrue(len(func.__doc__) > 0)

    def test_pep8(self):
        """
        Tests for PEP-8
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(["models/base_model.py"])
        self.assertEqual(result.total_errors, 0)

    def test_base_init(self):
        """
        Testing a class BaseModel
        """
        instance = BaseModel()
        self.assertIsInstance(instance, BaseModel)
        self.assertTrue(issubclass(type(instance), BaseModel))
        self.assertIs(type(instance), BaseModel)
        instance.name = "Holberton"
        instance.my_number = 89
        self.assertEqual(instance.name, "Holberton")
        self.assertEqual(instance.my_number, 89)
        """
        at_class = {
            "id": str,
            "created_at": datetime
            "updated_at": datetime
            "name": str
            "my_number": int
        }
        """

    def test_none(self):
        """Check if a new instance is not none"""
        bm1 = BaseModel()
        self.assertIsNotNone(bm1)

    def test_uuid(self):
        """Check ids in the created instances"""
        bm1 = BaseModel()
        bm2 = BaseModel()
        self.assertTrue(hasattr(bm1, "id"))
        self.assertNotEqual(bm1.id, bm2.id)

    def test_created_at(self):
        """Check if the instance has created_at Atttibute"""
        bm1 = BaseModel()
        bm2 = BaseModel()
        self.assertTrue(bm1, "created_at")
        self.assertTrue(bm2, "created_at")

    def test_updated_at(self):
        """Check if the instance has created_at Atttibute"""
        bm1 = BaseModel()
        bm2 = BaseModel()
        self.assertTrue(bm1, "updated_at")
        self.assertTrue(bm2, "updated_at")

    def test__str__(self):
        """Check the string of an created instance"""
        bm1 = BaseModel()
        printed = "[{}] ({}) {}".format(
            bm1.__class__.__name__, bm1.id, bm1.__dict__)
        self.assertEqual(str(bm1), printed)

    def test_to_dict(self):
        """Test the to_dict method from BaseModel"""
        bm1 = BaseModel()
        bm1_dict = bm1.to_dict()
        self.assertIsInstance(bm1_dict, dict)
        self.assertEqual(bm1_dict["__class__"], "BaseModel")
        self.assertEqual(str(bm1.id), bm1_dict["id"])
        self.assertIsInstance(bm1_dict["created_at"], str)
        self.assertIsInstance(bm1_dict["updated_at"], str)

    def test_save(self):
        """Test to check each update in the storage"""
        bm1 = BaseModel()
        self.assertTrue(hasattr(bm1, "updated_at"))
        bm1.save()
        self.assertTrue(hasattr(bm1, "updated_at"))
        t_arg = {'id': 'b6a6e15c-c67d-4312-9a75-9d084935e579',
                 'create_at': datetime(2017, 9, 28, 21, 5, 54, 119427),
                 'updated_at': datetime(2017, 9, 28, 21, 5, 54, 119572),
                 'name': 'bm1'}
        bm2 = BaseModel(t_arg)
        bm2.save()
        last_time = bm2.updated_at
        bm2.save()
        self.assertNotEqual(last_time, bm2.updated_at)

    def test_init_from_dict(self):
        """test to check a new instance witk Kwargs"""
        my_dict = {'id': '56d43177-cc5f-4d6c-a0c1-e167f8c27337',
                   'created_at': '2017-09-28T21:03:54.052298',
                   '__class__': 'BaseModel', 'my_number': 89,
                   'updated_at': '2017-09-28T21:03:54.052302',
                   'name': 'Holberton'}
        bm1 = BaseModel(**my_dict)
        self.assertIsInstance(bm1, BaseModel)
        self.assertIsInstance(bm1.id, str)
        self.assertEqual(bm1.id, '56d43177-cc5f-4d6c-a0c1-e167f8c27337')
        self.assertIsInstance(bm1.created_at, datetime)
        self.assertIsInstance(bm1.updated_at, datetime)
        self.assertIsInstance(bm1.name, str)
        self.assertEqual(bm1.name, 'Holberton')

    def test_new_attributte(self):
        """test to check if new attribute  can be added"""
        bm1 = BaseModel()
        bm1.name = "Betty"
        self.assertEqual(bm1.name, "Betty")
