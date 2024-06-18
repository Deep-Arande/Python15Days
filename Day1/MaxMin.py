#Given a list of numbers, find the maximum and minimum
#values


#create empty list
num_list=[]

print("Enter the number of items in list",end=' ')
n=int(input())

for i in range(0,n,1):
    ele=int(input(f"element [{i}]: "))
    num_list.append(ele)

max=num_list[0]
min=num_list[0]

for ele in num_list:
    
    
    if(max<ele):
        max=ele
    
    if(min>ele):
        min=ele
        

print(f"The maximum number in given list is:{max}")
print(f"The minimum number in list is:{min}")
