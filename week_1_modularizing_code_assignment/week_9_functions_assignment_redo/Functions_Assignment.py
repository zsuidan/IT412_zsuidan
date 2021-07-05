from functions.my_functions import *

program_running = True


#Creates an empty list to store dictionaries of employee information later
employee_info = []

#Creates a loop which has several prompts for users to fill in information
while program_running:

    #Obtains ID input from user and checks if it is valid, prompting them to input again if not
    employee_id = get_id()
    while not check_id(employee_id):
        employee_id = input("Employee ID was not properly formatted. Please try again: ")
  
    #Prompts user to enter their name
    employee_name = get_info("name", True)

    #Checks the name for banned characters, if any are detected the user will be asked to input until it is correct
    banned_name_characters = ["!", '"', "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "=", "+", ",", "<", ">", "/", "?", ";", ":", "[", "]", "{", "}", "\\"]

    while not check_characters(employee_name, banned_name_characters):
        employee_name = input("Employee name was not properly formatted. Please try again: ")

    #Prompts user to input an email
    employee_email = get_info("email", True)

    #Checks the email for banned characters, if any are detected the user will be asked to input until it is correct
    banned_email_characters = ["!", '"', "'", "#", "$", "%", "^", "&", "*", "(", ")", "=", "+", ",", "<", ">", "/", "?", ";", ":", "[", "]", "{", "}", "\\"]
    
    while not check_characters(employee_email, banned_email_characters):
        employee_email = input("Employee email was not properly formatted. Please try again: ")
        
    #Prompts user to enter an address or leave the address blank
    employee_address = get_info("address", False)

    #Checks if the address is properly formatted, prompting the user to input again if not
    banned_address_characters = ["!", '"', "'", "@", "$", "%", "^", "&", "*", "_", "=", "+", "<", ">", "?", ";", ":", "[", "]", "{", "}"]

    while not check_characters(employee_address, banned_address_characters):
        employee_address = input("Employee address was not properly formatted. Please try again: ")

    #Adds all inputs into the employee info list as a dictionary
    employee_info.append({'employee_id': employee_id, 'employee_name': employee_name, 'employee_email': employee_email, 'employee_address': employee_address})

    #If there are 5 employees, the loop ends, otherwise the user is asked if they would like to add more
    if len(employee_info) >= 5:
        print("You may only store 5 employees.")
        break
    else:
        continue_adding = add_another("employee")
        if not continue_adding:
            break
        
#Prints out each employee within the list on their own line 
for employee in employee_info:
    print(employee)