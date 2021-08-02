class Event():
    """A class for representing an event. Contains an event name, date, time, and type."""

    def __init__(self, name, date, time, type):
        """Constructor for the Event class"""
        self.name = name
        self.date = date
        self.time = time
        self.type = type

    def createEvent():
        """Creates a new Event using a series of user inputs.
        Returns:
            new_event -- the event created by the user
        """
        event_name = input("Please enter the event name: ")

        while not Event.okName(event_name):
            event_name = input("Event name was not formatted correctly. Please try again: ")

        event_date = input("Please enter the date for the event: ")

        while not Event.okDate(event_date):
            event_date = input("Event date was not formatted correctly. Please try again: ")

        event_time = input("Please enter the time for the event: ")

        while not Event.okTime(event_time):
            event_time = input("Event time was not formatted correctly. Please try again: ")

        event_type = input("Please enter the type of event (\"S\" for single occurrence, \"R\" for recurring, or \"F\" for fixed number of meetings): ")

        while not Event.okType(event_type):
            event_type = input("Event type was not formatted correctly. Please try again: ")

        if event_type.lower() == "s":
            event_type = "single occurrence"
        elif event_type.lower() == "r":
            event_type = "recurring"
        else:
            event_type = "fixed number of meetings"

        new_event = Event(event_name, event_date, event_time, event_type)

        return new_event

    def okDate(date):
        """Checks a date to ensure that it is formatted correctly.
        Arguments:
            date -- the date that is being tested
        Returns:
            True if the date is valid, False if invalid
        """
        allowed_characters = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "-"]

        if date:
            characters_ok = True
            for character in date:
                if character not in allowed_characters:
                    characters_ok = False
        else:
            characters_ok = False

        return characters_ok
   
    def okName(name):
        """Checks a name to ensure that it is formatted correctly.
        Arguments:
            name -- the name that is being tested
        Returns:
            True if the name is valid, False if invalid
        """
        if name.strip().isalpha():
            return True
        else:
            return False


    def okTime(time):
        """Checks a time to ensure that it is formatted correctly.
        Arguments:
            time -- the time that is being tested
        Returns:
            True if the time is valid, False if invalid
        """
        allowed_characters = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ":"]

        if time:
            characters_ok = True

            for character in time:
                if character not in allowed_characters:
                    characters_ok = False
        else:
            characters_ok = False

        return characters_ok

    def okType(type):
        """Checks an event type to ensure that it is formatted correctly.
        Arguments:
            type -- the type that is being tested
        Returns:
            True if the type is valid, False if invalid
        """
        if type.strip().lower() == "s" or type.strip().lower() == "r" or type.strip().lower() == "f":
            return True
        else:
            return False