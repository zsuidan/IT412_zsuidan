def get_id():
    """Obtains Employee ID information from the user
    Returns:
        returned_id -- the ID value entered by the user
    """

    returned_id = input("Enter your employee ID: ")
    return returned_id

def check_id(passed_id):
    """Checks a passed ID to see if it meets the required criteria of an ID
    
    Arguments:
        passed_id -- the ID of the user
    Returns:
        correct_id -- boolean value stating whether or not it is a valid ID
    """
    if len(passed_id) <= 7 and passed_id.isdigit():
        correct_id = True
    else: 
        correct_id = False
    
    return correct_id

def get_info(passed_info_name, passed_info_needed):
    """Obtain a piece of information from the user. Allows the field to be required or optional.
    Arguments: 
        passed_info_name --  label for the type of information being asked for
        passed_info_needed -- T/F, determines whether the user needs to enter a value or not
    Returns:
        returned_info -- returns the user input
    """

    if passed_info_needed:
        returned_info = input("Please enter your " + passed_info_name + ": ")
        while not returned_info:
            returned_info = input("Please enter your " + passed_info_name + ": ")
    else:
        returned_info = input("Please enter your " + passed_info_name + ". You may also leave this blank: ")

    return returned_info

def check_characters(passed_field_value, passed_banned_characters):
    """Checks to ensure that the value entered for a certain field was correct if the value exists. If blank, no check is necessary and it will return as True.
    Arguments: 
        passed_field_value -- any value 
        passed_banned_characters -- list of characters which CANNOT be present in the value
    Returns:
        correct_field -- boolean value stating whether or not it is free from banned characters
    """
    correct_field = True

    if passed_field_value:
        for character in passed_field_value:
            if character in passed_banned_characters:
                correct_field = False

    return correct_field

def add_another(passed_variable):
    """Asks user if they would like to continue adding more of a certain variable
    Arguments:
        passed_variable -- any variable
    Returns:
        True is returned if the user wishes to continue adding variables, False is returned if the user does not want to continue
    """

    add_more = input("Would you like to add another " + passed_variable + "? (Y/N): ")

    #Checks if Y or N was entered, prompting user to enter again if not
    correct_letter = False

    while not correct_letter:
        if add_more.upper() == "Y" or add_more.upper() == "N":
            correct_letter = True
        else:
            add_more = input("Invalid response. Answer with either Y or N: ")
    
    #Returns true if Y is entered and false is N is entered
    if add_more.upper() == "Y":
        return True
    elif add_more.upper() == "N":
        return False