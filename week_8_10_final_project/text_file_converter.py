import json

#Opens the basic customer export text file
with open("text_files/customer_export.txt") as text_file:
    #Creates a customer data list and customer dictionary used later in a json file
    customer_data = []
    customer = {}

    #Opens a CSV file to write cleaned output to
    with open("text_files/customer_export.csv", "w") as csv_file:
       
        for line in text_file:
            temp_line = line.split("|")
            place_counter = 0
            while place_counter < len(temp_line):
                temp_line[place_counter] = temp_line[place_counter][2:-2]

                
                place_counter += 1

            #Removes the extraneous information at the end of the text file lines
            temp_line.pop(11)
            temp_line.pop(11)

            #Writes the line to a CSV file
            csv_file.write(str(temp_line) + "\n")

            #Creates a customer dictionary using the information from the line
            customer = {'f_name': temp_line[0], 'l_name': temp_line[1], 'company': temp_line[2], 'address': temp_line[3], 'city': temp_line[4], 'county': temp_line[5],
                        'state': temp_line[6], 'zip': temp_line[7], 'primary_phone': temp_line[8], 'secondary_phone': temp_line[9], 'email_address': temp_line[10]}

            #Adds the customer dictionary to the customer data list
            customer_data.append(customer)

#Opens a json file to write customer data to
with open("text_files/customer_export.json", "w") as json_file:
    #Removes labels that were in the text file which are no longer needed
    customer_data.pop(0)

    #Dumps customer data list to the json file
    json.dump(customer_data, json_file, indent=1)