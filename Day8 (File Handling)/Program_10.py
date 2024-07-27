#  Given a CSV file with temperature data for each day of 
# the week, find the average temperature for each day.


import csv

with open("Temperature.csv","r") as t_file:
    
    data=csv.reader(t_file)
    data_list=list(data)


sum=int(0)
for  i in range(1,len(data_list)):
    
    sum+=int(data_list[i][1])

average=float(sum/7)
print(average)