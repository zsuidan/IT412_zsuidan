from classes.Calendar import Calendar

#Asks user if they would like to make a Calendar or view one
create_calendar = input("Would you like to create a new calendar or view an existing one? (C/V): ")

#Validates user input is correct
correct_input = False

while not correct_input:
    if create_calendar.strip().lower() == "c" or create_calendar.strip().lower() == "v":
        correct_input = True
    else:
        create_calendar = input("Invalid response. Please try again: ")

#Begins Calendar creation process if C was entered
if create_calendar.strip().lower() == "c":
    #Asks user for Calendar information
    calendar_name = input("Please enter the calendar name: ")
    calendar_owner = input("Please enter the calendar owner: ")

    #Creates a Calendar using the user input
    new_calendar = Calendar(calendar_name, calendar_owner)

    #Gives user various options to add/remove/view events, save their calendar, or exit the application
    change_event = input("\nWhat would you like to do? (enter \"A\" to add events, \"R\" to remove events, \"V\" to view events, \"S\" to save changes, or any other input to exit): ")

    while change_event.strip().lower() == "a" or change_event.strip().lower() == "r" or change_event.strip().lower() == "v" or change_event.strip().lower() == "s":
        #If "a" was entered, the user will be prompted to create as many new events as they want 
        if change_event.strip().lower() == "a":
            new_calendar.addEvents()
          
        #If "r" was entered, the user will be prompted to remove as many existing events as they want 
        elif change_event.strip().lower() == "r":
            new_calendar.removeEvents()
        
        #If "v" was entered, the user will be given a list of added events 
        elif change_event.strip().lower() == "v":
            new_calendar.viewEvents()
           
        #If "s" was entered, the Calendar information will be saved to a text file 
        elif change_event.strip().lower() == "s":
            new_calendar.saveCalendar()

        #Gives the user the option prompt again
        change_event = input("\nWhat would you like to do? (enter \"A\" to add events, \"R\" to remove events, \"V\" to view events, \"S\" to save changes, or any other input to exit): ")

else:
    #Displays information for a previously created Calendar
    Calendar.openCalendar()