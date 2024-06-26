# Write a function to check if a number is even or odd and
# return "Even" or "Odd" accordingly

#function definition to check number is odd or even

def check_num(num):
   

    if num%2 == 0:
         return "Even"
    
    else:
        return "Odd"
       
       
       
num=int(input("Enter the number: "))

if(check_num(num)=="Even"):
    print("The entered number is Even.")
    
else:
    print("The entered number is Odd.")