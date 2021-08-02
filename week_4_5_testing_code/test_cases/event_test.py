import unittest
from classes.Event import Event

class TestEventClass(unittest.TestCase):
    """Tests the Event class"""

    def test_ok_name_success(self):
        """These are values which I think should work"""
        valid_names_to_test = ["Birthday  ", "  birthday", "birthday", "  Birthday  "]

        for name in valid_names_to_test:
            self.assertTrue(Event.okName(name))

    def test_ok_name_failure(self):
        """These are values which I think should NOT work"""
        invalid_names_to_test = ["0123", "!@#^%#", "", "Birthday123", "Birthday!@#"]

        for name in invalid_names_to_test:
            self.assertFalse(Event.okName(name))

    def test_ok_date_success(self):
        """These are values which I think should work"""
        valid_dates_to_test = ["1-2-2021", "12-25-2021", "6-28"]

        for date in valid_dates_to_test:
            self.assertTrue(Event.okDate(date))
    
    def test_ok_date_failure(self):
        """These are values which I think should NOT work"""
        invalid_dates_to_test = ["", "  ", "1/2/2021", "12.25.2021", "abc-123", "asd", "!@#%", "12-!@%-21"]

        for date in invalid_dates_to_test:
            self.assertFalse(Event.okDate(date))

    def test_ok_time_success(self):
        """These are values which I think should work"""
        valid_times_to_test = ["9:30", "12:00", "23:15"]

        for time in valid_times_to_test:
            self.assertTrue(Event.okTime(time))

    def test_ok_time_failure(self):
        """These are values which I think should NOT work"""
        valid_times_to_test = ["", "  ", "9.30", "twelve", "9:30asd"]

        for time in valid_times_to_test:
            self.assertFalse(Event.okTime(time))

    def test_ok_type_success(self):
        """These are values which I think should work"""
        valid_types_to_test = ["s", "r", "f", "  f"," r ", "s  "]

        for type in valid_types_to_test:
            self.assertTrue(Event.okType(type))

    def test_ok_type_failure(self):
        """These are values which I think should NOT work"""
        invalid_types_to_test = ["", "123", "z", "!@#"]

        for type in invalid_types_to_test:
            self.assertFalse(Event.okType(type))