from functions.customer_database_functions import *
from classes.database_access import DB_Connect

#Connects to the database in python_projects
customer_database = DB_Connect('root', '', 'python_projects')

#Presents user with various options for managing the vehicle database and ensures they selected a valid option
correct_input = False

task_performed = input("1. Import a new data file\n2. Show data currently in a database\n3. Add a record to the databases\n4. Edit a record" 
                    + "\n5. Delete a record\n6. Quit the program\n\nWhat would you like to do? (1-6): ")

while not correct_input:
    if task_performed == "1" or task_performed == "2" or task_performed == "3" or task_performed == "4" or task_performed == "5" or task_performed == "6":
        correct_input = True
    else:
        task_performed = input("Invalid input. Please enter a number between 1-6: ")

#Allows user to continue making adjustments to the database until they enter the option to exit
while task_performed.strip() != "6":

    #If "1" is entered, allows the user to import a file containing data for a database
    if task_performed.strip() == "1":

        file_opened = input("Please enter the name of the file you would like to import: ")
        import_database_file(file_opened, customer_database)
    
    #If "2" is entered, allows the user to view a specified database table
    elif task_performed.strip() == "2":
        view_database(customer_database)

    #If "3" is entered, allows the user to add a new record to the database tables
    elif task_performed.strip() == "3":
        add_record(customer_database)

    #If "4" is entered, allows the user to edit an existing record in the database
    elif task_performed.strip() == "4":
        edit_record(customer_database)
    
    #If "5" is entered, allows the user to remove a specified record from the database tables
    elif task_performed.strip() == "5":
        delete_record(customer_database)

    #After the user performs their desired action, they are presented with the same options again
    correct_input = False

    task_performed = input("\n1. Import a new data file\n2. Show data currently in a database\n3. Add a record to the databases\n4. Edit a record" 
                        + "\n5. Delete a record\n6. Quit the program\n\nWhat would you like to do? (1-6): ")

    while not correct_input:
        if task_performed == "1" or task_performed == "2" or task_performed == "3" or task_performed == "4" or task_performed == "5" or task_performed == "6":
            correct_input = True
        else:
            task_performed = input("Invalid input. Please enter a number between 1-6: ")