#Create a function to count the number of vowels in a given string



def count_vowel(str1):
    
    vowels="aioue"
    
    str1.lower()
    count=0
    for i in str1:
        
        if(i in vowels):
           count=count+1
        
    return count

str2=str(input("Enter the string: "))

count=count_vowel(str2)

print(f"Entered string has {count} vowels.") 