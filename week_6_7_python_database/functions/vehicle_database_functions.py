from classes.database_access import DB_Connect

vehicle_db = DB_Connect('root', '', 'python_projects')

def addVehicle():
    """Adds a vehicle to the database using several user inputs."""
    #Gathers inputs from user and validates them if necessary
    vehicle_make = input("Please enter the vehicle make: ")

    while not validMake(vehicle_make):
        vehicle_make = input("Invalid vehicle make. Please try again: ")

    
    vehicle_model = input("Please enter the vehicle model: ")

    while not validModel(vehicle_model):
        vehicle_model = input("Invalid vehicle model. Please try again: ")


    vehicle_id_number = input("Please enter the vehicle VIN: ")

    while not validVIN(vehicle_id_number):
        vehicle_id_number = input("Invalid vehicle VIN. Please try again: ")


    person_purchased_from = input("Please enter the person the vehicle was purchased from (optional): ")

    while not validPerson(person_purchased_from):
        person_purchased_from = input("Invalid name. Please try again: ")


    price_paid = input("Please enter the price paid for the vehicle (optional): ")

    while not validPricePaid(price_paid):
        price_paid = input("Invalid price. Please try again: ")


    sales_price = input("Please enter the sales price: ")

    while not validSalesPrice(sales_price):
        sales_price = input("Invalid price. Please try again: ")


    vehicle_description = input("Please enter a vehicle description: ")

    #Inserts the entereed vehicle information into the database
    vehicle_db.executeQuery("INSERT INTO vehicles (vehicle_make, vehicle_model, vehicle_id_number, person_purchased_from, price_paid, sales_price, vehicle_description)" 
                    + " VALUES ('" + vehicle_make + "','" + vehicle_model + "','" + vehicle_id_number + "','" + person_purchased_from + "','" + price_paid + "','" + sales_price 
                                + "','" + vehicle_description + "');")

    #Sometimes you must add COMMIT; after the statement
    vehicle_db.conn.commit()

    #Notifies user the vehicle was added
    print("Vehicle added successfully")


def removeVehicle():
    """Removes the vehicle specified by the user from the database"""
    #Shows all vehicles in the database to the user
    showVehicles()

    #Creates a list of all the valid indexes in the database
    index_list = []
    database_indexes = vehicle_db.executeSelectQuery("SELECT index_id FROM vehicles")
    for index in database_indexes:
        index_list.append(str(index["index_id"]))

    #Prompts user for which vehicle they would like to remove and validates their input
    correct_index = False

    index_deleted = input("\nPlease enter the index of the vehicle you would like to remove: ")

    while not correct_index:

        if index_deleted in index_list:
            correct_index = True
        else:
            index_deleted = input("Invalid index. Please try again: ")

    correct_input = False

    #Ensures the user wants to delete the specified vehicle by giving them a confirmation prompt
    confirm_delete = input("Are you sure you would like to delete vehicle " + index_deleted + "? (Y/N): ")

    while not correct_input:
        if confirm_delete.lower() == "y" or confirm_delete.lower() == "n":
            correct_input = True
        else:
            confirm_delete = input("Invalid input. Please enter either Y or N: ")

    #Either deletes the vehicle or cancels the deletion depending on user confirmation
    if confirm_delete.lower().strip() == "y":
        vehicle_db.executeQuery("DELETE FROM vehicles WHERE index_id = " + index_deleted)
        vehicle_db.conn.commit()

        print("Vehicle deleted successfully")
    else:
        print("Vehicle deletion cancelled")


def showVehicles():
    """Prints out details for all vehicles contained in the database."""
    car_list = vehicle_db.executeSelectQuery("SELECT * FROM vehicles")

    for record in car_list:
        print("Index ID: " + str(record["index_id"]) + "\tVehicle Make: " + str(record["vehicle_make"]) + "\tVehicle Model: " + str(record["vehicle_model"]) 
            + "\tVIN: " + str(record["vehicle_id_number"]) + "\tPurchased From: " + str(record["person_purchased_from"]) + "\tPrice Paid: " + str(record["price_paid"]) 
            + "\tSales Price: " + str(record["sales_price"]) + "\tDescription: " + str(record["vehicle_description"]))


