# Given a text file with a list of numbers, write a function 
#that finds the sum of all numbers in the file

with open("num_list.txt","r") as num_file:
    
   sum=int(0)
   for i in num_file:
    
       sum+=int(i)

print(sum)


