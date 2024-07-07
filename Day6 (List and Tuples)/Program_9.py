#Write a program that checks if a given list is sorted in
#ascending order

#function definition to check order of list

def check_ascending(n_list):
    
    for i in range(len(n_list)-1):
       
        if n_list[i]>n_list[i+1]:
            
            return False
    
    return True

#code

n_list=[1,2,3,4,5,6,7,8,11,14,17,2]

if check_ascending(n_list):
    
    print(f"List is in acsending order.")
else:
    print(f"List is not in ascending order.")