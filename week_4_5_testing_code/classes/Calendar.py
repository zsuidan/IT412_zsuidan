from classes.Event import Event

import os.path
import shutil
import time


class Calendar():
    """A class which represents a calendar. Contains a calendar name, calendar owner, and a list of events."""

    def __init__(self, name, owner):
        """Constructor for the Calendar class"""
        self.name = name
        self.owner = owner
        self.events = []

    def addEvent(self, event):
        """Adds an event to the events list.
        Argument:
            event -- the event being added to the list
        """
        self.events.append(event)

    def addEvents(self):
        """Allows a user to add events to the calendar."""
        keep_adding = "y"
        
        while keep_adding.strip().lower() == "y":
            new_event = Event.createEvent()

            self.addEvent(new_event)

            print("\n" + new_event.name + " added to calendar.")

            keep_adding = input("\nWould you like to add more events? (Y/N): ")

            correct_letter = False

            while not correct_letter:
                if keep_adding.strip().lower() == "y" or keep_adding.strip().lower() == "n":
                    correct_letter = True
                else:
                    keep_adding = input("Invalid response. Please enter either \"Y\" or \"N\": ")

    def openCalendar():
        """Opens a text file for an existing calendar."""
        try:
            with open("text_files/calendar.txt") as file:
                for line in file:
                    print(line)
        except:
            print("Calendar does not exist.")

    def removeEvent(self, event):
        """Removes a specified event from the events list.
        Argument:
            event -- the event which should be removed
        """
        self.events.remove(event)

    def removeEvents(self):
        """Allows a user to remove events from the calendar."""
        keep_removing = "y"
        
        if len(self.events) == 0:
            print("No events remaining to remove.")

        while keep_removing.lower() == "y" and len(self.events) > 0:
            self.viewEvents()

            removed_event = input("\nWhich number event would you like to remove? (\"C\" to cancel): ")

            correct_input = False

            while not correct_input:
                if removed_event.isnumeric() and int(removed_event) < len(self.events) or removed_event.strip().lower() == "c":
                    correct_input = True
                else:
                    removed_event = input("Invalid response. Please try again: ")

            if removed_event.strip().lower() == "c":
                break
            else:
                self.events.pop(int(removed_event))

            print("\nEvent has been removed.")

            if len(self.events) > 0:
                keep_removing = input("\nWould you like to remove more events? (Y/N): ")

                correct_letter = False

                while not correct_letter:
                    if keep_removing.strip().lower() == "y" or keep_removing.strip().lower() == "n":
                        correct_letter = True
                    else:
                        keep_removing = input("Invalid response. Please enter either \"Y\" or \"N\": ")
            else:
                print("No events remaining to remove.")

    def saveCalendar(self):
        """Saves calendar information to a text file. If a calendar already exists, that one is backed up."""
        if os.path.isfile("text_files/calendar.txt"):
            shutil.copy2("text_files/calendar.txt", "text_files/calendar.txt.backup" + str(time.time()))

        try:
            with open("text_files/calendar.txt", "w") as file:
                file.write("Calendar Name: " + self.name)
                file.write("\nCalendar Owner: " + self.owner + "\nEvents: ")
                
                place_counter = 0

                while place_counter < len(self.events):
                    file.write("\nName: " + self.events[place_counter].name  + "\tDate: " + self.events[place_counter].date + "\tTime: " + self.events[place_counter].time + "\tType: " 
                    + self.events[place_counter].type)

                    place_counter += 1
                
                print("Calendar saved successfully.")
        except:
            print("File not found.")

    def viewEvents(self):
        """Prints out a list of the events and their details."""
        if len(self.events) == 0:
            print("No events added yet.")

        else:
            place_counter = 0

            while place_counter < len(self.events):
                print("Number: " + str(place_counter) + " Name: " + self.events[place_counter].name  + " Date: " + self.events[place_counter].date + " Time: " + self.events[place_counter].time + " Type: " 
                + self.events[place_counter].type)

                place_counter += 1