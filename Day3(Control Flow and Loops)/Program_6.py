#Implement a program that prints the multiplication table
#of a given number



#function definition to create multiplication table

def multi_table(num):
    
    for i in range(0,10,1):
        
        print(f"{num}*{i+1}={num*(i+1)}")
        


#code to take number

num=int(input("Enter the number: "))

print("The multiplication table of entered number is:")

multi_table(num)


