#Given a list of integers, find all the even numbers and
#store them in a new list


#create an empty list to add even numbers
e_list=list()

n=int(input("Enter the number of elements: "))

for i in range(0,n,1):
    
    ele=int(input(f"Enter the element [{i+1}]: "))
    
    if(ele%2==0):
        e_list.append(ele)
        
if(e_list):
   print(f"The even numbers in the list are: \n {e_list}")

else:
    print("There are no even numbers in the list.")