import json
import os.path
import shutil
import time
from functions.config_functions import *

#If the user created a new config, that config is displayed. If the user has not created their own config, the basic config is displayed.

config_data = load_file("text_files/config_override.json", "text_files/basic_config.json")

print("Safe Mode - " + config_data['Safe Mode'])
print("Memory - " + config_data['Memory'])
print("Error Log - " + config_data['Error Log'])

#Prompts user asking them whether they want to make changes to the configuration or not.
modify_config = continue_task("modify or add items to the configuration")

if modify_config:
    #If the user has already created a config_override file previously, that config is backed up with a timestamp.
    if os.path.isfile("text_files/config_override.json"):
        shutil.copy2("text_files/config_override.json", "text_files/config_override.json.backup" + str(time.time()))

    #Prompts user to enter various configuration information. After all information is entered, writes entered information to config_override.json.
    with open("text_files/config_override.json", 'w') as json_obj:
        print("\nModifications to basic configuration\n")
        safe_mode = input("Safe Mode: ")
        memory = input("Memory: ")
        error_log = input("Error Log Location: ")

        print("\nAdditional configuration options. If you would like an option removed, leave it blank.\n")
        allow_file_uploads = input("Allow File Uploads: ")
        use_caching = input("Use Caching: ")
        caching_file = input("Caching File Location: ")
        mail_host = input("Mail Host: ")

        new_config = {'Safe Mode': safe_mode, 'Memory': memory, 'Error Log': error_log, 'Allow File Uploads': allow_file_uploads, 
        'Use Caching': use_caching, 'Caching File': caching_file, 'Mail Host': mail_host}

        if not allow_file_uploads:
            new_config.pop('Allow File Uploads')
        if not use_caching:
            new_config.pop('Use Caching')
        if not caching_file:
            new_config.pop('Caching File')
        if not mail_host:
            new_config.pop('Mail Host')

        save_changes = continue_task("save your changes")

        if save_changes:
            json.dump(new_config, json_obj)
            print("Your changes have been saved.")
        else:
            print("Changes discarded.")