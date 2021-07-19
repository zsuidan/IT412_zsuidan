import json

#Attempts to open a json file containing information about a car model. If no file is found or the file is blank, prompts user to enter a model. 
#If a file already exists, the model is printed and the user is asked if they would like to change it.

try:
    with open("text_files/my_car.json") as json_obj:
        model_data = json.load(json_obj)
        print(model_data)

    with open("text_files/my_car.json", "w") as json_obj:
        
        change_model = input("Would you like to change the model information? (Y/N): ")

        correct_input = False

        while not correct_input:
            if change_model.upper() == "Y" or change_model.upper() == "N":
                correct_input = True
            else:
                continue_adding = input("Invalid response. Please enter either Y or N.")

        if change_model.upper() == "Y":
            new_model = input("What model is your car?: ")
            json.dump(new_model, json_obj)

except:
    car_model = input("What model is your car?: ")
    with open("text_files/my_car.json", "w") as json_obj:
        json.dump(car_model, json_obj)