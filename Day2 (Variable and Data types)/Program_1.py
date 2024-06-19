#Given a list of numbers, find the sum and average


#create empty list

n_list=[]
n=int(input("Enter the number of elements in list: "))

sum=0
for i in range(0,n,1):
    
    ele=int(input(f"Enter the elements [{i+1}]: "))
    n_list.append(ele)
    sum=sum+ele
    

average=float(sum/n)

print(f"The average: {average:.2f} and sum: {sum}")
    