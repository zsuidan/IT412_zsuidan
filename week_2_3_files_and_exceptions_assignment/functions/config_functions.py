import json
import os.path
import shutil
import time

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

def create_config():
    """Asks user to enter various configuration details.
    Returns: 
        new_config -- a dictionary contaning all of the new config information
    """

    #Prompts user to enter various configuration details
    print("\nBasic configuration options\n")
    safe_mode = input("Safe Mode: ")
    memory = input("Memory: ")
    error_log = input("Error Log Location: ")

    print("\nAdditional configuration options. If you would like an option removed, leave it blank.\n")
    allow_file_uploads = input("Allow File Uploads: ")
    use_caching = input("Use Caching: ")
    caching_file = input("Caching File Location: ")
    mail_host = input("Mail Host: ")

    #Creates a dictionary with all the configuration options entered by the user
    new_config = {'Safe Mode': safe_mode, 'Memory': memory, 'Error Log': error_log, 'Allow File Uploads': allow_file_uploads, 
    'Use Caching': use_caching, 'Caching File': caching_file, 'Mail Host': mail_host}

    #If any additional options were left blank, they are removed from the dictionary
    if not allow_file_uploads:
        new_config.pop('Allow File Uploads')
    if not use_caching:
        new_config.pop('Use Caching')
    if not caching_file:
        new_config.pop('Caching File')
    if not mail_host:
        new_config.pop('Mail Host')
    
    return new_config

def load_file(first_file, second_file):
    """Loads one of two json files depending on whether the first file exists or not.
    Arguments:
        first_file -- any json file
        second_file -- any other json file
    Returns:
        loaded_data -- data loaded from the file
    """
    try: 
        with open(first_file) as json_obj:
            loaded_data = json.load(json_obj)

    except:
        with open(second_file) as json_obj:
            loaded_data = json.load(json_obj)
    
    return loaded_data

def save_changes(data, file):
    """Asks a user if they would like to save data to a json file.
    Arguments:
        data -- the data being saved to the file
        file -- a json file
    """
    save_changes = input("\nWould you like to save your changes? (Y/N): ")

    #Checks if Y or N was entered, prompting user to enter again if not
    correct_letter = False

    while not correct_letter:
        if save_changes.upper() == "Y" or save_changes.upper() == "N":
            correct_letter = True
        else:
            save_changes = input("Invalid response. Answer with either Y or N: ")
    
    #Saves changes if Y is entered and discards them if N is entered. If changes are saved and the file exists already, creates a backup file.
    if save_changes.upper() == "Y":
        if os.path.isfile(file):
            shutil.copy2(file, file + ".backup" + str(time.time()))

        with open(file, 'w') as json_obj:
            json.dump(data, json_obj)
            print("Your changes have been saved.")
    else:
        print("Changes discarded.")