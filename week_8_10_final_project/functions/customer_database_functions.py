import json

def add_record(database):
    """Adds a new record to the database.
    Arguments:
        database -- the database the data will be added to
    """
    f_name = input("First name: ")

    while not validName(f_name):
        f_name = input("Invalid name. Please try again: ")

    l_name = input("Last name: ")

    while not validName(l_name):
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

    while (not primary_phone) or (not validPhone(primary_phone)):
        primary_phone = input("Invalid phone number. Please try again: ")

    secondary_phone = input("Secondary phone (optional): ")

    while not validPhone(secondary_phone):
        secondary_phone = input("Invalid phone number. Please try again: ")

    email_address = input("Email address (optional): ")

    while not validEmail(email_address):
        email_address = input("Invalid email. Please try again: ")

    f_name = fix_quotes(f_name)
    l_name = fix_quotes(l_name)
    company = fix_quotes(company)

    database.executeQuery("INSERT INTO mailings (name, company, address) VALUES ('" + f_name + " " + l_name + "','" + company + "','" + address + "')")

    database.executeQuery("INSERT INTO crm_data (f_name, l_name, address, city, state, zip, company, primary_phone, secondary_phone, email_address) VALUES ('" 
                        + f_name + "','" + l_name + "','" + address + "','" + city + "','" + state + "','" + zip + "','" + company + "','" + primary_phone + "','" 
                        + secondary_phone + "','" + email_address + "')")

    database.conn.commit()

def delete_record(database):
    """Removes the record specified by the user from the database.
    Arguments:
        database -- the database the record should be removed from
    """

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

