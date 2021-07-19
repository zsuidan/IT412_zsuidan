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
    create_backup("text_files/config_override.json")

    #Prompts user to enter various configuration information. After all information is entered, writes entered information to config_override.json.
    new_config = create_config()

    save_changes(new_config, "text_files/config_override.json")