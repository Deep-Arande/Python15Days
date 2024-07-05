#Create a function to reverse a given string


#function definition to reverse string

def reverse_str(str1):
    
    str2=str()
    character=str()
    
    for i in range(0,len(str1),1):
        
        character=str1[-1-i]
        str2=str2+character
        
    return str2


i_str=str(input("Enter the string: "))

n_str=reverse_str(i_str)

print(f"The reversed string is: {n_str}")
