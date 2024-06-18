# Given a list of integers, find the sum of all positive
#numbers


n_list=[]

n=int(input("Enter the number of elements in list: "))

sum=0
for i in range(0,n,1):
    
    ele=int(input(f"Enter the element [{i}]: "))
    
    n_list.insert(i,ele)
    if(ele>=0):
        sum=sum+ele
    

print(f"The sum of all positive elements in the list is: {sum}")