#Write a Python program to check if a given number is a prime number





#function definition to check number is prime or not
def check_prime(num):
    
    fact=0
    #start loop from 2
    for i in range(2,num//2+1,1):
        
        if(num%i==0):
            return False
        
    
    return True


num=int(input("Enter the number: "))

if(num==1):
     print(f"Entered number {num} is neither prime nor composite number.")

elif(check_prime(num)):
    print(f"Entered number {num} is a prime number.")
    
else:
    print(f"Entered number {num} is not a prime number.")

