class Calendar():
    """A class which represents a calendar. Stores a calendar name, calendar owner, and a list of events."""

    def __init__(self, name, owner):
        """Constructor for the Calendar class"""
        self.name = name
        self.owner = owner
        self.events = []

    def addEvent(self, event):
        """Adds an event to the list of events in the Calendar.
        Arguments:
            event -- the event being added
        """
        if event not in self.events:
            self.events.append(event)
        else:
            print("Event is already in Calendar.")

    def removeEvent(self, event):
        """Removes an event from the list of events in the Calendar.
        Arguments:
            event -- the event being removed
        """
        if event in self.events:
            self.events.remove(event)
        else:
            print("Event not found.")