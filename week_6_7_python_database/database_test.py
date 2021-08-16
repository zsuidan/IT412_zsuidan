from functions.car_database_functions import *

correct_input = False

task_performed = input("1. Show all vehicles\n2. Add a vehicle\n3. Edit a vehicle\n4. Remove a vehicle\n5. Exit program\n\nWhat would you like to do? (1-5): ")

while not correct_input:
    if task_performed == "1" or task_performed == "2" or task_performed == "3" or task_performed == "4" or task_performed == "5":
        correct_input = True
    else:
        task_performed = input("Invalid input. Please enter a number between 1-5: ")

while task_performed.strip() != "5":

    if task_performed.strip() == "1":

        showVehicles()
    
    elif task_performed.strip() == "2":

        addVehicle()

    elif task_performed.strip() == "3":

        updateVehicle()

    elif task_performed.strip() == "4":

        removeVehicle()

    correct_input = False

    task_performed = input("\n1. Show all vehicles\n2. Add a vehicle\n3. Edit a vehicle\n4. Remove a vehicle\n5. Exit program\n\nWhat would you like to do?: ")

    while not correct_input:
        if task_performed == "1" or task_performed == "2" or task_performed == "3" or task_performed == "4" or task_performed == "5":
            correct_input = True
        else:
            task_performed = input("Invalid input. Please enter a number between 1-5: ")