def edit_record(database):
    """Allows the user to edit a record in the database.
    Arguments:
        database -- the database which is being edited
    """
    #Creates a list of all the valid IDs in the database
    id_list = []
    database_ids = database.executeSelectQuery("SELECT mail_id FROM mailings")
    for id in database_ids:
        id_list.append(str(id["mail_id"]))

    #Prompts user for which records they would like to edit and validates their input
    correct_id = False

    id_edited = input("\nPlease enter the ID of the record you would like to edit: ")

    while not correct_id:

        if id_edited in id_list:
            correct_id = True
        else:
            id_edited = input("Invalid ID. Please try again: ")

    #Prompts the user for which table they would like to make changes to
    table_viewed = input("1. mailings\n2. crm_data\n\nWhich table would you like to edit?: ")

    correct_input = False
    while not correct_input:

        if table_viewed.strip() == "1" or table_viewed.strip() == "2":
            correct_input = True
        else:
            table_viewed = input("Incorrect input. Please enter either \"1\" or \"2\": ")
    
    #Allows user to edit the mailings table
    if table_viewed == "1":
        #Shows user the record being edited
        print(database.executeSelectQuery("SELECT * FROM mailings where mail_id = " + id_edited))

        #Prompts user for which field they would like to edit
        field_edited = input("1. name\n2. company\n3. address\n4. Stop editing\n\nWhat would you like to edit?: ")

        correct_input = False

        while not correct_input:
            if field_edited == "1" or field_edited == "2" or field_edited == "3" or field_edited == "4":
                correct_input = True
            else:
                field_edited = input("Invalid input. Please enter a number between 1-4: ")

        while field_edited != "4":
            if field_edited == "1":
                field_changed = "name"
                new_info = input("Please enter the new name: ")

                while not validName(new_info):
                    new_info = input("Invalid name. Please try again: ")

            elif field_edited == "2":
                field_changed = "company"
                new_info = input("Please enter the new company: ")

            elif field_edited == "3":
                field_changed = "address"
                new_info = input("Please enter the new address: ")

                while not validAddress:
                    new_info = input("Invalid address. Please try again: ")

            #Escapes quote and backslash characters before executing the SQL statement
            new_info = fix_quotes(new_info)

            #Updates the database with the new information
            database.executeQuery("UPDATE mailings SET " + field_changed + " = '" + new_info + "' WHERE mail_id = " + id_edited)
            database.conn.commit()
            print("Record updated successfully.\n")

            #Prompts user for which field they would like to edit again
            print(database.executeSelectQuery("SELECT * FROM mailings where mail_id = " + id_edited))
            field_edited = input("1. name\n2. company\n3. address\n4. Stop editing\n\nWhat would you like to edit?: ")

            correct_input = False

            while not correct_input:
                if field_edited == "1" or field_edited == "2" or field_edited == "3" or field_edited == "4":
                    correct_input = True
                else:
                    field_edited = input("Invalid input. Please enter a number between 1-4: ")

    #Allows user to edit the crm_data table
    else:
        #Shows user the record being edited
        print(database.executeSelectQuery("SELECT * FROM crm_data where crm_id = " + id_edited))

        #Prompts user for which field they would like to edit
        field_edited = input("1. f_name\n2. l_name\n3. address\n4. city\n5. state\n6. zip\n7. company\n8. primary_phone\n9. secondary_phone\n10. email_address\n11. Stop editing" + 
                            "\n\nWhat would you like to edit?: ")

        ok_inputs = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11"]

        correct_input = False

        while not correct_input:
            if field_edited in ok_inputs:
                correct_input = True
            else:
                field_edited = input("Invalid input. Please enter a number between 1-11: ")

        while field_edited != "11":
            if field_edited == "1":
                field_changed = "f_name"
                new_info = input("Please enter the new first name: ")

                while not validName(new_info):
                    new_info = input("Invalid name. Please try again: ")
            elif field_edited == "2":
                field_changed = "l_name"
                new_info = input("Please enter the new last name: ")

                while not validName(new_info):
                    new_info = input("Invalid name. Please try again: ")

            elif field_edited == "3":
                field_changed = "address"
                new_info = input("Please enter the new address: ")

                while not validAddress(new_info):
                    new_info = input("Invalid address. Please try again: ")

            elif field_edited == "4":
                field_changed = "city"
                new_info = input("Please enter the new city: ")

                while not validCity(new_info):
                    new_info = input("Invalid city. Please try again: ")

            elif field_edited == "5":
                field_changed = "state"
                new_info = input("Please enter the new state: ").upper()

                while not validState(new_info):
                    new_info = input("Invalid state. Please try again: ").upper()

            elif field_edited == "6":
                field_changed = "zip"
                new_info = input("Please enter the new ZIP: ")

                while not validZIP(new_info):
                    new_info = input("Invalid ZIP. Please try again: ")

            elif field_edited == "7":
                field_changed = "company"
                new_info = input("Please enter the new company: ")

            elif field_edited == "8":
                field_changed = "primary_phone"
                new_info = input("Please enter the new primary phone: ")

                while (not new_info) or (not validPhone(new_info)):
                        new_info = input("Invalid phone number. Please try again: ")

            elif field_edited == "9":
                field_changed = "secondary_phone"
                new_info = input("Please enter the new secondary phone: ")

                while not validPhone(new_info):
                    new_info = input("Invalid phone number. Please try again: ")

            elif field_edited == "10":
                field_changed = "email_address"
                new_info = input("Please enter the new email address: ")

                while not validEmail(new_info):
                    new_info = input("Invalid email address. Please try again: ")
            
            #Escapes quote and backslash characters before executing the SQL statement
            new_info = fix_quotes(new_info)

            #Updates the database with the new information
            database.executeQuery("UPDATE crm_data SET " + field_changed + " = '" + new_info + "' WHERE crm_id = " + id_edited)
            database.conn.commit()
            print("Record updated successfully.\n")

            #Prompts user for which field they would like to edit again
            print(database.executeSelectQuery("SELECT * FROM crm_data where crm_id = " + id_edited))
            field_edited = input("1. f_name\n2. l_name\n3. address\n4. city\n5. state\n6. zip\n7. company\n8. primary_phone\n9. secondary_phone\n10. email_address\n11. Stop editing" + 
                                "\n\nWhat would you like to edit?: ")
            
            correct_input = False

            while not correct_input:
                if field_edited in ok_inputs:
                    correct_input = True
                else:
                    field_edited = input("Invalid input. Please enter a number between 1-11: ")

