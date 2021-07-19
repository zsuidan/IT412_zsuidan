import json

with open("text_files/config.json") as json_obj:
    config_data = json.load(json_obj)

#Overwrites memory setting to 100MB
config_data["memory"] = "100MB"

#Changes the json file with the new memory setting (w must be included in order to write)
with open("text_files/config.json", "w") as json_obj:
    json.dump(config_data, json_obj)

print(config_data)

#Prints out only the information for memory
print(config_data["memory"])