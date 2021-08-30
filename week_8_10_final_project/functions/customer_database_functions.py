import json

def import_json_file(file, database):

    #Opens the basic customer export text file
    try:
        with open("text_files/" + file + ".txt") as text_file:
            #Creates a customer data list and customer dictionary used later in a json file
            customer_data = []
            customer = {}

            #Opens a CSV file to write cleaned output to
            with open("text_files/customer_export.csv", "w") as csv_file:
            
                for line in text_file:
                    temp_line = line.split("|")
                    place_counter = 0
                    while place_counter < len(temp_line):
                        temp_line[place_counter] = temp_line[place_counter][2:-2]

                        
                        place_counter += 1

                    #Removes the extraneous information at the end of the text file lines
                    temp_line.pop(11)
                    temp_line.pop(11)

                    #Writes the line to a CSV file
                    csv_file.write(str(temp_line) + "\n")

                    #Creates a customer dictionary using the information from the line
                    customer = {'f_name': temp_line[0], 'l_name': temp_line[1], 'company': temp_line[2], 'address': temp_line[3], 'city': temp_line[4], 'county': temp_line[5],
                                'state': temp_line[6], 'zip': temp_line[7], 'primary_phone': temp_line[8], 'secondary_phone': temp_line[9], 'email_address': temp_line[10]}

                    #Adds the customer dictionary to the customer data list
                    customer_data.append(customer)

        #Opens a json file to write customer data to
   
        with open("text_files/customer_export.json", "w") as json_file:
            #Removes labels that were in the text file which are no longer needed
            customer_data.pop(0)

            #Dumps customer data list to the json file
            json.dump(customer_data, json_file, indent=1)

        #Uploads the data to the database using the created json file
    
        with open("text_files/customer_export.json") as json_file:
            #Clears the current data from the database
            database.executeQuery("TRUNCATE TABLE `mailings`")
            database.executeQuery("TRUNCATE TABLE `crm_data`")

            #Adds the customers to the mailing database using the information from the customer_export json file
            customer_info = json.load(json_file)

            for customer in customer_info:
                database.executeQuery("INSERT INTO mailings (name, company, address) VALUES ('" + customer["f_name"] + " " + customer["l_name"] + "','" + customer["company"] 
                                                + "','" + customer["address"] + "')")

                database.executeQuery("INSERT INTO crm_data (f_name, l_name, address, city, state, zip, company, primary_phone, secondary_phone, email_address) VALUES ('" 
                                    + customer["f_name"] + "','" + customer["l_name"] + "','" + customer["address"] + "','" + customer["city"] + "','" + customer["state"] + "','" 
                                    + customer["zip"] + "','" + customer["company"] + "','" + customer["primary_phone"] + "','" + customer["secondary_phone"] + "','" 
                                    + customer["email_address"] + "')")

                database.conn.commit()

        print("File imported successfully.")

    except:
        print("File not found.")

def view_database(database):
    database_viewed = input("1. mailings\n2. crm_data\n\nWhich database would you like to view?: ")

    correct_input = False
    while not correct_input:

        if database_viewed.strip() == "1" or database_viewed.strip() == "2":
            correct_input = True
        else:
            database_viewed = input("Incorrect input. Please enter either \"1\" or \"2\": ")
    
    if database_viewed == "1":
        viewed_data = database.executeSelectQuery("SELECT * FROM mailings")
    else:
        viewed_data = database.executeSelectQuery("SELECT * FROM crm_data")

    for entry in viewed_data:
        print(entry)

