# Write a program that finds the average value of all the
#elements in a list of dictionaries


#function to find average value 

def find_average(d_list,key):
    
    sum=0
    
    for i in d_list:
        
        sum=sum+i[key]
    
    average=sum//len(d_list)
    
    return average

#code

dict_list=[
    
  {"name": "Alice", "age": 30, "score": 90},
  {"name": "Bob", "age": 25,"score":87},  
  {"name": "Charlie", "age": 35, "score": 95, "GPA": 3.8},
]

average=find_average(dict_list.copy(),"score")

print(f"Average is {average}")