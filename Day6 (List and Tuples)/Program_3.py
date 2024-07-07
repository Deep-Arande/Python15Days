#Implement a function that takes a list of numbers and
#returns a new list with the squared values



#function to return sqaure elements of list

def square_list(n_list):
    
    s_list=list()
    
    for i in n_list:
        
        s_list.append(i*i)
    
    return s_list

#code

n_list=[34,56,32,67,32,65,1,2,3,4]

s_list=square_list(n_list)

print(f"Elements in list after squaring:\n {s_list}")