def add_record(database):
    f_name = input("First name: ")

    while not validName(f_name):
        f_name = input("Invalid name. Please try again: ")

    l_name = input("Last name: ")

    while not validName(f_name):
        l_name = input("Invalid name. Please try again: ")

    address = input("Address: ")

    while not validAddress(address):
        address = input ("Invalid address. Please try again: ")

    city = input("City: ")

    while not validCity(city):
        city = input("Invalid city. Please try again: ")

    state = input("State: ").upper()

    while not validState(state):
        state = input("Invalid state. Please try again: ").upper()

    zip = input("ZIP: ")

    while not validZIP(zip):
        zip = input("Invalid ZIP code. Please try again: ")

    company = input("Company (optional): ")

    primary_phone = input("Primary phone: ")

    while not primary_phone or validPhone(primary_phone):
        primary_phone = input("Invalid phone number. Please try again: ")

    secondary_phone = input("Secondary phone (optional): ")

    while not validPhone(secondary_phone):
        secondary_phone = input("Invalid phone number. Please try again: ")

    email_address = input("Email address (optional): ")

    while not validEmail(email_address):
        email_address = input("Invalid email. Please try again: ")

    database.executeQuery("INSERT INTO mailings (name, company, address) VALUES ('" + f_name + " " + l_name + "','" + company + "','" + address + "')")

    database.executeQuery("INSERT INTO crm_data (f_name, l_name, address, city, state, zip, company, primary_phone, secondary_phone, email_address) VALUES ('" 
                        + f_name + "','" + l_name + "','" + address + "','" + city + "','" + state + "','" + zip + "','" + company + "','" + primary_phone + "','" 
                        + secondary_phone + "','" + email_address + "')")

    database.conn.commit()

def delete_record(database):
    """Removes the record specified by the user from the databases"""

    #Creates a list of all the valid IDs in the database
    id_list = []
    database_ids = database.executeSelectQuery("SELECT mail_id FROM mailings")
    for id in database_ids:
        id_list.append(str(id["mail_id"]))

    #Prompts user for which records they would like to remove and validates their input
    correct_id = False

    id_deleted = input("\nPlease enter the ID of the record you would like to remove (both databases will be affected): ")

    while not correct_id:

        if id_deleted in id_list:
            correct_id = True
        else:
            id_deleted = input("Invalid ID. Please try again: ")

    correct_input = False

    #Ensures the user wants to delete the specified vehicle by giving them a confirmation prompt
    confirm_delete = input("Are you sure you would like to delete record " + id_deleted + "? (Y/N): ")

    while not correct_input:
        if confirm_delete.lower() == "y" or confirm_delete.lower() == "n":
            correct_input = True
        else:
            confirm_delete = input("Invalid input. Please enter either Y or N: ")

    #Either deletes the vehicle or cancels the deletion depending on user confirmation
    if confirm_delete.lower().strip() == "y":
        database.executeQuery("DELETE FROM mailings WHERE mail_id = " + id_deleted)
        database.executeQuery("DELETE FROM crm_data WHERE crm_id = " + id_deleted)

        database.conn.commit()

        print("Record deleted successfully")
    else:
        print("Record deletion cancelled")

def validName(name):
    name_ok = True

    if name and not name.isspace():
        for character in name:
            if not (character.isalpha() or character == "'" or character == "-" or character == " "):
                name_ok = False
    else:
        name_ok = False
    
    return name_ok

def validAddress(address):
    invalid_characters = ["!", "\"", "'", "@", "$", "%", "^", "&", "*", "_", "=", "+", "<", ">", "?", ";", "[", "]", "{", "}"]
    address_ok = True

    if address and not address.isspace():
        for character in address:
            if character in invalid_characters:
                address_ok = False
    else:
        address_ok = False

    return address_ok

def validCity(city):
    city_ok = True

    if city and not city.isspace():
        for character in city:
            if not (character.isalpha() or character == "'" or character == " "):
                city_ok = False
    else:
        city_ok = False

    return city_ok

def validState(state):
    if state.isalpha() and len(state) == 2 and state.isupper():
        return True
    else:
        return False

def validZIP(zip):
    if zip.isnumeric() and (len(zip) == 4 or len(zip) == 5):
        return True
    else:
        return False

def validPhone(phone):
    phone_ok = True

    for character in phone:
        if not (character.isnumeric() or character == "-"):
            phone_ok = False

    return phone_ok

def validEmail(email):
    invalid_characters = ["!", "\"", "'", "#", "$", "%", "^", "&", "*", "(", ")", "=", "+", ",", "<", ">", "/", "?", ";", ":", "[", "]", "{", "}", "\\", " "]

    email_ok = True

    for character in email:
        if character in invalid_characters:
            email_ok = False

    return email_ok