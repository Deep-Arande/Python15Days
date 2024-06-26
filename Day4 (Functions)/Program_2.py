#Implement a program that checks if a given string is a palindrome


#function definition
def check_palindrome(str1):
    
 if(type(str1)==str):
    for i in range(0,len(str1)//2,1):
        
        #if not equal return false
        
        if str1[i]!=str1[(len(str1)-1)-i]:
            return False
    
    #if it is palindrome return true        
    return True    
            
        
   
        
#code

print("Enter the string to check palindrom:",end=' ')

str2=str(input())



if(check_palindrome(str2)):
    print("Enter string is a palindrom.")
    
else:
    print("Entered string is not palindrome.")
