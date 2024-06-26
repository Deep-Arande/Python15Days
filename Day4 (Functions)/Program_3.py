#Write a program that calculates the factorial of a given number


#function definition to calculate factorial of number
def factorial(num):
    
    if(num==0):
        return 1
    
    else:
        return num*factorial(num-1)
    


#code to take input

num=int(input("Enter the number to find factorial: "))

if(num<0):
    print("Entered number is invalid")

else:
    fact=factorial(num)

    print(f"The factorial of the number is: {fact}")
    


