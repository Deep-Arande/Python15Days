#Write a function that takes two lists and returns their
#intersection (common elements)



#function definition to intersect two list

def intersect_lists(n_list1,n_list2):
    
    i_list=list()
    
    for i in n_list1:
        
        if(i in n_list2):
            
            i_list.append(i)
            
    return i_list


#code
n_list1=list()
n_list2=list()
n=int(input("Enter the number of elements in both the list: "))

print("Enter the elements in list 1: ")
for i in range(n):
    
    ele=int(input(f"Enter the element [{i+1}]: "))
    n_list1.append(ele)
    
print("Enter the elements in list 2: ")
for i in range(n):
    
    ele=int(input(f"Enter the element [{i+1}]: "))
    n_list2.append(ele)

r_list=intersect_lists(n_list1,n_list2)

print(f"Intersection of two list are:\n {r_list}")

    
    
    
    