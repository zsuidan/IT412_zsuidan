#Opens a text file containing a list of dinner items, asking a user to enter items to add to the list and writing them to the list
with open("text_files/dinner_menu.txt", "w") as file_output:
    continue_adding = True

    while continue_adding:
        dinner_item = input("Enter something you would like for dinner this week: ")

        file_output.write(dinner_item + "\n")

        continue_adding = input("Would you like to add another item? (Y/N): ")

        correct_input = False

        while not correct_input:
            if continue_adding.upper() == "Y" or continue_adding.upper() == "N":
                correct_input = True
            else:
                continue_adding = input("Invalid response. Please enter either Y or N.")

        if continue_adding.upper() == "N":
            break