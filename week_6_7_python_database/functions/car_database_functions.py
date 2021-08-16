from classes.database_access import DB_Connect

vehicle_db = DB_Connect('root', '', 'python_projects')

def addVehicle():
    #Sometimes you must add COMMIT; after the statement
    vehicle_make = validateMake()
    
    vehicle_model = validateModel()

    vehicle_id_number = validateVIN()

    person_purchased_from = validatePerson()

    price_paid = validatePricePaid()

    sales_price = validateSalesPrice()

    vehicle_description = input("Please enter a vehicle description: ")

    vehicle_db.executeQuery("INSERT INTO vehicles (vehicle_make, vehicle_model, vehicle_id_number, person_purchased_from, price_paid, sales_price, vehicle_description)" 
                    + " VALUES ('" + vehicle_make + "','" + vehicle_model + "','" + vehicle_id_number + "','" + person_purchased_from + "','" + price_paid + "','" + sales_price 
                                + "','" + vehicle_description + "');")

    vehicle_db.conn.commit()

    print("Vehicle added successfully")


def removeVehicle():
    showVehicles()

    car_deleted = input("\nPlease enter the index of the vehicle you would like to remove: ")

    confirm_delete = input("Are you sure you would like to delete vehicle " + car_deleted + "? (Y/N): ")

    if confirm_delete.lower().strip() == "y":
        vehicle_db.executeQuery("DELETE FROM vehicles WHERE index_id = '" + car_deleted + "'")

        print("Vehicle deleted successfully")
    else:
        print("Vehicle deletion cancelled")


def showVehicles():
    car_list = vehicle_db.executeSelectQuery("SELECT * FROM vehicles")

    for record in car_list:
        print("Index ID: " + str(record["index_id"]) + "\tVehicle Make: " + str(record["vehicle_make"]) + "\tVehicle Model: " + str(record["vehicle_model"]) 
            + "\tVIN: " + str(record["vehicle_id_number"]) + "\tPurchased From: " + str(record["person_purchased_from"]) + "\tPrice Paid: " + str(record["price_paid"]) 
            + "\tSales Price: " + str(record["sales_price"]) + "\tDescription: " + str(record["vehicle_description"]))


def updateVehicle():
    showVehicles()

    index_list = []
    database_indexes = vehicle_db.executeSelectQuery("SELECT index_id FROM vehicles")
    for index in database_indexes:
        index_list.append(str(index["index_id"]))

    correct_index = False

    index_updated = input("\nPlease enter the index of the vehicle you would like to update: ")

    while not correct_index:

        if index_updated in index_list:
            correct_index = True
        else:
            index_updated = input("Invalid index. Please try again: ")

    keep_updating = "y"

    while keep_updating.lower() == "y":
        correct_input = False

        field_updated = input("\n1. Vehicle Make\n2. Vehicle Model\n3. VIN\n4. Purchased From\n5. Price Paid\n6. Sales Price\n7. Description\n\nWhich field would you like to update?: ")

        while not correct_input:
            if field_updated == "1" or field_updated == "2" or field_updated == "3" or field_updated == "4" or field_updated == "5" or field_updated == "6" or field_updated == "7":
                correct_input = True
            else:
                field_updated = input("Invalid field. Please enter a number from 1-7: ") 

        if field_updated == "1":
            new_info = validateMake()
            vehicle_db.executeQuery("UPDATE vehicles SET vehicle_make='" + new_info + "' WHERE index_id = '" + index_updated + "'")
        elif field_updated == "2":
            new_info = validateModel()
            vehicle_db.executeQuery("UPDATE vehicles SET vehicle_model='" + new_info + "' WHERE index_id = '" + index_updated + "'")
        elif field_updated == "3":
            new_info = validateVIN()
            vehicle_db.executeQuery("UPDATE vehicles SET vehicle_id_number ='" + new_info + "' WHERE index_id = '" + index_updated + "'")
        elif field_updated == "4":
            new_info = validatePerson()
            vehicle_db.executeQuery("UPDATE vehicles SET person_purchased_from='" + new_info + "' WHERE index_id = '" + index_updated + "'")
        elif field_updated == "5":
            new_info = validatePricePaid()
            vehicle_db.executeQuery("UPDATE vehicles SET price_paid='" + new_info + "' WHERE index_id = '" + index_updated + "'")
        elif field_updated == "6":
            new_info = validateSalesPrice()
            vehicle_db.executeQuery("UPDATE vehicles SET sales_price='" + new_info + "' WHERE index_id = '" + index_updated + "'")
        elif field_updated == "7":
            new_info = input("Please enter a vehicle description: ")
            vehicle_db.executeQuery("UPDATE vehicles SET vehicle_description='" + new_info + "' WHERE index_id = '" + index_updated + "'")

        vehicle_db.conn.commit()

        print("Update successful")

        correct_input = False

        keep_updating = input("Would you like to continue updating? (Y/N): ")

        while not correct_input:
            if keep_updating.lower() == "y" or keep_updating.lower() == "n":
                correct_input = True
            else:
                keep_updating = input("Invalid response. Please enter either Y or N: ")


def validateMake():
    vehicle_make = input("Please enter the vehicle make: ")

    correct_input = False

    while not correct_input:
        if vehicle_make and vehicle_make.isalpha():
            correct_input = True
        else:
            vehicle_make = input("Invalid vehicle make. Please use letters only: ")

    return vehicle_make


def validateModel():
    vehicle_model = input("Please enter the vehicle model: ")

    correct_input = False

    banned_characters = ["!", "\"", "@", "#", "$", "%", "^", "*", "(", ")", "_", "=", "+", ",", "<", ">", "/", "?", ";", ":", "[", "]", "{", "}", "?", "~", "|", "."]

    while not correct_input:
        correct_input = True

        if not vehicle_model:
            correct_input = False
            vehicle_model = input("Invalid vehicle model. Please try again: ")
        else:
            for character in vehicle_model:
                if character in banned_characters:
                    correct_input = False
                    vehicle_model = input("Invalid vehicle model. Please try again: ")
                    

    return vehicle_model


def validateVIN():
    vehicle_id_number = input("Please enter the vehicle VIN: ")

    correct_input = False

    while not correct_input:
        if vehicle_id_number and vehicle_id_number.isalnum():
            correct_input = True
        else:
            vehicle_id_number = input("Invalid VIN. Please try again: ")

    return vehicle_id_number


def validatePerson():
    person_purchased_from = input("Please enter who the vehicle was purchased from (optional): ")

    allowed_characters = [" ", ",", ".", "'", "-"]

    correct_input = False

    while not correct_input:
        correct_input = True

        for character in person_purchased_from:
            if not character.isalpha and character not in allowed_characters:
                correct_input = False
                person_purchased_from = input("Invalid name. Please try again: ")

    return person_purchased_from


def validatePricePaid():
    price_paid = input("How much did you pay for the vehicle?: ")

    correct_input = False

    while price_paid and not correct_input:

        is_float = isinstance(float(price_paid), float)
        
        if is_float:
            correct_input = True
        else:
            price_paid = input("Invalid price. Please try again: ")

    return price_paid


def validateSalesPrice():
    sales_price = input("How much did you pay for the vehicle?: ")

    correct_input = False

    while not correct_input:

        if sales_price:
            try:
                is_float = isinstance(float(sales_price), float)
                correct_input = is_float
            except:
                sales_price = input("Invalid price. Please try again: ")

        else:
            sales_price = input("Invalid price. Please try again: ")

    return sales_price