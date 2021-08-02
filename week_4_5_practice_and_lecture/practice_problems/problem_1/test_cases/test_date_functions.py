import unittest
from functions.function_library import *

class DateTestCase(unittest.TestCase):
    """Tests for functions in the function_library.py file."""

    def test_valid_date(self):
        """Here are a bunch of values I think should work"""
        valid_dates_to_test = ["6", "2 ", " 10", "  5  "]
        
        for date in valid_dates_to_test:
            self.assertTrue(validate_num(date))

    def test_invalid_date(self):
        """Here is a bunch of values I think should NOT work"""
        invalid_dates_to_test = ["a", "  ", "", "3#", "4f", "!@^"]
        
        for date in invalid_dates_to_test:
            self.assertFalse(validate_num(date))
    
    def test_date_creation(self):
        """Ensures that the create date function is formatted properly and removes blank space"""
        test_month = " 6"
        test_day = "28  "
        test_year = "  1997 "

        test_date = create_date(test_month, test_day, test_year)

        self.assertEqual(test_date, "6/28/1997")