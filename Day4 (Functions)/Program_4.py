#Create a function to find the square of each element in a
#given list



#function definition for squaring elements of list

def square_list(n_list):
    
    
    s_list=list()
    
    for i in n_list:
        
        square=i*i
        s_list.append(square)
    

    return s_list


n_list=list()

n=int(input("Enter the number of elements in the list: "))

for i in range(n):
    
    ele=int(input(f"Enter the element [{i+1}]: "))
    
    n_list.append(ele)

result=square_list(n_list)

print(f"The elements after squaring are:\n {result}")
    