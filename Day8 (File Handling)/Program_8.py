#Implement a program that reads a CSV file and generates 
#a bar chart to represent the data using Matplotlib)

import csv
import matplotlib.pyplot as plt
import numpy as np

with open("Student_data.csv","r") as s_file:
    
    data=csv.reader(s_file)
    
    data_list=list(data)


student_name=list()
student_score=list()

for i in range(1,len(data_list)):
    
    student_name.append(data_list[i][0])
    student_score.append(int(data_list[i][1]))

print(student_name)
print(student_score)


student_n=np.array(student_name)
student_s=np.array(student_score)

plt.bar(student_n,student_s,color="skyblue",width=0.8) #first x-axis, y-axis and color of bars



plt.ylim(1,100)
plt.xlabel("Student_names")
plt.ylabel("Student_score")
plt.title("Student_names vs Score")
plt.show()