import unittest
from functions.function_library import *

class NamePartTestCase(unittest.TestCase):
    """Tests for functions in the function_library.py file."""

    def test_valid_name_part(self):
        """Here are a bunch of values I think should work"""
        valid_names_to_test = ["Zach", "zach", " Zach", "Zach ", " zach", "zach "]
        
        for name in valid_names_to_test:
            self.assertTrue(validate_name_part(name))

    def test_invalid_name_part(self):
        """Here is a bunch of values I think should NOT work"""
        invalid_names_to_test = ["Zach'", "123", " Zach 123", "Zach#", "  ", "@#&*"]
        
        for name in invalid_names_to_test:
            self.assertFalse(validate_name_part(name))
