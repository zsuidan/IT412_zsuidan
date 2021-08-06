import unittest
from classes.Event import Event
from classes.Calendar import Calendar

class TestCalendarClass(unittest.TestCase):
    """Tests the Calendar class"""

    def setUp(self):
        """Create an instance of the Calendar class for testing all class functions"""
        self.test_calendar = Calendar("Test Calendar", "Zach")
        self.test_event = Event("Christmas", "12-25-2021", "2:00", "single occurrence")

    def test_add_event(self):
        """Tests adding an event to the Calendar"""
        self.test_calendar.addEvent(self.test_event)

        self.assertIn(self.test_event, self.test_calendar.events)

    def test_remove_event(self):
        """Tests removing an event from the Calendar"""
        self.test_calendar.addEvent(self.test_event)
        self.test_calendar.removeEvent(self.test_event)

        self.assertNotIn(self.test_event, self.test_calendar.events)


class TestEventClass(unittest.TestCase):
    """Tests the Event class"""
    def setUp(self):
        """Create an instance of the Event class for testing all class functions"""
        self.test_event = Event("", "", "", "")

    def test_ok_name_success(self):
        """These are values which I think should work"""
        valid_names_to_test = ["Birthday  ", "  birthday", "birthday", "  Birthday  "]

        for name in valid_names_to_test:
            self.test_event.name = name
            self.assertTrue(self.test_event.okName())

    def test_ok_name_failure(self):
        """These are values which I think should NOT work"""
        invalid_names_to_test = ["0123", "!@#^%#", "", "Birthday123", "Birthday!@#", "  "]

        for name in invalid_names_to_test:
            self.test_event.name = name
            self.assertFalse(self.test_event.okName())

    def test_ok_date_success(self):
        """These are values which I think should work"""
        valid_dates_to_test = ["1-2-2021", "12-25-2021", "6-28"]

        for date in valid_dates_to_test:
            self.test_event.date = date
            self.assertTrue(self.test_event.okDate())
    
    def test_ok_date_failure(self):
        """These are values which I think should NOT work"""
        invalid_dates_to_test = ["", "  ", "1/2/2021", "12.25.2021", "abc-123", "asd", "!@#%", "12-!@%-21"]

        for date in invalid_dates_to_test:
            self.test_event.date = date
            self.assertFalse(self.test_event.okDate())

    def test_ok_time_success(self):
        """These are values which I think should work"""
        valid_times_to_test = ["9:30", "12:00", "23:15"]

        for time in valid_times_to_test:
            self.test_event.time = time
            self.assertTrue(self.test_event.okTime())

    def test_ok_time_failure(self):
        """These are values which I think should NOT work"""
        valid_times_to_test = ["", "  ", "9.30", "twelve", "9:30asd"]

        for time in valid_times_to_test:
            self.test_event.time = time
            self.assertFalse(self.test_event.okTime())

    def test_ok_type_success(self):
        """These are values which I think should work"""
        valid_types_to_test = ["s", "r", "f", "  f"," r ", "s  "]

        for type in valid_types_to_test:
            self.test_event.type = type
            self.assertTrue(self.test_event.okType())

    def test_ok_type_failure(self):
        """These are values which I think should NOT work"""
        invalid_types_to_test = ["", "123", "z", "!@#", "  "]

        for type in invalid_types_to_test:
            self.test_event.type = type
            self.assertFalse(self.test_event.okType())