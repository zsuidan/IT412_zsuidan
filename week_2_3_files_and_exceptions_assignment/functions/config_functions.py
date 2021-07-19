def continue_task(passed_variable):
    """Asks user if they would like to continue with a certain task.
    Arguments:
        passed_variable -- any variable
    Returns:
        True is returned if the user wishes to continue, False is returned if the user does not want to continue.
    """

    add_more = input("Would you like to " + passed_variable + "? (Y/N): ")

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