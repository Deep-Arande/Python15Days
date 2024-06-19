#Write a Python program to check if a given string is a
#pangram (contains all letters of the alphabet)'


def check_pangram(str1):
    str1.lower()
    alphabet="abcdefghijklmnopqstruvwxyz"
    for i in alphabet:
        
        if(i not in  str1):
            return False
        
        
     #return true if all alphabets are present   
    return True    
        
        
str2=str(input("Enter the string to check Pangram: "))


if(check_pangram(str2)):
    print("Entered string is a Pangram.")
    
else:
    print("Entered string is not pangram.")
    