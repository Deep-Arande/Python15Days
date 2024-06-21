# Calculate the sum of digits of a given number


#function to calculate number of digits

def sum_digit(num):
    
    sum=0
    
    while(num>0):
        rem=num%10
        sum=sum+rem
        num=num//10
        
        
    return sum


#code

n=int(input("Enter the number: "))

sum=sum_digit(n)

print(f"The sum of digits of entered number is: {sum}")