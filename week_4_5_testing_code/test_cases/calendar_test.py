import unittest
from classes.Calendar import Calendar
from classes.Event import Event

class TestCalendarClass(unittest.TestCase):
    """Tests the Calendar class"""

    def setUp(self):
        """Create an instance of the Calendar class for testing all class functions"""
        self.test_calendar = Calendar("Test Calendar", "Zach")

    def test_add_event(self):
        """Tests adding an event to the Calendar"""
        sample_event = Event("Christmas", "12-25-2021", "2:00", "single occurrence")
        self.test_calendar.addEvent(sample_event)

        self.assertIn(sample_event, self.test_calendar.events)

    def test_remove_event(self):
        """Tests removing an event from the Calendar"""
        sample_event = Event("Christmas", "12-25-2021", "2:00", "single occurrence")
        self.test_calendar.addEvent(sample_event)
        self.test_calendar.removeEvent(sample_event)

        self.assertNotIn(sample_event, self.test_calendar.events)
