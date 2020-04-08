# DONT RUN THIS CODE # 
# NOTE TAKING ONLY #
####################
#how to save a variable to a .json file on the HDD
import json
file_name = 'my_file.json'

with open(file_name, 'w') as file_to_save:
    json.dump(python_variable_to_save, file_to_save)


#how to import a variable from a .json file
import json
file_name = 'my_file.json'

with open(file_name, 'r') as file_to_load:
    python_variable = json.load(file_to_load)