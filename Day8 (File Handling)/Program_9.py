# Write a function that reads a JSON file and extracts
# specific information from it


import json  # library to handle json files


def print_json(key):
    with open("J.json", "r") as j_file:
        data = json.load(j_file)
        
# Accessing specific data
    for employee in data['employees']:
        print(employee[key])

#code

print_json(key="salary")
