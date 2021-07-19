from functions.config_functions import *

#If the user created a new config, that config is displayed. If the user has not created their own config, the basic config is displayed.

config_data = load_file("text_files/config_override.json", "text_files/basic_config.json")

print("Safe Mode - \"" + config_data['Safe Mode'] + "\"")
print("Memory - \"" + config_data['Memory'] + "\"")
print("Error Log - \"" + config_data['Error Log'] + "\"")

#Prompts user asking them whether they want to make changes to the configuration or not.
modify_config = continue_task("modify or add items to the configuration")

if modify_config:
    #Prompts user to enter various configuration information
    new_config = create_config()

    #Saves the config information to config_override. If the user has already created a config_override file previously, that config is backed up with a timestamp.
    save_changes(new_config, "text_files/config_override.json")