#Should use / instead of \ for mac compatibility 
with open("text_files/SacramentocrimeJanuary2006.csv") as csv_file:
    for line in csv_file:
        temp_line = line.split(",")
        place_counter = 0
        while place_counter < len(temp_line):
            #Loop through list, for each element take current value and create a substring
            #Removes double quotes
            temp_line[place_counter] = temp_line[place_counter][1:-1]

            #Pulls out specific values from the list
            if place_counter == 0:
                print(temp_line[place_counter])
            if place_counter == 1:
                print(temp_line[place_counter])
            if place_counter == 5:
                print(temp_line[place_counter] + "\n\n")
            place_counter = place_counter + 1

import os.path
import shutil
import time

temp_output = ""

with open("text_files/pet.py") as python_file:
    for line in python_file:
        #Removes white spaces from start and end of the line
        temp_line = line.strip()

        #Prints each line skipping lines starting with # or """
        if temp_line.startswith("#") or temp_line.startswith('"""'):
            pass
        else:
            temp_output = temp_output + line

#Writes to a file called cleaned_output, if the file already exists, creates a backup
#Backup is tagged with a time to make sure as many backups can be created as needed
if os.path.isfile("text_files/cleaned_output.py"):
    shutil.copy2("text_files/cleaned_output.py", "text_files/cleaned_output.py.backup" + str(time.time()))

with open("text_files/cleaned_output.py", "w") as file_output:
    file_output.write(temp_output)