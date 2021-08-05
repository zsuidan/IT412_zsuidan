class Event():
    """A class for representing an event. Contains an event name, date, time, and type."""

    def __init__(self, name, date, time, type):
        """Constructor for the Event class"""
        self.name = name
        self.date = date
        self.time = time
        self.type = type

    def createEvent(self):
        """Creates a new Event using a series of user inputs.
        Returns:
            new_event -- the event created by the user
        """
        self.name = input("Please enter the event name: ")

        while not self.okName():
            self.name = input("Event name was not formatted correctly. Please try again: ")

        self.date = input("Please enter the date for the event: ")

        while not self.okDate():
            self.date = input("Event date was not formatted correctly. Please try again: ")

        self.time = input("Please enter the time for the event: ")

        while not self.okTime():
            self.time = input("Event time was not formatted correctly. Please try again: ")

        self.type = input("Please enter the type of event (\"S\" for single occurrence, \"R\" for recurring, or \"F\" for fixed number of meetings): ")

        while not self.okType():
            self.type = input("Event type was not formatted correctly. Please try again: ")

        if self.type.lower() == "s":
            self.type = "single occurrence"
        elif self.type.lower() == "r":
            self.type = "recurring"
        else:
            self.type = "fixed number of meetings"

        return self

    def okDate(self):
        """Checks a date to ensure that it is formatted correctly.
        Arguments:
            date -- the date that is being tested
        Returns:
            True if the date is valid, False if invalid
        """
        allowed_characters = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "-"]

        if self.date:
            characters_ok = True
            for character in self.date:
                if character not in allowed_characters:
                    characters_ok = False
        else:
            characters_ok = False

        return characters_ok
   
    def okName(self):
        """Checks a name to ensure that it is formatted correctly.
        Arguments:
            name -- the name that is being tested
        Returns:
            True if the name is valid, False if invalid
        """
        if self.name.strip().isalpha():
            return True
        else:
            return False


    def okTime(self):
        """Checks a time to ensure that it is formatted correctly.
        Arguments:
            time -- the time that is being tested
        Returns:
            True if the time is valid, False if invalid
        """
        allowed_characters = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ":"]

        if self.time:
            characters_ok = True

            for character in self.time:
                if character not in allowed_characters:
                    characters_ok = False
        else:
            characters_ok = False

        return characters_ok

    def okType(self):
        """Checks an event type to ensure that it is formatted correctly.
        Arguments:
            type -- the type that is being tested
        Returns:
            True if the type is valid, False if invalid
        """
        if self.type.strip().lower() == "s" or self.type.strip().lower() == "r" or self.type.strip().lower() == "f":
            return True
        else:
            return False