def updateVehicle():
    """Allows a user to make changes to an existing vehicle."""
    #Shows all vehicles in the database to the user
    showVehicles()

    #Creates a list of all the valid indexes in the database
    index_list = []
    database_indexes = vehicle_db.executeSelectQuery("SELECT index_id FROM vehicles")
    for index in database_indexes:
        index_list.append(str(index["index_id"]))

    #Prompts user for which vehicle they would like to update and validates their input
    correct_index = False

    index_updated = input("\nPlease enter the index of the vehicle you would like to update: ")

    while not correct_index:

        if index_updated in index_list:
            correct_index = True
        else:
            index_updated = input("Invalid index. Please try again: ")

    keep_updating = "y"

    #Allows user to repeatedly modify specific fields of the selected vehicle until they choose to stop
    while keep_updating.lower() == "y":
        #Prompts user for the field they would like to change
        correct_input = False

        field_updated = input("\n1. Vehicle Make\n2. Vehicle Model\n3. VIN\n4. Purchased From\n5. Price Paid\n6. Sales Price\n7. Description\n\nWhich field would you like to update?: ")

        while not correct_input:
            if field_updated == "1" or field_updated == "2" or field_updated == "3" or field_updated == "4" or field_updated == "5" or field_updated == "6" or field_updated == "7":
                correct_input = True
            else:
                field_updated = input("Invalid field. Please enter a number from 1-7: ") 

        #Prompts user to enter new information for the field and edits the selected field
        if field_updated == "1":
            new_info = input("Please enter the vehicle make: ")

            while not validMake(new_info):
                new_info = input("Invalid vehicle make. Please try again: ")

            vehicle_db.executeQuery("UPDATE vehicles SET vehicle_make='" + new_info + "' WHERE index_id = '" + index_updated + "'")

        elif field_updated == "2":
            new_info = input("Please enter the vehicle model: ")

            while not validModel(new_info):
                new_info = input("Invalid vehicle model. Please try again: ")

            vehicle_db.executeQuery("UPDATE vehicles SET vehicle_model='" + new_info + "' WHERE index_id = '" + index_updated + "'")

        elif field_updated == "3":
            new_info = input("Please enter the vehicle VIN: ")

            while not validVIN(new_info):
                new_info = input("Invalid vehicle VIN. Please try again: ")

            vehicle_db.executeQuery("UPDATE vehicles SET vehicle_id_number ='" + new_info + "' WHERE index_id = '" + index_updated + "'")

        elif field_updated == "4":
            new_info = input("Please enter the person the vehicle was purchased from (optional): ")

            while not validPerson(new_info):
                new_info = input("Invalid name. Please try again: ")

            vehicle_db.executeQuery("UPDATE vehicles SET person_purchased_from='" + new_info + "' WHERE index_id = '" + index_updated + "'")

        elif field_updated == "5":
            new_info = input("Please enter the price paid for the vehicle (optional): ")

            while not validPricePaid(new_info):
                new_info = input("Invalid price. Please try again: ")

            vehicle_db.executeQuery("UPDATE vehicles SET price_paid='" + new_info + "' WHERE index_id = '" + index_updated + "'")

        elif field_updated == "6":
            new_info = input("Please enter the sales price: ")

            while not validSalesPrice(new_info):
                new_info = input("Invalid price. Please try again: ")

            vehicle_db.executeQuery("UPDATE vehicles SET sales_price='" + new_info + "' WHERE index_id = '" + index_updated + "'")

        elif field_updated == "7":
            new_info = input("Please enter a vehicle description: ")
            vehicle_db.executeQuery("UPDATE vehicles SET vehicle_description='" + new_info + "' WHERE index_id = '" + index_updated + "'")

        vehicle_db.conn.commit()

        print("Update successful")

        #Asks user if they would like to continue making updates
        correct_input = False

        keep_updating = input("Would you like to continue updating? (Y/N): ")

        while not correct_input:
            if keep_updating.lower() == "y" or keep_updating.lower() == "n":
                correct_input = True
            else:
                keep_updating = input("Invalid response. Please enter either Y or N: ")


def validMake(vehicle_make):
    """Verifies a vehicle make is formatted correctly.
    Arguments:
        vehicle_make -- the vehicle make being validated
    Returns:
        Either True or False depending on if it passes validation"""

    if vehicle_make.isalpha():
        return True
    else:
        return False


def validModel(vehicle_model):
    """Verifies a vehicle model is formatted correctly.
    Arguments:
        vehicle_model -- the vehicle model being validated
    Returns:
        ok_model -- True or False depending on if it passes validation"""

    ok_model = True

    banned_characters = ["!", "\"", "@", "#", "$", "%", "^", "*", "(", ")", "_", "=", "+", ",", "<", ">", "/", "?", ";", ":", "[", "]", "{", "}", "?", "~", "|", "."]

    if not vehicle_model:
        ok_model = False
    else:
        for character in vehicle_model:
            if character in banned_characters:
                ok_model = False

    return ok_model


def validPerson(person_purchased_from):
    """Verifies a person's name is formatted correctly.
    Arguments:
        person_purchased_from -- the name being validated
    Returns:
        ok_person -- True or False depending on if it passes validation"""

    ok_person = True

    allowed_characters = [" ", ",", ".", "'", "-"]

    for character in person_purchased_from:
        if not character.isalpha() and character not in allowed_characters:
            ok_person = False

    return ok_person


def validPricePaid(price_paid):
    """Verifies a price paid is formatted correctly.
    Arguments:
        price_paid -- the price paid being validated
    Returns:
        ok_price -- True or False depending on if it passes validation"""

    ok_price = True

    if price_paid:
        try:
            is_float = isinstance(float(price_paid), float)
        
            if not is_float:
                ok_price = False
        except:
            ok_price = False

    return ok_price


def validSalesPrice(sales_price):
    """Verifies a sales price is formatted correctly.
    Arguments:
        sales_price -- the sales price being validated
    Returns:
        ok_sales_price -- True or False depending on if it passes validation"""

    ok_sale_price = True

    if sales_price:
        try:
            is_float = isinstance(float(sales_price), float)

            if not is_float:
                ok_sale_price = False
        except:
            ok_sale_price = False

    else:
        ok_sale_price = False           

    return ok_sale_price


def validVIN(vehicle_id_number):
    """Verifies a vehicle VIN is formatted correctly.
    Arguments:
        vehicle_id_number -- the VIN being validated
    Returns:
        Either True or False depending on if it passes validation"""

    if vehicle_id_number and vehicle_id_number.isalnum():
        return True
    else:
        return False