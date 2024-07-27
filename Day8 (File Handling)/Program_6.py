#Write a program that reads a CSV file and finds the total 
#sales revenue for a specific product

#code

import csv

with open("sales_revenue.csv","r") as s_file:
    
    readline=csv.reader(s_file)
    data_list=list(readline)

#loop to find column index of revenue in csv file


#loop to make list of 
rev_index=int()
k=0 #flag to break loop
for i in range(len(data_list)):
    
    for j in range(len(data_list[i])):
        
        if data_list[i][j]=="Revenue":
            rev_index=j
            k=1
            break
    if k==1:
        break

print(rev_index)
for i in range(1,len(data_list)):
    
    print(f"Revenue of product {data_list[i][0]} is {data_list[i][rev_index]}")