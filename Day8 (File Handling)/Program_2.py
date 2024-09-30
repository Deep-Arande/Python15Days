# Given a CSV file with student names and scores, find the
# student with the highest score

import csv

with open("Student_score.csv", "r") as c_file:

    read = csv.reader(c_file)
    data_list=list(read) 
   


#loop to find index of the score 
for i in range(len(data_list)):

    for j in range(len(data_list[i])):

        if data_list[i][j] == "Score":

            score_index = j

#loop to find highest score of students 
high_score = int(0)
hscore_index = 1
for i in range(1, len(data_list)):

    current_score = data_list[i][score_index]

    if int(current_score) > int(high_score):

        high_score = int(current_score)
        hscore_index = i


print(
    f"Student with highest score is {data_list[hscore_index][score_index-1]} with score {high_score}")
