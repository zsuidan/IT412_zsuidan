from classes.Calendar import Calendar
from classes.Event import Event


calendar_name = input("Please enter the calendar name: ")
calendar_owner = input("Please enter the calendar owner: ")

new_calendar = Calendar(calendar_name, calendar_owner)

change_event = input("\nWould you like to add or remove an event? (enter \"A\" to add, \"R\" to remove, any other input for neither): ")

if change_event.lower() == "a":
    new_event = Event.createEvent()

    new_calendar.addEvent(new_event)

    print("\n" + new_event.name + " added to calendar.")

    keep_adding = input("\nWould you like to add more events? (Y/N): ")
    
    while keep_adding.lower() == "y":
        new_event = Event.createEvent()

        new_calendar.addEvent(new_event)

        print(new_event.name + " added to calendar.")

        keep_adding = input("\nWould you like to add more events? (Y/N): ")

else:
    removed_event = input("What event would you like to remove?: ")

    new_calendar.removeEvent(removed_event)

    keep_removing = input("\nWould you like to remove more events? (Y/N): ")
    
    while keep_removing.lower() == "y":
        removed_event = input("\nWhat event would you like to remove?: ")

        new_calendar.removeEvent(removed_event)

        keep_removing = input("\nWould you like to remove more events? (Y/N): ")