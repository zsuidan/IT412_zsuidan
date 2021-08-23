import json
from classes.database_access import DB_Connect

customer_database = DB_Connect('root', '', 'python_projects')

def import_json_file(file):
    with open("text_files/" + file + ".json") as json_file:
        #Clears the current data from the database
        customer_database.executeQuery("TRUNCATE TABLE `mailings`")
        customer_database.executeQuery("TRUNCATE TABLE `crm_data`")

        #Adds the customers to the mailing database using the information from the customer_export json file
        customer_info = json.load(json_file)

        for customer in customer_info:
            customer_database.executeQuery("INSERT INTO mailings (name, company, address) VALUES ('" + customer["f_name"] + " " + customer["l_name"] + "','" + customer["company"] 
                                            + "','" + customer["address"] + "')")

            customer_database.executeQuery("INSERT INTO crm_data (f_name, l_name, address, city, state, zip, company, primary_phone, secondary_phone, email_address) VALUES ('" 
                                + customer["f_name"] + "','" + customer["l_name"] + "','" + customer["address"] + "','" + customer["city"] + "','" + customer["state"] + "','" 
                                + customer["zip"] + "','" + customer["company"] + "','" + customer["primary_phone"] + "','" + customer["secondary_phone"] + "','" 
                                + customer["email_address"] + "')")

            customer_database.conn.commit()

def view_database():
    database_viewed = input("1. mailings\n2. crm_data\n\nWhich database would you like to view?: ")

    correct_input = False
    while not correct_input:

        if database_viewed.strip() == "1" or database_viewed.strip() == "2":
            correct_input = True
        else:
            database_viewed = input("Incorrect input. Please enter either \"1\" or \"2\": ")
    
    if database_viewed == "1":
        viewed_data = customer_database.executeSelectQuery("SELECT * FROM mailings")
    else:
        viewed_data = customer_database.executeSelectQuery("SELECT * FROM crm_data")

    for entry in viewed_data:
        print(entry)

def add_record():
    f_name = input("First name: ")
    l_name = input("Last name: ")
    address = input("Address: ")
    city = input("City: ")
    state = input("State: ")
    zip = input("ZIP: ")
    company = input("Company (optional): ")
    primary_phone = input("Primary phone: ")
    secondary_phone = input("Secondary phone (optional): ")
    email_address = input("Email address (optional): ")

    customer_database.executeQuery("INSERT INTO mailings (name, company, address) VALUES ('" + f_name + " " + l_name + "','" + company + "','" + address + "')")

    customer_database.executeQuery("INSERT INTO crm_data (f_name, l_name, address, city, state, zip, company, primary_phone, secondary_phone, email_address) VALUES ('" 
                        + f_name + "','" + l_name + "','" + address + "','" + city + "','" + state + "','" + zip + "','" + company + "','" + primary_phone + "','" 
                        + secondary_phone + "','" + email_address + "')")

    customer_database.conn.commit()

def delete_record():
    """Removes the record specified by the user from the databases"""

    #Creates a list of all the valid IDs in the database
    id_list = []
    database_ids = customer_database.executeSelectQuery("SELECT mail_id FROM mailings")
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
        customer_database.executeQuery("DELETE FROM mailings WHERE mail_id = " + id_deleted)
        customer_database.executeQuery("DELETE FROM crm_data WHERE crm_id = " + id_deleted)

        customer_database.conn.commit()

        print("Record deleted successfully")
    else:
        print("Record deletion cancelled")