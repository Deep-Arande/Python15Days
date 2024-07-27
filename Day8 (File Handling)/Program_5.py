#Given a CSV file with employee details (name, age, salary), 
# calculate the average salary of all employees

#code

import csv

with open("employee_details.csv","r") as e_file:
    
    read_data=csv.reader(e_file)
    data_list=list(read_data)
   



#loop to find index of salary

sal_index=int()
k=0 #flag to break loop
for i in range(len(data_list)):
    
    for j in range(len(data_list[i])):
        
        if data_list[i][j]=="Salary":
            sal_index=j
            k=1
            break
    if k==1:
        break


#loop to calculate the average of salaries 

total=int(0)
for i in range(1,len(data_list)):
    
    total+=int(data_list[i][sal_index])

n_employee=int(len(data_list)-1)

print(f"The average of salary of {n_employee} employees are {total/n_employee}")