def fix_quotes(data):
    """Adds escape characters to data so quotes can be inserted/updated properly.
    Arguments:
        data -- the raw data being checked
    Returns:
        data -- data with quotes properly escaped
    """
    i = 0

    while i < len(data):
        
        if data[i] == "'" or data[i] == "\"" or data[i] == "\\":
            #Adds the escape character (\) before the character
            data = data[:i] + "\\" + data[i:]
            #Increments index an additional time since a new character was added
            i += 1
        print(data)
        i += 1

    return data

def import_database_file(file, database):
    """Opens a text file containing database information, then converts the file into json and csv format and uploads it to a database.
    Arguments:
        file -- the file being imported
        database -- the database which should be written to
    """
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

def validAddress(address):
    """Ensures an address is properly formatted.
    Arguments:
        address -- the address being validated
    Returns:
        address_ok -- boolean value which is either true if the address is valid or false if not
    """
    invalid_characters = ["!", "\"", "'", "@", "$", "%", "^", "&", "*", "_", "=", "+", "<", ">", "?", ";", "[", "]", "{", "}"]
    address_ok = True

    if address and not address.isspace():
        for character in address:
            if character in invalid_characters:
                address_ok = False
    else:
        address_ok = False

    return address_ok

def validCompany(company):
    company_ok = True

    return company_ok

def validCity(city):
    """Ensures a city is properly formatted.
    Arguments:
        city -- the city being validated
    Returns:
        city_ok -- boolean value which is either true if the city is valid or false if not
    """
    city_ok = True

    if city and not city.isspace():
        for character in city:
            if not (character.isalpha() or character == "'" or character == " "):
                city_ok = False
    else:
        city_ok = False

    return city_ok

def validEmail(email):
    """Ensures an email is properly formatted.
    Arguments:
        email -- the email being validated
    Returns:
        email_ok -- boolean value which is either true if the email is valid or false if not
    """
    invalid_characters = ["!", "\"", "'", "#", "$", "%", "^", "&", "*", "(", ")", "=", "+", ",", "<", ">", "/", "?", ";", ":", "[", "]", "{", "}", "\\", " "]

    email_ok = True

    for character in email:
        if character in invalid_characters:
            email_ok = False

    return email_ok

def validName(name):
    """Ensures a name is properly formatted.
    Arguments:
        name -- the name being validated
    Returns:
        name_ok -- boolean value which is either true if the name is valid or false if not
    """
    name_ok = True

    if name and not name.isspace():
        for character in name:
            if not (character.isalpha() or character == "'" or character == "-" or character == " "):
                name_ok = False
    else:
        name_ok = False
    
    return name_ok

def validPhone(phone):
    """Ensures a phone number is properly formatted.
    Arguments:
        phone -- the phone number being validated
    Returns:
        phone_ok -- boolean value which is either true if the phone number is valid or false if not
    """
    phone_ok = True

    for character in phone:
        if not (character.isnumeric() or character == "-"):
            phone_ok = False

    return phone_ok

def validState(state):
    """Ensures a state is properly formatted.
    Arguments:
        state -- the state being validated
    Returns:
        Either true if the city is valid or false if not
    """
    if state.isalpha() and len(state) == 2 and state.isupper():
        return True
    else:
        return False

def validZIP(zip):
    """Ensures a ZIP code is properly formatted.
    Arguments:
        zip -- the ZIP code being validated
    Returns:
        Either true if the ZIP is valid or false if not
    """
    if zip.isnumeric() and (len(zip) == 4 or len(zip) == 5):
        return True
    else:
        return False

def view_database(database):
    """Shows all data contained in a database.
    Arguments:
        database -- the database being viewed
    """
    table_viewed = input("1. mailings\n2. crm_data\n\nWhich table would you like to view?: ")

    correct_input = False
    while not correct_input:

        if table_viewed.strip() == "1" or table_viewed.strip() == "2":
            correct_input = True
        else:
            table_viewed = input("Incorrect input. Please enter either \"1\" or \"2\": ")
    
    if table_viewed == "1":
        viewed_data = database.executeSelectQuery("SELECT * FROM mailings")
    else:
        viewed_data = database.executeSelectQuery("SELECT * FROM crm_data")

    for entry in viewed_data:
        print(entry)