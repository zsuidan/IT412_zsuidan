from functions.customer_database_functions import *
from classes.database_access import DB_Connect

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

    if task_performed.strip() == "1":

        file_opened = input("Please enter the name of the file you would like to import: ")
        import_json_file(file_opened, customer_database)
    
    elif task_performed.strip() == "2":
        view_database(customer_database)

    elif task_performed.strip() == "3":
        add_record(customer_database)

    #elif task_performed.strip() == "4":
        #edit_record()
    
    elif task_performed.strip() == "5":
        delete_record(customer_database)

    correct_input = False

    task_performed = input("\n1. Import a new data file\n2. Show data currently in a database\n3. Add a record to the databases\n4. Edit a record" 
                        + "\n5. Delete a record\n6. Quit the program\n\nWhat would you like to do? (1-6): ")

    while not correct_input:
        if task_performed == "1" or task_performed == "2" or task_performed == "3" or task_performed == "4" or task_performed == "5" or task_performed == "6":
            correct_input = True
        else:
            task_performed = input("Invalid input. Please enter a number between 1-6: ")