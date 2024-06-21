#Create a loop that prints all prime numbers between 1 and 50

#We will create program to print prime numbers from 1 to n  but
#question is about printing prime number between 1 to 50 


#function definition to check prime number 

def check_prime(num):
    
    for i in range(2,num//2+1,1):
        
        if(num%i==0):
            #return false if we found atleast one factor in given range
            return False
        
    #return True if number is prime
    return True 

#code to take input


n=int(input("Enter number up to which we need to find prime number: "))

print(f"Prime numbers from 1 to {n} are:")
for i in range(2,n+1,1):
    
    if(check_prime(i)==True):
        print(f"{i}",end=' ')
