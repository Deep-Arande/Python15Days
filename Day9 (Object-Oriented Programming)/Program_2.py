# Given a CSV file with employee details (name, position,
# salary), create a class to represent an Employee.

import csv


class employee:

    def __init__(self, name, pos, sal):

        self.name = name
        self.position = pos
        self.salary = sal
    
    def __str__(self):
        
        return f"Name={self.name}\nPosition={self.position}\nSalary={self.salary}"



#open file to store employee in dictionary format
with open("employee_details.csv", "r") as e_file:

    data = csv.DictReader(e_file) #converts data into dictionary with head element as key
   
    data_list = list(data) #add each dictionary to list where keys are same in each dict but values are different
    


#open file again to store header keys in list
with open("employee_details.csv", "r") as e_file:

    data = csv.reader(e_file)
    head = list(data)



key_list=list(head[0])



e_list = list()
for row in data_list:
   #row is dictionary
    employee_obj = employee(row[key_list[0]], row[key_list[1]], row[key_list[2]])
    e_list.append(employee_obj)


for i in e_list:
    print(f"{i}\n\n")
